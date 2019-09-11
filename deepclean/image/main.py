import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import cv2, os
import numpy as np
import imageio


class CleanImage(object):
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

    def __init__(self, fname = ''):

        if fname:
            self.filename = fname
            self.shape = self.read_image(fname).size
            #self.format = self.read_image(fname).format
        else:
            pass

    def read_image(self, file):
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
        img = Image.open(file)
        im = imageio.imread(file)
        return im

    def getDim(self, file):
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
        img = Image.open(file)
        return img.size

    # checks whether it has file path as argument
    def _file_or_not(self,arg):
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
        if os.path.isfile(arg):
            return True
        else:
            return False,"only supports .jpg for now"

    def getSummary(self, text):
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
        print('Filename:', self.file_name)
        print('Dimensions:', self.shape)
        print('Format:', self.format)
