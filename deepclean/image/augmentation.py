from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2

from deepclean.main import Data


class Augmentation(Data):
    """
    Augmentation is a sub-class of Data Class which implements various methods
    for augmenting image data.
    """

    def __init__(self):
        pass


    def flip_image(self, image):
        """
        Flips a given image.

        Parameters
        ----------
        image : ndarray, ints, floats
                input data

        Returns
        ------
        denoised_image : ndarray, ints, floats
                Denoised image
        """

        img = Data._read_image(self, image)
        flipped_img = np.fliplr(img)
        return flipped_img

    def translation(self, image, shifting, width, height):
        """
        Translation

        Parameters
        ----------
        image : ndarray, ints, floats
                input data

        Returns
        ------
        denoised_image : ndarray, ints, floats
                Denoised image

        """

        img = Data._read_image(self, image)

        HEIGHT = height
        WIDTH = width

        if shifting == 'left':
            for i in range(HEIGHT, 1, -1):
                for j in range(WIDTH):
                    if (i < HEIGHT-20):
                        img[j][i] = img[j][i-20]
                    elif (i < HEIGHT-1):
                        img[j][i] = 0

        elif shifting == 'right':
            # Shifting target_height
            for j in range(WIDTH):
                for i in range(HEIGHT):
                    if (i < HEIGHT-20):
                        img[j][i] = img[j][i+20]

        elif shifting == 'up':
            # Shifting Up
            for j in range(WIDTH):
                for i in range(HEIGHT):
                    if (j < WIDTH - 20 and j > 20):
                        img[j][i] = img[j+20][i]
                    else:
                        img[j][i] = 0

        else:
            for j in range(WIDTH, 1, -1):
                for i in range(278):
                    if (j < 144 and j > 20):
                        img[j][i] = img[j-20][i]

        return img



    def add_noise(self, img, width, height, depth):
        """
        Adds random noise to the image.

        Parameters
        ----------
        image : ndarray, ints, floats
                input image
        height : int
                height of the image
        width : int
                width of the image
        depth : int
                depth of the image

        Returns
        ------
        denoised_image : ndarray, ints, floats
                Denoised image

        """

        img = Data._read_image(self, img)
        HEIGHT = height
        WIDTH = width
        DEPTH = depth

        noise = np.random.randint(5, size = (200, 300, 2), dtype = 'uint8')

        for i in range(WIDTH):
            for j in range(HEIGHT):
                for k in range(DEPTH):
                    if (img[i][j][k] != 255):
                        img[i][j][k] += noise[i][j][k]

        return img

    def contrast_adjust(self, image, alpha=1.3, beta=20):
        """
        Increase/ Decrease -- adjust the contrast of the given image.

        Parameters
        ----------
        image : ndarray, ints, floats
                input data

        Returns
        ------
        denoised_image : ndarray, ints, floats
                Denoised image

        """

        img = Data._read_image(self, image)
        newimage = img.astype(np.float32) * alpha + beta

        if type(img[0,0,0])==np.uint8:
            newimage[newimage < 0] = 0
            newimage[newimage > 255] = 255
            return np.uint8(newimage)
        else:
            newimage[newimage < 0] = 0
            newimage[newimage > 1] = 1.
            return newimage

    def random_flip(self, image, lr, ud):
        """
        Flips the given image randomly.

        Parameters
        ----------
        image : ndarray, ints, floats
                input data

        Returns
        -------
        denoised_image : ndarray, ints, floats
                Denoised image
        """
        img = Data._read_image(self, image)

        if lr:
            if np.random.random() > 0.5:
                img = cv2.flip(img, flipCode=1)
        if ud:
            if np.random.random() > 0.5:
                img = cv2.flip(img, flipCode=0)
        return img


    def image_crop(self, image, crop=None, random_crop=False):
        """
        Crop the given image.
            - If crop is None crop size is generated with a random size range from [0.5*height,height]
            - If random_crop == True image croped from a random position

        Parameters:
        -------------
        image: ndarray [H, W, C]
                input data
        crop: list, int
                [target_height, target_width], height and width of crop

        Returns:
        ----------
        croped image with shape[crop[0], crop[1], C]

        """
        image = Data._read_image(self, image)

        hei, wid, _ = image.shape
        if crop is None:
            crop = (np.random.randint(int(hei / 2),  hei), np.random.randint(int(wid / 2),  wid))
            th, tw = [int(round(x / 2)) for x in crop]
        if random_crop:
            th, tw = np.random.randint(0, hei - crop[0] - 1), np.random.randint(0, wid - crop[1] - 1)
        return image[th:th + crop[0], tw:tw + crop[1]]

    def image_pad(self, image, pad_width=None, axis=0, mode='symmetric'):
        """
        Adds padding to the given image.

        Parameters
        ----------
        image : ndarray, ints, floats
                input data
        pad_width : int

        Returns
        ------
        denoised_image : ndarray, ints, floats
                Denoised image
        """
        image = Data._read_image(self, image)
        hei,wid=image.shape[0],image.shape[1]

        if pad_width is None:
            th=hei//10
            tw=wid//10
            pad_width=((th,th),(tw,tw),(0,0))
        if axis==0:
            if type(pad_width[0])==tuple:
                pad_width=(pad_width[0],(0,0),(0,0))
            else:
                pad_width=(pad_width,(0,0),(0,0))
        if axis==1:
            if type(pad_width[0])==tuple:
                pad_width=((0,0),pad_width[1],(0,0))
            else:
                pad_width=((0,0),pad_width,(0,0))
        if len(image.shape)==3:
            newimage=np.pad(image,pad_width,mode)
        elif len(image.shape)==2:
            newimage=np.squeeze(np.pad(image[:,:,np.newaxis],pad_width,mode))

        return cv2.resize(newimage,(wid,hei),interpolation=cv2.INTER_NEAREST)
