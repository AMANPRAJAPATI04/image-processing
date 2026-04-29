import cv2
import numpy as np

# Read image in grayscale
img = cv2.imread('sample.jpg', 0)

# Check image loaded
if img is None:
    print("Error: Image not found")
    exit()

# -------------------------------
# Threshold Segmentation
# -------------------------------

# Apply Binary Threshold
_, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# -------------------------------
# Region-Based Segmentation
# (Simple Region Growing)
# -------------------------------

# Create empty output image
region = np.zeros_like(img)

# Seed point (change if needed)
seed_x = img.shape[0] // 2
seed_y = img.shape[1] // 2

# Threshold difference
threshold_value = 10

# Stack for region growing
stack = [(seed_x, seed_y)]

visited = np.zeros_like(img, dtype=bool)

while stack:
    x, y = stack.pop()

    if x < 0 or y < 0 or x >= img.shape[0] or y >= img.shape[1]:
        continue

    if visited[x, y]:
        continue

    visited[x, y] = True

    if abs(int(img[x, y]) - int(img[seed_x, seed_y])) < threshold_value:
        region[x, y] = 255

        # Add neighbors
        stack.extend([
            (x+1, y),
            (x-1, y),
            (x, y+1),
            (x, y-1)
        ])

# -------------------------------
# Combine Images in One Frame
# -------------------------------

# Convert to color
img_c = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
thresh_c = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)
region_c = cv2.cvtColor(region, cv2.COLOR_GRAY2BGR)

# Add labels
cv2.putText(img_c, "Original", (10, 25),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

cv2.putText(thresh_c, "Threshold", (10, 25),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

cv2.putText(region_c, "Region-Based", (10, 25),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

# Combine horizontally
combined = np.hstack((img_c, thresh_c, region_c))

# -------------------------------
# Save Output
# -------------------------------

cv2.imwrite("segmentation_output.png", combined)

# Show Output
cv2.imshow("Threshold and Region-Based Segmentation", combined)

cv2.waitKey(0)
cv2.destroyAllWindows()