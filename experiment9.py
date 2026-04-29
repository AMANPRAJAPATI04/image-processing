# Experiment 9: Huffman Coding and Run Length Coding
# With Image Display

import cv2
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import heapq

# Read Image
image = cv2.imread('sample.jpg', 0)

if image is None:
    print("Error: Image not found")
    exit()

# Display Original Image
plt.imshow(image, cmap='gray')
plt.title("Original Image")
plt.axis('off')
plt.show()

# -------- Huffman Coding --------

pixels = image.flatten()

frequency = Counter(pixels)

heap = [[weight, [symbol, ""]]
        for symbol, weight in frequency.items()]

heapq.heapify(heap)

while len(heap) > 1:

    lo = heapq.heappop(heap)
    hi = heapq.heappop(heap)

    for pair in lo[1:]:
        pair[1] = '0' + pair[1]

    for pair in hi[1:]:
        pair[1] = '1' + pair[1]

    heapq.heappush(heap,
                   [lo[0]+hi[0]] +
                   lo[1:] +
                   hi[1:])

huffman_code = dict(heapq.heappop(heap)[1:])

print("Huffman Codes Generated")

# Show some Huffman codes
print("\nSample Huffman Codes:")
for i, (k, v) in enumerate(huffman_code.items()):
    if i < 10:
        print(f"Pixel {k}: Code {v}")

# -------- Run Length Coding --------

rle = []

prev_pixel = pixels[0]
count = 1

for pixel in pixels[1:]:

    if pixel == prev_pixel:
        count += 1

    else:
        rle.append((prev_pixel, count))
        prev_pixel = pixel
        count = 1

rle.append((prev_pixel, count))

print("\nRun Length Coding Completed")

# Show first few RLE values
print("\nSample RLE Output:")
print(rle[:10])