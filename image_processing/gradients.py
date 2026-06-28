import cv2 as cv
import numpy as np
img=cv.imread('photos/cats.jpg')

gray=cv.cvtColor(img,cv.COLOR_BGR2BGRA)
lap=cv.Laplacian(gray,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow('lap',lap)

sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)

cv.imshow('sobelx',sobelx)
cv.imshow('sobely',sobely)

combined=cv.bitwise_or(sobelx,sobely)
cv.imshow('combine',combined)

canny=cv.Canny(gray,150,170)
cv.imshow("canny",canny)


cv.waitKey(0)