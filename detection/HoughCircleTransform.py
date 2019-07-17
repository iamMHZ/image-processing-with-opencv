import cv2


def main():
    camera = cv2.VideoCapture(0)

    while camera.isOpened():
        _, frame = camera.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        circle_2D_array = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 1)

        if circle_2D_array is not None:
            for circles in circle_2D_array:
                print(len(circles), circles)
                for circle in circles:
                    x, y, r = circle.reshape(3)
                    cv2.circle(frame, (x, y), r, (0, 200, 150), thickness=2)

        cv2.imshow("frame", frame)

        if (cv2.waitKey(1) == 32):
            break

    camera.release()
    cv2.destroyAllWindows()


main()
