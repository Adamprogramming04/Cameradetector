##Camera Detetector

## Overview
This project utilizes **OpenCV** and **MediaPipe** to detect hand gestures in real-time using a webcam. It can identify:

- **Waving Gesture** – Detects when the user waves their hand.
- **Holding a Pen** – Recognizes when the thumb and index finger are close together, simulating a pen-holding position.

## Installation
To install the required dependencies, run:

```sh
pip install opencv-python mediapipe numpy
```

## How It Works
### Hand Tracking with MediaPipe
- Detects hand landmarks and draws them on the screen.
- Tracks the position of key points like the **index finger tip** and **thumb tip**.

### Gesture Recognition
- **Waving Detection**: If the index finger moves side-to-side rapidly, it's considered a wave.
- **Pen Detection**: If the **index finger tip** and **thumb tip** are close together, it assumes the user is holding a pen.

### Live Webcam Feed
- Opens a window displaying the real-time video feed.
- Detected gestures are overlaid as text on the screen.

## Usage
Run the script using:

```sh
python hand_gesture_recognition.py
```

Press `q` to **exit** the program.

## Code Explanation
### MediaPipe Hands
- Used to track and detect hand key points.
- Identifies important landmarks such as the index finger and thumb tip.

### OpenCV
- Captures video from the webcam and processes frames in real-time.
- Converts images to RGB format for MediaPipe processing.

### NumPy
- Used for mathematical calculations, such as measuring the distance between fingers.

## Future Improvements
### Planned Features
- Add more gesture recognition (thumbs-up, pointing, etc.).
- Integrate voice feedback using text-to-speech (TTS).
- Implement object detection (pen, phone, cup, etc.) using YOLO or TensorFlow.

## License
This project is open-source and available for modification and use under the MIT License.

