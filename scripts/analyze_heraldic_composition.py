from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import tempfile
from pathlib import Path
import xml.etree.ElementTree as ET

import cairosvg
import cv2
import numpy as np

NS = {"svg": "http://www.w3.org/2000/svg"}
MAX_RENDER_DIMENSION = 1000


def parse_viewbox(root: ET.Element) -> tuple[float, float, float, float]:
    raw = root.get("viewBox")
    if not raw:
        width = float(root.get("width", "1000"))
        height = float(root.get("height", "1000"))
        return 0.0, 0.0, width, height
    min_x, min_y, width, height = (float(value) for value in raw.replace(",", " ").split())
    return min_x, min_y, width, height


def render_dimensions(width: float, height: float) -> tuple[int, int]:
    if width <= 0 or height <= 0:
        return MAX_RENDER_DIMENSION, MAX_RENDER_DIMENSION
    if width >= height:
        out_width = MAX_RENDER_DIMENSION
        out_height = max(1, round(MAX_RENDER_DIMENSION * (height / width)))
        return out_width, out_height
    out_height = MAX_RENDER_DIMENSION
    out_width = max(1, round(MAX_RENDER_DIMENSION * (width / height)))
    return out_width, out_height


def render_svg_to_rgba(svg_path: Path, out_png: Path) -> tuple[np.ndarray, int, int]:
    root = ET.parse(svg_path).getroot()
    _, _, canvas_width, canvas_height = parse_viewbox(root)
    out_width, out_height = render_dimensions(canvas_width, canvas_height)
    png_bytes = cairosvg.svg2png(
        url=str(svg_path),
        output_width=out_width,
        output_height=out_height,
    )
    buffer = np.frombuffer(png_bytes, dtype=np.uint8)
    image = cv2.imdecode(buffer, cv2.IMREAD_UNCHANGED)
    if image is None:
        raise RuntimeError(f"Unable to render {svg_path}")
    return image, out_width, out_height


def measure_mask(mask: np.ndarray) -> dict[str, object]:
    coords = cv2.findNonZero(mask)
    if coords is None:
        return {
            "area_px": 0,
            "bbox_px": None,
            "center_x_px": None,
            "center_y_px": None,
            "width_px": 0,
            "height_px": 0,
        }

    x, y, w, h = cv2.boundingRect(coords)
    area = int(np.count_nonzero(mask))
    moments = cv2.moments(mask)
    center_x = float(moments["m10"] / moments["m00"]) if moments["m00"] else x + (w / 2.0)
    center_y = float(moments["m01"] / moments["m00"]) if moments["m00"] else y + (h / 2.0)
    return {
        "area_px": area,
        "bbox_px": [int(x), int(y), int(w), int(h)],
        "center_x_px": center_x,
        "center_y_px": center_y,
        "width_px": int(w),
        "height_px": int(h),
    }


def project_metrics(metrics: dict[str, object], scale_x: float, scale_y: float) -> dict[str, object]:
    bbox_px = metrics["bbox_px"]
    bbox = None
    if bbox_px is not None:
        bbox = [
            round(bbox_px[0] * scale_x, 2),
            round(bbox_px[1] * scale_y, 2),
            round(bbox_px[2] * scale_x, 2),
            round(bbox_px[3] * scale_y, 2),
        ]

    center_x = None if metrics["center_x_px"] is None else round(metrics["center_x_px"] * scale_x, 2)
    center_y = None if metrics["center_y_px"] is None else round(metrics["center_y_px"] * scale_y, 2)
    return {
        "area_px": metrics["area_px"],
        "bbox": bbox,
        "center_x": center_x,
        "center_y": center_y,
        "width": round(metrics["width_px"] * scale_x, 2),
        "height": round(metrics["height_px"] * scale_y, 2),
        "bbox_px": bbox_px,
        "center_x_px": None if metrics["center_x_px"] is None else round(metrics["center_x_px"], 2),
        "center_y_px": None if metrics["center_y_px"] is None else round(metrics["center_y_px"], 2),
        "width_px": metrics["width_px"],
        "height_px": metrics["height_px"],
    }


def primary_layer_ids(svg_path: Path) -> list[str]:
    root = ET.parse(svg_path).getroot()
    ids: list[str] = []
    for group in root.findall("svg:g", NS):
        group_id = group.get("id")
        if group_id:
            ids.append(group_id)
    if ids:
        return ids

    for group in root.findall(".//svg:g", NS):
        group_id = group.get("id")
        if group_id:
            ids.append(group_id)
    return ids


def isolate_primary_group(svg_path: Path, target_id: str, all_ids: list[str], output_dir: Path) -> Path:
    tree = ET.parse(svg_path)
    root = tree.getroot()
    for group in root.findall("svg:g", NS):
        gid = group.get("id")
        if gid in all_ids and gid != target_id:
            group.set("display", "none")
    digest = hashlib.sha1(target_id.encode("utf-8")).hexdigest()[:10]
    out_svg = output_dir / f"{digest}.svg"
    tree.write(out_svg, encoding="utf-8", xml_declaration=True)
    return out_svg


