import cv2 as cv

def rescaleFrame(frame, scale):
	width = int(frame.shape[1] * scale)
	height = int(frame.shape[0] * scale)
	dimensions = (width, height)
	return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture('Images/penguinvideo.mp4')

while True:
	isTrue, frame = capture.read()
	cv.imshow('Penguin', frame)
	resizedFrame = rescaleFrame(frame, 0.75)
	cv.imshow('Penguin Resized', resizedFrame)

	if cv.waitKey(20) & 0xFF==ord('d'):
		break

capture.release()
cv.destroyAllWindows()
