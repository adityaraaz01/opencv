'''
Date: 03-06-2020. Aditya Raj.
Level = Beginners.
Objective = Adaptive Thresholding Techniques.
'''

import numpy as np
import cv2

img = cv2.imread('sudoku.png', 0)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2);
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2);





cv2.imshow("Image", img)
cv2.imshow("th3", th3)
cv2.imshow("th2", th2)









cv2.waitKey(0)
cv2.destroyAllWindows()