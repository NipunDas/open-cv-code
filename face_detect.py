import cv2 as cv

def rescaleFrame(frame, scale):
	width = int(frame.shape[1]*scale)
	height = int(frame.shape[0]*scale)
	dimensions = (width, height)
	return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('Images/person.jpeg')
img = rescaleFrame(img, 0.5)
cv.imshow('Person', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
	cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Faces Detected', img)

cv.waitKey(0)
