import cv2 as cv
import numpy as np

def rescaleFrame(frame, scale):
	width = int(frame.shape[1]*scale)
	height = int(frame.shape[0]*scale)
	dimensions = (width, height)

	return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

img = cv.imread('Images/cat.jpeg')
img = rescaleFrame(img, 0.5)
cv.imshow('Cat', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image', blank)

mask_circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Circular Mask', mask_circle)

mask_rectangle = cv.rectangle(blank.copy(), (img.shape[1]//2 - 75, img.shape[0]//2 - 75), (img.shape[1]//2 + 75, img.shape[0]//2 + 75), 255, -1)
cv.imshow('Rectangular Mask', mask_rectangle)

combined_mask = cv.bitwise_and(mask_rectangle, mask_circle)
cv.imshow('Final Mask', combined_mask)

masked = cv.bitwise_and(img, img, mask=combined_mask)
cv.imshow('Masked Image', masked)

cv.waitKey(0)
