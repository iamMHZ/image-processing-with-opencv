import cv2
import numpy as np


def main():
    camera = cv2.VideoCapture(0)

    while True:
        flag, frame = camera.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        edges = cv2.Canny(gray, 50, 150)

        # maxLineGap is the  maximum gap between two lines to become one line
        lines = cv2.HoughLinesP(edges, 2, np.pi / 180, 100, minLineLength=40, maxLineGap=10)

        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line.reshape(4)
                cv2.line(frame, (x1, y1), (x2, y2), (100, 255, 0), 2)
                cv2.line(gray, (x1, y1), (x2, y2), (100, 255, 0), 2)
                cv2.line(edges, (x1, y1), (x2, y2), (100, 255, 0), 2)
                cv2.imshow("Straight Lines on original frame", frame)
                cv2.imshow("Straight Lines on canny frame", edges)
                cv2.imshow("Straight Lines on gray frame", gray)

        # for line in lines:
        #     print(line)

        if (cv2.waitKey(1) == 32):
            break

    cv2.destroyAllWindows()
    camera.release()


main()
