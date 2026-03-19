from __future__ import annotations

import argparse
import copy
import json
import re
from pathlib import Path
import xml.etree.ElementTree as ET

REPO_ROOT = Path(__file__).resolve().parents[1]
RED_LIKE = {"#c62828", "#ff0000", "#c41e3a"}
WHITE_LIKE = {"#fff", "#ffffff", "#f5f5f5", "#f5f5f5ff"}


def strip_ns(element: ET.Element) -> ET.Element:
    for node in element.iter():
        if "}" in node.tag:
            node.tag = node.tag.split("}", 1)[1]
    return element


def resolve_path(path_text: str, recipe_path: Path) -> Path:
    path = Path(path_text)
    if path.is_absolute():
        return path

    anchor = path.parts[0] if path.parts else ""
    if anchor in {"assets", "docs", "scripts", "tests"}:
        return (REPO_ROOT / path).resolve()

    recipe_relative = (recipe_path.parent / path).resolve()
    family_relative = (recipe_path.parent.parent / path).resolve()
    repo_relative = (REPO_ROOT / path).resolve()

    if recipe_path.parent.name == "recipes":
        candidates = [family_relative, recipe_relative, repo_relative]
    else:
        candidates = [recipe_relative, family_relative, repo_relative]
    for candidate in candidates:
        if candidate.exists():
            return candidate

    if recipe_path.parent.name == "recipes":
        return family_relative
    return recipe_relative


def normalize_color(value: str | None) -> str | None:
    if value is None:
        return None
    return value.strip().lower()


def is_red_like(value: str | None) -> bool:
    color = normalize_color(value)
    return color in RED_LIKE


def is_white_like(value: str | None) -> bool:
    color = normalize_color(value)
    return color in WHITE_LIKE


def format_number(value: float | int) -> str:
    text = f"{float(value):.6f}".rstrip("0").rstrip(".")
    return text if text else "0"


def parse_simple_matrix(transform: str) -> tuple[float, float, float, float] | None:
    match = re.fullmatch(
        r"matrix\(\s*([-+0-9.eE]+)\s+0\s+0\s+([-+0-9.eE]+)\s+([-+0-9.eE]+)\s+([-+0-9.eE]+)\s*\)",
        transform.strip(),
    )
    if not match:
        return None
    sx, sy, tx, ty = (float(group) for group in match.groups())
    return sx, sy, tx, ty


def compose_transform(parts: list[str]) -> str | None:
    filtered = [part for part in parts if part]
    return " ".join(filtered) if filtered else None


def serialize_transform(
    transform: str | dict[str, object] | None,
    *,
    simplify_transforms: bool,
    mutations: dict[str, object] | None = None,
) -> str | None:
    if transform is None and not mutations:
        return None

    mutation_map = mutations or {}

    if isinstance(transform, str):
        if simplify_transforms:
            parsed = parse_simple_matrix(transform)
            if parsed is not None:
                sx, sy, tx, ty = parsed
                parts = [
                    f"translate({format_number(tx)} {format_number(ty)})",
                    f"scale({format_number(sx)} {format_number(sy)})",
                ]
                return compose_transform(parts)
        return transform

    transform_map = transform or {}
    translate = transform_map.get("translate", [0.0, 0.0])
    scale = transform_map.get("scale", [1.0, 1.0])
    rotate = float(transform_map.get("rotate", 0.0))

    tx = float(translate[0])
    ty = float(translate[1])
    sx = float(scale[0])
    sy = float(scale[1])

    if mutation_map.get("flip_x"):
        sx *= -1.0
    if mutation_map.get("flip_y"):
        sy *= -1.0

    parts: list[str] = []
    if tx != 0.0 or ty != 0.0:
        parts.append(f"translate({format_number(tx)} {format_number(ty)})")
    if rotate != 0.0:
        parts.append(f"rotate({format_number(rotate)})")
    if sx != 1.0 or sy != 1.0:
        parts.append(f"scale({format_number(sx)} {format_number(sy)})")
    return compose_transform(parts)


def load_svg_group(
    source_path: Path,
    group_id: str,
    transform: str | dict[str, object] | None,
    *,
    simplify_transforms: bool,
    mutations: dict[str, object] | None = None,
) -> ET.Element:
    tree = ET.parse(source_path)
    source_root = strip_ns(tree.getroot())

    attributes = {"id": group_id}
    serialized_transform = serialize_transform(
        transform,
        simplify_transforms=simplify_transforms,
        mutations=mutations,
    )
    if serialized_transform:
        attributes["transform"] = serialized_transform

    layer_group = ET.Element("g", attributes)
    for child in list(source_root):
        layer_group.append(copy.deepcopy(child))
    return layer_group


def find_first(group: ET.Element, *, tag: str | None = None, target_id: str | None = None) -> ET.Element | None:
    for node in group.iter():
        if tag and node.tag != tag:
            continue
        if target_id and node.get("id") != target_id:
            continue
        return node
    return None


def apply_selector_mutations(group: ET.Element, mutations: list[dict[str, object]]) -> None:
    for mutation in mutations:
        selector = mutation["selector"]
        tag = selector.get("tag")
        target_id = selector.get("id")

        target = find_first(group, tag=tag, target_id=target_id)
        if target is None:
            raise ValueError(f"Mutation target not found: {selector}")

        for key, value in mutation.get("attributes", {}).items():
            target.set(str(key), str(value))


