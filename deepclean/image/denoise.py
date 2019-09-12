import numpy as np
import cv2
import scipy.ndimage as nd
from skimage.restoration import (denoise_tv_chambolle, denoise_bilateral,
                                 denoise_wavelet, estimate_sigma)
from deepclean.image.main import CleanImage

class Denoise():
    """
    Denoise is a sub-class  of Data Class which implements various methods
    for denoising image data.

    ...

    Attributes
    ----------


    """

    def __init__(self):
        pass

    def gauss_denoised(self, image):
        """
        Denoise image using gauss filter.

        Parameters
        ----------
        image : ndarray
                input data

        Returns
        ------
        denoised_image : ndarray
                Denoised image

        """
        img = CleanImage.read_image(self, image)
        denoised_image = nd.gaussian_filter(img, 2)
        return denoised_image

    def med_denoised(self, image):
        """
        Denoise image using median filter.

        Parameters
        ----------
        image : ndarray
                input data

        Returns
        ------
        denoised_image : ndarray
                Denoised image

        """
        img = CleanImage.read_image(self, image)
        denoised_image = nd.median_filter(img, 3)
        return denoised_image

    def total_variation_denoised(self, image):
        """
        Perform total-variation denoising.

        Parameters
        ----------
        image : ndarray
                input data

        Returns
        ------
        denoised_image : ndarray
                Denoised image

        """
        img = CleanImage.read_image(self, image)
        denoised_image = denoise_tv_chambolle(img,  weight=100)
        return denoised_image

    def bilateral_denoised(self, image):
        """
        Denoise image using bilateral filter.


        Parameters
        ----------
        image : ndarray
                input data

        Returns
        ------
        denoised_image : ndarray
                Denoised image

        """
        img = CleanImage.read_image(self, image)
        denoised_image = denoise_bilateral(img, sigma=0.1)
        return denoised_image

    def wavelet_denoised(self, image):
        """
        Perform wavelet denoising on an image.


        Parameters
        ----------
        image : ndarray
                input data

        Returns
        ------
        denoised_image : ndarray
                Denoised image

        """
        img = CleanImage.read_image(self, image)
        denoised_image = denoise_wavelet(img, sigma=0.1)
        return denoised_image
