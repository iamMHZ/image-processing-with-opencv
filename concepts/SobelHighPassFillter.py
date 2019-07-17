import cv2


def main():
    camera = cv2.VideoCapture(0)

    while True:
        flag, frame = camera.read()

        edges = cv2.Sobel(frame, -1, 1, 0, ksize=3)

        cv2.imshow("Original", frame)
        cv2.imshow("edges", edges)

        if (cv2.waitKey(1) == 32):
            break


main()
