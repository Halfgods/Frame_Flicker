import cv2
import os

# === Crop coordinates based on original 1080x1920 ===
x1, y1 = 5, 380
x2, y2 = 1074, 1336

# === Input and output folders ===
input_folder = "yt/every_3rd_frame"
output_folder = "yt/cropped"
os.makedirs(output_folder, exist_ok=True)

# === Process all .jpg files in input folder ===
for filename in sorted(os.listdir(input_folder)):
    if not filename.endswith(".jpg"):
        continue

    input_path = os.path.join(input_folder, filename)
    img = cv2.imread(input_path)
    if img is None:
        print(f"❌ Failed to load: {input_path}")
        continue

    # Crop image
    cropped = img[y1:y2, x1:x2]

    # Save to cropped folder with same filename
    output_path = os.path.join(output_folder, filename)
    cv2.imwrite(output_path, cropped)
    print(f" Saved: {output_path}")
