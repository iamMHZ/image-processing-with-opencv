import cv2


def main():
    camera = cv2.VideoCapture(0)

    print("Width", camera.get(3))
    print("Height", camera.get(4))

    windowName = "LIVE DEFAULT RESEOLUTION"
    cv2.namedWindow(windowName)

    camera.set(3, 960.0)
    camera.set(4, 720.0)

    while camera.isOpened():
        # img = None
        # camera.read(img)
        # img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        # cv2.imshow("LIVE", img)
        flag, frame = camera.read()
        cv2.imshow(windowName, frame)

        # hit space key to exit:
        if cv2.waitKey(1) == 32:
            break

    camera.release()
    cv2.destroyAllWindows()


main()
