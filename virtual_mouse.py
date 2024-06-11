#This imports the OpenCV library, which is used for computer vision tasks such as image and video processing.means capturing video 
import cv2
#This imports the MediaPipe library, which provides pre-trained machine learning models for computer vision tasks. Here, it's used for hand detection and tracking.
import mediapipe as mp
#This imports the PyAutoGUI library, which allows Python to control and automate GUI tasks, like moving the mouse and clicking.

import pyautogui

cap = cv2.VideoCapture(0)
#This initializes the MediaPipe Hands solution, which detects and tracks hands in the video frames.
hand_detector =mp.solutions.hands.Hands()
#This initializes drawing utilities from MediaPipe, which are used to draw hand landmarks on the frames.
#hamre hath pe 21 point hai 0 se leke 20 tak
drawing_utils = mp.solutions.drawing_utils
#This gets the width and height of the screen in pixels using PyAutoGUI, which will be used to map hand coordinates to screen coordinates.
screen_width, screen_height = pyautogui.size()
#This initializes a variable to store the y-coordinate of the index finger, used for mouse movement.
index_y = 0
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    #This converts the frame from BGR color space (default in OpenCV) to RGB color space (expected by MediaPipe).
    rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    #This processes the RGB frame to detect and track hands using the MediaPipe Hands model. The result is stored in output
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame,hand)
            #This draws the hand landmarks on the frame for visualization.
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)
                #This checks if the current landmark is the tip of the index finger (landmark ID 8).
                if id == 8:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_height*y
                    pyautogui.moveTo(index_x, index_y)
                    #This checks if the current landmark is the tip of the thumb (landmark ID 4).

                if id == 4:
                    #This draws a yellow circle on the frame at the thumb tip location for visualization
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                    thumb_x = screen_width/frame_width*x
                    thumb_y = screen_height/frame_height*y
                    print('outside', abs(index_y - thumb_y))
                    #his checks if the vertical distance between the index finger tip and the thumb tip is less than 40 pixels, indicating a clicking gesture.
                    if (abs(index_y - thumb_y) < 40):
                        #If the click gesture is detected, this clicks the mouse and pauses for 1 second to prevent multiple rapid clicks.
                        pyautogui.click()
                        pyautogui.sleep(1)
    print(hands)
    cv2.imshow('Virtual Mouse', frame)
    #This waits for 1 millisecond for a key press. It allows the frame to be displayed and the loop to continue running smoothly.
    cv2.waitKey(1)
Why are you using it?

You are using OpenCV to capture video from the webcam, process each video frame, and display the processed frames. Specifically, OpenCV helps you read frames from the webcam, flip them, convert color formats, and display the results.
How are you using it?

cv2.VideoCapture(0): Opens the webcam to capture video.
cap.read(): Reads a frame from the webcam.
cv2.flip(frame, 1): Flips the frame horizontally.
cv2.cvtColor(frame, cv2.COLOR_BGR2RGB): Converts the frame from BGR to RGB color format.
cv2.circle(...): Draws circles on the frame for visualization.
cv2.imshow('Virtual Mouse', frame): Displays the processed frame in a window.
cv2.waitKey(1): Keeps the window open and refreshes it every millisecond.
What is MediaPipe?

MediaPipe is a framework developed by Google that provides pre-trained machine learning models for a variety of computer vision tasks. It simplifies the use of complex models for tasks like hand tracking, face detection, pose estimation, and more.
Why are you using it?

You are using MediaPipe to detect and track the position of hands in the video frames. Specifically, the Hands solution from MediaPipe can identify and provide coordinates of key points (landmarks) on the hands.
How are you using it?

mp.solutions.hands.Hands(): Initializes the hand tracking model.
hand_detector.process(rgb_frame): Processes the RGB frame to detect hands and their landmarks.
output.multi_hand_landmarks: Retrieves the detected hand landmarks.
mp.solutions.drawing_utils: Provides utilities to draw the detected hand landmarks on the frame for visualization.
What is PyAutoGUI?

PyAutoGUI is a library that allows you to control the mouse and keyboard programmatically. It can be used to move the mouse cursor, click, type on the keyboard, and perform other GUI automation tasks.
Why are you using it?

You are using PyAutoGUI to control the mouse cursor based on the detected position of your hand. It enables you to move the cursor and perform click actions using hand gestures detected by the webcam.
How are you using it?

pyautogui.size(): Gets the width and height of the screen.
pyautogui.moveTo(index_x, index_y): Moves the mouse cursor to the specified screen coordinates.
pyautogui.click(): Simulates a mouse click.
pyautogui.sleep(1): Pauses the execution for 1 second to avoid multiple clicks being registered too quickly.

. Key Components and Workflow
Video Capture: "We use OpenCV to capture video frames from the webcam."
Hand Detection and Tracking: "MediaPipe's pre-trained hand tracking model is used to detect and track hand landmarks within the video frames."
Mouse Control: "PyAutoGUI is used to move the mouse cursor and perform click actions based on the detected hand gestures."
3. Technical Details
Frame Processing: "Each frame is captured and flipped horizontally for a mirror effect. It's then converted from BGR to RGB color space because MediaPipe expects RGB input."
Hand Landmark Detection: "The MediaPipe model identifies key points on the hand, such as the tips of the fingers and joints."
Gesture to Action Mapping: "The coordinates of specific landmarks (index finger and thumb tips) are mapped to screen coordinates. When the index finger moves, the mouse cursor follows. If the distance between the thumb and index finger tips is small, a click action is triggered."
