import numpy as np
import cv2 as cv

p = list(np.load('people.npy', allow_pickle=True))  # load saved label mapping
print("People order:", p)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

capture = cv.VideoCapture(0)
while True:
    isTrue, frame = capture.read()
    frame=cv.flip(frame,1)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces_rect = haar_cascade.detectMultiScale(gray, 1.2, 6)

    for (x, y, w, h) in faces_rect:
        faces_roi = gray[y:y+h, x:x+w]
        label, confidence = face_recognizer.predict(faces_roi)
        if confidence>40:
            cv.putText(frame, str(p[label]), (x, y+30), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
            cv.putText(frame, f"confidence: {confidence:.2f}", (x, y-20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
        
            cv.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), thickness=2)

    cv.imshow("Detected", frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()