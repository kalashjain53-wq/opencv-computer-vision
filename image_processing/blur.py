import cv2 as cv

img=cv.imread('photos/lady.jpg')
average=cv.blur(img,(7,7))
cv.imshow("average",average)

gauss=cv.GaussianBlur(img,(7,7),0)
cv.imshow("auss",gauss)

median=cv.medianBlur(img,7)
cv.imshow("median",median)

bilateral=cv.bilateralFilter(img,5,35,25)
cv.imshow('bilateral',bilateral)

cv.waitKey(0)