import cv2
import numpy as np


def main():
    camera = cv2.VideoCapture(0)

    camera.set(3, 300)
    camera.set(4, 300)
    # i = 1

    while camera.isOpened():
        flag, frame = camera.read()

        blur = cv2.blur(frame, (5, 5))
        gaussian_blur = cv2.GaussianBlur(frame, (7, 7), 12)
        median_blur = cv2.medianBlur(frame, 5)

        # self-defined kernel:
        kernel = np.array(([1, 1, 1, 1, 1], [1, 1, -5, 1, 1], [1, 1, 1, 1, 1]))
        effect = cv2.filter2D(frame, -1, kernel)

        # cv2.imwrite("C:\\Users\hMd\\Desktop\\new\\result" + str(i) + ".jpg", effect)
        # i += 1

        cv2.imshow("Original", frame)
        cv2.imshow("Blur", blur)
        cv2.imshow("Gaussian", gaussian_blur)
        cv2.imshow("Median", median_blur)
        cv2.imshow("Effect", effect)

        if cv2.waitKey(1) == 32:
            break

    camera.release()
    cv2.destroyAllWindows()


main()
