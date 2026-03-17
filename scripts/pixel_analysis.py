import cv2
import numpy as np

def analyze_pixels(image_path):
    print(f"\n--- Analisi Pixel: {image_path} ---")
    img = cv2.imread(image_path)
    
    # 1. Albero (Verde scuro)
    # BGR format in OpenCV: #1B5E20 è circa (32, 94, 27)
    lower_green = np.array([0, 50, 0])
    upper_green = np.array([100, 255, 100])
    mask_green = cv2.inRange(img, lower_green, upper_green)
    green_pixels = cv2.findNonZero(mask_green)
    
    if green_pixels is not None:
        x_coords = green_pixels[:, 0, 1]
        min_x, max_x = x_coords.min(), x_coords.max()
        print(f"Albero (Verde): Bounding Box X da {min_x} a {max_x}. Centro visivo: {((min_x + max_x) / 2):.1f}")
    else:
        print("Albero: Colore verde non trovato o coperto.")

    # 2. Leoni (Rosso scuro)
    # #C62828 è circa (40, 40, 198) in BGR
    lower_red = np.array([0, 0, 150])
    upper_red = np.array([80, 80, 255])
    mask_red = cv2.inRange(img, lower_red, upper_red)
    
    # Escludiamo la riga rossa centrale che abbiamo disegnato noi (X = 498-502)
    mask_red[:, 495:505] = 0
    
    red_pixels = cv2.findNonZero(mask_red)
    if red_pixels is not None:
        x_coords = red_pixels[:, 0, 1]
        min_x, max_x = x_coords.min(), x_coords.max()
        print(f"Leoni (Rossi): Bounding Box X da {min_x} a {max_x}. Centro visivo globale: {((min_x + max_x) / 2):.1f}")
    else:
        print("Leoni: Colore rosso non trovato.")

analyze_pixels('scripts/debug_v01.png')
analyze_pixels('scripts/debug_v05.png')
