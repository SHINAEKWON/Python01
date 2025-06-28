import numpy as np
from PIL import Image

def ft_load(path: str) -> list:
    """
    This function allows to load an image file.
    Input should be (path + ) filename. 
    """

    try:
        img = Image.open(path)
        array = np.array(img)
        print(f"The shape of image is {array.shape}")
        print(array)
        return(array)

    except Exception as e:
        print("Unhandled error has occured:", e)
