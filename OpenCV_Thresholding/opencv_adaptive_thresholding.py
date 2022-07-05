import cv2 as cv
import numpy as np

img = cv.imread("sudoku.png" ,0)
frame = cv.adaptiveThreshold(img , 255 , cv.ADAPTIVE_THRESH_MEAN_C , cv.THRESH_BINARY , 11 , 7)
frame2 = cv.adaptiveThreshold(img , 255 , cv.ADAPTIVE_THRESH_GAUSSIAN_C , cv.THRESH_BINARY , 11 , 7)

cv.imshow("frame" , frame)
cv.imshow("frame2" , frame2)

cv.waitKey(0)
cv.destroyAllWindows()

