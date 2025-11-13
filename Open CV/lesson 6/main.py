import cv2
import os
from PIL import Image

path = "lesson 6\Images"
os.chdir(path)
num_of_images = len(os.listdir('.'))
width = 0
height = 0
files = os.listdir('.')

#getting the mean width and height
for file in files:
    image = Image.open(file)
    w,h = image.size
    width += w
    height += h

width = width//num_of_images
height = height//num_of_images
print(f'width:{width} height:{height}')

#changing the dimentions of the images
for file in files:
    if file.endswith('.png') or file.endswith('.jpg') or  file.endswith('.jpeg'):
        image = Image.open(file)
        resized_img = image.resize((width,height),Image.Resampling.LANCZOS)
        resized_img.save(file,'JPEG',quality=95)

video = 'video.avi'
list_of_images = []
list = os.listdir('.')
for file in list:
    if file.endswith('.jpeg') or file.endswith('.png') or file.endswith('.jpg'):
        list_of_images.append(file)

frame1 = cv2.imread(list_of_images[0])
h,w,layers = frame1.shape
video_file = cv2.VideoWriter(video,0,1,(w,h))

for image in list_of_images:
    video_file.write(cv2.imread(image))
cv2.destroyAllWindows()
video_file.release()