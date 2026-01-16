import cv2
import numpy
import os

video='lesson 9/Cars.mp4'
haarfile='lesson 9/cars.xml'
video = cv2.VideoCapture(video)

carcascade =cv2.CascadeClassifier(haarfile)

while(video.isOpened()):
    return_val,frame = video.read()
    if return_val == False:
        break
    grame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cars = carcascade.detectMultiScale(grame,1.1,3)
    for car in cars:
        x,y,w,h=car
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,100,0),2)
    cv2.imshow('video',frame)
    esc = cv2.waitKey(10)
    if esc == 27:
        break
        



    

