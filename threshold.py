import cv2 as cv
import numpy as np

img=cv.imread('photos/cats.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow('gray',gray)

threshold,thresh=cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow("simple threshold",thresh)

adaptive=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,3)
cv.imshow("adaptive",adaptive)

 
cv.waitKey(0)