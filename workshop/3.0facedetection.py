import cv2

camera=cv2.VideoCapture(0)
#initializing the video source, 6-default webcam, 1-USB cameras
#give the file path to load a video in your computer
#give the ip address to load wifi camera

#loaded a pretrained face detection ML classifier
face_clsfr=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while(1):
    ret,img=camera.read()

    #color convert to gray
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #results=clsfr.predict(test_data)
    faces=face_clsfr.detectMultiScale(gray)

    for x,y,w,h in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    
    #gray live
    cv2.imshow('GRAY',gray)
    #color live 
    cv2.imshow('LIVE',img)
    
    #delay
    cv2.waitKey(1)
