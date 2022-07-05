import numpy as np
import cv2

img = cv2.imread("lena_e.jpg" , 1)
img = cv2.line(img , (255 , 302) , (455,147) , (255 , 250 , 255) , 2)
img = cv2.arrowedLine(img , (452 , 214) , (245 , 102) , (0 , 0, 255) , 3)
img = cv2.circle(img , (203 , 302) , 212 , (255,0 ,0) , 4)
img = cv2.rectangle(img , (102, 301) , (451 , 125) , (0 ,0 ,0), -1)
font = cv2.FONT_HERSHEY_PLAIN
img = cv2.putText(img , "OpenCV" , (101, 122) ,font ,  10 , (255 , 0 , 0) , 9)

cv2.imshow("image" , img)

cv2.waitKey(0)
cv2.destroyAllWindows()
