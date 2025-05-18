import cv2
import numpy as np

def get_dominant_color(image, contour):
    mask = np.zeros(image.shape[:2], dtype=np.uint8)
    cv2.drawContours(mask, [contour], -1, 255, -1)  # -1: filled
    mean_val = cv2.mean(image, mask=mask)
    b, g, r = int(mean_val[0]), int(mean_val[1]), int(mean_val[2])

    if r > 150 and g < 100 and b < 100:
        return "Merah"
    elif g > 150 and r < 100 and b < 100:
        return "Hijau"
    elif b > 150 and r < 100 and g < 100:
        return "Biru"
    elif r > 150 and g > 150 and b < 100:
        return "Kuning"
    elif r > 150 and g > 150 and b > 150:
        return "Putih"
    elif r < 80 and g < 80 and b < 80:
        return "Hitam"
    else:
        return "Tak dikenal"

def detect_shapes_from_frame(img):
    output = img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 100:
            continue

        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.04 * perimeter, True)
        vertices = len(approx)
        x, y, w, h = cv2.boundingRect(contour)

        shape_name = "Tidak diketahui"
        if vertices == 3:
            shape_name = "Segitiga"
        elif vertices == 4:
            aspect_ratio = float(w) / h
            shape_name = "Persegi" if 0.95 <= aspect_ratio <= 1.05 else "Persegi Panjang"
        elif vertices == 5:
            shape_name = "Pentagon"
        elif vertices == 6:
            shape_name = "Hexagon"
        elif vertices >= 8:
            area = cv2.contourArea(contour)
            circle_area = (np.pi * (w / 2) * (h / 2))
            area_ratio = area / circle_area
            shape_name = "Lingkaran" if area_ratio > 0.8 else f"Poligon ({vertices} sisi)"

        warna = get_dominant_color(img, contour)
        label = f"{shape_name} {warna}"

        cv2.drawContours(output, [contour], -1, (0, 255, 0), 2)
        cv2.putText(output, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 0, 255), 2)

    return output

def main():
    cap = cv2.VideoCapture(0)  # 0 untuk webcam utama

    if not cap.isOpened():
        print("Gagal membuka kamera.")
        return

    print("Tekan 'q' untuk keluar.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Gagal membaca frame.")
            break

        result = detect_shapes_from_frame(frame)
        cv2.imshow("Deteksi Bentuk dan Warna - Real Time", result)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
