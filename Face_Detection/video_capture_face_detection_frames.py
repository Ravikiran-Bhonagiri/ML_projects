import cv2, time

video = cv2.VideoCapture(0)

a = 1

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    a = a+1
    check, frame = video.read()
    print(frame)

    gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #cv2.imshow("Capturing", gray_img)

    faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.1,
                                          minNeighbors=5)
    for x,y,w,h in faces:
        gray_img = cv2.rectangle(gray_img, (x,y), (x+w,y+h),(0,255,0),3)

    cv2.imshow("Capturing", gray_img)

    key = cv2.waitKey(1000)
    if key == ord('q'):
        break

print(a)
video.release()
cv2.destroyAllWindows()