def apply_semantic_mutations(group: ET.Element, mutations: dict[str, object]) -> None:
    shield_field = find_first(group, target_id="shield-field")
    shield_outline = find_first(group, target_id="shield-outline")

    if "fill_shield_field" in mutations:
        if shield_field is None:
            raise ValueError("Unable to find #shield-field for fill_shield_field mutation")
        shield_field.set("fill", str(mutations["fill_shield_field"]))

    if "stroke_shield_outline" in mutations:
        if shield_outline is None:
            raise ValueError("Unable to find #shield-outline for stroke_shield_outline mutation")
        shield_outline.set("stroke", str(mutations["stroke_shield_outline"]))

    if "stroke_width_outline" in mutations:
        if shield_outline is None:
            raise ValueError("Unable to find #shield-outline for stroke_width_outline mutation")
        shield_outline.set("stroke-width", format_number(float(mutations["stroke_width_outline"])))

    fill_color = mutations.get("fill_color")
    gem_color = mutations.get("gemma_centrale_color")
    stroke_color = mutations.get("stroke_color")
    stroke_width = mutations.get("stroke_width")

    for node in group.iter():
        original_fill = normalize_color(node.get("fill"))
        original_stroke = normalize_color(node.get("stroke"))

        if gem_color and is_red_like(original_fill):
            node.set("fill", str(gem_color))
        elif fill_color and original_fill not in (None, "none") and not is_white_like(original_fill):
            node.set("fill", str(fill_color))

        if stroke_color and original_stroke not in (None, "none"):
            node.set("stroke", str(stroke_color))

        if stroke_width is not None and original_stroke not in (None, "none"):
            node.set("stroke-width", format_number(float(stroke_width)))

    if "opacity" in mutations:
        group.set("opacity", format_number(float(mutations["opacity"])))


def apply_mutations(group: ET.Element, mutations: list[dict[str, object]] | dict[str, object]) -> None:
    if not mutations:
        return
    if isinstance(mutations, list):
        apply_selector_mutations(group, mutations)
        return
    apply_semantic_mutations(group, mutations)


def extract_output_path(recipe: dict[str, object], output_override: str | None) -> str:
    if output_override:
        return output_override
    output = recipe["output"]
    if isinstance(output, dict):
        return str(output["path"])
    return str(output)


def output_options(recipe: dict[str, object]) -> dict[str, object]:
    output = recipe.get("output", {})
    return output if isinstance(output, dict) else {}


def canvas_background(canvas: dict[str, object]) -> str | None:
    if "background_color" in canvas:
        return str(canvas["background_color"])
    if "background" in canvas:
        return str(canvas["background"])
    return None


def layer_source(layer: dict[str, object]) -> str:
    if "asset" in layer:
        return str(layer["asset"])
    return str(layer["source"])


def layer_mutations(layer: dict[str, object]) -> list[dict[str, object]] | dict[str, object]:
    mutations = layer.get("mutations", {})
    return mutations


def maybe_add_metadata(root: ET.Element, recipe: dict[str, object]) -> None:
    options = output_options(recipe)
    if not options.get("embed_metadata"):
        return

    metadata_payload = {
        "metadata": recipe.get("metadata", {}),
        "validation": recipe.get("validation", {}),
    }
    metadata_node = ET.SubElement(root, "metadata")
    metadata_node.text = json.dumps(metadata_payload, ensure_ascii=True)


def build_svg(recipe: dict[str, object], recipe_path: Path, output_override: str | None = None) -> Path:
    canvas = recipe["canvas"]
    output_path = resolve_path(extract_output_path(recipe, output_override), recipe_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    root = ET.Element(
        "svg",
        {
            "xmlns": "http://www.w3.org/2000/svg",
            "viewBox": str(canvas["viewBox"]),
            "width": str(canvas["width"]),
            "height": str(canvas["height"]),
        },
    )

    maybe_add_metadata(root, recipe)

    background = canvas_background(canvas)
    if background not in (None, "transparent"):
        root.append(
            ET.Element(
                "rect",
                {
                    "width": "100%",
                    "height": "100%",
                    "fill": str(background),
                },
            )
        )

    simplify_transforms = bool(output_options(recipe).get("simplify_transforms"))
    layers = sorted(recipe["layers"], key=lambda layer: int(layer.get("z_order", 0)))
    for layer in layers:
        mutations = layer_mutations(layer)
        source_path = resolve_path(layer_source(layer), recipe_path)
        group = load_svg_group(
            source_path,
            str(layer["id"]),
            layer.get("transform"),
            simplify_transforms=simplify_transforms,
            mutations=mutations if isinstance(mutations, dict) else None,
        )
        apply_mutations(group, mutations)
        root.append(group)

    ET.register_namespace("", "http://www.w3.org/2000/svg")
    ET.ElementTree(root).write(output_path, encoding="utf-8", xml_declaration=True)
    return output_path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Compose a heraldic SVG from a JSON recipe.")
    parser.add_argument("--recipe", required=True, help="Path to the recipe JSON.")
    parser.add_argument("--output", help="Optional output override.")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    recipe_path = Path(args.recipe).resolve()
    recipe = json.loads(recipe_path.read_text(encoding="utf-8"))
    output_path = build_svg(recipe, recipe_path, output_override=args.output)
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
