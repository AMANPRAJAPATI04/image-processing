# Experiment 3: Image Enhancement

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read Image
image = cv2.imread('sample.jpg', 0)

# -------- Contrast Stretching --------
min_val = np.min(image)
max_val = np.max(image)

contrast_stretch = ((image - min_val) /
                   (max_val - min_val)) * 255
contrast_stretch = contrast_stretch.astype(np.uint8)

# -------- Histogram Equalization --------
hist_equalized = cv2.equalizeHist(image)

# -------- Display Results --------
titles = ['Original Image',
          'Contrast Stretching',
          'Histogram Equalization']

images = [image,
          contrast_stretch,
          hist_equalized]

plt.figure(figsize=(10,5))

for i in range(3):
    plt.subplot(1,3,i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.show()