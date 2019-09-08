import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import cv2, os
import numpy as np

import deepclean.image.main as img

file = 'cat.jpg'

ob = img.CleanImage(file)
ob.read_image(file)
