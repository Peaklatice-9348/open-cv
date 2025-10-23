import cv2
import numpy as np
image = cv2.imread('lesson 6/image.png',1)
params = cv2.SimpleBlobDetector_Params()
params.filterByArea = True
params.minArea = 100

#set circularity filtering parametrers
params.filterByCircularity = True
params.minCircularity = 0.9

#set convexity filtering parametrers
params.filterByConvexity = True
params.minConvexity = 0.2

#set inertia filtering parametrers
params.filterByInertia = True
params.minInertiaRatio = 0.01

#creating detector
detector = cv2.SimpleBlobDetector_create(params)
keypoints = detector.detect(image)
blank = np.zeros((1,1))
blob = cv2.drawKeypoints(image,keypoints,blank,(0,0,0),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
number_of_blobs = len(keypoints)
text = 'number of circular blobs: '+str(len(keypoints))
cv2.putText(blob,text,(600,580),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),3)
cv2.imshow('blob',blob)

cv2.waitKey(0)
