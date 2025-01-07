import mediapipe as mp

class FaceDetection:
    """
    A wrapper class for MediaPipe's face detection module.
    """

    def __init__(self, min_detection_confidence=0.2):
        """
        Initializes the FaceDetection instance.

        Args:
            min_detection_confidence (float): Minimum confidence threshold for detecting faces.
        """
        self.mp_face_detection = mp.solutions.face_detection
        self.face_detection = self.mp_face_detection.FaceDetection(min_detection_confidence)

    def detect_faces(self, rgb_frame):
        """
        Detects faces in an RGB image frame.

        Args:
            rgb_frame: An image frame in RGB format.

        Returns:
            A Detection object containing the results of face detection.
        """
        return self.face_detection.process(rgb_frame)
