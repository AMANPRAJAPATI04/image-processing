import cv2
import numpy as np

# Read image
img = cv2.imread('sample.jpg', 0)

# Check if image loaded
if img is None:
    print("Error: Image not found")
    exit()

# Define 5x5 square structuring element
kernel = np.ones((5, 5), np.uint8)

# Morphological operations
dilation = cv2.dilate(img, kernel, iterations=1)
erosion = cv2.erode(img, kernel, iterations=1)

# Convert grayscale images to BGR
img_color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
dilation_color = cv2.cvtColor(dilation, cv2.COLOR_GRAY2BGR)
erosion_color = cv2.cvtColor(erosion, cv2.COLOR_GRAY2BGR)

# Combine images horizontally
combined = np.hstack((img_color, dilation_color, erosion_color))

# Save output image to PC
cv2.imwrite("morphology_output.png", combined)

# Show image
cv2.imshow("Morphological Operations (Original | Dilation | Erosion)", combined)

cv2.waitKey(0)
cv2.destroyAllWindows()