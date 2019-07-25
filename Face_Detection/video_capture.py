import cv2, time

video = cv2.VideoCapture(0)

check, frame = video.read()

print(check)
print(frame)

time.sleep(1)

cv2.imshow("label", frame)

cv2.waitKey(2000)

video.release()

cv2.destroyAllWindows()
