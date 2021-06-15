import cv2 as cv

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

#Simple thresholding
threshold, thresh = cv.threshold(gray, 200, 255, cv.THRESH_BINARY)
cv.imshow('Simple Threshold', thresh)

#Inverse simple thresholding (reverses black and white)
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Threshold Inversed', thresh_inv)

#Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 13, 9)
cv.imshow('Adaptive Thresholding', adaptive_thresh)

cv.waitKey(0)
