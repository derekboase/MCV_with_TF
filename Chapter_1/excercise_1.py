import matplotlib.pyplot as plt
import numpy as np

import cv2

from PIL import Image

image = Image.open('imgs/car1.jpg')
plt.imshow(image)

image_arr = np.asarray(image)
print(image_arr.shape)
print()

## For gray scale
# gray = cv2.cvtColor(image_arr, cv2.COLOR_BGR2GRAY)
# plt.imshow(gray, cmap='gray')
# plt.show()

for chan in range(image_arr.shape[-1]):
    print(chan)
    plt.imshow(image_arr[:, :, chan])
    plt.show()