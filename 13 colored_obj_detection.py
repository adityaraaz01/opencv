'''
Date: 01-06-2020. Aditya Raj.
Level = Beginners.
Objective = Detection of colored object using OpenCV by taking video input through webcam.
'''

import numpy as np
import cv2

def nothing(x): #Dummy Function
    pass

cap = cv2.VideoCapture(0);
cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)# Lower Hue
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)# Lower saturation
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)# Lower Value
cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)# Upper Hue
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)# Upper Saturation
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)# Upper Value

while True:
    #frame = cv2.imread('smarties.png')
    # we can also take input as an image and detect colored object on that image
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")

    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")

    l_b = np.array([l_h, l_s, l_v]) #lower bound for specific color
    u_b = np.array([u_h, u_s, u_v]) #upper bound for specific color

    mask1 = cv2.inRange(hsv, l_b, u_b)

    res = cv2.bitwise_and(frame, frame, mask = mask1)

    cv2.imshow("frame", frame)
    #cv2.imshow("Masked", mask1) #This window shows mask.
    cv2.imshow("Resultant", res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()