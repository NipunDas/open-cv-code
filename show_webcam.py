import cv2 as cv

capture = cv.VideoCapture(0)

def changeRes(width, height):
	capture.set(3, width)
	capture.set(4, height)

#changeRes(1200, 800)

while True:
	isTrue, frame = capture.read()
	cv.imshow('Webcam', frame)

	if cv.waitKey(20) & 0xFF==ord('d'):
		break

capture.release()
cv.destroyAllWindows()
