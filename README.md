# 🧥 Invisible Cloak — OpenCV Magic


> *"It is our choices, Harry, that show what we truly are..."* — Dumbledore

A real-time invisibility cloak using **OpenCV + NumPy** (optionally KMeans from `scikit-learn`), built to run smooth even on potato laptops (4GB RAM, no GPU).

## ⚡ What Makes This Special

🟩 **User-Defined Cloak Color** — Hold your cloak in the center box. We detect it.  
🎯 **Robust Detection** — No hardcoded HSV. Uses **KMeans clustering** to lock in the dominant color.  
🪄 **Real-Time Illusion** — Background gets swapped over cloak-colored pixels, making you disappear.  
🔌 **Zero BS Setup** — Just calibrate once, then vanish on command.

## 🧠 How It Works (Fast Version)

1. **Capture Background**  
   - You move out → We snap a clean background.

2. **Detect Cloak Color**  
   - You hold cloak in center box → We cluster it → Lock dominant color.

3. **Magic Loop Begins**  
   - Each frame → mask cloak-color pixels → replace with background → BOOM: you're invisible.

## 🚀 Getting Started

```bash
git clone https://github.com/Halfgods/Invisible-cloak.git
cd invisible-cloak
pip install -r requirements.txt
```
Create and Update Config.json`:
```bash
config = {
    "ipcam_url": 0  # Use 0 for built-in webcam
}
```

Then run:
```bash
python Filename.py
```

## ✅ Features

- 🖥️ Runs on low-spec machines  
- 🎨 Dynamic color detection via KMeans (or fallback NumPy logic)  
- 📷 Supports webcam + IP cam  
- 🧑‍💻 Minimal user interaction, smooth UX  

## 🤝 Contribute

Pull requests welcome — whether it's smarter detection, a slicker UI, or a port to edge devices.

---

Want to feel like a wizard? Clone the repo, grab a cloak, and disappear. 🪄
Sayonara
