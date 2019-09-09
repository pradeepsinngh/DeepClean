import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import cv2, os
import numpy as np

import deepclean.image.main as img
import deepclean.image.normalize as nz
import deepclean.image.augmentation as aug
import deepclean.image.denoise as dn


file = 'cat.jpg'

ob = dn.Denoise()
ob.total_variation_denoised(file)
