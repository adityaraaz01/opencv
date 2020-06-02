'''
Date: 03-06-2020. Aditya Raj.
Level = Beginners.
Objective = Matplotlib with OpenCV. Showing all simple thresholding methods in a single window.
'''

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('gradient.png', 0)
_,th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)# Pixel value > Threshold will assign to 255 and Pixel value < Threshold will assign to zero
_,th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)# Just opposite of THRESH_BINARY
_,th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)# After threshold the pixel value will remain that of the threshold value.
_,th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)#Pixel value < Threshold value will be assigned to zero.
_,th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV) #Just opposite of THRESH_TOZERO

titles = ['Original Image', 'Binary', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img ,th1, th2, th3, th4, th5]

for i in  range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()