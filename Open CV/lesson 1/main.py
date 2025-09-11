
import cv2

#load the image in colour from using 1 or cv2.IMREAD_COLOR
image = cv2.imread('lesson 1/pikachu.png',1)
cv2.imshow('pikachu',image)

cv2.waitKey(0)
cv2.destroyAllWindows()

image2 = cv2.imread('lesson 1/pikachu.png',cv2.IMREAD_COLOR)
cv2.imshow('pikachu',image2)

cv2.waitKey(0)
cv2.destroyAllWindows()

#load the image in greyscale/black and white from using 0 or cv2.IMREAD_GRAYSCALE
image3 = cv2.imread('lesson 1/pikachu.png',0)
cv2.imshow('pikachu',image3)

cv2.waitKey(0)
cv2.destroyAllWindows()

image4 = cv2.imread('lesson 1/pikachu.png',cv2.IMREAD_GRAYSCALE)
cv2.imshow('pikachu',image4)

cv2.waitKey(0)
cv2.destroyAllWindows()

#load the image unchanged from using -1 or cv2.IMREAD_UNCHANGED
image5 = cv2.imread('lesson 1/pikachu.png',-1)
cv2.imshow('pikachu',image5)

cv2.waitKey(0)
cv2.destroyAllWindows()

image6 = cv2.imread('lesson 1/pikachu.png',cv2.IMREAD_UNCHANGED)
cv2.imshow('pikachu',image6)

cv2.waitKey(0)
cv2.destroyAllWindows()

#saving the image after making changes
import cv2
import os

image_folder = 'C:/Users/navee/OneDrive/Desktop/Python/Build GUI/Open CV/images'
image7 = cv2.imread('lesson 1/pikachu.png',cv2.IMREAD_GRAYSCALE)
cv2.imshow('pikachu',image7)

cv2.waitKey(0)
cv2.destroyAllWindows()

#change current execution directory

os.chdir(image_folder)

#write image to this directory
cv2.imwrite('pikachoo.png',image7)
print('message')

#printing images in a different colour form
import cv2
image8 = cv2.imread('lesson 1/pikachu.png',cv2.IMREAD_UNCHANGED)

#red green blue
#open cv stores images using BGR instead of RGB

b,g,r = cv2.split(image8)

cv2.imshow('original',image8)
cv2.waitKey(0)

cv2.imshow('blue saturation image',b)
cv2.waitKey(0)

cv2.imshow('green saturation image',g)
cv2.waitKey(0)

cv2.imshow('red saturation image',r)
cv2.waitKey(0)

cv2.destroyAllWindows()

