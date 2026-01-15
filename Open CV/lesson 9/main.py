import cv2
import numpy
import os 

dataset = r"lesson 8\images"
haarfile = r'lesson 9\haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(haarfile)

path = os.path.join(dataset)

images = []
labels = []
id = 0
names  = {}

for (subdirectorys,directorys,files) in os.walk(dataset):
    for directory in directorys:
        names[id]=directory

        path2 = os.path.join(path,directory)
        for file in os.listdir(path2):
            path3 = os.path.join(path2,file)
            image = cv2.imread(path3,0)
            images.append(image)
            labels.append(id)
        id+=1
(images,labels) = [numpy.array(list)for list in [images,labels]]

#training the model to reconize the images
model = cv2.face.LBPHFaceRecognizer_create()
model.train(images,labels)
webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    width = 130
    height = 100
    (isread,animage) = webcam.read()
    ganimage = cv2.cvtColor(animage,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(ganimage,1.3,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,100,0),2)
        face = ganimage[y:y+h,x:x+w]
        face_resized = cv2.resize(face,(width,height))
        (label,ps) = model.predict(face_resized)
        if ps<500:
            new_image = cv2.putText(animage,names[label],(10,30),cv2.FONT_ITALIC,1,(0,0,0),2)
        else:
            new_image = cv2.putText(animage,'not detected',(10,30),cv2.FONT_ITALIC,1,(0,0,0),2)
        new_image = cv2.putText(new_image,f'ps score:{round(ps,2)}',(10,50),cv2.FONT_ITALIC,1,(0,0,0),2)
    cv2.imshow('cam',animage)
    t = cv2.waitKey(10)
    if t==27:
        break

