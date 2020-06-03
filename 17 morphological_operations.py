'''
Date: 03-06-2020. Aditya Raj.
Level = Beginners.
Objective = Learn different morphological operations like Erosion, Dilation, Opening, Closing etc.
'''

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('smarties.png', 0)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)
#Applying mask as Morphological transformations are generally performed on binary images.

kernal = np.ones((2,2), np.uint8) # structuring element

dilation = cv2.dilate(mask, kernal, iterations = 3)
#Dilation: Increases the white region in the image or size of foreground object increases.

erosion = cv2.erode(mask, kernal, iterations=1)
#Erosion: Erodes away the boundaries of foreground object.

#dilation1 = cv2.dilate(erosion, kernal, iterations = 3)

opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal) #Erosion followed by Dilation.

closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)#Dilation followed by Erosion.

mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal) #Difference between dilation and erosion of an image.

th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal)# Difference between input image and Opening of the image.


titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'mg', 'th']
images = [img, mask, dilation, erosion, opening, closing, mg, th]





for i in  range(8):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()









cv2.waitKey(0)
cv2.destroyAllWindows()