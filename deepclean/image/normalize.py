from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2, os

from deepclean.image.main import CleanImage

class Normalize(CleanImage):
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

    def __inti__(self):
        pass

    def remove_mean(self, image):
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

        mean = [0.48462227599918,  0.45624044862054, 0.40588363755159]
        img = img.astype(np.float32)
        img = np.subtract(np.divide(img, 255.0), mean)
        return img


    def standardize(self, image, mean=0.48462227599918, std=0.22889466674951):
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
        img = img.astype(np.float32) / 255.0
        img = np.divide(np.subtract(img, mean), std)
        return img

    def sample_wise_normalization(self, image):
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
        data = img

        data.astype(np.float32)
        if np.max(data) == np.min(data):
            return np.ones_like(data, dtype=np.float32) * 1e-6
        else:
            return 1.0 * (data - np.min(data)) / (np.max(data) - np.min(data))
