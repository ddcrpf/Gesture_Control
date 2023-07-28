import cv2
import mediapipe as mp
import pyautogui
import time



cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

while True:
  ret , frame = cap.read()
  if not ret:
    break
  image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  result = hands.process(image_rgb)
  
  if result.multi_hand_landmarks:
    for hand_landmarks in result.multi_hand_landmarks:
      mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
      
      thumb_tip  = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
      index_finger_tip  = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
      middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
      ring_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
      pinky_tip  = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
      
      
      cv2.putText(frame, f"Thumb tip y: {round(thumb_tip.y, 2)}", (10, 20), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
      cv2.putText(frame, f"Index finger tip y: {round(index_finger_tip.y, 2)}", (10, 60), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
      cv2.putText(frame, f"Middle finger tip y: {round(middle_finger_tip.y, 2)}", (10, 90), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
      cv2.putText(frame, f"Ring finger tip y: {round(ring_finger_tip.y, 2)}", (10, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
      cv2.putText(frame, f"Pinky tip y: {round(pinky_tip.y, 2)}", (10, 150), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
      
      
      
      is_hand_closed = (
        index_finger_tip.y > thumb_tip.y and
        middle_finger_tip.y > thumb_tip.y and
        ring_finger_tip.y > thumb_tip.y and
        pinky_tip.y > thumb_tip.y
      )
      
      if is_hand_closed:
        pass
      else:
        pyautogui.press("space")
        time.sleep(0.1)
        
      cv2.imshow("hand_gesture", frame)
      
  if cv2.waitKey(1) & 0xFF == ord("q"):
        break
        
cap.release()      
cv2.destroyAllWindows()
  