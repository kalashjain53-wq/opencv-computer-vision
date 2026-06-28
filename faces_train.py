import os
import cv2 as cv
import numpy as np

DIR = r'D:\opencv\faces'
p = sorted(os.listdir(DIR))  # sorted for consistent label indices

features = []
labels = []

haar_cascade = cv.CascadeClassifier('haar_face.xml')

def create_train():
    print("running")
    for person in p:
        path = os.path.join(DIR, person)
        label = p.index(person)
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=9)
            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
print("done")

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(features, labels)
face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)
np.save('people.npy', np.array(p))  # save label mapping
print("Saved. People order:", p)