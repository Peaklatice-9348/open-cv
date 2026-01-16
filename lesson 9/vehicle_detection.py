import cv2
import pytesseract

video='lesson 9/Cars.mp4'
video = cv2.VideoCapture(video)

haarfile='lesson 9/cars.xml'
platefile='lesson 9/haarcascade_frontalface_default.xml'

carcascade =cv2.CascadeClassifier(haarfile)
plate_cascade= cv2.CascadeClassifier(platefile)

while(video.isOpened()):
    return_val,frame = video.read()
    if return_val == False:
        break
    grame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cars = carcascade.detectMultiScale(grame,1.1,3)
    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,100,0),2)
        vehicle_gray = grame[y:y+h,x:x+w]
        vehicle = frame[y:y+h,x:x+w]
        plates = plate_cascade.detectMultiScale(vehicle,1.1,8)
        for (px,py,pw,ph)in plates:
            cv2.rectangle(frame,(px,py),(px+pw,py+ph),(0,100,0),2)
            plate_region =vehicle_gray[py:py+ph,px:px+pw]
            plate_text = pytesseract.image_to_string(plate_region,config='--psm 8 --oem 3')
            cv2.putText(frame,plate_text.strip(),(x,y-10),1,1,(0,0,0),1)
    cv2.imshow('video',frame)
    esc = cv2.waitKey(10)
    if esc == 27:
        break
video.release()
cv2.destroyAllWindows()

