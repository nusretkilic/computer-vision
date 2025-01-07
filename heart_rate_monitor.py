import numpy as np
import time
import cv2

class HeartRateMonitor:
    """
    Tracks and calculates heart rate using green channel intensity from a face region.
    """

    def __init__(self):
        """
        Initializes necessary variables for heart rate tracking.
        """
        self.time_data = []
        self.heart_rate_data = []
        self.heart_rate = 0

    def process_face_roi(self, frame, detection):
        """
        Processes the face region of interest (ROI) for heart rate calculation.

        Args:
            frame: Current video frame.
            detection: Detected face bounding box.
        """
        bboxC = detection.location_data.relative_bounding_box
        ih, iw, _ = frame.shape
        x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        face_roi = frame[y:y + h, x:x + w]
        green_channel = face_roi[:, :, 1]
        green_mean = np.mean(green_channel)

        self.time_data.append(time.time())
        self.heart_rate_data.append(green_mean)

        if len(self.time_data) > 100:
            time_diff = np.diff(self.time_data)
            heart_rate_signal = np.array(self.heart_rate_data[-100:])
            self.heart_rate = np.mean(heart_rate_signal)
            self.heart_rate_data = self.heart_rate_data[-100:]
            self.time_data = self.time_data[-100:]

    def get_heart_rate(self):
        """
        Returns the current heart rate.
        """
        return self.heart_rate
