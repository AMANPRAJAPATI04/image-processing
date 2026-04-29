# Experiment 8: Color Image Processing

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('sample.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Color Segmentation (example: red color)
lower_red = np.array([0,120,70])
upper_red = np.array([10,255,255])

mask = cv2.inRange(hsv,
                   lower_red,
                   upper_red)

segmented = cv2.bitwise_and(
                image_rgb,
                image_rgb,
                mask=mask)

# Display
titles = ['Original',
          'Mask',
          'Segmented']

images = [image_rgb,
          mask,
          segmented]

plt.figure(figsize=(10,5))

for i in range(3):
    plt.subplot(1,3,i+1)
    plt.imshow(images[i],
               cmap='gray' if i==1 else None)
    plt.title(titles[i])
    plt.axis('off')

plt.show()