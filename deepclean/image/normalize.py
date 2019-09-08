from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2, os



def remove_mean(image):
    """
    remove RGB mean values which from ImageNet
    input:
        image:  RGB image np.ndarray
                type of elements is np.uint8
    return:
        image:  remove RGB mean and scale to [0,1]
                type of elements is np.float32
    """
    mean = [0.48462227599918,  0.45624044862054, 0.40588363755159]
    image = image.astype(np.float32)
    image = np.subtract(np.divide(image, 255.0), mean)
    return image


def standardize(image, mean=[0.48462227599918,  0.45624044862054, 0.40588363755159], std=[0.22889466674951, 0.22446679341259, 0.22495548344775]):
    """
    standardize RGB mean and std values which from ImageNet
    input:
        image:  RGB image np.ndarray
                type of elements is np.uint8
    return:
        image:  standarded image
                type of elements is np.float32
    """
    image = image.astype(np.float32) / 255.0
    image = np.divide(np.subtract(image, mean), std)
    return image

def sample_wise_normalization(data):
    """
    normalize each sample to 0-1
    Input:
        sample image
    Output:
        Normalized sample
    x=1.0*(x-np.min(x))/(np.max(x)-np.min(x))
    """
    data.astype(np.float32)
    if np.max(data) == np.min(data):
        return np.ones_like(data, dtype=np.float32) * 1e-6
    else:
        return 1.0 * (data - np.min(data)) / (np.max(data) - np.min(data))
