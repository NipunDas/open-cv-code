import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def rescaleFrame(frame, scale):
        width = int(frame.shape[1]*scale)
        height = int(frame.shape[0]*scale)
        dimensions = (width, height)

        return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('Images/cat.jpeg')
img = rescaleFrame(img, 0.5)

blank = np.zeros(img.shape[:2], dtype='uint8')

#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked', masked)

#full image histogram
#gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])

#masked histogram
#gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])

# Using matplotlib to plot the histogram
#plt.figure()
#plt.title('Grayscale Histogram')
#plt.xlabel('Bins')
#plt.ylabel('Number of Pixels')
#plt.plot(gray_hist)
#plt.xlim([0,256])
#plt.show()

#Colored histogram
plt.figure()
plt.title('Colored Histogram')
plt.xlabel('Bins')
plt.ylabel('Number of Pixels')

colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
	hist = cv.calcHist([img], [i], mask, [256], [0,256])
	#Plotting Histogram
	plt.plot(hist, color=col)
	plt.xlim([0,256])

plt.show()
cv.waitKey(0)
