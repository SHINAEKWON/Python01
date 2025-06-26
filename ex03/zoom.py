import numpy as np
from PIL import Image
from load_image import ft_load

def main():
    try:
        array = ft_load("animal.jpeg")
        r = array[:, :, 0]
        g = array[:, :, 1]
        b = array[:, :, 2]
        grayscale = 0.2989 * r + 0.5870 * g + 0.1140 * b
        grayscale = grayscale.astype(np.uint8)

        cropped = grayscale[0:400, 500:900]
        reshaped = cropped[:, :, np.newaxis]
        print("New shape after slicing:", reshaped.shape, "or", cropped.shape)
        print(reshaped[:, :, 0:1])

        img_to_save= Image.fromarray(reshaped.squeeze())
        img_to_save.save("modified.jpeg")

    except Exception as e:
        print("Unhandled error has occured:", e)

if __name__ == "__main__":
    main()