def full_mask(svg_path: Path, output_dir: Path) -> tuple[np.ndarray, int, int]:
    png = output_dir / "full.png"
    rgba, out_width, out_height = render_svg_to_rgba(svg_path, png)
    return np.where(rgba[:, :, 3] > 0, 255, 0).astype(np.uint8), out_width, out_height


def guess_shield_id(layer_ids: list[str]) -> str:
    for layer_id in layer_ids:
        lowered = layer_id.lower()
        if "shield" in lowered or "scudo" in lowered:
            return layer_id
    raise RuntimeError("Unable to identify shield layer")


def role_from_id(layer_id: str) -> str | None:
    lowered = layer_id.lower()
    if "shield" in lowered or "scudo" in lowered:
        return "shield"
    if "tree" in lowered or "albero" in lowered:
        return "tree"
    if "crown" in lowered or "corona" in lowered:
        return "crown"
    return None


def lion_candidates(layer_ids: list[str]) -> list[str]:
    result = []
    for layer_id in layer_ids:
        lowered = layer_id.lower()
        if "lion" in lowered or "leone" in lowered:
            result.append(layer_id)
    return result


def build_role_map(layer_ids: list[str], components: dict[str, dict[str, object]]) -> dict[str, str]:
    roles: dict[str, str] = {}
    for layer_id in layer_ids:
        role = role_from_id(layer_id)
        if role:
            roles[role] = layer_id

    lions = lion_candidates(layer_ids)
    if lions:
        lions = sorted(lions, key=lambda layer_id: components[layer_id]["center_x"] or 0.0)
        if len(lions) >= 1:
            roles["lion_left"] = lions[0]
        if len(lions) >= 2:
            roles["lion_right"] = lions[-1]
    return roles


def analyze(svg_path: Path, output_dir: Path) -> dict[str, object]:
    layer_ids = primary_layer_ids(svg_path)
    shield_id = guess_shield_id(layer_ids)

    root = ET.parse(svg_path).getroot()
    _, _, canvas_width, canvas_height = parse_viewbox(root)
    canvas_center_x = canvas_width / 2.0
    canvas_center_y = canvas_height / 2.0

    full_mask_data, render_width, render_height = full_mask(svg_path, output_dir)
    scale_x = canvas_width / max(render_width, 1)
    scale_y = canvas_height / max(render_height, 1)

    shield_svg = isolate_primary_group(svg_path, shield_id, layer_ids, output_dir)
    shield_rgba, _, _ = render_svg_to_rgba(shield_svg, output_dir / "shield.png")
    shield_mask = np.where(shield_rgba[:, :, 3] > 0, 255, 0).astype(np.uint8)
    shield_metrics = project_metrics(measure_mask(shield_mask), scale_x, scale_y)
    shield_area = max(shield_metrics["area_px"], 1)
    shield_width = max(float(shield_metrics["width"]), 1.0)
    shield_height = max(float(shield_metrics["height"]), 1.0)

    components: dict[str, dict[str, object]] = {}
    for component_id in layer_ids:
        isolated_svg = isolate_primary_group(svg_path, component_id, layer_ids, output_dir)
        digest = hashlib.sha1(component_id.encode("utf-8")).hexdigest()[:10]
        rgba, _, _ = render_svg_to_rgba(isolated_svg, output_dir / f"{digest}.png")
        mask = np.where(rgba[:, :, 3] > 0, 255, 0).astype(np.uint8)
        metrics = project_metrics(measure_mask(mask), scale_x, scale_y)
        overlap = cv2.bitwise_and(mask, shield_mask)
        overlap_area = int(np.count_nonzero(overlap))

        center_offset_x = None
        center_offset_y = None
        center_offset_x_pct = None
        center_offset_y_pct = None
        shield_offset_x = None
        shield_offset_y = None
        shield_offset_x_pct = None
        shield_offset_y_pct = None
        if metrics["center_x"] is not None:
            center_offset_x = round(metrics["center_x"] - canvas_center_x, 2)
            center_offset_x_pct = round(center_offset_x / max(canvas_width, 1.0), 4)
            shield_offset_x = round(metrics["center_x"] - float(shield_metrics["center_x"]), 2)
            shield_offset_x_pct = round(shield_offset_x / max(shield_width, 1.0), 4)
        if metrics["center_y"] is not None:
            center_offset_y = round(metrics["center_y"] - canvas_center_y, 2)
            center_offset_y_pct = round(center_offset_y / max(canvas_height, 1.0), 4)
            shield_offset_y = round(metrics["center_y"] - float(shield_metrics["center_y"]), 2)
            shield_offset_y_pct = round(shield_offset_y / max(shield_height, 1.0), 4)

        metrics.update(
            {
                "center_offset_from_canvas_x": center_offset_x,
                "center_offset_from_canvas_y": center_offset_y,
                "center_offset_from_canvas_x_pct": center_offset_x_pct,
                "center_offset_from_canvas_y_pct": center_offset_y_pct,
                "center_offset_from_shield_x": shield_offset_x,
                "center_offset_from_shield_y": shield_offset_y,
                "center_offset_from_shield_x_pct": shield_offset_x_pct,
                "center_offset_from_shield_y_pct": shield_offset_y_pct,
                "area_vs_shield": round(metrics["area_px"] / shield_area, 4),
                "width_vs_shield": round(float(metrics["width"]) / shield_width, 4),
                "height_vs_shield": round(float(metrics["height"]) / shield_height, 4),
                "inside_shield_ratio": round(overlap_area / max(metrics["area_px"], 1), 4),
            }
        )
        components[component_id] = metrics

    roles = build_role_map(layer_ids, components)

    result = {
        "file": str(svg_path),
        "canvas": {
            "viewBox": root.get("viewBox"),
            "width": canvas_width,
            "height": canvas_height,
            "center_x": round(canvas_center_x, 2),
            "center_y": round(canvas_center_y, 2),
            "render_width": render_width,
            "render_height": render_height,
        },
        "full": project_metrics(measure_mask(full_mask_data), scale_x, scale_y),
        "shield_id": shield_id,
        "shield": shield_metrics,
        "components": components,
        "roles": roles,
    }

    if "lion_left" in roles and "lion_right" in roles:
        left = components[roles["lion_left"]]
        right = components[roles["lion_right"]]
        result["symmetry"] = {
            "left_id": roles["lion_left"],
            "right_id": roles["lion_right"],
            "lion_area_delta_px": left["area_px"] - right["area_px"],
            "lion_width_delta": round(float(left["width"]) - float(right["width"]), 2),
            "lion_height_delta": round(float(left["height"]) - float(right["height"]), 2),
            "lion_axis_balance": round(
                abs((canvas_center_x - float(left["center_x"])) - (float(right["center_x"]) - canvas_center_x)),
                2,
            ),
            "lion_area_ratio": round(left["area_px"] / max(right["area_px"], 1), 4),
            "lions_combined_area_vs_shield": round(
                (left["area_px"] + right["area_px"]) / shield_area,
                4,
            ),
        }
    return result


