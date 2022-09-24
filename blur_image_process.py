import cv2
import numpy as np
from skimage.util import random_noise
# Load an image
im_arr = cv2.imread("herhangigörsel.PNG")
# Add salt and pepper noise to the image
noise_img = random_noise(im_arr, mode="s&p",amount=0.3)
noise_img = np.array(255*noise_img, dtype = 'uint8')
# Apply median filter
median = cv2.medianBlur(noise_img,5)
Görselin blur’lanması.