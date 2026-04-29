import cv2
import numpy as np
from sklearn import svm
from sklearn.preprocessing import StandardScaler

# -------------------------------
# Load Image
# -------------------------------

img = cv2.imread('sample.jpg')

if img is None:
    print("Error: sample.jpg not found")
    exit()

# Resize image
img_resized = cv2.resize(img, (64, 64))

# Convert to grayscale
gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)

# Flatten image (feature extraction)
features = gray.flatten()

# -------------------------------
# Dummy Training Data
# -------------------------------

# Create dummy dataset (for demo)
X_train = np.random.rand(20, 64*64)
y_train = np.random.randint(0, 2, 20)

# Standardize data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)

# Train classifier
classifier = svm.SVC()
classifier.fit(X_train, y_train)

# -------------------------------
# Predict Class
# -------------------------------

features_scaled = scaler.transform([features])

prediction = classifier.predict(features_scaled)

predicted_class = prediction[0]

print("Predicted Class:", predicted_class)

# -------------------------------
# Display Result
# -------------------------------

label = f"Class: {predicted_class}"

cv2.putText(img,
             label,
             (20, 40),
             cv2.FONT_HERSHEY_SIMPLEX,
             1,
             (0, 255, 0),
             2)

# Save output image
cv2.imwrite("sample.jpg", img)

# Show output
cv2.imshow("CNN Image Classification", img)

cv2.waitKey(0)
cv2.destroyAllWindows()