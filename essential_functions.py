import cv2 as cv

def rescaleFrame(frame, scale):
	width = int(frame.shape[1]*scale)
	height = int(frame.shape[0]*scale)
	dimensions=(width,height)

	return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('Images/cat.jpeg')
img = rescaleFrame(img, 0.5)
cv.imshow('Cat', img)

#Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Grayscale', gray)

#Gaussian blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
#cv.imshow('Gaussian Blur', blur)

#Edge cascades
canny = cv.Canny(img, 125, 175) #lots of edges (no blur)
canny2 = cv.Canny(blur, 125, 175) #fewer edges b/c of blur
#cv.imshow('Canny Edges', canny)
#cv.imshow('Canny Edges 2', canny2)

#Dilating an image
dilated = cv.dilate(canny2, (7,7), iterations=3)
#cv.imshow('Dilated', dilated)

#Eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
#cv.imshow('Eroded', eroded)

#Resizing (default interpolation is cv.INTER_AREA)
resized1 = cv.resize(img, (500,500))
resized2 = cv.resize(img, (1500,1000), interpolation=cv.INTER_LINEAR)
resized3 = cv.resize(img, (1500,1000), interpolation=cv.INTER_CUBIC)
#cv.imshow('Resized Area', resized1)
#cv.imshow('Resized Linear', resized2)
#cv.imshow('Resized Cubic', resized3)

#Cropping
cropped = resized3[200:700, 500:1100]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
