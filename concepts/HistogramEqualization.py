import cv2
import matplotlib.pyplot as plt


def main():
    image = cv2.imread("D:\Programming\database of image\wiki.jpg", 0)

    normalized_image = cv2.equalizeHist(image)

    hist2 = cv2.calcHist([normalized_image], [0], None, [255], [0, 255])

    cv2.imshow("original", image)
    cv2.imshow("Normalized", normalized_image)

    hist1 = cv2.calcHist([image], [0], None, [255], [0, 255])
    plt.plot(hist1)
    plt.title("original histogram")
    plt.show()

    plt.plot(hist2)
    plt.title("equalized histogram")
    plt.show()

    cv2.waitKey(0)


main()
