import cv2
import os
from PIL import Image
os.chdir('C:\\Users\\navee\\OneDriveDesktop\\tem')
path = 'C:\\Users\\navee\\OneDriveDesktop\\tem'

mean_width = 0
mean_height = 0
num_images = len(os.listdir(''))

for img in os.listdir('.'):
    imgg = Image.open(os.path.join(path,img))
    width,height = imgg.size
    mean_width = mean_width+width
    mean_height = mean_height+height

mean_width = mean_width/num_images
mean_height = mean_height/num_images

for img in os.listdir('.'):
    if img.endswith('.jpeg') or img.endswith('.jpg') or img.endswith('.png'):
        file = Image.open(os.path.join(path,img))
        width,height = imgg.size
        print(width,height)
        
        resized_img = img.resize((mean_width,mean_height),Image.Resampling.LANCZOS)
        resized_img.save(img,'.png',quality=95)
    print(img,split('\\')[-1],'rezized')



def video_generator():
    video_name = 'videoname.avi'

    os.chdir('C:\\Users\\navee\\OneDriveDesktop\\tem')
    images = []
    for img in os.listdir('.'):
        if img.endswith('.jpeg') or img.endswith('.jpg') or img.endswith('.png'):
            images.append(img)
    
    frame = cv2.imread(os.path.join('.',images[0]))
    height,width,layers = frame.shape
    video = cv2.VideoWriter(video_name,0,1,(width,height))
    for image in images:
        video.write(cv2.imread(os.path.join('.',image)))
    
    cv2.destroyAllWindows()
    video.release()
video_generator()