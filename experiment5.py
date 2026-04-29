# Experiment 5: Noise Model and Spatial Filtering

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
image = cv2.imread('sample.jpg', 0)

# -------- Add Gaussian Noise --------
mean = 0
std = 25
gaussian_noise = np.random.normal(mean, std, image.shape)

noisy_image = image + gaussian_noise
noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)

# -------- Spatial Filtering --------
# Mean Filter
mean_filtered = cv2.blur(noisy_image, (5,5))

# Median Filter
median_filtered = cv2.medianBlur(noisy_image, 5)

# Display
titles = ['Original',
          'Noisy Image',
          'Mean Filter',
          'Median Filter']

images = [image,
          noisy_image,
          mean_filtered,
          median_filtered]

plt.figure(figsize=(10,6))

for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.show()