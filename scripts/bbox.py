import re
import sys

def parse_svg(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        paths = re.findall(r'd=["\']([^"\']+)["\']', content)
        min_x, max_x = 999999, -999999
        for d in paths:
            # Estraggo tutti i numeri
            coords = [float(x) for x in re.findall(r'[-+]?\d*\.\d+|\d+', d)]
            if len(coords) < 2: continue
            # Molto approssimativo: assumo che molte X siano nei posti pari e che
            # analizzare tutti i numeri dia comunque un bounding box accettabile
            for i in range(len(coords)):
                x = coords[i]
                # Filtriamo i valori assurdi che non possono essere coordinate X nel range 0-1000
                if -1000 < x < 2000:
                    if x < min_x: min_x = x
                    if x > max_x: max_x = x
        return min_x, max_x
    except Exception as e:
        return str(e)

print('Crown bbox:', parse_svg('assets/araldica/giardina/normalized/corona_principesca.normalized.svg'))
print('Tree bbox:', parse_svg('assets/araldica/giardina/extracted/albero_sradicato.svg'))
print('Shield bbox:', parse_svg('assets/araldica/giardina/normalized/scudo_base.normalized.svg'))
print('Lion heraldry bbox (v01):', parse_svg('assets/araldica/giardina/normalized/lion_rampant_heraldry.normalized.svg'))
print('Lion element bbox (v05):', parse_svg('assets/araldica/giardina/normalized/lion_rampant_element.normalized.svg'))
