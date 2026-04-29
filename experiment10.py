# Experiment 10: Edge Detection

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('sample.jpg', 0)

# -------- Edge Detection --------
sobelx = cv2.Sobel(image,
                   cv2.CV_64F,
                   1, 0,
                   ksize=5)

sobely = cv2.Sobel(image,
                   cv2.CV_64F,
                   0, 1,
                   ksize=5)

canny = cv2.Canny(image,
                  100,
                  200)

# -------- Segmentation --------
ret, thresh = cv2.threshold(
                image,
                127,
                255,
                cv2.THRESH_BINARY)

# Display
titles = ['Original',
          'Sobel X',
          'Canny Edge',
          'Threshold Segmentation']

images = [image,
          sobelx,
          canny,
          thresh]

plt.figure(figsize=(10,6))

for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.show()