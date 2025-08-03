import cv2
import os

def extract_all_frames(video_path, output_dir="frames"):
    os.makedirs(output_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        raise Exception(f"❌ Could not open video: {video_path}")

    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_path = os.path.join(output_dir, f"frame_{frame_count:05d}.jpg")
        cv2.imwrite(frame_path, frame)
        frame_count += 1

    cap.release()
    print(f"✅ Extracted {frame_count} frames to '{output_dir}'")

# Run it
video_file = "yt/downloads/short.f616.mp4"  # Replace with your actual path
extract_all_frames(video_file, "frames")
