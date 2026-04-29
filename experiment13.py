import cv2
import numpy as np

# Read binary image
img = cv2.imread('sample.jpg', 0)

# Check image loaded
if img is None:
    print("Error: Image not found")
    exit()

# Convert to binary (if not already binary)
_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Find contours (boundary detection)
contours, _ = cv2.findContours(binary,
                               cv2.RETR_EXTERNAL,
                               cv2.CHAIN_APPROX_NONE)

# Create blank image to draw boundary
boundary_img = np.zeros_like(binary)

# Draw contour boundary
cv2.drawContours(boundary_img, contours, -1, 255, 1)

# -------------------------------
# Chain Code Generation
# -------------------------------

# 8-direction Freeman Chain Code
directions = [
    (0, 1),    # 0
    (-1, 1),   # 1
    (-1, 0),   # 2
    (-1, -1),  # 3
    (0, -1),   # 4
    (1, -1),   # 5
    (1, 0),    # 6
    (1, 1)     # 7
]

chain_code = []

# Take first contour
if len(contours) > 0:

    contour = contours[0]

    for i in range(len(contour) - 1):

        x1, y1 = contour[i][0]
        x2, y2 = contour[i + 1][0]

        dx = x2 - x1
        dy = y2 - y1

        # Match direction
        for idx, (d_x, d_y) in enumerate(directions):
            if dx == d_x and dy == d_y:
                chain_code.append(idx)
                break

# Save chain code to text file
with open("chain_code.txt", "w") as f:
    f.write("Chain Code:\n")
    f.write(" ".join(map(str, chain_code)))

# -------------------------------
# Combine Images
# -------------------------------

# Convert to color
img_c = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)
boundary_c = cv2.cvtColor(boundary_img, cv2.COLOR_GRAY2BGR)

# Add labels
cv2.putText(img_c, "Original Shape",
            (10, 25),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7, (0,0,255), 2)

cv2.putText(boundary_c, "Boundary",
            (10, 25),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7, (0,0,255), 2)

# Combine side-by-side
combined = np.hstack((img_c, boundary_c))

# Save output image
cv2.imwrite("shape_chaincode_output.png", combined)

# Show output
cv2.imshow("Shape Representation and Chain Code", combined)

cv2.waitKey(0)
cv2.destroyAllWindows()