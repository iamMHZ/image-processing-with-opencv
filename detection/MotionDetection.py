import cv2


def main():
    camera = cv2.VideoCapture(0)

    _, frame1 = camera.read()
    _, frame2 = camera.read()

    while camera.isOpened():

        diff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        gray = cv2.blur(gray, (5, 5))

        _, thresh = cv2.threshold(gray, 10, 250, cv2.THRESH_BINARY)
        # thresh = cv2.dilate(thresh, (5, 5))

        # using frame3 for drawing contours we can not use frame2 because gray and diff are based on frame2
        # so the contours will draw on them too
        frame3 = frame2.copy()
        contours, hierchay = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(frame3, contours, -1, (0, 255, 100), 2)

        cv2.imshow("Diff", diff)
        cv2.imshow("Thresh", thresh)
        cv2.imshow("GRAY", gray)
        cv2.imshow("Original", frame2)
        cv2.imshow("Motion detection", frame3)

        frame1 = frame2

        _, frame2 = camera.read()

        if cv2.waitKey(1) == 32:
            break

    camera.release()
    cv2.destroyAllWindows()


main()
