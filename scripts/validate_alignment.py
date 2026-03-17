import cairosvg
import cv2
import numpy as np
import xml.etree.ElementTree as ET
import os
import copy

def validate_svg_alignment(svg_path, element_ids):
    print(f"\nAnalizzando: {svg_path}")
    tree = ET.parse(svg_path)
    root = tree.getroot()
    ns = {'svg': 'http://www.w3.org/2000/svg'}
    ET.register_namespace('', 'http://www.w3.org/2000/svg')

    # Viewbox center
    vb = root.get('viewBox').split()
    center_x = float(vb[2]) / 2
    print(f"Centro ideale (ViewBox): X = {center_x}")

    for el_id in element_ids:
        # Create a deep copy of the tree to isolate the element
        temp_tree = copy.deepcopy(tree)
        temp_root = temp_tree.getroot()
        
        # Add visible markers at corners to force 1000x1000 rendering
        # Using a very faint color to be sure they are not picked as "non-zero" but Cairo renders them
        # Actually, let's use small dots in the corner that we then exclude
        marker_tl = ET.Element('rect', {'x': '0', 'y': '0', 'width': '1', 'height': '1', 'fill': '#000000', 'fill-opacity': '0.01'})
        marker_br = ET.Element('rect', {'x': '999', 'y': '999', 'width': '1', 'height': '1', 'fill': '#000000', 'fill-opacity': '0.01'})
        temp_root.append(marker_tl)
        temp_root.append(marker_br)

        target_found = False
        for g in temp_root.findall('.//svg:g', ns):
            gid = g.get('id')
            if gid == el_id:
                target_found = True
            elif gid in element_ids:
                # hide other primary components
                g.set('display', 'none')
        
        if not target_found:
            print(f"Elemento {el_id} non trovato!")
            continue

        temp_svg = f"temp_{el_id}.svg"
        temp_png = f"temp_{el_id}.png"
        temp_tree.write(temp_svg)

        cairosvg.svg2png(url=temp_svg, write_to=temp_png, output_width=1000, output_height=1000)

        img = cv2.imread(temp_png, cv2.IMREAD_UNCHANGED)
        if img is None or img.shape[2] != 4:
            print(f"Errore lettura o no alpha channel per {el_id}")
            continue

        alpha = img[:, :, 3]
        # Ignore corner markers for bbox calculation
        alpha[0, 0] = 0
        alpha[999, 999] = 0
        
        coords = cv2.findNonZero(alpha)
        if coords is None:
            print(f"{el_id}: Nessun pixel visibile.")
            continue
            
        y_coords, x_coords = coords[:, 0, 0], coords[:, 0, 1]
        min_x, max_x = np.min(y_coords), np.max(y_coords) # coords[:,0,0] is X in OpenCV findNonZero! 
        # Wait: findNonZero returns (x, y) but wait.
        # Actually it's (x, y). Let's re-verify.
        # coords[:, 0, 0] -> X, coords[:, 0, 1] -> Y
        
        real_min_x, real_max_x = np.min(coords[:, 0, 0]), np.max(coords[:, 0, 0])
        
        visual_center_x = (real_min_x + real_max_x) / 2.0
        diff = abs(visual_center_x - center_x)
        
        status = "PERFETTO" if diff < 1.0 else "DA CORREGGERE"
        print(f"[{el_id}] MinX: {real_min_x}, MaxX: {real_max_x} -> Centro Visivo: {visual_center_x} ({status} - Offset: {diff:.2f}px)")

        os.remove(temp_svg)
        os.remove(temp_png)

if __name__ == "__main__":
    validate_svg_alignment(
        'assets/araldica/giardina/varianti/v01_giardina_oro_completo.svg', 
        ['v01-shield-layer', 'v01-tree', 'v01-crown', 'v01-lion-left', 'v01-lion-right']
    )
    validate_svg_alignment(
        'assets/araldica/giardina/varianti/v05_giardina_albero_dominante.svg', 
        ['v05-shield-layer', 'v05-tree', 'v05-crown', 'v05-lion-left', 'v05-lion-right']
    )
