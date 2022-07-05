import cv2
img = cv2.imread("messi5.jpg")
img1 = cv2.imread("opencv-logo-white.png")

print(img.shape)
print(img.size)
print(img.dtype)

b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

ball = img[280:340,330:390]
img[273:333,100:160] = ball



img = cv2.resize(img , (512,512))
img1 = cv2.resize(img1 , (512,512))

# dst = cv2.add(img , img1)
dst2 = cv2.addWeighted(img , .9 , img1 , .1,0)

cv2.imshow("image" , dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()