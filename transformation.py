import cv2 as cv
import numpy as np

img=cv.imread('photos/cat.jpg')
cv.imshow('cat',img)

flip=cv.flip(img,0)
cv.imshow('Flip',flip)

#translation
def translate(img,x,y):
    tranMat=np.float32([[1,0,x],[0,1,y]])
    dimension=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,tranMat,dimension)

def rotation(img, theta):
    rotateMat=np.float32([[np.cos(theta),np.sin(theta),0],[(-1*np.sin(theta)),np.cos(theta),0],[0,0,1]])
    dimension=(img.shape[1],img.shape[0])
    transMate=np.float32([[1,0,img.shape[1]//2],[0,1,img.shape[0]//2],[0,0,1]])
    inverse_transMate=np.float32([[1,0,-1*(img.shape[1]//2)],[0,1,-1*(img.shape[0]//2)],[0,0,1]])
    c=transMate@rotateMat@inverse_transMate
    return cv.warpAffine(img,c[0:2][:],dimension)

#translated=translate(img,100,100)
#cv.imshow('translate',translated)

rotate=rotation(img,1.57)
cv.imshow("rotate",rotate)

flip=cv.flip(img,0)
cv.imshow('flip',flip)


cv.waitKey(0)