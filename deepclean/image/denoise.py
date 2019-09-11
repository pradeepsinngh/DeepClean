import numpy as np
import cv2
import scipy.ndimage as nd
from skimage.restoration import (denoise_tv_chambolle, denoise_bilateral,
                                 denoise_wavelet, estimate_sigma)
from deepclean.image.main import CleanImage


class Denoise():
    """
    A class used to represent Tokenization techniques for text.

    ...

    Attributes
    ----------
    says_str : str
        a formatted string to print out what the animal says
    name : str
        the name of the animal
    sound : str
        the sound that the animal makes
    num_legs : int
        the number of legs the animal has (default 4)

    Methods
    -------
    split_by_words(text)
        Return the sentences splitted by white spaces.

    split_by_words(text)
        Retunr

    split_into_sentences(text)

    split_into_words(text)
    """

    def __init__(self):
        pass

    def gauss_denoised(self, image):
        """Prints what the animals name is and what sound it makes.

        If the argument `sound` isn't passed in, the default Animal
        sound is used.

        Parameters
        ----------
        text : str, optional
            The sound the animal makes (default is None)

        Raises
        ------
        NotImplementedError
            If no sound is set for the animal or passed in as a
            parameter.
        """
        img = CleanImage.read_image(self, image)
        denoised_image = nd.gaussian_filter(img, 2)
        return denoised_image

    def med_denoised(self, image):
        """Prints what the animals name is and what sound it makes.

        If the argument `sound` isn't passed in, the default Animal
        sound is used.

        Parameters
        ----------
        text : str, optional
            The sound the animal makes (default is None)

        Raises
        ------
        NotImplementedError
            If no sound is set for the animal or passed in as a
            parameter.
        """
        img = CleanImage.read_image(self, image)
        denoised_image = nd.median_filter(img, 3)
        return denoised_image

    def total_variation_denoised(self, image):
        """Prints what the animals name is and what sound it makes.

        If the argument `sound` isn't passed in, the default Animal
        sound is used.

        Parameters
        ----------
        text : str, optional
            The sound the animal makes (default is None)

        Raises
        ------
        NotImplementedError
            If no sound is set for the animal or passed in as a
            parameter.
        """
        img = CleanImage.read_image(self, image)
        denoised_image = denoise_tv_chambolle(img,  weight=100)
        return denoised_image

    def bilateral_denoised(self, image):
        """Prints what the animals name is and what sound it makes.

        If the argument `sound` isn't passed in, the default Animal
        sound is used.

        Parameters
        ----------
        text : str, optional
            The sound the animal makes (default is None)

        Raises
        ------
        NotImplementedError
            If no sound is set for the animal or passed in as a
            parameter.
        """
        img = CleanImage.read_image(self, image)
        denoised_image = denoise_bilateral(img, sigma=0.1)
        return denoised_image

    def wavelet_denoised(self, image):
        """Prints what the animals name is and what sound it makes.

        If the argument `sound` isn't passed in, the default Animal
        sound is used.

        Parameters
        ----------
        text : str, optional
            The sound the animal makes (default is None)

        Raises
        ------
        NotImplementedError
            If no sound is set for the animal or passed in as a
            parameter.
        """
        img = CleanImage.read_image(self, image)
        denoised_image = denoise_wavelet(img, sigma=0.1)
        return denoised_image
