import cv2
import numpy
import os 


webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

count = 0
while True:
    (isread,image) = webcam.read()
    cv2.imshow('animage',image)
    count+=1
    t = cv2.waitKey(1)
    if t==27:
        break
webcam.release()