def compare(old: dict[str, object], new: dict[str, object]) -> dict[str, object]:
    shared_roles = sorted(set(old["roles"]) & set(new["roles"]))
    delta: dict[str, object] = {}
    for role in shared_roles:
        old_component = old["components"][old["roles"][role]]
        new_component = new["components"][new["roles"][role]]
        delta[role] = {
            "area_px": new_component["area_px"] - old_component["area_px"],
            "area_vs_shield": round(new_component["area_vs_shield"] - old_component["area_vs_shield"], 4),
            "center_x_shield_pct": None
            if new_component["center_offset_from_shield_x_pct"] is None
            else round(
                new_component["center_offset_from_shield_x_pct"] - old_component["center_offset_from_shield_x_pct"],
                4,
            ),
            "center_y_shield_pct": None
            if new_component["center_offset_from_shield_y_pct"] is None
            else round(
                new_component["center_offset_from_shield_y_pct"] - old_component["center_offset_from_shield_y_pct"],
                4,
            ),
            "width_vs_shield": round(new_component["width_vs_shield"] - old_component["width_vs_shield"], 4),
            "height_vs_shield": round(new_component["height_vs_shield"] - old_component["height_vs_shield"], 4),
            "inside_shield_ratio": round(
                new_component["inside_shield_ratio"] - old_component["inside_shield_ratio"],
                4,
            ),
        }
    return delta


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Analyze heraldic SVG composition with CairoSVG + OpenCV.")
    parser.add_argument("--svg", required=True, help="Target SVG to analyze.")
    parser.add_argument("--baseline", help="Optional baseline SVG for metric comparison.")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    svg_path = Path(args.svg).resolve()
    output_dir = Path(__file__).resolve().parent / f".analysis_tmp_{os.getpid()}"
    if output_dir.exists():
        shutil.rmtree(output_dir, ignore_errors=True)
    output_dir.mkdir(parents=True, exist_ok=True)

    try:
        current = analyze(svg_path, output_dir)
        payload: dict[str, object] = {"current": current}
        if args.baseline:
            baseline_path = Path(args.baseline).resolve()
            baseline = analyze(baseline_path, output_dir)
            payload["baseline"] = baseline
            payload["delta"] = compare(baseline, current)
        print(json.dumps(payload, indent=2))
    finally:
        shutil.rmtree(output_dir, ignore_errors=True)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
