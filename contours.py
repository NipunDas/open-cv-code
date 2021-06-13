import cv2 as cv
import numpy as np

def rescaleFrame(frame, scale):
	width = int(frame.shape[1]*scale)
	height = int(frame.shape[0]*scale)
	dimensions = (width, height)

	return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('Images/cat.jpeg')
img = rescaleFrame(img, 0.5)

cv.imshow('Cat', img)

#grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#blur
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#Canny edges
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)

#using thresholding instead of canny edges
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresholding', thresh)

#drawing contours on a blank imgae
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

#finding contours from canny edges
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print (f'{len(contours)} contour(s) found!')

#drawing contours
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours', blank)

cv.waitKey(0)
