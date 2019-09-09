from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2, os

from deepclean.image.main import CleanImage

class Normalize(CleanImage):

    def __inti__(self):
        pass

    def remove_mean(self, image):
        """
        remove RGB mean values which from ImageNet
        input:
            image:  RGB image np.ndarray
                    type of elements is np.uint8
        return:
            image:  remove RGB mean and scale to [0,1]
                    type of elements is np.float32
        """

        img = CleanImage.read_image(self, image)

        mean = [0.48462227599918,  0.45624044862054, 0.40588363755159]
        img = img.astype(np.float32)
        img = np.subtract(np.divide(img, 255.0), mean)
        return img


    def standardize(self, image, mean=0.48462227599918, std=0.22889466674951):
        """
        standardize RGB mean and std values which from ImageNet
        input:
            image:  RGB image np.ndarray
                    type of elements is np.uint8
        return:
            image:  standarded image
                    type of elements is np.float32
        """
        img = CleanImage.read_image(self, image)
        img = img.astype(np.float32) / 255.0
        img = np.divide(np.subtract(img, mean), std)
        return img

    def sample_wise_normalization(self, image):
        """
        normalize each sample to 0-1
        Input:
            sample image
        Output:
            Normalized sample
            x=1.0*(x-np.min(x))/(np.max(x)-np.min(x))
        """
        img = CleanImage.read_image(self, image)
        data = img

        data.astype(np.float32)
        if np.max(data) == np.min(data):
            return np.ones_like(data, dtype=np.float32) * 1e-6
        else:
            return 1.0 * (data - np.min(data)) / (np.max(data) - np.min(data))
