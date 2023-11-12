import cv2
import numpy as np
import matplotlib.pyplot as plt

# Resmi siyah beyaz olarak oku
image = cv2.imread("renkli_foto.jpg", 0)

# Resmi göster
cv2.imshow("Image", image)
cv2.waitKey()

# Histogram hesapla
def calculate_histogram(image):
    width, height = image.shape
    histogram = np.zeros(256)

    for row in range(width):
        for col in range(height):
            pixel_value = image[row, col]
            histogram[pixel_value] += 1

    return histogram

# Kumulatif histogram hesapla
def calculate_cumulative_histogram(image):
    width, height = image.shape
    histogram = np.zeros(256)
    cumulative_histogram = np.zeros(256)

    for row in range(width):
        for col in range(height):
            pixel_value = image[row, col]
            histogram[pixel_value] += 1

    cumulative_sum = 0
    for i in range(256):
        cumulative_sum += histogram[i]
        cumulative_histogram[i] = cumulative_sum

    normal_histogram = calculate_histogram(image)

    return cumulative_histogram, normal_histogram

# Kumulatif histogram ve normal histogramu hesapla
cumulative_histogram, normal_histogram = calculate_cumulative_histogram(image)

# Kumulatif histogramu görselleştir
plt.plot(range(256), cumulative_histogram)
plt.title("Cumulative Histogram")
plt.show()

# Normal histogramu görselleştir
plt.bar(range(256), normal_histogram)
plt.title("Normal Histogram")
plt.show()
