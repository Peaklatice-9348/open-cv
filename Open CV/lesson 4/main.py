#lines on an image
import cv2

image1 = cv2.imread('lesson 4/city.png')
sp = (310,0)
sp2 =(430,0)
ep = (365,100)
color = (0,150,150)
thickness = 8

image101 = cv2.line(image1,sp,ep,color,thickness)
image102 = cv2.line(image101,sp2,ep,color,thickness)
cv2.imshow('image',image101)

cv2.waitKey()
cv2.destroyAllWindows()

#creating a rectangle on an image
import cv2

image2 = cv2.imread('lesson 4/flower.png')
sp = (20,20)
ep = (280,680)
color = (0,200,200)
thickness = 8

image201 = cv2.rectangle(image2,sp,ep,color,thickness)
cv2.imshow('image',image201)

cv2.waitKey()
cv2.destroyAllWindows()

#creating a rectangle on an image
import cv2

image3 = cv2.imread('lesson 4/pikachuu.png')
sp = (20,20)
ep = (100,100)
color = (0,0,0)
thickness = -1
ce = (250,100)
ra = 100


image301 = cv2.rectangle(image3,sp,ep,color,thickness)
cv2.imshow('image',image301)

cv2.waitKey()
cv2.destroyAllWindows()

image302 = cv2.circle(image3,ce,ra,color,thickness)
cv2.imshow('image',image302)

cv2.waitKey()
cv2.destroyAllWindows()

#creating a rectangle on an image
import cv2

image4 = cv2.imread('lesson 4/flower.png')
ce = (15,80)
tx = 'sun flower'
color = (0,150,150)
thickness = 8

image401 = cv2.putText(image4,tx,ce,1,3,color,thickness)
cv2.imshow('image',image401)

cv2.waitKey()
cv2.destroyAllWindows()