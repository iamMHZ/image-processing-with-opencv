import cv2


def main():
    camera = cv2.VideoCapture(0)

    while True:
        flag, frame = camera.read()

        # frame = cv2.cvtColor(frame , cv2.COLOR_RGB2GRAY)

        edges = cv2.Laplacian(frame, -1, ksize=5)

        cv2.imshow("Original", frame)
        cv2.imshow("egedes using Laplacian Algorithm", edges)

        if (cv2.waitKey(1) == 32):
            break

    cv2.destroyAllWindows()
    camera.release()


main()
