import cv2
import numpy as np
import os
import tensorflow as tf
from datetime import datetime

# Load the Keras model
model_path = r'model/model.h5'
model = tf.keras.models.load_model(model_path)

# Folder untuk menyimpan hasil tangkapan
hasil_folder = 'hasil'
if not os.path.exists(hasil_folder):
    os.makedirs(hasil_folder)

# Daftar nama label (kelas)
shape_names = ['circle', 'square', 'star', 'triangle']

# Real-time shape detection with webcam
cap = cv2.VideoCapture(0)
cap.set(3, 200)
cap.set(4, 200)

while True:
    success, img = cap.read()
    if not success:
        break

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gray_resized = cv2.resize(img_gray, (200, 200))
    img_input = np.expand_dims(img_gray_resized, axis=-1).reshape(1, 200, 200, 1) / 255.0

    preds = model.predict(img_input)
    label = np.argmax(preds)
    res = shape_names[label] if label < len(shape_names) else "Unknown"

    # Tambahkan teks label
    cv2.putText(img, res, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Tambahkan bounding box di tengah frame
    h, w, _ = img.shape
    box_size = 150
    top_left = (w // 2 - box_size // 2, h // 2 - box_size // 2)
    bottom_right = (w // 2 + box_size // 2, h // 2 + box_size // 2)
    cv2.rectangle(img, top_left, bottom_right, (255, 0, 0), 2)

    cv2.imshow("Real-Time Shape Detection", img)

    key = cv2.waitKey(1) & 0xFF

    # Tombol 's' untuk simpan gambar
    if key == ord('s'):
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{hasil_folder}/shape_{res}_{timestamp}.jpg"
        cv2.imwrite(filename, img)
        print(f"[INFO] Gambar disimpan: {filename}")

    # Tombol 'q' untuk keluar
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
