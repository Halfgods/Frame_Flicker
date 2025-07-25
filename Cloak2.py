from threading import Thread
import cv2
import json

with open("config.json" , "r") as f:
    config = json.load(f)
class VideoStream:
    def __init__(self, src=(config[ipcam_url])):
        self.cap = cv2.VideoCapture(src)
        self.ret, self.frame = self.cap.read()
        self.running = True
        Thread(target=self.update, daemon=True).start()

    def update(self):
        while self.running:
            self.ret, self.frame = self.cap.read()

    def read(self):
        return self.frame

    def stop(self):
        self.running = False
        self.cap.release()

# Usage
stream = VideoStream("http://192.168.X.X:8080/video")
while True:
    frame = stream.read()
    if frame is not None:
        frame = cv2.resize(frame, (640, 480))
        cv2.imshow("Threaded Stream", frame)
    if cv2.waitKey(1) == ord('q'):
        break

stream.stop()
cv2.destroyAllWindows()
