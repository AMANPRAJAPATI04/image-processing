# Experiment 1: Image Acquisition and Display

import cv2
import matplotlib.pyplot as plt

# Acquire Image (Read from file)
image = cv2.imread('sample.jpg')

# Convert BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display Image
plt.imshow(image_rgb)
plt.title("Acquired Image")
plt.axis('off')
plt.show()

# Display Image Properties
print("Image Dimensions:", image.shape)
print("Height:", image.shape[0])
print("Width:", image.shape[1])
print("Channels:", image.shape[2])