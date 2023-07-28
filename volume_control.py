import cv2
import mediapipe as mp
import pyautogui
import time


cap =  cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)

mp_drawing = mp.solutions.drawing_utils

while True:
  ret, frame = cap.read()
  if not ret:
    break
  
  image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  
  result = hands.process(image_rgb)
  
  if result.multi_hand_landmarks:
    for hand_landmark in result.multi_hand_landmarks:
      mp_drawing.draw_landmarks(frame, hand_landmark, mp_hands.HAND_CONNECTIONS)
      
      index_finger_y = hand_landmark.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
      thumb_y = hand_landmark.landmark[mp_hands.HandLandmark.THUMB_TIP].y
      
      if index_finger_y < thumb_y:
        hand_gesture = "pointing up"
        
      elif index_finger_y > thumb_y:
        hand_gesture = "pointing down"
      else:
        hand_gesture = "no gesture"
        
        
      if hand_gesture == "pointing up":
        pyautogui.press("volumeup")
      elif hand_gesture == "pointing down":
        pyautogui.press("volumedown")
        
      cv2.imshow("hand_gesture", frame)
      
  if cv2.waitKey(1) & 0xFF == ord("q"):
        break
  
cap.release()
cv2.destroyAllWindows()
