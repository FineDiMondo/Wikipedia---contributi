import xml.etree.ElementTree as ET
import cairosvg
import cv2

def add_center_line_and_render(svg_path, output_png):
    tree = ET.parse(svg_path)
    root = tree.getroot()
    ns = {'svg': 'http://www.w3.org/2000/svg'}
    ET.register_namespace('', 'http://www.w3.org/2000/svg')
    
    # Crea una linea rossa centrale
    line = ET.Element('line', {
        'x1': '500', 'y1': '0',
        'x2': '500', 'y2': '1000',
        'stroke': '#FF0000',
        'stroke-width': '2',
        'id': 'center-line-debug'
    })
    root.append(line)
    
    temp_svg = svg_path.replace('.svg', '_debug.svg')
    tree.write(temp_svg)
    
    # Renderizza il file completo (con linea)
    cairosvg.svg2png(url=temp_svg, write_to=output_png, output_width=1000, output_height=1000)
    print(f"Salvato rendering di debug: {output_png}")
    
    # Trova la colonna della linea rossa
    img = cv2.imread(output_png, cv2.IMREAD_COLOR)
    # Cerca i pixel rossi (BGR: 0, 0, 255)
    lower_red = (0, 0, 200)
    upper_red = (50, 50, 255)
    mask = cv2.inRange(img, lower_red, upper_red)
    red_pixels = cv2.findNonZero(mask)
    if red_pixels is not None:
        x_coords = red_pixels[:, 0, 1]
        print(f"La linea di simmetria è renderizzata alla colonna X = {int(x_coords.mean())}")

add_center_line_and_render('assets/araldica/giardina/varianti/v01_giardina_oro_completo.svg', 'scripts/debug_v01.png')
add_center_line_and_render('assets/araldica/giardina/varianti/v05_giardina_albero_dominante.svg', 'scripts/debug_v05.png')
