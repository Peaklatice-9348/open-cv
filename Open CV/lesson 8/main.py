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
while count<30:
    (isread,image) = webcam.read()
    
    g_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = facecascade.detectMultiScale(g_image,1.3,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,100,0),2)
        face = g_image[y:y+h,x:x+w]
        face_resized = cv2.resize(face,(width,height))
        cv2.imwrite(rf'{path}\animage{count}.png',face_resized)
        cv2.imshow('animage',face_resized)
    count+=1

    cv2.waitKey(1)

webcam.release()