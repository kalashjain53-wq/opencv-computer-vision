import cv2 as cv

img=cv.imread('Photos/cat.jpg')
cv.imshow('Cat',img)

#converting to greyscale
#gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow('gray',gray)

#blur

#blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
#cv.imshow("blur",blur)

#edge cascade

#canny=cv.Canny(blur,125,175)
#cv.imshow("Canny",canny)

#dialeted
#dialted=cv.dilate(canny,(7,7),iterations=5)
#cv.imshow("dialeted",dialted)

#eroding
#eroded=cv.erode(dialted,(3,3),iterations=5)
#cv.imshow("eroded",eroded)

#resize=cv.resize(img,(304,235))
#cv.imshow("Resize",resize)

crop=img[50:200,200:400]
cv.imshow('crop',crop)

cv.waitKey(0)