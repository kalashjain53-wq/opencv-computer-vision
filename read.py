import cv2 as cv

#img=cv.imread('photos/cat_large.jpg')
#cv.imshow('Cat',img)

def rescale(frame,scale):
    height=int(frame.shape[0]*scale)
    width=int(frame.shape[0]*scale)

    dimensions=(height,width)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

capture= cv.VideoCapture(0)
while True:
    isTrue, frame= capture.read()
    resized=rescale(frame,0.2)
    cv.imshow('Video',frame)
    cv.imshow('Resized video',resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()