import cv2
import numpy as np
sahur = cv2.imread('lesson 1/download (5).jpg',1)
cv2.imshow('tung sahur',sahur)

cv2.waitKey(0)
cv2.destroyAllWindows()

#bluring image

#gaussin
import cv2
sahur = cv2.imread('lesson 1/download (5).jpg',1)

gaussin = cv2.GaussianBlur(sahur,(7,7),0)
cv2.imshow('tung tung sahur',gaussin)
cv2.waitKey(0)
cv2.destroyAllWindows()

#median
import cv2
sahur = cv2.imread('lesson 1/download (5).jpg',1)

median = cv2.medianBlur(sahur,9)
cv2.imshow('tung tung tung sahur',median)
cv2.waitKey(0)
cv2.destroyAllWindows()

#bilateral
import cv2
sahur = cv2.imread('lesson 1/download (5).jpg',1)

bilateral = cv2.bilateralFilter(sahur,0,75,75)
cv2.imshow('tung tung tung tung sahur',bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()

#bordering
import cv2
sahur = cv2.imread('lesson 1/download (5).jpg',1)

border = cv2.copyMakeBorder(sahur,105,105,15,15,cv2.BORDER_CONSTANT,value=0)
cv2.imshow('tung tung tung tung sahur',border)
cv2.waitKey(0)
cv2.destroyAllWindows()

#reflective bordering
import cv2
sahur = cv2.imread('lesson 1/download (5).jpg',1)

border = cv2.copyMakeBorder(sahur,1500,1500,1500,1500,cv2.BORDER_REFLECT,value=50)
cv2.imshow('tung tung tung tung sahur',border)
cv2.waitKey(0)
cv2.destroyAllWindows()