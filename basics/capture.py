import cv2 as cv
import os

name = input("Enter person name: ")
save_dir = rf'D:\opencv\faces\{name}'
os.makedirs(save_dir, exist_ok=True)

haar_cascade = cv.CascadeClassifier('haar_face.xml')
capture = cv.VideoCapture(0)
count = 0
target = 100  # collect 100 images

print(f"Collecting {target} images for {name}. Press 's' to start...")

while True:
    isTrue, frame = capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 9)

    for (x, y, w, h) in faces_rect:
        cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

    cv.putText(frame, f"Saved: {count}/{target}", (10,30), 
               cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), 2)
    cv.imshow("Collecting", frame)

    key = cv.waitKey(20) & 0xFF
    if key == ord('s') and len(faces_rect) > 0:
        x, y, w, h = faces_rect[0]
        face = gray[y:y+h, x:x+w]
        cv.imwrite(os.path.join(save_dir, f'{count}.jpg'), face)
        count += 1
        if count >= target:
            print("Done collecting!")
            break
    elif key == ord('d'):
        break

capture.release()
cv.destroyAllWindows()