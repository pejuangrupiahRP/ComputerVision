# 🎯 Shape & Object Detective - Interactive Learning App

## 📚 Background

The rapid advancement of computer technology and artificial intelligence—particularly in **computer vision**—has enabled countless innovative applications.
One of the core capabilities of computer vision is the ability to **automatically recognize and interpret shapes** from visual data, whether from static images or live video streams.

**Shape detection** plays a crucial role in digital image analysis with applications in:

* 🏦 Manufacturing (quality inspection)
* 🎥 Automated surveillance systems
* 🤖 Robotics (navigation and interaction)
* 🧩 Pattern recognition
* 🏫 Educational tools

This project demonstrates a **real-time shape detection system** using **OpenCV**, **YOLO (You Only Look Once)**, **Next.js**, and **Python** to identify basic geometric shapes such as:

* 🔺 Triangle
* 🔳 Square
* 🗾 Rectangle
* 🔸 Circle
* ⭐ Star
* 🥚 Oval

The system supports input from **live webcam feed** and displays a **child-friendly web interface** with gamified features to enhance learning experience.

---

## 🎮 Key Features

### 🌟 **Interactive Web Interface**

* **Kid-friendly design** with bright colors and engaging animations
* **Real-time camera feed** with clearly marked scan area
* **Intuitive controls** with large, easy-to-use buttons

### 🎯 **Gamification System**

* **Score System** - Earn points for each detection and saved image
* **Streak Counter** - Track consecutive detections for bonus points
* **Daily Challenges** - Missions like "Circle Hunter" and "Square Master"
* **Achievement System** - Earn badges to motivate continued learning
* **Progress Tracking** - Comprehensive learning statistics

### 🔊 **Audio & Visual Effects**

* **Sound effects** for detection, saving, and achievements
* **Celebration animations** when milestones are reached
* **Colorful visual feedback** to enhance engagement

### 📚 **Educational Content**

* **Fun facts** about each geometric shape
* **Easy-to-understand explanations** in Bahasa Indonesia (customizable)
* **Visual cards** with shape definitions and trivia

---

## ⚖️ Scope & Limitations

1. **Supported Shape Types**
   Currently supports basic geometric shapes: **triangle, square, rectangle, circle, star, and oval**.
   Complex or irregular shapes are not yet implemented.

2. **Lighting & Environment**
   Detection performance may degrade under:

   * Extreme lighting (too bright/dark)
   * High image noise
   * Busy or complex backgrounds

3. **Browser Compatibility**
   Requires modern browsers that support WebRTC for camera access.

---

## 🎯 Objectives

* 💡 Implement shape detection algorithms using **OpenCV**, **YOLO**, and **Python** to identify basic geometric shapes.
* 📷 Accept image input from webcam/live camera
* 🏷️ Annotate detected shapes with:

  * Colored bounding boxes
  * Shape name labels (e.g., "Circle", "Rectangle")
* 🎮 Provide an engaging and interactive learning experience for children
* 📊 Track learning progress with a point system and achievements

---

## 🌟 Benefits

* 🎓 **Interactive Learning**
  Live camera input transforms passive learning into an engaging, exploratory experience.

* 🔎 **Exploratory-Based Learning**
  Encourages users to actively search and identify shapes in their environment, promoting discovery-based education.

* 🎮 **Gamified Learning**
  The point system, challenges, and achievements turn learning into a game.

* 👶 **Child-Friendly**
  Interface specially designed for children with engaging visuals and simple controls.

---

## ✅ Result

This application allows users to explore and recognize shapes in their surroundings using a webcam or mobile camera.
Utilizing **computer vision**, the system **automatically detects shapes** such as triangles, squares, rectangles, circles, stars, and ovals in **real time**.

Detected shapes will:

* 🖼️ **Be highlighted on screen** with colored bounding boxes
* 🏷️ **Be labeled with their shape name**
* 🎯 **Appear in the latest detection panel**
* 📸 **Be savable as part of a collection**

Creating an educational and enjoyable learning experience!

---

## 📦 Technology Stack

### **Frontend (Web Interface)**

* **Next.js 15** ⚡ - React framework for web apps
* **React 18** ⚛️ - UI library
* **TypeScript** 📜 - Type-safe JavaScript
* **Tailwind CSS** 🎨 - Styling framework
* **shadcn/ui** 🧩 - Modern UI components
* **Lucide React** 🎯 - Icon library

### **Backend (Detection Engine)**

* **Python 3.8+** 🐍 - Main programming language
* **OpenCV** 🔭 - Computer vision library
* **YOLO (Ultralytics)** 🔎 - Object detection model
* **NumPy** 🔢 - Numerical computing

### **Additional Features**

* **Web Audio API** 🔊 - Sound effects
* **WebRTC** 📹 - Camera access in browser
* **CSS Animations** ✨ - Animations and transitions

---

## 🚀 Installation & Setup Guide

### **Requirements**

```bash
# Ensure Node.js is installed (v18 or higher)
node --version

# Ensure Python is installed (v3.8 or higher)
python --version
```

### **1. Setup Web Interface (Next.js)**

```bash
# Clone or extract the project
cd yolo-learning-app

# Install dependencies
npm install

# Run development server
npm run dev
```

Web app will be available at: `http://localhost:3000`

### **2. Setup Python Environment**

```bash
# Create a virtual environment (recommended)
python -m venv yolo_env

# Activate virtual environment
# Windows:
yolo_env\Scripts\activate
# Mac/Linux:
source yolo_env/bin/activate

# Install Python dependencies
pip install ultralytics opencv-python numpy
```

### **3. YOLO Model Preparation**

Required folder structure:

```bash
yolo-learning-app/
├── model2/
│   ├── shape.pt    # Custom shape detection model (optional)
│   └── name.pt     # Custom object detection model (optional)
├── scripts/
│   └── yolo_detection.py
└── hasil/          # Folder for saved images (auto-created)
```

**Note:** If custom models are not available, the script will fallback to pre-trained YOLO:

```python
# The script automatically downloads the model on first run
model = YOLO('yolov8n.pt')  # Nano version (lightweight)
```

---

Happy Detecting & Learning! 🌟
