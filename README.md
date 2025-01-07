# Computer Vision

## Description

The purpose of this project is to measure heart rate using a small-scale camera feed or a video by analyzing a face. The application is still under development and may have incomplete or unrefined features.

## Installation

### Pre-requirements

- **Python 3.12**: Required because Mediapipe does not yet support Python 3.13.

### Steps

1. **Create a virtual environment:**

    ```bash
    python3.12 -m venv venv
    ```

2. **Activate the virtual environment:**

    On macOS/Linux:

    ```bash
    source venv/bin/activate
    ```

    On Windows:
    ```bash
    venv\Scripts\activate
    ```

3. **Install the necessary requirements:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application:**

    Ensure that your video or camera feed is accessible, and run the application:
    
    ```bash
    python app.py
    ```

### Limitations

- **GPU Processing**: Advanced GPU functionality is not yet implemented. The application currently defaults to using CPU for processing.
  
- **Performance**: Accuracy may vary depending on lighting conditions. It is recommended to use the application in well-lit environments to get the best results.

### Usage

1. **Select the Mode**: Choose between video or real-time camera mode.
   
2. **For Video Mode**: Browse and select the desired video file for processing.

3. **For Camera Mode**: Ensure your webcam or camera is properly connected.

4. **GPU**: Set GPU to false as it is not yet supported.

5. **Apply the Parameters**: Once the settings are configured, click "Start" to begin the heart rate monitoring.

The program will begin processing the input feed and display the heart rate.

## Features

- Measure heart rate from a **real-time camera feed**.
- Measure heart rate from a **video file** input.

### Future Improvements

- **Enhanced BPM accuracy** through improved detection algorithms.
- **Data export functionality** for analysis (CSV, etc.).
- **Graphical representation** of heart rate data over time.
- **Face region selection** and better OpenCV-based precision for face detection.

### Known Issues

- **Low Light Conditions**: The face detection may struggle or be inaccurate under low light, resulting in poor heart rate detection.
