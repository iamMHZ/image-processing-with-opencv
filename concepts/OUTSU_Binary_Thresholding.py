import cv2
import matplotlib.pyplot as plt


def main():
    original = cv2.imread("D:\Programming\database of image\woman_blonde.tif", 0)
    cv2.imshow("original", original)

    _, binary = cv2.threshold(original, 100, 255, cv2.THRESH_BINARY)
    # when we wanna separate background and foreground  we use OTSU algorithm
    _, binary_outsu = cv2.threshold(original, 0, 255, cv2.THRESH_OTSU)

    cv2.imshow("original", original)
    cv2.imshow("binary", binary)
    cv2.imshow("BINARY_OUTSU", binary_outsu)

    # plt.imshow(binary , cmap='gray')
    # plt.show()

    cv2.waitKey(0)


main()
