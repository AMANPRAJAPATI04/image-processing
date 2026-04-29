# Image Processing & Computer Vision Mini Projects

## Student Details
Name: YOUR NAME  
Roll No: YOUR ROLL NUMBER  
Course: Image Processing & Computer Vision  
Instructor: Satinder Pal Singh  
Date: ADD DATE  

---

# Project Overview

This repository contains four mini projects related to Digital Image Processing and Computer Vision.  
The projects simulate real-world applications such as document scanning, surveillance restoration, medical image processing, and traffic monitoring.

Each assignment demonstrates fundamental concepts including image acquisition, filtering, segmentation, compression, and feature extraction.

---

# Software Requirements

Install the following before running:

Python 3.8 or higher

Required libraries:

pip install opencv-python numpy matplotlib scipy scikit-image

---

# Folder Structure


---

# Assignment 1  
## Smart Document Scanner & Quality Analysis System

### Objective

To simulate a smart document scanning system and analyze the effects of sampling and quantization on image quality.

### Features Implemented

- Image acquisition  
- Grayscale conversion  
- Resolution sampling  
- Gray-level quantization  
- Image quality comparison  

### Observations

- Higher resolution improves readability.  
- Lower resolution reduces edge clarity.  
- Lower gray levels create banding artifacts.  
- OCR accuracy decreases with poor image quality.

---

# Assignment 2  
## Noise Modeling and Image Restoration

### Objective

To simulate noise in surveillance images and restore them using spatial filtering techniques.

### Features Implemented

- Gaussian noise addition  
- Salt-and-pepper noise addition  
- Mean filtering  
- Median filtering  
- Gaussian filtering  
- MSE calculation  
- PSNR calculation  

### Observations

- Median filter performs best for salt-and-pepper noise.  
- Gaussian filter smooths noise effectively.  
- Mean filter reduces noise but blurs edges.

---

# Assignment 3  
## Medical Image Compression & Segmentation

### Objective

To compress medical images and extract meaningful regions using segmentation techniques.

### Features Implemented

- Run Length Encoding (RLE)  
- Compression ratio calculation  
- Global thresholding  
- Otsu thresholding  
- Morphological dilation  
- Morphological erosion  

### Observations

- RLE reduces storage size for repetitive pixel values.  
- Otsu thresholding gives better segmentation automatically.  
- Morphological operations improve region quality.

---

# Assignment 4  
## Feature-Based Traffic Monitoring System

### Objective

To detect objects and extract features from traffic images.

### Features Implemented

- Sobel edge detection  
- Canny edge detection  
- Contour detection  
- Bounding box generation  
- Object area calculation  
- Object perimeter calculation  
- ORB feature extraction  

### Observations

- Canny produces sharper edges than Sobel.  
- Contours help identify object boundaries.  
- ORB detects reliable feature points.  

---

# Performance Metrics Used

## Mean Squared Error (MSE)

Measures difference between original and restored image.

Lower value indicates better restoration.

## Peak Signal-to-Noise Ratio (PSNR)

Measures image quality after restoration.

Higher value indicates better quality.

---

# How to Run the Programs

Step 1: Open VS Code  
Step 2: Open project folder  
Step 3: Open terminal  

Run example:


---

# Output Description

Each program generates:

- Processed images  
- Comparison figures  
- Performance metrics  
- Console-based analysis  

All output images are saved in:


folder.

---

# Applications

These projects simulate real-world systems such as:

- Document digitization  
- Surveillance monitoring  
- Medical imaging  
- Traffic monitoring  

---

# References

1. Gonzalez, R. C., & Woods, R. E.  
   Digital Image Processing (4th Edition)

2. OpenCV Documentation  
https://opencv.org/

3. NumPy Documentation  
https://numpy.org/

4. Matplotlib Documentation  
https://matplotlib.org/

---

# Academic Integrity Statement

This project was developed for academic purposes.  
All code is original and written by the student.

External references were used only for learning support.

---

# Conclusion

These projects demonstrate fundamental image processing techniques used in real-world systems.  
The implementation improves understanding of digital image acquisition, restoration, compression, segmentation, and feature extraction.
