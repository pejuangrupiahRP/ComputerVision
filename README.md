# 🔍 Shape Detection in Objects

## 📚 Background  
The rapid advancement of computer technology and artificial intelligence—particularly in the field of **computer vision**—has unlocked countless innovative applications.  
One fundamental aspect of computer vision is the ability to **automatically recognize and interpret shapes** from visual data, whether from static images or live video streams.

**Shape detection** plays a crucial role in digital image analysis, with applications in:

- 🏭 Manufacturing (quality inspection)  
- 🎥 Automated surveillance systems  
- 🤖 Robotics (navigation and interaction)  
- 🧩 Pattern recognition  
- 🏫 Educational tools

This project features a **real-time shape detection system** using **OpenCV**, **YOLO (You Only Look Once)**, and **Python** to identify basic geometric shapes such as:

- 🔺 Triangle  
- 🟥 Square  
- 🟦 Rectangle  
- 🟠 Circle  

The system supports input from both **static image files** and **live webcam feeds**, enabling interactive and automatic shape identification.

---

## 🚧 Scope & Limitations

1. **Detected Shape Types**  
   Currently supports detection of basic geometric shapes: **triangle, square, rectangle, and circle**.  
   Detection of more complex or irregular shapes is not implemented.

2. **Lighting & Environment**  
   System performance may degrade under:
   - Extreme lighting conditions (too bright/dark)
   - High image noise
   - Busy or complex backgrounds

---

## 🎯 Objectives

- 💡 Implement a shape detection algorithm using **OpenCV** and **Python** to identify basic geometric shapes.
- 📷 Accept image input from:
  - Static image files
  - Live webcam/video streams
- 🏷️ Annotate detected shapes in the output with:
  - Bounding outlines
  - Name labels (e.g., "Circle", "Rectangle")

---

## 🌟 Benefits

- 🎓 **Interactive Learning**  
  Real-time camera input transforms passive learning into an engaging, exploratory experience.

- 🔎 **Exploration-Based Learning**  
  Encourages users to actively find and identify shapes in their environment, promoting discovery-based education.

---

## ✅ Result

This application enables users to explore and recognize shapes in their surroundings using a webcam or mobile camera.  
By leveraging **computer vision**, the system **automatically detects shapes** such as triangles, squares, rectangles, and circles in **real-time**.

Detected shapes are:

- 🖼️ **Outlined on the screen**
- 🏷️ **Labeled with their shape names**

Making the experience both educational and fun!

---

## 📦 Technologies Used

- Python 🐍
- OpenCV 👁️‍🗨️
- YOLO (You Only Look Once) 🔎

---

## 🚀 How to Run

```bash
# Clone this repository
git clone https://github.com/yourusername/shape-detection.git
cd shape-detection

# Install dependencies
pip install -r requirements.txt

# Run the script
python shape_detector.py
