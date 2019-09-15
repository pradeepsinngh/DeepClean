from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2, os

from deepclean.main import Data

class Normalize(Data):
    """
    Normalize is a sub-class  of Data Class which implements various methods
    for normalizing text data.

    ...

    Attributes
    ----------


    """

    def __inti__(self):
        pass

    def remove_mean(self, image):
        """
        Subtract give mean from each pixel of the image.

        Parameters
        ----------
        image : ndarray
                input data

        Returns:
        ----------
        img : int (2d array of ints)
                normalized 2d array of pixel values
        """

        img = Data._read_image(self, image)

        mean = [0.48462227599918,  0.45624044862054, 0.40588363755159]
        img = img.astype(np.float32)
        img = np.subtract(np.divide(img, 255.0), mean)
        return img


    def standardize(self, image, mean=0.48462227599918, std=0.22889466674951):
        """
        standardize a given image, by subtracting mean and dividing by standar deviation.

        Parameters
        ----------
        image : ndarray
                input data

        mean : float
                given mean, will be subtracted from each pixel

        std : float
                given standar deviation, will be subtracted from each pixel.

        Returns
        ---------
        img : int (2d array of ints)
                2d array of pixel values


        """
        img = Data._read_image(self, image)
        img = img.astype(np.float32) / 255.0
        img = np.divide(np.subtract(img, mean), std)
        return img

    def sample_wise_normalization(self, image):
        """
        Sample wise normalization.

        Parameters
        ----------
        image : ndarray
                input data

        Returns
        ------

        """
        img = Data._read_image(self, image)
        data = img

        data.astype(np.float32)
        if np.max(data) == np.min(data):
            return np.ones_like(data, dtype=np.float32) * 1e-6
        else:
            return 1.0 * (data - np.min(data)) / (np.max(data) - np.min(data))
