import cv2 as cv

capture = cv.VideoCapture(0)

def analyzeFrame(frame):
	#blur = cv.GaussianBlur(frame, (5,5), cv.BORDER_DEFAULT)
	#canny = cv.Canny(blur, 125, 175)
	#dilated = cv.dilate(canny, (7,7), iterations=3)
	gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
	ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
	return thresh

while True:
	isTrue, frame = capture.read()
	analyzedFrame = analyzeFrame(frame)
	cv.imshow('Webcam', analyzedFrame)

	if cv.waitKey(20) & 0xFF==ord('d'):
		break

capture.release()
cv.destroyAllWindows()
