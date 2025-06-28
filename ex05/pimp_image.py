from load_image import ft_load
from PIL import Image
import numpy as np

def ft_invert(array) -> list:
    """
    This function takes an array of image(3d numpy list or numpy array) and inverts colors.
    It returns a list array of inverted image.
    """
    try:
        inverted = 255 - array
        img_to_save=Image.fromarray(inverted)
        img_to_save.save("inverted.jpg")

    except Exception as e:
        print("Error has occured:", e)
        return []

    return inverted


def ft_red(array) -> list:
    """
    This function takes an array of image(3d numpy list or numpy array) and preserves only red colors.
    It returs a list array of filtered image in red.
    """
    try:
        np_array = np.array(array)
        
        red = np_array * [1, 0, 0]

        # After multiplication uint8 switches to int8
        # So it must be converted again to uint8
        if red.dtype != np.uint8:
            red = red.astype(np.uint8)

        img=Image.fromarray(red)
        img.save("red.jpg")

    except Exception as e:
        print("Error has occured:", e)
        return []

    return red

def ft_green(array) -> list:
    """
    This function takes an array of image(3d numpy list or numpy array) and preserves only green colors.
    It returs a list array of filtered image in green.
    """
    try:
        np_array = np.array(array)

        # print(np_array.ndim)
        # print(np_array.shape)
        # print(np_array[0][0])
        # print(np_array[0][0][1])
        # print(np_array.shape[2])
        # print(np_array.dtype)

        green = np.zeros_like(np_array)
        green[:, :, 1] = np_array[:, :, 1]
        green = np_array - (np_array - green) #Line added only to use the '-' operator

        img = Image.fromarray(green)
        img.save("green.jpg")

    except Exception as e:
        print("Error has occured:", e)
        return []
    
    return green

def ft_blue(array) -> list:
    """
    This function takes an array of image(3d numpy list or numpy array) and preserves only blue colors.
    It returs a list array of filtered image in blue.
    """
    try:
        np_array = np.array(array)

        blue = np.zeros_like(np_array)
        blue[:, :, 2] = np_array[:, :, 2]

        img = Image.fromarray(blue)
        img.save("blue.jpg")
    
    except Exception as e:
        print("Error has occured:", e)
        return []

    return blue

def ft_grey(array) -> list:
    """
    This functions transforms an RGB image to a grayscale image
    Input parameter: an array
    Return value: list
    """
    try:
        np_array = np.array(array)
        r = np_array[:, :, 0]
        g = np_array[:, :, 1]
        b = np_array[:, :, 2]

        r = r / (1000/299)
        g = g / (1000/587)
        b = b / (1000/114)

        gray_stack = np.stack([r, g, b], axis=2)
        gray = np.sum(gray_stack, axis=2)

        gray = gray.astype(np.uint8)

        img = Image.fromarray(gray)
        img.save("gray.jpg")

    except Exception as e:
        print("Error has occured:", e)
        return []

    return gray
