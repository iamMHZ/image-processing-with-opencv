# this tutorial is about colorSpaces

import matplotlib.pyplot as plt
import cv2


def main():
    # image location:
    path = "D:\Programming\database of image\lena_color_256.tif"
    # create two images :
    image = cv2.imread(path)
    image2 = cv2.imread(path)

    plt.imshow(image)
    plt.title("BGR")
    plt.show()

    # convert first image to RGB to plot the image in the normal way:
    image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
    plt.imshow(image2)
    plt.title("RGB")
    # remove numbers around  corners :
    plt.xticks([])
    plt.yticks([])
    plt.show()


# just call that method that we just created:
main()
