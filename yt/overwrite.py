import cv2
import os

# === Settings ===
INPUT_DIR = "yt/cropped"
TEMPLATE_FILENAME = "0015.jpg"
START = 16
END = 54

# === Load the reference image once ===
template_path = os.path.join(INPUT_DIR, TEMPLATE_FILENAME)
template_img = cv2.imread(template_path)

if template_img is None:
    raise FileNotFoundError(f"❌ Failed to load: {template_path}")

# === Overwrite all in range ===
for i in range(START, END + 1):
    filename = f"{i:04d}.jpg"
    target_path = os.path.join(INPUT_DIR, filename)

    if os.path.exists(target_path):
        cv2.imwrite(target_path, template_img)
        print(f"Overwritten: {filename}")
    else:
        pass
