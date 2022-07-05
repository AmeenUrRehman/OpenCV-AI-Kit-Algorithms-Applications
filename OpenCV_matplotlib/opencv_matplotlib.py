import matplotlib.pyplot as plt
import cv2 as cv


img = cv.imread("lena.jpg" , -1)
cv.imshow("image" , img)

img = cv.cvtColor(img , cv.COLOR_RGB2BGR)

plt.imshow(img)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()