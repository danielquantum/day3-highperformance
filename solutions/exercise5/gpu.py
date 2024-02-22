# Write a 2D Fourier transform on arrays of size 128x128 using numpy
import numpy as np
import matplotlib.pyplot as plt

# Generate a 128x128 array (you can replace this with your own data)
data = np.random.random((128, 128))

# Perform 2D Fourier transform
fourier_transform = np.fft.fft2(data)

# Shift zero frequency component to the center
fourier_transform_shifted = np.fft.fftshift(fourier_transform)

# Calculate the magnitude spectrum
magnitude_spectrum = np.abs(fourier_transform_shifted)

# Display the original image and its Fourier transform
plt.subplot(121), plt.imshow(data, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(np.log(1 + magnitude_spectrum), cmap='gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])

plt.show()
