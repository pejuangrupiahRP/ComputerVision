# 🎯 Detektif Bentuk & Benda - Aplikasi Pembelajaran Interaktif

## 📚 Latar Belakang  
Kemajuan pesat teknologi komputer dan kecerdasan buatan—khususnya dalam bidang **computer vision**—telah membuka berbagai aplikasi inovatif yang tak terbatas.  
Salah satu aspek fundamental dari computer vision adalah kemampuan untuk **mengenali dan menginterpretasi bentuk secara otomatis** dari data visual, baik dari gambar statis maupun streaming video langsung.

**Deteksi bentuk** memainkan peran penting dalam analisis gambar digital, dengan aplikasi dalam:

- 🏭 Manufaktur (inspeksi kualitas)  
- 🎥 Sistem pengawasan otomatis  
- 🤖 Robotika (navigasi dan interaksi)  
- 🧩 Pengenalan pola  
- 🏫 Alat pembelajaran edukatif

Proyek ini menampilkan **sistem deteksi bentuk real-time** menggunakan **OpenCV**, **YOLO (You Only Look Once)**, **Next.js**, dan **Python** untuk mengidentifikasi bentuk geometri dasar seperti:

- 🔺 Segitiga  
- 🟥 Persegi  
- 🟦 Persegi Panjang  
- 🟠 Lingkaran  
- ⭐ Bintang
- 🥚 Oval

Sistem ini mendukung input dari **webcam langsung** dan menampilkan antarmuka web yang **ramah anak** dengan fitur gamifikasi untuk pembelajaran yang menyenangkan.

---

## 🎮 Fitur Utama

### 🌟 **Antarmuka Web Interaktif**
- **Desain ramah anak** dengan warna-warna cerah dan animasi menarik
- **Tampilan real-time** dari kamera dengan area scan yang jelas
- **Kontrol mudah** dengan tombol besar dan intuitif

### 🎯 **Sistem Gamifikasi**
- **Sistem Skor** - Dapatkan poin untuk setiap deteksi dan gambar yang disimpan
- **Streak Counter** - Hitung deteksi berturut-turut untuk bonus poin
- **Tantangan Harian** - Misi khusus seperti "Pemburu Lingkaran" dan "Master Persegi"
- **Achievement System** - Badge pencapaian untuk memotivasi pembelajaran
- **Progress Tracking** - Statistik pembelajaran yang komprehensif

### 🔊 **Efek Audio & Visual**
- **Efek suara** untuk deteksi, penyimpanan, dan pencapaian
- **Animasi perayaan** saat mencapai milestone
- **Visual feedback** dengan warna dan animasi yang menarik

### 📚 **Konten Edukatif**
- **Fakta menarik** tentang setiap bentuk geometri
- **Informasi dalam bahasa Indonesia** yang mudah dipahami
- **Visual cards** dengan penjelasan yang menarik

---

## 🚧 Ruang Lingkup & Keterbatasan

1. **Jenis Bentuk yang Terdeteksi**  
   Saat ini mendukung deteksi bentuk geometri dasar: **segitiga, persegi, persegi panjang, lingkaran, bintang, dan oval**.  
   Deteksi bentuk yang lebih kompleks atau tidak beraturan belum diimplementasikan.

2. **Pencahayaan & Lingkungan**  
   Performa sistem dapat menurun dalam kondisi:
   - Pencahayaan ekstrem (terlalu terang/gelap)
   - Noise gambar yang tinggi
   - Latar belakang yang sibuk atau kompleks

3. **Kompatibilitas Browser**  
   Memerlukan browser modern yang mendukung WebRTC untuk akses kamera.

---

## 🎯 Tujuan

- 💡 Mengimplementasikan algoritma deteksi bentuk menggunakan **OpenCV**, **YOLO**, dan **Python** untuk mengidentifikasi bentuk geometri dasar.
- 📷 Menerima input gambar dari webcam/kamera langsung
- 🏷️ Memberikan anotasi pada bentuk yang terdeteksi dengan:
  - Garis batas berwarna
  - Label nama bentuk (misalnya "Lingkaran", "Persegi Panjang")
