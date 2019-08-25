import cv2
import numpy as np


def main():
    # image = cv2.imread("D:\Programming\database of image\\art3.jpg")
    image = cv2.imread("D:\Programming\database of image\\test1.jpg")
    cv2.imshow("original", image)

    kernel = np.ones((5, 5), np.uint8)
    erode = cv2.erode(image, kernel)

    cv2.imshow("Erode", erode)

    dilate = cv2.dilate(image, kernel)
    cv2.imshow("Dilate", dilate)

    open_ = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    cv2.imshow("open", open_)

    close = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("close", close)

    gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)
    cv2.imshow("gradient", gradient)

    top_hat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)
    cv2.imshow("top hat", top_hat)

    black_hat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)
    cv2.imshow("back hat", black_hat)

    cv2.waitKey(0)


main()
