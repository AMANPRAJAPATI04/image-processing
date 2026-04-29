# Experiment 6: Periodic Noise Reduction

import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import wiener

image = cv2.imread('sample.jpg', 0)

# FFT
f = np.fft.fft2(image)
fshift = np.fft.fftshift(f)

rows, cols = image.shape
crow, ccol = rows//2, cols//2

# -------- Inverse Filtering --------
mask = np.ones((rows, cols))
mask[crow-10:crow+10,
     ccol-10:ccol+10] = 0

inverse_filter = fshift * mask

inverse_ishift = np.fft.ifftshift(inverse_filter)
inverse_image = np.fft.ifft2(inverse_ishift)
inverse_image = np.abs(inverse_image)

# -------- Wiener Filtering --------
wiener_image = wiener(image, (5,5))

# Display
titles = ['Original',
          'Inverse Filter',
          'Wiener Filter']

images = [image,
          inverse_image,
          wiener_image]

plt.figure(figsize=(10,5))

for i in range(3):
    plt.subplot(1,3,i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.show()