import cv2
import os
import subprocess
import sys

def create_dir_if_not_exists(directory):
    """Creates a directory if it does not already exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def download_video(url, output_path):
    """Downloads a video from a given URL using yt-dlp."""
    print(f"Downloading video from: {url}")
    command = [
        'yt-dlp',
        '-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        '-o', output_path,
        url
    ]
    try:
        process = subprocess.run(command, check=True, capture_output=True, text=True)
        print("Download successful.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error downloading video: {e.stderr}", file=sys.stderr)
        return False
    except FileNotFoundError:
        print("Error: yt-dlp command not found.", file=sys.stderr)
        print("Please ensure yt-dlp is installed and in your system's PATH.", file=sys.stderr)
        sys.exit(1)


def extract_frames(video_path, output_folder):
    """Extracts all frames from a video file and saves them as images."""
    print(f"Extracting frames from: {video_path}")
    video_capture = cv2.VideoCapture(video_path)
    if not video_capture.isOpened():
        print(f"Error: Could not open video file at {video_path}", file=sys.stderr)
        return

    create_dir_if_not_exists(output_folder)

    frame_count = 0
    while True:
        success, frame = video_capture.read()
        if not success:
            break

        frame_filename = os.path.join(output_folder, f"{frame_count:05d}.jpg")
        cv2.imwrite(frame_filename, frame)
        frame_count += 1

    video_capture.release()
    print(f"Successfully extracted {frame_count} frames to '{output_folder}'.")

def main():
    """Main function to download a YouTube Short and extract its frames."""
    if len(sys.argv) != 2:
        print("Usage: python process_short.py <youtube_shorts_url>", file=sys.stderr)
        sys.exit(1)

    youtube_url = sys.argv[1]
    downloads_dir = "/home/halfy/Desktop/everything/yt/downloads"
    frames_dir = "frames"
    video_filepath = os.path.join(downloads_dir, "short.mp4")

    create_dir_if_not_exists(downloads_dir)

    if download_video(youtube_url, video_filepath):
        extract_frames(video_filepath, frames_dir)

if __name__ == "__main__":
    main()
