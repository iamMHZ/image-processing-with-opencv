import cv2


def main():
    camera = cv2.VideoCapture(0)

    print(camera.get(cv2.CAP_PROP_FPS))
    print(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(camera.get(cv2.CAP_PROP_FOCUS))
    print(camera.get(cv2.CAP_PROP_FORMAT))

    while camera.isOpened():
        _, frame = camera.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 50, 150, cv2.THRESH_BINARY)
        contour, hierachy = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        cv2.drawContours(frame, contour, -1, (0, 0, 255))
        cv2.imshow("frame", frame)
        # cv2.imshow("contoures", contour)

        if (cv2.waitKey(1) == 32):
            break

    camera.release()
    cv2.destroyAllWindows()


main()
