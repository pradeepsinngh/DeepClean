import numpy as np
import cv2
import scipy.ndimage as nd
from skimage.restoration import (denoise_tv_chambolle, denoise_bilateral,
                                 denoise_wavelet, estimate_sigma)
from deepclean.image.main import CleanImage


class Denoise():
    '''
    Implements five different image denoising filters
    '''

    def __init__(self):
        pass

    def gauss_denoised(self, image):
        """
        """
        img = CleanImage.read_image(self, image)
        denoised_image = nd.gaussian_filter(img, 2)
        return denoised_image

    def med_denoised(self, image):
        """
        """
        img = CleanImage.read_image(self, image)
        denoised_image = nd.median_filter(img, 3)
        return denoised_image

    def total_variation_denoised(self, image):
        """
        """
        img = CleanImage.read_image(self, image)
        denoised_image = denoise_tv_chambolle(img,  weight=100)
        return denoised_image

    def bilateral_denoised(self, image):
        """
        """
        img = CleanImage.read_image(self, image)
        denoised_image = denoise_bilateral(img, sigma=0.1)
        return denoised_image

    def wavelet_denoised(self, image):
        """
        """
        img = CleanImage.read_image(self, image)
        denoised_image = denoise_wavelet(img, sigma=0.1)
        return denoised_image
