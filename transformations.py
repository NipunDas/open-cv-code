import cv2 as cv
import numpy as np

def rescaleFrame(frame, scale):
	width = int(frame.shape[1]*scale)
	height = int(frame.shape[0]*scale)
	dimensions = (width, height)

	return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('Images/cat.jpeg')
img = rescaleFrame(img, 0.5)

#Translation
def translate(img, x, y):
	transMat = np.float32([[1,0,x],[0,1,y]])
	dimensions = (img.shape[1], img.shape[0])
	return cv.warpAffine(img, transMat, dimensions)

translated = translate(img, 100, 100)
cv.imshow('Translated', translated)

#Rotation
def rotate(img, angle, rotPoint):
	(height, width) = img.shape[:2]
	if rotPoint is None:
		rotPoint = (width//2, height//2)

	rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
	dimensions = (width, height)

	return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45, None)
rotated2 = rotate(rotated, 45, None)
rotated3 = rotate(img, 45, (0,0))
cv.imshow('Rotated', rotated)
cv.imshow('Rotated Back', rotated2)
cv.imshow('Off-center Rotation', rotated3)

#Flipping
verticalFlip = cv.flip(img, 0)
horizontalFlip = cv.flip(img, 1)
doubleFlip = cv.flip(img, -1)
cv.imshow('Vertical Flip', verticalFlip)
cv.imshow('Horizontal Flip', horizontalFlip)
cv.imshow('Vertical & Horizontal Flip', doubleFlip)

cv.waitKey(0)
