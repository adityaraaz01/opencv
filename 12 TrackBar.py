'''
Date: 31-05-2020. Aditya Raj.
Level = Beginners.
Objective = Learn to add Trackbars in an OpenCV window by using cv::createTrackbar
'''


import numpy as np
import cv2

def nothing(x): #callback function
    print(x)




# To createe a black image, window
img = np.zeros((300,512,3), np.uint8)

cv2.namedWindow('image')

cv2.createTrackbar('B', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('R', 'image', 0, 255, nothing)

'''
While switch = 0, the image will be black
When switch = 1, image color changes corresponding to the [b,g,r]
'''

switch = '0 : OFF\n 1 : ON'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)
while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1)
    if k == 27:
        break
    b = cv2.getTrackbarPos('B', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    r = cv2.getTrackbarPos('R', 'image')
    s = cv2.getTrackbarPos(switch, 'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]


cv2.destroyAllWindows()



















cv2.waitKey(0),
cv2.destroyAllWindows()