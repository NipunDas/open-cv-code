import cv2 as cv
import numpy as np

#creating blank image
blank = np.zeros((700, 500, 3), dtype='uint8')
#cv.imshow('Blank Image', blank)

#making all pixels green
blank[:] = 0,255,0
#cv.imshow('Green', blank)

#making purple square
blank[0:100, 400:500] = 255,0,255
#cv.imshow('Purple square', blank)

#making red rectangle (not filled) using cv.rectangle()
cv.rectangle(blank, (10,10), (250,300), (255,0,0), thickness=2)
#cv.imshow('Red Rectangle', blank)

#filling a rectangle using cv.rectangle()
cv.rectangle(blank, (400,400), (450,450), (0,0,255), thickness=cv.FILLED)
#cv.imshow('Filled Blue Square', blank)

#testing out .shape() property of blank image
cv.rectangle(blank, (0,500), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=-1)
cv.imshow('Drawing 1', blank)

blank2 = np.zeros((500,500,3), dtype='uint8')

#drawing a circle
cv.circle(blank2, (blank2.shape[1]//2, blank2.shape[0]//2), 50, (0,0,255), thickness=3)
#cv.imshow('Red Circle', blank2)

#drawing a line
cv.line(blank2, (blank2.shape[1]//2, blank2.shape[0]//2), (500,500), (0,255,255), thickness=2)
#cv.imshow('Diagonal Line', blank2)

#adding text
cv.putText(blank2, 'Hello World', (50,50), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,0,0), thickness=2)
cv.imshow('Drawing Test', blank2)

#can draw on cat image as well, but looks nicer to draw on blank image
#img = cv.imread('Images/cat.jpeg')
#cv.imshow('Cat', img)

cv.waitKey(0)
