import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3),dtype='uint8')
#cv.imshow('black',blank)

#blank[200:300,300:400]=0,0,255
#cv.imshow('red',blank)

#cv.rectangle(blank,(100,100),(200,200),(0,255,0), thickness=cv.FILLED)
#cv.imshow("rectangle",blank)

#cv.circle(blank,(blank.shape[1]//2,(blank.shape[0]//2)),40,(0,255,0),thickness=3)
#cv.imshow('circle',blank)

#cv.line(blank,(0,0),(blank.shape[1]//2,(blank.shape[0]//2)),(0,255,0))
#cv.imshow("line",blank)

cv.putText(blank,"Hello world",(0,250),cv.FONT_HERSHEY_TRIPLEX,2,(0,255,0),thickness=3)
cv.imshow('text',blank)

cv.waitKey(0)