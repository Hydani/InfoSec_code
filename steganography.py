"""
UTA CSE 4381-001 Information Security II / Homework 4
Submission Date: 12.03.2023

Name: Hyeonjun An
Student ID: 1001342487

Install numpy and opencv:
pip install numpy
pip install opencv-python
"""

import cv2
import numpy as np

# Read in two images for steganography
imagename1 = input("Type in your cover image with the file extension:")
imagename2 = input("Type in your secret image with the file extension:")

coverimage = cv2.imread(imagename1, 0)
secretimage = cv2.imread(imagename2, 0)

# Check for correct input of images
if coverimage is None or secretimage is None:
    if coverimage is None:
        print(f"Error: Unable to load image at '{coverimage}'")
    if secretimage is None:
        print(f"Error: Unable to load image at '{secretimage}'")

cover_height, cover_width = coverimage.shape
secret_height, secret_width = secretimage.shape

# Condition check
if cover_height < secret_height or cover_width < secret_width:
    print(f"Error: the secret image must be smaller than or the same size as the cover image.")
    exit(0)

cv2.imshow('Cover Image', coverimage)
# Empty image to store the new pixel values
emptyimage1 = np.zeros((cover_height, cover_width), dtype=np.uint8)
emptyimage2 = coverimage.copy()

# iterate over pixels and create a new image 
# storing the 4 most significant digits of each pixel value from the secret image 
# to the 4 least significant digits of each pixel value from the cover image.
for row in range(secret_height):
    for column in range(secret_width):
        cover_digit = '{0:08b}'.format(coverimage[row,column])[:4]
        secret_digit = '{0:08b}'.format(secretimage[row,column])[:4]
        new_digit = cover_digit + secret_digit

        emptyimage1[row, column] = int(new_digit, 2) # for comparison
        emptyimage2[row, column] = int(new_digit, 2)


# Save the image as "steganography.jpg"
cv2.imwrite('steganography.jpg', emptyimage2)

cv2.imshow('Cover Image', coverimage)
cv2.imshow('Secret Image', secretimage)
cv2.imshow('Steganography 1', emptyimage1)
cv2.imshow('Steganograpyh 2', emptyimage2)
cv2.waitKey(0)