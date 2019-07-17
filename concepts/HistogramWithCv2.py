import cv2
import matplotlib.pyplot as plt


def main():
    image = cv2.imread("D:\Programming\database of image\sheep.jpg")

    red_channel_histogram = cv2.calcHist([image], [0], None, [255], [0, 255])
    green_channel_histogram = cv2.calcHist([image], [1], None, [255], [0, 255])
    blue_channel_histogram = cv2.calcHist([image], [2], None, [255], [0, 255])

    plt.plot(red_channel_histogram)
    plt.title("Red channel histogram")
    plt.show()

    plt.plot(green_channel_histogram)
    plt.title("Green channel histogram")
    plt.show()

    plt.plot(blue_channel_histogram)
    plt.title("Blue channel histogram")
    plt.show()


main()
