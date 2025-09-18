import cv2
image = cv2.imread('lesson 3/kirby.jpg')
(row,column) = image.shape[:2]
a = cv2.getRotationMatrix2D((column/2,row/2),90,1)
#0.5=half 2=doubled 1=original size of image

result = cv2.warpAffine(image,a,(column,row))
cv2.imshow('kirby',result)

cv2.waitKey(0)
cv2.destroyAllWindows()
#edge detection in an image
import cv2
image = cv2.imread('lesson 1/metaknight.jpg')

edge = cv2.Canny(image,1,200)
cv2.imshow('kirby2',edge)
cv2.waitKey(0)
cv2.destroyAllWindows()

#grayscaling of an image read as colour-using cvtColor() funtion
import cv2

image = cv2.imread('lesson 1/kirby.jpg')
gimage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow('kirby3',gimage)
cv2.waitKey(0)
cv2.destroyAllWindows()

#inverted image
import cv2

image = cv2.imread('lesson 1/kirby.jpg')
gimage = cv2.bitwise_not(image)

cv2.imshow('kirby3',gimage)
cv2.waitKey(0)
cv2.destroyAllWindows()

#HSV
import cv2

image = cv2.imread('lesson 1/kirby.jpg')
gimage = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
image2 = cv2.imread('lesson 1/download (5).jpg')
gimage2 = cv2.cvtColor(image2,cv2.COLOR_BGR2HSV)

cv2.imshow('kirby3',gimage)
cv2.imshow('Feather',gimage2)
cv2.waitKey(0)
cv2.destroyAllWindows()