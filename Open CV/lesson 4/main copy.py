#lines on an image
import cv2

image = cv2.imread('lesson 4/city.png')
p1 = (100,20)
p2 = (140,50)
p3 = (125,100)
p4 = (75,100)
p5 = (60,50)
color = (0,150,150)
thickness = 8

image = cv2.line(image,p1,p3,color,thickness)
image = cv2.line(image,p3,p5,color,thickness)
image = cv2.line(image,p5,p2,color,thickness)
image = cv2.line(image,p2,p4,color,thickness)
image = cv2.line(image,p4,p1,color,thickness)
cv2.imshow('name',image)

cv2.waitKey(0)
cv2.destroyAllWindows()