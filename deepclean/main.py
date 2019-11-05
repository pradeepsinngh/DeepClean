import os, copy, cv2, imageio
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import numpy as np


class Data(object):
    """
    A base class for text, image data (and speech). It implements basic methods to provide
    support for child class.
    ...

    Attributes
    ---------
    file_name : str
        a str to store file name
    data : str
        a formatted string to print out what the animal says
    words : str
        list of strings, tokens from sentences
    count_words : int
        variable to store total number of words in given data
    count_sentences : int
        variable to store total number of sentences in given data
    each_word_count : dict
        python dict to store key: value for every word (key) and its count (value).
    shape : list
        dimensions of image in a list
    format : str
        format of image (eg: jpg/ png)

    Methods
    -------
    - getSummary() :
    - _file_or_not() :
    - _reader() :
    - _read_image()
    - _getDim()

    """

    filename = ''
    text = []
    nsentences = 0
    nwords = 0
    each_word_count = {}
    tokens = []
    words = []
    sentences = []
    dim = []

    def __init__(self, fname='', dtype = None):

        if dtype == "text":
            if fname:
                self.data, file =  self._reader(fname)
                self.words = [each.split(' ') for each in self.data]
                self.count_words = len([word for sent in self.words for word in sent])
                self.count_sentences = sum(each.count('.') for each in self.data)
                temp = self._flatlist(self.words)
                self.each_word_count = {x:temp.count(x) for x in temp}
                self.file_name = file.split('\\')[-1]
            else:
                pass

        elif dtype == "image":
            if fname:
                self.file_name = fname
                self.shape = self.getDim(fname)
                self.format = self.read_image(fname).format
            else:
                pass

        else:
            pass


    def _flatlist(self,lis):
        """
        Returns list of words.

        Parameters
        ----------
        lis : list
            words list

        Retunrs
        ------
        words : list
                Returns list of words in a given sentences in a list.

        """
        return [word for sent in lis for word in sent]


    def copy(self):
        """
        Create a copy of self.

        Parameters
        ----------
        text : str, optional
            The sound the animal makes (default is None)

        Returns
        ---------
        temp : file
                Returns a copy of file.
        """
        temp = copy.deepcopy(self)
        return temp


    def _file_or_not(self,arg):
        """
        Checks whether if arg is a regular file.

        Parameters
        ----------
        arg : str
            file name

        Returns
        ---------
        True : Boolean
                Return True if given arg is a file
        False: Boolean
                Return False if given arg is not a file.

        Raises
        ------
        ValueError
                Raise value error if given argument is not a valid file.

        """

        if os.path.isfile(arg):
            return True
        else:
            raise ValueError('Given arg is not a valid file.')


    def _reader(self,file):
        """
        Read given file.

        Parameters
        ----------
        text : str, optional
            file name

        Raises
        ------
        NotImplementedError
            If no sound is set for the animal or passed in as a
            parameter.
        """
        if type(file)==str and self._file_or_not(file)==True:
            with open(file,'r') as f:
                return f.readlines(),file

        elif type(file)==str:
            return file.split('\n'),''

        else: return file,''


    def _read_image(self, file):
        """
        Given a image filename, return image.

        Parameters
        ----------
        file : str
                file name of image

        Returns
        ----------
        img : image (2d array of pixels)
                Returns image

        Raises
        ------
        ValueError
            If file name is invalid, raise value error.
        """

        if type(file) == None: # or file is not:
            raise ValueError('file name not given or file does not exist. Check file name.')

        img = imageio.imread(file)
        return img

    def _getDim(self, file):
        """
        Return shape of a given image.

        Parameters
        ----------
        file : str
                image file name

        Returns
        ----------
        size : list
                list contains width and height of a image.

        Raises
        ------
        ValueError
            If file name is invalid, raise value error.
        """

        if file == None: # or file is not:
            raise ValueError('file name not given or file does not exist. Check file name.')

        img = Image.open(image)
        size = img.size
        return size


    def _getSummary(self, data, dtype):
        """
        Print summary of data - filename, words and sentences count, image shape and format etc.

        Parameters
        ----------
        data : text (.txt)/ image (.png/ .jpg)
                Text/ Image given by user

        dtype : str
                Type of data (text or image)

        Returns
        --------
                Doesn't return anything

        Raises
        -------
        ValueError
                If dtype value is not given/ invalid. dtype can only be: text or image as of now.
        """

        if dtype == "text":
            print('Filename:', self.file_name)
            print('Number of Words:', self.count_words)
            print('Number of Sentences:', self.count_sentences)

        elif dtype == "image":
            print('Filename:', self.file_name)
            print('Dimensions:', self.shape)
            print('Format:', self.format)

        else:
            raise ValueError("dtype is invalid or not given. dtype can only be: 'text' or 'image'.")
