import cv2 as cv
import numpy as np

img = cv.imread("gradient.png" , 0)

ret, Frame1 = cv.threshold(img , 127 , 255 , cv.THRESH_BINARY)
ret, Frame2 = cv.threshold(img , 127 , 255 , cv.THRESH_BINARY_INV)
ret, Frame3 = cv.threshold(img , 127 , 255 , cv.THRESH_TRUNC)
ret, Frame4 = cv.threshold(img , 127 , 255 , cv.THRESH_TOZERO)
ret, Frame5 = cv.threshold(img , 127 , 255 , cv.THRESH_TOZERO_INV)


cv.imshow("frame1" , Frame1)
cv.imshow("frame2" , Frame2)
cv.imshow("frame3" , Frame3)
cv.imshow("frame4" , Frame4)
cv.imshow("frame5" , Frame5)

cv.waitKey(0)
cv.destroyAllWindows()

