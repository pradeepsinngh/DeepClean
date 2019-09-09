import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import cv2, os
import numpy as np
import imageio


class CleanImage(object):

    def __init__(self, fname = ''):

        if fname:
            self.filename = fname
            self.shape = self.read_image(fname).size
            #self.format = self.read_image(fname).format
        else:
            pass

    def read_image(self, file):
        img = Image.open(file)
        im = imageio.imread(file)
        return im

    def getDim(self, file):
        img = Image.open(file)
        return img.size

    # checks whether it has file path as argument
    def _file_or_not(self,arg):
        if os.path.isfile(arg):
            return True
        else:
            return False,"only supports .jpg for now"

    def getSummary(self, text):
        print('Filename:', self.file_name)
        print('Dimensions:', self.shape)
        print('Format:', self.format)
