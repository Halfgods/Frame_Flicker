import os
import shutil

# === CONFIGURATION ===
INPUT_DIR = 'yt/frames'  # Current folder (where original frames are)
OUTPUT_DIR = 'every_3rd_frame'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Sort frames (assumes names like 0001.jpg, 0002.jpg...)
frames = sorted([f for f in os.listdir(INPUT_DIR) if f.endswith('.jpg')])

# Keep every 3rd frame
for i, filename in enumerate(frames):
    if i % 3 == 0:
        shutil.copy(os.path.join(INPUT_DIR, filename), os.path.join(OUTPUT_DIR, filename))

print(f"✅ Copied every 3rd frame to: {OUTPUT_DIR}")
