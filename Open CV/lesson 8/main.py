import cv2
import numpy
import os 

dataset = r"lesson 8/images"
subdata = 'Yusuf'
haarfile = r'lesson 8/haarcascade_frontalface_default.xml'

path = os.path.join(dataset,subdata)

if not os.path.isdir(path):
    os.mkdir(path)

(width,height) = (130,100)
webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print('camera does not exist')

else:
    print('camera does exist')

facecascade =cv2.CascadeClassifier(haarfile)
count = 0

while count<10:
    (isread,image) = webcam.read()

    if isread == False:
        print('image not captured')

    else:
        print('image captured')
    
    g_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imwrite(f'{path}/animage{count}.png',g_image)
    cv2.imshow('animage',g_image)
    count+=1

    cv2.waitKey(1)
webcam.release()