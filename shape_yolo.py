from ultralytics import YOLO
import cv2

model = YOLO('model/best.pt')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    # Plot dengan konfidensi minimum 0.25
    annotated_frame = results[0].plot(conf=0.25)

    # Cetak label di terminal (debug)
    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            conf = box.conf[0]
            print(f"Detected {model.names[cls]} with confidence {conf:.2f}")

    cv2.imshow("YOLOv8 Shape Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
