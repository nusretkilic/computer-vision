import sys
import cv2
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QLabel, QVBoxLayout, QRadioButton, QLineEdit, 
    QPushButton, QFileDialog
)
from PyQt6.QtCore import Qt, QTimer
from face_detection import FaceDetection
from heart_rate_monitor import HeartRateMonitor
from data_holder import DataHolder
from mode_type import ModeType
from param_config import ParamConfig
from ui_v2 import Ui_main_window


class MainWindow(QMainWindow, Ui_main_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.param_config = ParamConfig()
        self.data_holder = DataHolder()

        self.cap = None
        self.timer = QTimer(self)
        self.camera_active = False

        self.apply_params_btn.clicked.connect(self.on_apply_params)
        self.start_btn.clicked.connect(self.on_start)
        self.stop_btn.clicked.connect(self.stop_camera)
        self.browse_file_btn.clicked.connect(self.on_browse)

        self.timer.timeout.connect(self.update_frame)

        self.label.setFixedSize(300, 300)
        self.label_2.setFixedSize(300, 300)

    def on_apply_params(self):
        """
        Applies user-specified parameters and prints them to the console.
        """
        self.update_param_config()
        print(f"Mode: {self.param_config.mode}")
        print(f"Path: {self.param_config.path}")
        print(f"Use GPU: {self.param_config.gpu}")

    def update_param_config(self):
        """
        Updates the parameter configuration based on user input from the UI.
        """
        if self.video_mode_button.isChecked():
            self.param_config.mode = ModeType.VIDEO.value
        elif self.real_time_mode.isChecked():
            self.param_config.mode = ModeType.CAMERA.value

        if self.gpu_true_radio.isChecked():
            self.param_config.gpu = True
        elif self.gpu_false_radio.isChecked():
            self.param_config.gpu = False

        if self.param_config.mode == ModeType.VIDEO.value:
            self.param_config.path = self.path_display_line.text()
        elif self.param_config.mode == ModeType.CAMERA.value:
            self.param_config.path = 0

    def on_browse(self):
        """
        Opens a file dialog to select a video file and sets its path in the UI.
        """
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Video", "", "Video Files (*.mp4 *.avi)")
        if file_path:
            self.path_display_line.setText(file_path)

    def on_start(self):
        """
        Starts the process based on the selected parameters.
        """
        self.start_process_with_params()

    def start_process_with_params(self):
        """
        Starts video or camera processing based on the mode selected by the user.
        """
        if self.param_config.mode == ModeType.VIDEO.value:
            self.process_video_or_camera(self.param_config.path)
        elif self.param_config.mode == ModeType.CAMERA.value:
            self.process_video_or_camera(0)

    def process_video_or_camera(self, source):
        """
        Handles common initialization for both camera and video processing.
        """
        self.cap = cv2.VideoCapture(source)

        if not self.cap.isOpened():
            print(f"Unable to open source: {source}")
            return

        self.heart_rate_monitor = HeartRateMonitor()
        self.face_detection = FaceDetection()

        self.camera_active = True
        self.timer.start(30) 

    def update_frame(self):
        """
        Captures and processes frames, detects faces, and calculates heart rate.
        """
        ret, frame = self.cap.read()
        if not ret:
            self.stop_camera()
            return

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        detections = self.face_detection.detect_faces(rgb_frame)

        if detections.detections:
            for det in detections.detections:
                self.heart_rate_monitor.process_face_roi(frame, det)

        heart_rate = self.heart_rate_monitor.get_heart_rate()
        self.data_holder.add_new_bpm_input(heart_rate)

        self.label.setText(f"BPM: {heart_rate:.2f}")

        self.display_video(frame)

    def display_video(self, frame):
        """
        Converts a video frame to QPixmap and displays it in a QLabel.
        """
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        height, width, _ = frame.shape

        qimg = QImage(frame_rgb.data, width, height, 3 * width, QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(qimg)

        self.label_2.setPixmap(pixmap.scaled(self.label_2.size(), Qt.AspectRatioMode.KeepAspectRatio))

    def stop_camera(self):
        """
        Stops the camera or video processing.
        """
        self.camera_active = False
        if self.cap:
            self.cap.release()
        self.timer.stop()
        self.label_2.clear()
        self.label.setText("BPM: 0")

    def closeEvent(self, event):
        """
        Ensures all resources are released when the application is closed.
        """
        self.stop_camera()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
