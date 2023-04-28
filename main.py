# Importing Libraries
import cv2
import mediapipe as mp
import pyautogui

# Used to convert protobuf message to a dictionary.
from google.protobuf.json_format import MessageToDict

# Initializing the Model
mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False, min_detection_confidence=0.75, min_tracking_confidence=0.75, max_num_hands=1)

mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(1)
last_vertical, last_horizontal = 0, 0

while True:
    # Read video frame by frame
    success, img = cap.read()

    # Flip the image(frame)
    img = cv2.flip(img, 1)

    # Convert BGR image to RGB image
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # imgRGB = img

    # Process the RGB image
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for id, lm in enumerate(results.multi_hand_landmarks[0].landmark):
            h, w, _ = imgRGB.shape
            cx, cy = int(lm.x*w), int(lm.y*h)
            #
            # if id in [4,3,2,1,0]:
            #     cv2.circle(img, (cx, cy), 20, (0, 0, 255))
            #
            # if id in [8,7,6,5,0]:
            #     cv2.circle(img, (cx, cy), 21, (0, 255, 0))
            #
            # if id in [12,11,10,9,0]:
            #     cv2.circle(img, (cx, cy), 22, (255, 0, 0))
            #
            # if id in [16,15,14,13,0]:
            #     cv2.circle(img, (cx, cy), 23, (0, 0, 0))
            #
            # if id in [20,19,18,17,0]:
            #     cv2.circle(img, (cx, cy), 24, (0, 255, 255))

            if id == 0:
                if last_vertical or last_horizontal:
                    diff_vertical = cy - last_vertical
                    diff_horizontal = cx - last_horizontal
                    # print(diff_horizontal, diff_vertical)

                    if abs(diff_horizontal) < abs(diff_vertical):
                        # vertical
                        if not(abs(diff_vertical) <= 10):
                            if diff_vertical > 0:
                                print("down")
                                pyautogui.press("down")
                            else:
                                print("top")
                                pyautogui.press("up")
                    else:
                        # vertical
                        if not (abs(diff_horizontal) <= 10):
                            if diff_horizontal > 0:
                                print("right")
                                pyautogui.press("right")
                            else:
                                print("left")
                                pyautogui.press("left")
                last_vertical = cy
                last_horizontal = cx


            cv2.circle(img, (cx, cy), 3, (100, 100, 100))

        mp_draw.draw_landmarks(img, results.multi_hand_landmarks[0], mp.solutions.hands.HAND_CONNECTIONS)

    # Display Video and when 'q'
    # is entered, destroy the window
    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break