- 🎮 Menyediakan pengalaman pembelajaran yang interaktif dan menyenangkan untuk anak-anak
- 📊 Melacak kemajuan pembelajaran dengan sistem skor dan achievement

---

## 🌟 Manfaat

- 🎓 **Pembelajaran Interaktif**  
  Input kamera real-time mengubah pembelajaran pasif menjadi pengalaman yang menarik dan eksploratif.

- 🔎 **Pembelajaran Berbasis Eksplorasi**  
  Mendorong pengguna untuk aktif mencari dan mengidentifikasi bentuk di lingkungan mereka, mempromosikan pendidikan berbasis penemuan.

- 🎮 **Gamifikasi Pembelajaran**  
  Sistem poin, tantangan, dan achievement membuat pembelajaran menjadi seperti bermain game.

- 👶 **Ramah Anak**  
  Antarmuka yang dirancang khusus untuk anak-anak dengan visual yang menarik dan kontrol yang mudah.

---

## ✅ Hasil

Aplikasi ini memungkinkan pengguna untuk menjelajahi dan mengenali bentuk di sekitar mereka menggunakan webcam atau kamera mobile.  
Dengan memanfaatkan **computer vision**, sistem **secara otomatis mendeteksi bentuk** seperti segitiga, persegi, persegi panjang, lingkaran, bintang, dan oval dalam **waktu nyata**.

Bentuk yang terdeteksi akan:

- 🖼️ **Digarisbawahi di layar** dengan kotak berwarna
- 🏷️ **Diberi label dengan nama bentuknya**
- 🎯 **Ditampilkan di panel deteksi terbaru**
- 📸 **Dapat disimpan sebagai koleksi gambar**

Membuat pengalaman belajar menjadi edukatif dan menyenangkan!

---

## 📦 Teknologi yang Digunakan

### **Frontend (Web Interface)**
- **Next.js 15** ⚡ - React framework untuk aplikasi web
- **React 18** ⚛️ - Library UI interaktif
- **TypeScript** 📝 - Type-safe JavaScript
- **Tailwind CSS** 🎨 - Styling framework
- **shadcn/ui** 🧩 - Komponen UI modern
- **Lucide React** 🎯 - Icon library

### **Backend (Detection Engine)**
- **Python 3.8+** 🐍 - Bahasa pemrograman utama
- **OpenCV** 👁️‍🗨️ - Computer vision library
- **YOLO (Ultralytics)** 🔎 - Object detection model
- **NumPy** 🔢 - Numerical computing

### **Additional Features**
- **Web Audio API** 🔊 - Efek suara
- **WebRTC** 📹 - Akses kamera browser
- **CSS Animations** ✨ - Animasi dan transisi

---

## 🚀 Cara Instalasi dan Menjalankan

### **Prasyarat**
\`\`\`bash
# Pastikan Node.js terinstall (minimal v18)
node --version

# Pastikan Python terinstall (minimal v3.8)
python --version
\`\`\`

### **1. Setup Web Interface (Next.js)**

\`\`\`bash
# Clone atau extract project
cd yolo-learning-app

# Install dependencies
npm install

# Jalankan development server
npm run dev
\`\`\`

Web interface akan berjalan di: `http://localhost:3000`

### **2. Setup Python Environment**

\`\`\`bash
# Buat virtual environment (opsional tapi direkomendasikan)
python -m venv yolo_env

# Aktifkan virtual environment
# Windows:
yolo_env\Scripts\activate
# Mac/Linux:
source yolo_env/bin/activate

# Install Python dependencies
pip install ultralytics opencv-python numpy
\`\`\`

### **3. Persiapan Model YOLO**

Struktur folder yang diperlukan:
\`\`\`
yolo-learning-app/
├── model2/
│   ├── shape.pt    # Model untuk deteksi bentuk (opsional)
│   └── name.pt     # Model untuk deteksi objek (opsional)
├── scripts/
│   └── yolo_detection.py
└── hasil/          # Folder untuk menyimpan gambar (otomatis dibuat)
\`\`\`

**Catatan:** Jika tidak memiliki model custom, script akan menggunakan model pre-trained YOLO:

```python
# Script akan otomatis download model pertama kali
model = YOLO('yolov8n.pt')  # Nano version (paling ringan)
