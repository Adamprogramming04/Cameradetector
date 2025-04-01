import cv2
import mediapipe as mp
import numpy as np


mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils


cap = cv2.VideoCapture(0)

# Hand tracking model
with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5, max_num_hands=2) as hands:
    
    prev_x, prev_y = None, None  

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

       
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        gesture_text = ""

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
               
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                
                landmark_list = hand_landmarks.landmark
                h, w, _ = frame.shape

                
                index_finger_tip = (int(landmark_list[8].x * w), int(landmark_list[8].y * h))
                thumb_tip = (int(landmark_list[4].x * w), int(landmark_list[4].y * h))
                wrist = (int(landmark_list[0].x * w), int(landmark_list[0].y * h))

               
                if prev_x is not None:
                    movement = abs(index_finger_tip[0] - prev_x)
                    if movement > 30:  # Threshold for wave detection
                        gesture_text = "Waving!"

                prev_x, prev_y = index_finger_tip

               
                distance = np.linalg.norm(np.array(index_finger_tip) - np.array(thumb_tip))
                if distance < 40:  # Adjust based on real-life testing
                    gesture_text = "Holding a pen!"

        if gesture_text:
            cv2.putText(frame, gesture_text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Hand Gesture Recognition", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
