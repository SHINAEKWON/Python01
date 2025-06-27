import numpy as np
from PIL import Image
from load_image import ft_load

def rotater(array: list) -> list:
    """
    This functions takes a list and rotate to 90 degrees.
    """
    try:
        new_array = []
        width =  len(array[0])
        height = len(array)
        for j in range(width):
            new_row=[]
            for i in range(0, height -1, 1):  #start, stop, step
                new_row.append(array[i][j])
            new_array.append(new_row)

    except Exception as e:
        print("Unhandled error has occured:", e)

    return new_array

def main():
    """
    Main entry point of rotate program.
    It takes, crops and rotate an image.
    """

    try:
        array = ft_load("animal.jpeg")
        cropped = array[50:450, 500:900]
        print(cropped)
        rotated = rotater(cropped)
        print(np.array(rotated))
        rotated = np.array(rotated)
        img_to_save=Image.fromarray(rotated.squeeze())
        img_to_save.save("rotated.jpeg")

    except Exception as e:
        print("Unhandled error has occured:", e)

if __name__ == "__main__":
    main()