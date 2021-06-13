import cv2 as cv

def rescaleFrame(frame, scale):
        width = int(frame.shape[1]*scale)
        height = int(frame.shape[0]*scale)
        dimensions = (width, height)

        return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('Images/cat.jpeg')
img = rescaleFrame(img, 0.5)
cv.imshow('Cat', img)

#Average Blur
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

#Gaussian Blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

#Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

#Bilateral Blur
bilateral =  cv.bilateralFilter(img, 10, 15, 15)
cv.imshow('Bilateral Blur', bilateral)

cv.waitKey(0)
