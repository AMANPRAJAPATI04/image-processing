# Experiment 2: Sampling and Quantization

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read Image in Grayscale
image = cv2.imread('sample.jpg', 0)

# -------- Sampling --------
# Reduce resolution
sampling_rates = [1, 2, 4]

plt.figure(figsize=(10,5))

for i, rate in enumerate(sampling_rates):
    sampled = image[::rate, ::rate]

    plt.subplot(1,3,i+1)
    plt.imshow(sampled, cmap='gray')
    plt.title(f"Sampling Rate: {rate}")
    plt.axis('off')

plt.show()

# -------- Quantization --------
levels = [256, 64, 16]

plt.figure(figsize=(10,5))

for i, level in enumerate(levels):
    quantized = np.floor(image / (256/level)) * (256/level)

    plt.subplot(1,3,i+1)
    plt.imshow(quantized, cmap='gray')
    plt.title(f"Quantization Level: {level}")
    plt.axis('off')

plt.show()