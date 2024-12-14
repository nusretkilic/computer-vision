import mediapipe as mp

class FaceDetection:
    def __init__(self, min_detection_confidence=0.2):
        self.mp_face_detection = mp.solutions.face_detection
        self.face_detection = self.mp_face_detection.FaceDetection(min_detection_confidence)

    def detect_faces(self, rgb_frame):
        return self.face_detection.process(rgb_frame)