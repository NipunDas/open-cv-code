import cv2 as cv

def rescaleFrame(frame, scale):
	width = int(frame.shape[1]*scale)
	height = int(frame.shape[0]*scale)
	dimensions = (width, height)

	return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

img = cv.imread('Images/cat.jpeg')
img = rescaleFrame(img, 0.5)
cv.imshow('Cat', img)

#BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

#BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
#cv.imshow('HSV', hsv)

#BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
#cv.imshow('LAB', lab)

#BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
#cv.imshow('RGB', rgb)

#inverse functions
original1 = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
original2 = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
original3 = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
original4 = cv.cvtColor(rgb, cv.COLOR_RGB2BGR)
cv.imshow('Grayscale to BGR', original1)
cv.imshow('HSV to BGR', original2)
cv.imshow('LAB to BGR', original3)
cv.imshow('RGB to BGR', original4)

cv.waitKey(0)
