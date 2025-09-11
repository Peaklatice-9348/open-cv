import cv2
import numpy as np
import os

image1 = cv2.imread('lesson 1/download (3).jpg',cv2.IMREAD_UNCHANGED)
image2 = cv2.imread('lesson 1/download (4).jpg',cv2.IMREAD_UNCHANGED)
newimage = cv2.addWeighted(image1,0.5,image2,0.5,0)
'''
cv2.imshow('image1',image1)
cv2.imshow('image2',image2)
cv2.imshow('huh',newimage)
cv2.waitKey(0)

image_folder = 'C:/Users/navee/OneDrive/Desktop/Python/Build GUI/Open CV/images'
cv2.imshow('huh',newimage)

cv2.waitKey(0)
cv2.destroyAllWindows()
os.chdir(image_folder)
cv2.imwrite('newimage2.png',newimage)
print('message')
'''
#subtraction
image3 = cv2.imread('images/newimage2.png',cv2.IMREAD_UNCHANGED)
new_image = cv2.subtract(image3,image2)
new_image2 = cv2.subtract(image3,image1)
new_image3 = cv2.subtract(image1,image2)
new_image4 = cv2.subtract(image2,image1)
new_image5 = cv2.subtract(image2,image3)
new_image6 = cv2.subtract(image1,image3)
new_image7 = cv2.subtract(image3,image3)
cv2.imshow('image1',image1)
cv2.imshow('image2',image2)
cv2.imshow('image3',image3)
cv2.imshow('image4',new_image)
cv2.imshow('image5',new_image2)
cv2.imshow('image6',new_image3)
cv2.imshow('image7',new_image4)
cv2.imshow('image8',new_image5)
cv2.imshow('image9',new_image6)
cv2.imshow('image10',new_image7)
cv2.waitKey(0)