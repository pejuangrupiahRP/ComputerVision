from ultralytics import YOLO
import cv2
import numpy as np
import os
from datetime import datetime

def compute_iou(box1, box2):
    """Compute Intersection over Union (IoU) of two bounding boxes."""
    xi1 = max(box1[0], box2[0])
    yi1 = max(box1[1], box2[1])
    xi2 = min(box1[2], box2[2])
    yi2 = min(box1[3], box2[3])
    inter_area = max(0, xi2 - xi1) * max(0, yi2 - yi1)

    box1_area = (box1[2] - box1[0]) * (box1[3] - box1[1])
    box2_area = (box2[2] - box2[0]) * (box2[3] - box2[1])
    union_area = box1_area + box2_area - inter_area

    return inter_area / union_area if union_area != 0 else 0

class YOLODetector:
    def __init__(self, shape_model_path='model2/shape.pt', object_model_path='model2/name.pt'):
        """Initialize YOLO models for shape and object detection."""
        self.model_shapes = YOLO(shape_model_path)
        self.model_objects = YOLO(object_model_path)
        
        # Image enhancement parameters
        self.alpha = 1.5  # Contrast
        self.beta = 30    # Brightness
        
        # Create output folder
        self.output_folder = 'hasil'
        os.makedirs(self.output_folder, exist_ok=True)
        
        print("[INFO] YOLO Shape & Object Detector initialized!")
        print("[INFO] Models loaded successfully!")
    
    def enhance_image(self, frame):
        """Enhance image contrast and brightness."""
        return cv2.convertScaleAbs(frame, alpha=self.alpha, beta=self.beta)
    
    def get_focus_area(self, width, height, scale=0.5):
        """Get the focus area coordinates (center of frame)."""
        box_w, box_h = int(width * scale), int(height * scale)
        x1_focus = (width - box_w) // 2
        y1_focus = (height - box_h) // 2
        x2_focus = x1_focus + box_w
        y2_focus = y1_focus + box_h
        return [x1_focus, y1_focus, x2_focus, y2_focus]
    
    def detect_objects(self, frame, focus_box):
        """Detect shapes and objects in the frame."""
        enhanced_frame = self.enhance_image(frame)
        
        # Run detection on both models
        results_shapes = self.model_shapes(enhanced_frame, conf=0.15)
        results_objects = self.model_objects(enhanced_frame, conf=0.3)
        
        # Process shape detections
        shape_detections = []
        for r in results_shapes:
            for box in r.boxes:
                cls_id = int(box.cls[0])
                label = r.names[cls_id]
                conf = float(box.conf[0])
                coords = list(map(int, box.xyxy[0]))
                if compute_iou(coords, focus_box) > 0.3:
                    shape_detections.append((coords, label, conf))
        
        # Process object detections
        object_detections = []
        for r in results_objects:
            for box in r.boxes:
                cls_id = int(box.cls[0])
                label = r.names[cls_id]
                conf = float(box.conf[0])
                coords = list(map(int, box.xyxy[0]))
                if compute_iou(coords, focus_box) > 0.3:
                    object_detections.append((coords, label, conf))
        
        return shape_detections, object_detections, enhanced_frame
    
    def draw_detections(self, frame, shape_detections, object_detections, focus_box):
        """Draw bounding boxes and labels on the frame."""
        # Merge overlapping detections
        used_object = set()
        
        # Draw merged detections (shape + object)
        for shape_box, shape_label, shape_conf in shape_detections:
            merged = False
            for i, (obj_box, obj_label, obj_conf) in enumerate(object_detections):
                iou = compute_iou(shape_box, obj_box)
                if iou > 0.3 and i not in used_object:
                    x1, y1, x2, y2 = shape_box
                    label = f'{shape_label} - {obj_label}'
                    conf = (shape_conf + obj_conf) / 2
                    
                    # Draw colorful bounding box
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
                    
                    # Draw label background
                    label_text = f'{label} {conf:.2f}'
                    (text_width, text_height), _ = cv2.getTextSize(label_text, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)
                    cv2.rectangle(frame, (x1, y1 - text_height - 10), (x1 + text_width, y1), (0, 255, 0), -1)
                    cv2.putText(frame, label_text, (x1, y1 - 5),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
                    
                    used_object.add(i)
                    merged = True
                    break
            
            if not merged:
                x1, y1, x2, y2 = shape_box
                cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 3)
                label_text = f'{shape_label} {shape_conf:.2f}'
                (text_width, text_height), _ = cv2.getTextSize(label_text, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)
                cv2.rectangle(frame, (x1, y1 - text_height - 10), (x1 + text_width, y1), (255, 0, 0), -1)
                cv2.putText(frame, label_text, (x1, y1 - 5),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        # Draw remaining object detections
        for i, (obj_box, obj_label, obj_conf) in enumerate(object_detections):
            if i not in used_object:
                x1, y1, x2, y2 = obj_box
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
                label_text = f'{obj_label} {obj_conf:.2f}'
                (text_width, text_height), _ = cv2.getTextSize(label_text, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)
                cv2.rectangle(frame, (x1, y1 - text_height - 10), (x1 + text_width, y1), (0, 0, 255), -1)
                cv2.putText(frame, label_text, (x1, y1 - 5),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        # Draw focus area
        x1_focus, y1_focus, x2_focus, y2_focus = focus_box
        cv2.rectangle(frame, (x1_focus, y1_focus), (x2_focus, y2_focus), (0, 255, 255), 3)
        cv2.putText(frame, "🎯 SCAN AREA 🎯", (x1_focus + 10, y1_focus - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
        
        return frame
    
    def save_image(self, frame):
        """Save the current frame with timestamp."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(self.output_folder, f"capture_{timestamp}.jpg")
        cv2.imwrite(filename, frame)
        print(f"[INFO] 📸 Image saved: {filename}")
        return filename
    
    def run_detection(self):
        """Main detection loop."""
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("[ERROR] Could not open camera!")
            return
        
        print("[INFO] 🎯 Shape & Object Detection Active!")
        print("[INFO] Controls:")
        print("  - Press 'S' to save image")
        print("  - Press 'Q' to quit")
        print("  - Press 'R' to reset detection count")
        
        detection_count = 0
        
        while True:
            ret, frame = cap.read()
            if not ret:
                print("[ERROR] Failed to read from camera!")
                break
            
            height, width = frame.shape[:2]
            focus_box = self.get_focus_area(width, height)
            
            # Detect objects
            shape_detections, object_detections, enhanced_frame = self.detect_objects(frame, focus_box)
            
            # Draw detections
            result_frame = self.draw_detections(enhanced_frame.copy(), shape_detections, object_detections, focus_box)
            
            # Update detection count
            total_detections = len(shape_detections) + len(object_detections)
            if total_detections > 0:
                detection_count += 1
            
            # Add info overlay
            info_text = f"Detections: {total_detections} | Total Frames: {detection_count}"
            cv2.putText(result_frame, info_text, (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            
            # Display frame
            cv2.imshow("🎯 YOLO Shape & Object Detector - Kids Learning Edition", result_frame)
            
            # Handle key presses
            key = cv2.waitKey(1) & 0xFF
            if key == ord('s') or key == ord('S'):
                saved_file = self.save_image(result_frame)
                print(f"[SUCCESS] 🎉 Picture saved successfully!")
            elif key == ord('q') or key == ord('Q'):
                print("[INFO] 👋 Goodbye! Thanks for learning!")
                break
            elif key == ord('r') or key == ord('R'):
                detection_count = 0
                print("[INFO] 🔄 Detection count reset!")
        
        cap.release()
        cv2.destroyAllWindows()
        print(f"[INFO] 📊 Session complete! Total detection frames: {detection_count}")

def main():
    """Main function to run the YOLO detector."""
    try:
        detector = YOLODetector()
        detector.run_detection()
    except Exception as e:
        print(f"[ERROR] An error occurred: {e}")
        print("[INFO] Please make sure your YOLO model files are in the correct location!")

if __name__ == "__main__":
    main()
