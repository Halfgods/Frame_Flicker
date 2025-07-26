import cv2
import numpy as np
from sklearn.cluster import KMeans
import json 
with open("config.json", "r") as f:
    config = json.load(f)
def get_dominant_hsv_range(roi, k=2):
    """Extracts dominant HSV color range using KMeans clustering."""
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    pixels = hsv.reshape((-1, 3))

    kmeans = KMeans(n_clusters=k, n_init='auto')
    kmeans.fit(pixels)
    
    # Get dominant cluster (largest)
    labels, counts = np.unique(kmeans.labels_, return_counts=True)
    dominant = kmeans.cluster_centers_[labels[np.argmax(counts)]]

    # Add buffer around dominant HSV
    h, s, v = dominant
    lower = np.array([max(h - 15, 0), max(s - 50, 0), max(v - 50, 0)], dtype=np.uint8)
    upper = np.array([min(h + 15, 179), min(s + 50, 255), min(v + 50, 255)], dtype=np.uint8)

    return lower, upper

def capture_background(cap, num_frames=30):
    """Captures a clean background frame with no object in front."""
    for i in range(num_frames):
        ret, frame = cap.read()
        if ret:
            bg = np.copy(frame)
    return bg

def main():
    cap = cv2.VideoCapture(config["ipcam_url"])  # Use 0 for webcam
    cap.set(3, 640)  # Width
    cap.set(4, 480)  # Height

    print("[INFO] Capturing background... Please move away from frame.")
    cv2.waitKey(2000)
    background = capture_background(cap)

    print("[INFO] Place the cloak inside the green box to calibrate.")
    lower_bound, upper_bound = None, None

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)

        # Define ROI in center
        h, w = frame.shape[:2]
        cx, cy = w // 2, h // 2
        size = 60
        roi = frame[cy-size:cy+size, cx-size:cx+size]

        # Draw rectangle
        cv2.rectangle(frame, (cx-size, cy-size), (cx+size, cy+size), (0, 255, 0), 2)
        cv2.putText(frame, "Place cloak here & press 'c'", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        if lower_bound is not None:
            # Convert to HSV and create mask
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, lower_bound, upper_bound)
            mask_inv = cv2.bitwise_not(mask)

            cloak_area = cv2.bitwise_and(background, background, mask=mask)
            rest = cv2.bitwise_and(frame, frame, mask=mask_inv)
            final = cv2.addWeighted(cloak_area, 1, rest, 1, 0)
            cv2.imshow("Invisible Cloak", final)
        else:
            cv2.imshow("Invisible Cloak", frame)

        key = cv2.waitKey(1)
        if key == ord('c'):
            lower_bound, upper_bound = get_dominant_hsv_range(roi)
            print("[INFO] Cloak color calibrated.")
        elif key == 27:
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
