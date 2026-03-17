import xml.etree.ElementTree as ET
import os

def strip_ns(el):
    """Remove namespaces from element and its children tags."""
    for node in el.iter():
        if '}' in node.tag:
            node.tag = node.tag.split('}', 1)[1]
    return el

def create_layer_from_svg(content_svg_path, layer_id, scale_x, scale_y, tx, ty):
    tree = ET.parse(content_svg_path)
    root = tree.getroot()
    root = strip_ns(root)
    
    # Wrap all children in a new group with transform
    layer_g = ET.Element('g', {
        'id': layer_id,
        'transform': f'matrix({scale_x} 0 0 {scale_y} {tx} {ty})'
    })
    
    # Copy all children of the source SVG into the new layer group
    for child in list(root):
        layer_g.append(child)
        
    return layer_g

def build_variant(output_path, variant_id, config):
    print(f"Building {variant_id}...")
    root = ET.Element('svg', {
        'xmlns': 'http://www.w3.org/2000/svg',
        'viewBox': '0 0 1000 1000',
        'width': '1000',
        'height': '1000'
    })

    # 1. Shield Layer
    shield_path = 'assets/araldica/giardina/normalized/scudo_base.normalized.svg'
    shield_tree = ET.parse(shield_path)
    shield_src_root = strip_ns(shield_tree.getroot())
    shield_layer = ET.Element('g', {'id': f'{variant_id}-shield-layer'})
    for child in list(shield_src_root):
        shield_layer.append(child)
    
    # Set shield color based on config
    field = shield_layer.find(".//path[@id='shield-field']")
    if field is not None:
        field.set('fill', config['field_color'])
    
    root.append(shield_layer)

    # 2. Tree Layer
    tree_layer = create_layer_from_svg(
        'assets/araldica/giardina/extracted/albero_sradicato.svg',
        f'{variant_id}-tree',
        config['tree_scale'], config['tree_scale'],
        config['tree_tx'], config['tree_ty']
    )
    root.append(tree_layer)

    # 3. Lions Layer
    lion_src = config['lion_src']
    # Left Lion
    lion_l = create_layer_from_svg(
        lion_src,
        f'{variant_id}-lion-left',
        config['lion_l_scale_x'], config['lion_scale_y'],
        config['lion_l_tx'], config['lion_ty']
    )
    root.append(lion_l)
    
    # Right Lion
    lion_r = create_layer_from_svg(
        lion_src,
        f'{variant_id}-lion-right',
        config['lion_r_scale_x'], config['lion_scale_y'],
        config['lion_r_tx'], config['lion_ty']
    )
    root.append(lion_r)

    # 4. Crown Layer
    if config.get('has_crown'):
        crown_layer = create_layer_from_svg(
            'assets/araldica/giardina/normalized/corona_principesca.normalized.svg',
            f'{variant_id}-crown',
            config['crown_scale'], config['crown_scale'],
            config['crown_tx'], config['crown_ty']
        )
        root.append(crown_layer)

    # Save
    ET.register_namespace('', 'http://www.w3.org/2000/svg')
    tree = ET.ElementTree(root)
    tree.write(output_path, encoding='utf-8', xml_declaration=True)
    print(f"Saved {output_path}")

if __name__ == "__main__":
    # Internal Centers (from bbox analysis)
    TREE_C = 432.44
    CROWN_C = 831.59
    LION_H_C = 547.95 # Heraldry (v01)
    LION_E_C = 225.71 # Element (v05)

    # V01 Configuration (Enhanced Classical)
    v01_scale_tree = 0.48 * 1.15 # ~0.55
    v01_scale_lion = 0.20 * 1.50 # 0.30
    v01_scale_crown = 0.35 * 1.40 # 0.49
    v01_config = {
        'field_color': '#D4A017',
        'tree_scale': v01_scale_tree,
        'tree_tx': 224.43, 
        'tree_ty': 240, 
        'lion_src': 'assets/araldica/giardina/normalized/lion_rampant_heraldry.normalized.svg',
        'lion_l_scale_x': -v01_scale_lion, # Face right
        'lion_r_scale_x': v01_scale_lion,  # Face left
        'lion_scale_y': v01_scale_lion,
        'lion_l_tx': 350.5, # Closer to tree
        'lion_r_tx': 649.5, 
        'lion_ty': 320,
        'has_crown': True,
        'crown_scale': v01_scale_crown,
        'crown_tx': 255.45,
        'crown_ty': -20
    }

    # V05 Configuration (Super Dominant)
    v05_scale_tree = 0.60 * 1.15 # 0.69
    v05_scale_lion = 0.22 * 1.50 # 0.33
    v05_scale_crown = 0.40 * 1.40 # 0.56
    v05_config = {
        'field_color': '#D4A017',
        'tree_scale': v05_scale_tree,
        'tree_tx': 155.54, 
        'tree_ty': 180, 
        'lion_src': 'assets/araldica/giardina/normalized/lion_rampant_element.normalized.svg',
        'lion_l_scale_x': -v05_scale_lion, # Face right
        'lion_r_scale_x': v05_scale_lion,  # Face left
        'lion_scale_y': v05_scale_lion,
        'lion_l_tx': 370.65, # Closer to tree
        'lion_r_tx': 629.35, 
        'lion_ty': 360,
        'has_crown': True,
        'crown_scale': v05_scale_crown,
        'crown_tx': 220.36,
        'crown_ty': -30
    }

    build_variant('assets/araldica/giardina/varianti/v01_giardina_oro_completo.svg', 'v01', v01_config)
    build_variant('assets/araldica/giardina/varianti/v05_giardina_albero_dominante.svg', 'v05', v05_config)
