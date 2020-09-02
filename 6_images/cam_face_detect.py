import cv2, time

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video = cv2.VideoCapture(0)
a = 1
while True:
    a = a + 1
    check, frame = video.read()

    # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = frame
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=5)
    print(type(faces))
    # time.sleep(1)

    if not isinstance(faces, tuple):
        for x, y, w, h in faces:
            print(faces)
            img = cv2.rectangle(gray, (x,y),(x+w,y+h),(0,255,0),3)
            cv2.imshow("Capturing",img)
    else: 
        cv2.imshow("Capturing",gray)

    key = cv2.waitKey(10)
    if key == ord('q'):
        break
print(a)
video.release()
cv2.destroyAllWindows