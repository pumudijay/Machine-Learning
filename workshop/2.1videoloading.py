import cv2

camera=cv2.VideoCapture(0)
#initializing the video source, 6-default webcam, 1-USB cameras
#give the file path to load a video in your computer
#give the ip address to load wifi camera

while(1):
    ret,img=camera.read()

    #color convert to gray
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #(variable_name,(x1,y1),(x2,y2),(colour),line_thickness)
    cv2.rectangle(img,(50,50),(150,150),(0,255,0),2)
    
    #gray live
    cv2.imshow('GRAY',gray)
    #color live 
    cv2.imshow('LIVE',img)
    
    #delay
    cv2.waitKey(1)
