import cv2
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# -------------------------------
# Load Face Detector
# -------------------------------

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 
    'haarcascade_frontalface_default.xml'
)

# -------------------------------
# Training Data (Dummy Faces)
# -------------------------------

# Create dummy training data
# (In real case, use real face images)
X_train = np.random.rand(10, 10000)
y_train = np.array([0,1,0,1,0,1,0,1,0,1])

# Train KNN Classifier
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)

# -------------------------------
# Load Test Image
# -------------------------------

img = cv2.imread('sample.jpg')

if img is None:
    print("Error: sample.jpg not found")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect Faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.3,
    minNeighbors=5
)

# -------------------------------
# Face Recognition
# -------------------------------

for (x, y, w, h) in faces:

    # Extract face region
    face = gray[y:y+h, x:x+w]

    # Resize face
    face_resized = cv2.resize(face, (100, 100))

    # Flatten
    face_flat = face_resized.flatten()

    # Predict
    prediction = knn.predict([face_flat])

    label = f"Person {prediction[0]}"

    # Draw rectangle
    cv2.rectangle(
        img,
        (x, y),
        (x+w, y+h),
        (0, 255, 0),
        2
    )

    # Add label
    cv2.putText(
        img,
        label,
        (x, y-10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0,255,0),
        2
    )

# -------------------------------
# Save Output
# -------------------------------

cv2.imwrite("face_recognition_output.png", img)

# Show Output
cv2.imshow("Face Recognition", img)

cv2.waitKey(0)
cv2.destroyAllWindows()