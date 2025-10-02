import cv2
import numpy as np
image = cv2.imread('lesson 5/eyes.png',1)
image2 = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
image3 = cv2.blur(image2,(3,3))

detected_circles = cv2.HoughCircles(image3,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=50)

if detected_circles is not None:
    detected_circle = np.uint16(np.around(detected_circles))

    for i in detected_circles[0,:]:
        a,b,r = i[0],i[1],i[2]
        cv2.circle(image,(a,b),r,(200,0,0),2)
        cv2.circle(image,(a,b),1,(0,200,0),4)
        cv2.imshow('circles',image)
        cv2.waitKey(0)