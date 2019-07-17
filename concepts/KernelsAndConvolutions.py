import cv2
import numpy as np


def main():
    camera = cv2.VideoCapture(0)

    while True:
        flag, frame = camera.read()

        sharpen_kernel = np.array(([0, -1, 0], [-1, 5, -1], [0, -1, 0]), np.float32)
        edge_detection_kernel = np.array(([-1, -1, -1], [-1, 8, -1], [-1, -1, -1]), np.float32)

        # -1 is depth
        sharpen = cv2.filter2D(frame, -1, sharpen_kernel)
        edges = cv2.filter2D(frame, -1, edge_detection_kernel)

        cv2.imshow("Original", frame)
        cv2.imshow("sharpen", sharpen)
        cv2.imshow("edges", edges)

        if (cv2.waitKey(1) == 32):
            break

    cv2.destroyAllWindows()
    camera.release()


main()
