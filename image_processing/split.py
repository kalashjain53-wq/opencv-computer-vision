import cv2 as cv
import numpy as np


img=cv.imread('photos/park.jpg')

blank=np.zeros(img.shape[:2],dtype="uint8")
b,g,r=cv.split(img)
blue=cv.merge([b,blank,blank])
cv.imshow("blue",blue)
cv.imshow("red",r)
cv.imshow("green",g)
print(b.shape)

merge=cv.merge([b,g,r])
cv.imshow("mere",merge)

cv.waitKey(0)
