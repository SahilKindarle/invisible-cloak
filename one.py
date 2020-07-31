import numpy as np
import cv2
import time


cap = cv2.VideoCapture(0) # Connected to webcam, "(0)" means the first webvcam connected to laptop or device. YOu can run this program on a vide as well just pass the path to video in brackets in place of 0 like ("voide.mp4")


time.sleep(2) #takes 2 sec to setuo anadjust envionment


background=0 #Capturing the background


for i in range(20): #20 iterations are passed in order to get 20 images of steady background

    ret, background = cap.read() #Reading the background using video caputure object, ret is a boolean it tells whether it get the input or not


while(cap.isOpened()):

    ret, img = cap.read() #Getting every single frame and every command below eill get executed, ret is a boolean it tells whether it get the input or not

    if not ret: # it executes when ret is false that means when it does not gets input i.e thw python program is closed

        break; 

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_red = np.array([170, 120, 70])
    upper_red = np.array([180, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    mask = mask1 + mask2

    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3), np.uint8), iteration=2)

    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3,3), np.uint8), iteration=1)

    mask2 = cv2.bitwise_not(mask1)

    res1 = cv2.bitwise_and(background, background, mask=mask1)
    res2 = cv2.bitwise_and(img, img, mask=mask2)

    final_output = cv2.addWeighted(res1,1,res2,1, 0)

    cv2.imshow("Sahil Here", final_output)
    k = cv2.waitKey(10)

    if k == 27:
        break

    cap.release()
    cv2.destroyAllWindows