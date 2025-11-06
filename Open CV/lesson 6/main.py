import cv2
import os
from PIL import Image

path = "lesson 6\Images"
os.chdir(path)
num_of_images = len(os.listdir('.'))
width = 0
height = 0
files = os.listdir('.')

for file in files:
    image = Image.open(file)
    w,h = image.size
    width += w
    height += h

width = width//num_of_images
height = height//num_of_images
print(f'width:{width} height:{height}')

