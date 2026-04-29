# Experiment 4: Frequency Domain Filtering

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read Image
image = cv2.imread('sample.jpg', 0)

# Convert to Frequency Domain
f = np.fft.fft2(image)
fshift = np.fft.fftshift(f)

rows, cols = image.shape
crow, ccol = rows//2 , cols//2

# -------- Low Pass Filter --------
lpf_mask = np.zeros((rows, cols), np.uint8)
lpf_mask[crow-30:crow+30,
         ccol-30:ccol+30] = 1

lpf = fshift * lpf_mask

# Inverse Transform
lpf_ishift = np.fft.ifftshift(lpf)
lpf_image = np.fft.ifft2(lpf_ishift)
lpf_image = np.abs(lpf_image)

# -------- High Pass Filter --------
hpf_mask = np.ones((rows, cols), np.uint8)
hpf_mask[crow-30:crow+30,
         ccol-30:ccol+30] = 0

hpf = fshift * hpf_mask

# Inverse Transform
hpf_ishift = np.fft.ifftshift(hpf)
hpf_image = np.fft.ifft2(hpf_ishift)
hpf_image = np.abs(hpf_image)

# -------- Display --------
titles = ['Original Image',
          'Low Pass Filter',
          'High Pass Filter']

images = [image,
          lpf_image,
          hpf_image]

plt.figure(figsize=(10,5))

for i in range(3):
    plt.subplot(1,3,i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.show()