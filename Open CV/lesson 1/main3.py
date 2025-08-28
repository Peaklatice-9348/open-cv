import cv2
kirbyimage = cv2.imread('lesson 1/kirby.jpg',cv2.IMREAD_UNCHANGED)
metaknightimage = cv2.imread('lesson 1/metaknight.jpg',cv2.IMREAD_UNCHANGED)
newimage = cv2.addWeighted(kirbyimage,0.3,metaknightimage,0.3,0)
cv2.imshow('kirby',kirbyimage)
cv2.imshow('meta knight',metaknightimage)
cv2.imshow('huh',newimage)
cv2.waitKey(0)
