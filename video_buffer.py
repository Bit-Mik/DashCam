import cv2
import numpy as np
import threading as th
import datetime as dt
import os

# Ensure the output directory exists
output_dir = "output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    
# Define buffer parameters
fps = 30  # Frames per second
duration = 5 * 60  # 5 minutes in seconds
buffer_size = fps * duration

# Initialize the circular buffer
buffer = [None] * buffer_size
index = 0
lock = th.Lock()
save_threads = []  # List to keep track of save threads

# Function to save recent footage
def save_recent_footage(frames_to_save):
    frames = [f for f in frames_to_save if f is not None]

    if not frames:
        print("No frames to save.")
        return

    # Define video writer
    height, width, _ = frames[0].shape
    size = (width, height)
    date = dt.datetime.now().strftime("%Y%m%d_%H%M")
    out_path = os.path.join(output_dir, f"{date}.avi")
    out = cv2.VideoWriter(out_path, cv2.VideoWriter_fourcc(*'XVID'), fps, size)

    if not out.isOpened():
        print("Error: Unable to open video writer.")
        return

    # Write frames to the video file
    for frame in frames:
        ret, jpeg = cv2.imencode('.jpg', frame)
        if ret:
            frame = cv2.imdecode(jpeg, cv2.IMREAD_COLOR)
            out.write(frame)

    out.release()
    print(f"Recent footage saved to {out_path}.")

# Function to capture video frames
def capture_frames():
    global index
    cap = cv2.VideoCapture(0)  # '0' selects the default camera

    if not cap.isOpened():
        print("Error: Unable to access the camera.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to read frame.")
            break

        with lock:
            buffer[index] = frame
            index = (index + 1) % buffer_size

        # Display the frame (optional)
        cv2.imshow('Live Feed', frame)

        # Break loop on 'q' key press
        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):
            with lock:
                start = index % buffer_size
                frames_to_save = buffer[start:] + buffer[:start]
            save_thread = th.Thread(target=save_recent_footage, args=(frames_to_save,))
            save_thread.start()
            save_threads.append(save_thread)
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print("Press 's' to save and 'q' to quit.")
    capture_thread = th.Thread(target=capture_frames)
    capture_thread.start()
    capture_thread.join()

    # Wait for all save threads to finish
    for save_thread in save_threads:
        save_thread.join()
