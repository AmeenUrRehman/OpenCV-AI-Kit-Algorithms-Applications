import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("salt&pepper.jpg")
img = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)

kernal = np.ones((5,5) , np.float32)/25
# filter2D(sourceImage , dde[th , kernal)
dst = cv2.filter2D(img , -1 , kernal )
# blur(sourceimage , kernal_shape)
blur = cv2.blur(img , (5,5))
# GaussianBlur(source_image , kernel_shape , sigmaX)
gb = cv2.GaussianBlur(img , (5,5) , 0)
#Median // Best for Salt and Pepper Image processing
# medianBlur(sourceimage , kernal_size (take value greater than 2 and odd no.)
median = cv2.medianBlur(img , 5)


titles = ["image" , "2D Convolution" , "Blur" , "GaussianBlur" , "Median"]
images = [img , dst , blur , gb , median]

for i in range(5):
    plt.subplot(2 , 3 , i+1) , plt.imshow(images[i] , 'gray')
    plt.title(titles[i])
    plt.xticks([]) , plt.yticks([])

plt.show()