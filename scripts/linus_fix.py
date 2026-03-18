import xml.etree.ElementTree as ET

def clean_svg_structure():
    # Ricalcolo TX basandomi sull'ultima validazione OpenCV (Offset rilevati)
    # TREE: Offset +123.5 -> TX = 239.8 - 123.5 = 116.3
    # CROWN: Offset -78.0 -> TX = 197.2 + 78.0 = 275.2
    # LIONS: Symmetrically shift towards center
    
    root = ET.Element('svg', {
        'xmlns': 'http://www.w3.org/2000/svg',
        'viewBox': '0 0 1000 1000',
        'width': '1000',
        'height': '1000'
    })

    def get_clean_paths(source_svg, group_id, scale_x, scale_y, tx, ty):
        tree = ET.parse(source_svg)
        src_root = tree.getroot()
        group = ET.Element('g', {'id': group_id, 'transform': f'matrix({scale_x} 0 0 {scale_y} {tx} {ty})'})
        for path in src_root.findall('.//{http://www.w3.org/2000/svg}path'):
            new_path = ET.Element('path')
            for attr, val in path.attrib.items():
                if '}' in attr: attr = attr.split('}', 1)[1]
                new_path.set(attr, val)
            group.append(new_path)
        return group

    # 1. Shield (X=500 centered)
    shield_g = ET.Element('g', {'id': 'shield-layer'})
    shield_path = ET.Element('path', {
        'id': 'shield-shape',
        'd': 'M 500,800 C 500,800 500,862 575,883 650,904 685,894.5 710,930 735,894.5 770,904 845,883 920,862 920,800 920,800 L 920,418 80,418 80,800 C 80,800 80,862 155,883 230,904 265,894.5 290,930 315,894.5 350,904 425,883 500,862 500,800 500,800 Z',
        'fill': '#D4A017', 'stroke': '#1A1A1A', 'stroke-width': '8'
    })
    shield_g.append(shield_path)
    root.append(shield_g)

    # 2. Tree (Visual centering)
    tree_g = get_clean_paths('assets/araldica/giardina/extracted/albero_sradicato.svg', 'tree-layer', 0.55, 0.55, 116.3, 440)
    root.append(tree_g)

    # 3. Lions (Compact symmetry)
    lion_scale = 0.30
    # Left: Shift +175.0 -> TX = 514.4 + 175 = 689.4
    lion_l = get_clean_paths('assets/araldica/giardina/normalized/lion_rampant_heraldry.normalized.svg', 'lion-left', -lion_scale, lion_scale, 689.4, 520)
    root.append(lion_l)
    # Right: Shift -174.0 -> TX = 485.6 - 174 = 311.6
    lion_r = get_clean_paths('assets/araldica/giardina/normalized/lion_rampant_heraldry.normalized.svg', 'lion-right', lion_scale, lion_scale, 311.6, 520)
    root.append(lion_r)

    # 4. Crown (Visual centering, no oval)
    crown_g = get_clean_paths('assets/araldica/giardina/normalized/corona_principesca.normalized.svg', 'crown-layer', 0.50, 0.50, 275.2, 50)
    for path in list(crown_g):
        if path.get('id') == 'path4167': crown_g.remove(path)
    root.append(crown_g)

    ET.register_namespace('', 'http://www.w3.org/2000/svg')
    output_path = 'assets/araldica/giardina/varianti/v01_giardina_oro_completo.svg'
    with open(output_path, 'wb') as f:
        ET.ElementTree(root).write(f, encoding='utf-8', xml_declaration=True)
    print(f"File {output_path} rigenerato con correzioni empiriche.")

if __name__ == "__main__":
    clean_svg_structure()
