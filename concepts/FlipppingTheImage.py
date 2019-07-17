import cv2
import numpy as np


def main():
    capture = cv2.VideoCapture(0)
    rainVideo = cv2.VideoCapture('E:\LEARN\\2.1) OpenCv\Kerman workshop\session 2\\rain.mp4')

    while True:
        _, frame = capture.read()
        _, rainFrame = rainVideo.read()

        rainFrame = cv2.resize(rainFrame, frame.shape[1::-1])

        flippingByX = np.copy(frame)
        flippingByY = np.copy(frame)
        flippingByXY = np.copy(frame)

        cv2.flip(frame, 0, flippingByX)
        cv2.flip(frame, 1, flippingByY)
        cv2.flip(frame, -1, flippingByXY)

        cv2.imshow("original", frame)
        cv2.imshow("flipped by X axis ", flippingByX)
        cv2.imshow("flipped by Y axis", flippingByY)
        cv2.imshow("flipped by X and Y axises ", flippingByXY)
        cv2.imshow("RAINY", frame + rainFrame)

        if cv2.waitKey(1) == 32:
            break

    cv2.destroyAllWindows()
    capture.release()
    rainVideo.release()


main()
