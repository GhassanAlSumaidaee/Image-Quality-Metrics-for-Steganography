import cv2
import numpy as np

def calculate_psnr(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if mse == 0:
        return float('inf')
    max_pixel = 255.0
    psnr = 20 * np.log10(max_pixel / np.sqrt(mse))
    return psnr

# Load the original and steganographic images
original_image = cv2.imread("C:/Users/gh_m_/PycharmProjects/PythonExamples/Patient1.png")
steganographic_image = cv2.imread("C:/Users/gh_m_/PycharmProjects/PythonExamples/output_image.png")

# Calculate PSNR
psnr_value = calculate_psnr(original_image, steganographic_image)

print(f"PSNR: {psnr_value} dB")
