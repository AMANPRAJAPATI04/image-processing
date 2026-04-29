# Experiment 7: Geometric Transformations

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('sample.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

rows, cols = image.shape[:2]

# -------- Translation --------
M_translate = np.float32([[1,0,50],
                          [0,1,30]])

translated = cv2.warpAffine(image_rgb,
                            M_translate,
                            (cols, rows))

# -------- Scaling --------
scaled = cv2.resize(image_rgb,
                    None,
                    fx=0.5,
                    fy=0.5)

# -------- Rotation --------
M_rotate = cv2.getRotationMatrix2D(
            (cols/2, rows/2),
            45,
            1)

rotated = cv2.warpAffine(image_rgb,
                         M_rotate,
                         (cols, rows))

# Display
titles = ['Original',
          'Translated',
          'Scaled',
          'Rotated']

images = [image_rgb,
          translated,
          scaled,
          rotated]

plt.figure(figsize=(10,6))

for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis('off')

plt.show()