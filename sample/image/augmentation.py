from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def flip_image(image, ):
    """
    """

    flipped_img = np.fliplr(img)
    return flipped_img

def translation(image, shiftting = None, width, height, depth):
    """
    """

    if shiftting == left:
        for i in range(HEIGHT, 1, -1):
            for j in range(WIDTH):
                if (i < HEIGHT-20):
                    img[j][i] = img[j][i-20]
                elif (i < HEIGHT-1):
                    img[j][i] = 0

    elif shiftting == right:
        # Shifting target_height
        for j in range(WIDTH):
            for i in range(HEIGHT):
                if (i < HEIGHT-20):
                    img[j][i] = img[j][i+20]

    elif Shifting == up:
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



def add_noise(img, width, height, depth):
    """
    """

    noise = np.random.randint(5, size = (164, 278, 4), dtype = 'uint8')

    for i in range(WIDTH):
        for j in range(HEIGHT):
            for k in range(DEPTH):
                if (img[i][j][k] != 255):
                    img[i][j][k] += noise[i][j][k]

    return img

# REf: https://freecontent.manning.com/the-computer-vision-pipeline-part-3-image-preprocessing/

def de_texture():
    """
    """

def de_color():
    """
    """

def edge_enhanced():
    """
    """

def salient_edge_map():
    """
    """
    
