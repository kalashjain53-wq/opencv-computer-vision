import cv2 as cv

capture=cv.VideoCapture(0)
haar=cv.CascadeClassifier('haar_face.xml')
while True:
    isTrue,frame=capture.read()
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    
    faces_rect=haar.detectMultiScale(gray,1.01,minNeighbors=8)

    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=3)
    cv.imshow("Detected",frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()