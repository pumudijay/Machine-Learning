#import open cv module
import cv2

#loading an image to img object.imread->read image
img=cv2.imread('Samples/flower.jpg')

img[100:120,100:130]=[0,255,255]

#imshow->show image
cv2.imshow('IMAGE',img)


