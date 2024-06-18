import cv2
import numpy as np
from skimage.metrics import structural_similarity as compare_ssim

# Load the original and steganographic images
original_image = cv2.imread("C:/Users/gh_m_/PycharmProjects/PythonExamples/Patient1.png")
steganographic_image = cv2.imread("C:/Users/gh_m_/PycharmProjects/PythonExamples/output_image.png")

# Convert the images to grayscale
original_gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
steganographic_gray = cv2.cvtColor(steganographic_image, cv2.COLOR_BGR2GRAY)

# Calculate SSIM
ssim_value = compare_ssim(original_image, steganographic_image)

print(f"SSIM: {ssim_value}")
