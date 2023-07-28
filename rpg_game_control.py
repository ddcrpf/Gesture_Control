

import mediapipe as mp
import cv2

import pyautogui
import time

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands


cap = cv2.VideoCapture(0)
pTime = 0
cTime = 0
with mp_hands.Hands(min_detection_confidence = 0.8, min_tracking_confidence = 0.5) as hands:
  while cap.isOpened():
    
    ret, frame = cap.read()
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = hands.process(image)
    
    image.flags.writeable = True
    
    

    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
    print(results)
    
    
    

    
    
    
    
    if results.multi_hand_landmarks:
      for num , hand in enumerate(results.multi_hand_landmarks):
  
        mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS, 
                                  mp_drawing.DrawingSpec(color = (121,22,76), thickness = 2, circle_radius = 4),
                                  mp_drawing.DrawingSpec(color = (250,44,250), thickness = 2, circle_radius = 2))
        
        thumb_tip  = hand.landmark[mp_hands.HandLandmark.THUMB_TIP]
        index_finger_tip  = hand.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
        # middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
        # ring_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
        pinky_tip  = hand.landmark[mp_hands.HandLandmark.PINKY_TIP]
        wrist = hand.landmark[mp_hands.HandLandmark.WRIST]
        
          # forward motion
        if index_finger_tip.y < wrist.y:
          pyautogui.press("up")
          time.sleep(0.1)
        #backward motion
        if index_finger_tip.y > wrist.y:
          pyautogui.press("down")
          time.sleep(0.1)
        # left motion
        if thumb_tip.y< pinky_tip.y:
          pyautogui.press("left")
          time.sleep(0.1)
        #right motion 
        if thumb_tip.y> pinky_tip.y:
          pyautogui.press("right")
          time.sleep(0.1)
      
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(image, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                      (255, 0, 255), 3)

    
    
    cv2.imshow("Hand Tracking", image)
    
    if cv2.waitKey(10) & 0xFF == ord("q"):
      break
cap.release()
cv2.destroyAllWindows()