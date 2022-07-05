import cv2 as cv
import numpy as np


image = cv.imread("smarties.png")
output = image.copy()
gray = cv.cvtColor(output , cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray , 7)
circles = cv.HoughCircles(gray , cv.HOUGH_GRADIENT , 1 , 35 ,param1 = 50 , param2 =30)

detected_circles = np.uint16(np.around(circles))
for (x , y , r) in detected_circles[0,:]:
    cv.circle(output , (x,y) , r , (0,255,0),3)
    # cv.circle(output , (x ,y) , 2 , (0,255,255) , 3)

cv.imshow("output" , output)
cv.waitKey(0)
cv.destroyAllWindows()