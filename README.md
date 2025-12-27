# 🖐️ Two-Hand Smart Mouse Control (Computer Vision)

A computer vision–based smart mouse system that allows you to control your mouse cursor using **hand gestures captured via webcam**.

- **Left hand** → Mouse movement  
- **Right hand** → Clicks, Drag, Scroll  
- Built using **OpenCV, MediaPipe, and PyAutoGUI**
- No hardware required except a webcam

---

## ✨ Features

- Smooth and stable mouse movement
- Gesture-based:
  - Left Click
  - Right Click
  - Drag & Drop
  - Scroll
- Two-hand separation for better accuracy
- Adjustable smoothing and control area
- Real-time performance

---

## 🧠 How It Works (High Level)

- The webcam captures frames using OpenCV
- MediaPipe detects hands and landmarks
- Gestures are interpreted based on finger distances
- PyAutoGUI sends mouse commands to the OS

---

## 📂 Project Structure



HandMouseController/
│
├── main.py # Main loop & orchestration

├── camera.py # Camera handling

├── hand_tracking.py # MediaPipe processing

├── gestures.py # Gesture logic (click, drag, scroll)

├── mouse_control.py # Mouse movement & actions

├── utils.py # Helper math functions

└── README.md


---

## 🧩 Requirements

- Python **3.10 or 3.11** (recommended)
- Webcam
- Supported OS:
  - Windows ✅
  - macOS ✅
  - Linux ✅ (may need extra camera permissions)

---

## 📥 Installation Guide

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/mhmdtmrsid-lab/Hand_Mouse.git
cd Hand_Mouse

2️⃣ Create a Virtual Environment (Recommended)

Windows👇
python -m venv venv
venv\Scripts\activate

macOS / Linux👇
python3 -m venv venv
source venv/bin/activate

3️⃣ Install Required Libraries (Manual Installation)

Install the dependencies manually using pip:

pip install opencv-python
pip install mediapipe
pip install pyautogui
pip install numpy


ℹ️ MediaPipe may take a few minutes to install.
Make sure you are using Python 3.10 or 3.11 for best compatibility.

▶️ Run the Project

From the project folder:

python main.py


Allow camera permissions if prompted

Press ESC to exit

🖐️ Gesture Mapping
🖱 Mouse Movement

Left Hand

Index finger controls cursor position

👆 Left Click

Right Hand

Index finger + thumb pinch

👉 Right Click

Right Hand

Middle finger + thumb pinch

✊ Drag & Drop

Right Hand

Make a fist → drag

Release fist → drop

🔄 Scroll

Right Hand

Raise index & middle fingers together

Move fingers up/down to scroll

⚙️ Customization

You can tweak parameters inside the code:

Smoothing factor

Scroll sensitivity

Gesture thresholds

Screen mapping margin

All logic is modular and easy to extend.

⚠️ Notes

Keep your hand well-lit for better detection

Avoid cluttered backgrounds

First few seconds help MediaPipe stabilize tracking

🚀 Future Improvements

GUI for calibration

Gesture customization

AI-based gesture learning

Multi-monitor support

🤝 Contributing

Pull requests are welcome.
Feel free to fork and improve the project.
