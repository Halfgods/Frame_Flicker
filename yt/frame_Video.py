import cv2
import os
from natsort import natsorted

# === CONFIGURATION ===
FRAME_DIR = 'yt/cropped'  # Directory with frames like 0001.jpg
OUTPUT_VIDEO = 'Output.mp4'
FPS = 24

# Get all .jpg files sorted naturally
frame_files = natsorted([f for f in os.listdir(FRAME_DIR) if f.endswith('.jpg')])

# Load first frame to get size
first_frame = cv2.imread(os.path.join(FRAME_DIR, frame_files[0]))
height, width, _ = first_frame.shape

# Define video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(OUTPUT_VIDEO, fourcc, FPS, (width, height))

# Write frames
for filename in frame_files:
    frame_path = os.path.join(FRAME_DIR, filename)
    frame = cv2.imread(frame_path)
    out.write(frame)

out.release()
print(f"✅ Done. Video saved as {OUTPUT_VIDEO}")

# ffmpeg -i Output.mp4 -c:v libx264 -crf 23 -preset fast Cropp.mp4
