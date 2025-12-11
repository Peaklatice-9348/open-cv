import cv2
import numpy
import os 

dataset = r"lesson 8\images"
subdata = 'Yusuf'
haarfile = r'lesson 8\haarcascade_frontalface_default.xml'

path = os.path.join(dataset,subdata)

if not os.path.isdir(path):
    os.mkdir(path)

(width,height) = (130,100)
webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

facecascade =cv2.CascadeClassifier(haarfile)
count = 0
while True:
    (isread,image) = webcam.read()
    cv2.imshow('animage',image)
    count+=1
    t = cv2.waitKey(1)
    if t==27:
        break
webcam.release()