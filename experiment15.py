import cv2
import numpy as np

# Read image
img = cv2.imread('sample.jpg')

# Check if image loaded
if img is None:
    print("Error: sample.jpg not found")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Threshold to detect object
_, thresh = cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY)

# Find contours (object detection)
contours, _ = cv2.findContours(thresh,
                               cv2.RETR_EXTERNAL,
                               cv2.CHAIN_APPROX_SIMPLE)

# Draw bounding box around detected object
tracked_img = img.copy()

for cnt in contours:
    area = cv2.contourArea(cnt)

    # Ignore very small areas
    if area > 500:

        x, y, w, h = cv2.boundingRect(cnt)

        # Draw rectangle (tracking box)
        cv2.rectangle(tracked_img,
                      (x, y),
                      (x + w, y + h),
                      (0, 255, 0),
                      2)

# -------------------------------
# Combine Original + Tracking
# -------------------------------

combined = np.hstack((img, tracked_img))

# Save output
cv2.imwrite("motion_tracking_output.png", combined)

# Show output
cv2.imshow("Motion Estimation and Object Tracking", combined)

cv2.waitKey(0)
cv2.destroyAllWindows()