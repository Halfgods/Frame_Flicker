import cv2

# === Load and resize image ===
original = cv2.imread("yt/every_3rd_frame/0072.jpg")
original_h, original_w = original.shape[:2]

resized_w, resized_h = 400, 500
resized = cv2.resize(original, (resized_w, resized_h))
scale_x = original_w / resized_w
scale_y = original_h / resized_h

# === Globals ===
drawing = False
x1, y1 = -1, -1

def mouse_callback(event, x, y, flags, param):
    global x1, y1, drawing, resized

    temp = resized.copy()

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        x1, y1 = x, y

    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        cv2.rectangle(temp, (x1, y1), (x, y), (0, 255, 0), 2)
        cv2.imshow("Draw Rectangle", temp)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        x2, y2 = x, y
        cv2.rectangle(temp, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.imshow("Draw Rectangle", temp)

        orig_x1 = int(x1 * scale_x)
        orig_y1 = int(y1 * scale_y)
        orig_x2 = int(x2 * scale_x)
        orig_y2 = int(y2 * scale_y)

        print(f"Selected region in original image:")
        print(f"x1={orig_x1}, y1={orig_y1}, x2={orig_x2}, y2={orig_y2}")

cv2.namedWindow("Draw Rectangle")
cv2.setMouseCallback("Draw Rectangle", mouse_callback)
cv2.imshow("Draw Rectangle", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
