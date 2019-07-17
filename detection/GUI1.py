# importing needed libraries

import cv2
import numpy as np


def emptyFunction():
    pass


def main():
    img = cv2.imread("D:\Programming\database of image\lena_color_256.tif")

    img1 = np.zeros((512, 512, 3), np.uint8)

    windowName = 'Colors'
    cv2.namedWindow(windowName)

    cv2.createTrackbar('Blue', windowName, 0, 255, emptyFunction)
    cv2.createTrackbar('Green', windowName, 0, 255, emptyFunction)
    cv2.createTrackbar('Red', windowName, 0, 255, emptyFunction)

    while (True):
        cv2.imshow(windowName, img)

        if cv2.waitKey(1) == 27:
            break

        blue = cv2.getTrackbarPos('Blue', windowName)
        green = cv2.getTrackbarPos('Green', windowName)
        red = cv2.getTrackbarPos('Red', windowName)

        cv2.putText(img1, str(blue) + str(green) + str(red), (20, 40), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 100, 255), 5)

        img[:] = [blue, green, red]
        print(blue, green, red)

    cv2.destroyAllWindows()

    cv2.imshow("Lena", cv2.imread("D:\Programming\database of image\lena_color_256.tif"))
    cv2.waitKey(0)


main()
