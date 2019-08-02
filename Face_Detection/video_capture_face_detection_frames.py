import cv2, time

video = cv2.VideoCapture(0)

video.set(3,640) # set Width
video.set(4,480) # set Height
a = 1

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    a = a+1
    check, frame = video.read()
    
    ## flipping the image
    #frame = cv2.flip(frame, -1)
    #print(frame)   ## printing the frame

    ###################################################
    ## converting to grey scale image
    ################################################

    #gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #cv2.imshow("Capturing", gray_img)

    faces = face_cascade.detectMultiScale(frame, scaleFactor = 1.05,
                                          minNeighbors=5)
    for x,y,w,h in faces:
        frame = cv2.rectangle(frame, (x,y), (x+w,y+h),(0,255,0),2)

    cv2.imshow("Capturing", frame)

    key = cv2.waitKey(1000)
    if key == ord('q'):
        break

print(a)
video.release()
cv2.destroyAllWindows()
