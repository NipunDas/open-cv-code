import cv2 as cv

def rescaleFrame(frame, scale):
	width = int(frame.shape[1] * scale)
	height = int(frame.shape[0] * scale)
	dimensions = (width, height)
	return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('Images/cat.jpeg')

cv.imshow('Cat', img)
resizedImg = rescaleFrame(img, 0.75)
cv.imshow('Resized Cat', resizedImg)

cv.waitKey(0)
