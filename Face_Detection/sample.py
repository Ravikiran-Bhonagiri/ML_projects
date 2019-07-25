import cv2

print("Hello World")
img = cv2.imread("penguin.jpeg", 1) ## color
img_1 = cv2.imread("penguin.jpeg", 0) ## gray


## Hello Ravikiran
resized = cv2.resize( img, ( int(img.shape[0]/2), int(img.shape[1]/2) ))

print( img.shape )
print( img_1.shape )

print( type(img) )
print( type(img_1) )

cv2.imshow("Penguins", img)
cv2.waitKey(2000)

cv2.imshow("Penguins", img_1)
cv2.waitKey(2000)

cv2.imshow("Penguins", resized)
cv2.waitKey(2000)

cv2.destroyAllWindows()
