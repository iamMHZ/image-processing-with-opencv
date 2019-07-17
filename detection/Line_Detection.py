import cv2
import numpy as np


def main():
    camera = cv2.VideoCapture(0)
    # camera.set(3 , 900)
    # camera.set(4 , 700)
    while True:
        flag, frame = camera.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # tresholding the gray image in a specific range:
        edges = cv2.Canny(gray, 70, 180)
        # finding lines using below function:
        lines = cv2.HoughLinesP(edges, 1, np.pi, -200)

        for line in lines:
            x1, y1, x2, y2 = line[0]
            if x1 == x2 or y1 == y2:
                cv2.line(frame, (x1, y1), (x2, y2), (50, 100, 155), 2)

        cv2.imshow("LINE DETECTION", frame)
        cv2.imshow("Gray", gray)
        cv2.imshow("Edges", edges)
        # cv2.imshow("LINES", line)

        if cv2.waitKey(1) == 32:
            break

    camera.release()
    cv2.destroyAllWindows()


main()
