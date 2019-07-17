import cv2


def main():
    camera = cv2.VideoCapture(0)

    camera.set(3, 300)
    camera.set(4, 500)

    while camera.isOpened():
        _, img = camera.read()

        _, img1 = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY)
        _, img2 = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY_INV)
        _, img3 = cv2.threshold(img, 200, 155, cv2.THRESH_MASK)
        _, img4 = cv2.threshold(img, 125, 255, cv2.THRESH_TOZERO)
        _, img5 = cv2.threshold(img, 125, 255, cv2.THRESH_TRUNC)
        _, img6 = cv2.threshold(img, 125, 255, cv2.THRESH_TOZERO_INV)
        # _, img7 = cv2.threshold(img, 125, 255, cv2.THRESH_OTSU)

        cv2.imshow("ORIGINAL ", img)
        cv2.imshow("Binary", img1)
        cv2.imshow("Binary Invert", img2)
        cv2.imshow("Mask", img3)
        cv2.imshow("TOZero", img4)
        cv2.imshow("TRUNK", img5)
        cv2.imshow("TOZERO Invert", img6)
        # cv2.imshow("OTSU", img7)

        if cv2.waitKey(1) == 32:
            break

    camera.release()
    cv2.destroyAllWindows()


main()
