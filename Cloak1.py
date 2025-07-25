# import cv2

# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # Flip for mirror
#     frame = cv2.flip(frame, 1)

#     # Resize to 4K artificially
#     upscale_frame = cv2.resize(frame, (3840, 2160), interpolation=cv2.INTER_CUBIC)

#     cv2.imshow("Upscaled 4K", upscale_frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
import cv2
import numpy as np
import time

# Step 1: Start webcam
cap = cv2.VideoCapture("https://192.168.21.194:8080/video")
time.sleep(2)  # Wait for camera to warm up

# Step 2: Capture static background (60 frames avg)
print("Capturing background. Stay out of frame...")
for i in range(60):
    ret, bg = cap.read()
    if not ret:
        continue
    bg = cv2.flip(bg, 1)

print("Background captured!")

# Step 3: Tune dark red HSV range
# Red wraps around HSV (0–180), so we define two ranges
lower_red1 = np.array([0, 120, 50])
upper_red1 = np.array([10, 255, 255])

lower_red2 = np.array([160, 120, 50])
upper_red2 = np.array([180, 255, 255])

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Step 4: Create masks for dark red cloak
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = cv2.add(mask1, mask2)

    # Step 5: Refine the mask (remove noise)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN,
                            np.ones((3, 3), np.uint8), iterations=2)
    mask = cv2.dilate(mask, np.ones((3, 3), np.uint8), iterations=1)

    # Step 6: Invert the mask to get foreground (non-cloak)
    mask_inv = cv2.bitwise_not(mask)

    # Extract background where cloak is
    cloak_area = cv2.bitwise_and(bg, bg, mask=mask)

    # Extract current frame where cloak is not
    foreground = cv2.bitwise_and(frame, frame, mask=mask_inv)

    # Combine cloak area and current frame
    final_output = cv2.add(cloak_area, foreground)

    cv2.imshow("Invisible Cloak - Dark Red", final_output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
