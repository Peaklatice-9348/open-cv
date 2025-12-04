import cv2
from PIL import Image
import time
import numpy

video = cv2.VideoCapture(r'lesson 7\video.mp4')
for i in range(60):
    return_val, background = video.read()
    if return_val == False:
        continue
# To join hands one hand has to be the mirror image of the other.
background = numpy.flip(background, axis = 1)

while(video.isOpened()):
    return_val,frame = video.read()
    if return_val == False:
        break
    frame = numpy.flip(frame,axis=1)
    hsvframe = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    lower_red = numpy.array([100,40,40])
    higher_red = numpy.array([100,255,255])
    mask1 = cv2.inRange(hsvframe,lower_red,higher_red)

    lower_red2 = numpy.array([155,40,40])
    higher_red2 = numpy.array([180,255,255])
    mask2 = cv2.inRange(hsvframe,lower_red2,higher_red2)

    mask1 = mask1+mask2

    mask1 = cv2.morphologyEx(mask1,cv2.MORPH_OPEN,numpy.ones((3,3),numpy.uint8),iterations=2)
    mask1 = cv2.dilate(mask1,numpy.ones((3,3),numpy.uint8),iterations=1)
    mask2 = cv2.bitwise_not(mask1)
    result1 = cv2.bitwise_and(background,background,mask=mask1)
    result2 = cv2.bitwise_and(frame,frame,mask=mask2)
    final_result = cv2.addWeighted(result1,1,result2,1,0)
    cv2.imshow('final_result',final_result)
    k=cv2.waitKey(10)
    if k == 27:
        break


    