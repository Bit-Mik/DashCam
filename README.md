# Dash Cam

## Overview
This project implements a **circular video buffer** that continuously records video frames but only saves the last 5 minutes when triggered. It is designed for efficient memory usage and fast saving using multi-threading.

## Features
- **Circular Buffer Implementation**: Stores the last 5 minutes of video in memory.
- **Multi-threading**: Uses threads for capturing and saving frames without blocking.
- **Automatic Frame Storage**: Captures frames at 30 FPS and maintains a buffer.
- **Save Last 5 Minutes**: Press 's' to save the last 5 minutes of footage.
- **Exit Easily**: Press 'q' to quit the application.

## Requirements
Make sure you have the following installed:
- **Python 3.x**
- **OpenCV** (`cv2` module)
- **NumPy**

### Install Dependencies
Run the following command to install the required libraries:
```sh
pip install opencv-python numpy
```

## How to Run the Script
1. Clone or download the project.
2. Open a terminal and navigate to the project directory.
3. Run the script:
   ```sh
   python video_buffer.py
   ```
4. The webcam feed will appear.
5. Press:
   - **'s'** to save the last 5 minutes of video.
   - **'q'** to quit the application.

## Folder Structure
```
dash-cam/
│── video_buffer.py   # Main script
│── output/           # Folder where saved videos are stored
│── README.md         # Documentation
```

## How It Works
- The script initializes a circular buffer with a size of `5 minutes * 30 FPS`.
- Frames are continuously captured and stored in memory.
- When 's' is pressed, the last 5 minutes of video is saved as an `.avi` file.
- When 'q' is pressed, the program stops.

## Possible Enhancements
- **Increase FPS**: Modify `fps` for smoother video.
- **Motion Detection**: Save frames only when motion is detected.
- **Video Compression**: Use `.mp4` instead of `.avi` for better compression.
- **Headless Mode**: Run without `cv2.imshow()` for server use.

## License
This project is open-source. Feel free to modify and improve it!

## Author
Biswajit Mallik

