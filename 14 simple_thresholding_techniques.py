'''
Date: 02-06-2020. Aditya Raj.
Level = Beginners.
Objective = Simple Thresholding Techniques.
'''

import numpy as np
import cv2

img = cv2.imread('gradient.png', 0)
_,th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)# Pixel value > Threshold will assign to 255 and Pixel value < Threshold will assign to zero
_,th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)# Just opposite of THRESH_BINARY
_,th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)# After threshold the pixel value will remain that of the threshold value.
_,th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)#Pixel value < Threshold value will be assigned to zero.
_,th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV) #Just opposite of THRESH_TOZERO


cv2.imshow("Image", img)
cv2.imshow("th1", th1)
#cv2.imshow("th2", th2)
cv2.imshow("th3", th3)
cv2.imshow("th4", th4)
#cv2.imshow("th5", th5)




cv2.waitKey(0)
cv2.destroyAllWindows()