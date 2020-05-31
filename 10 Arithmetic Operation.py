'''
Date: 30-05-2020. Aditya Raj.
Level = Beginners.
Objective = Arithmetic operations on images.
'''

import numpy as np
import cv2

img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')
print(img.shape)
print(img.size)
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

ball = img[280:340, 330:390]
img[270:330, 10:70] = ball

img = cv2.resize(img, (512,512))
img2 = cv2.resize(img2, (512,512))

#dst = cv2.add(img, img2 )
dst = cv2.addWeighted(img, .8, img2, .2 , 0)
#[273:333, 100:160]

'''


# To find (x,y) coordinates. Run this program
def click_event(event, x, y, flags, param): #opens a new window of the color where mouse click
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)

'''
#cv2.imshow('Image', img)
cv2.imshow('ADD', dst)

#cv2.setMouseCallback('Image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
