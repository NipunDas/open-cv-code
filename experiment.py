import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)

def analyzeFrame(frame):
	gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
	blur = cv.GaussianBlur(gray, (9,9), cv.BORDER_DEFAULT)
	canny = cv.Canny(blur, 100, 200)
	dilated = cv.dilate(canny, (7,7), iterations=3)
	#eroded = cv.erode(canny, (3,3), iterations=1)
	contours, hierarchies = cv.findContours(dilated, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
	blank = np.zeros(frame.shape, dtype='uint8')

	for contour in contours:
		(x,y,w,h) = cv.boundingRect(contour)
		if w > 100 & w < 1000:
			cv.rectangle(blur, (x,y), (x+w,y+h), (0,255,0), thickness=1)

	#cv.drawContours(blank, contours, -1, (0,0,255), 2)
	cv.imshow('Contours', blur)
	cv.imshow('Edges', dilated)

while True:
	isTrue, frame = capture.read()
	analyzeFrame(frame)
	#cv.imshow('Webcam', frame)

	if cv.waitKey(20) & 0xFF==ord('d'):
		break

capture.release()
cv.destroyAllWindows()
