import cv2

class Camera:
    def __init__(self, source=0):
        self.cap = cv2.VideoCapture(source)
        if not self.cap.isOpened():
            raise Exception("No camera detected.")
        
    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            raise Exception("Failed to capture image")
        return frame

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()