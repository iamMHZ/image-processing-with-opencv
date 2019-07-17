import cv2


def main():
    camera = cv2.VideoCapture(0)

    camera.set(3, 500)
    camera.set(4, 300)

    print("Width: ", camera.get(3))
    print("Height: ", camera.get(4))

    while camera.isOpened():

        flag, frame = camera.read()

        # tuple = (frame,)

        cv2.imshow("RGB", frame)

        img1 = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        cv2.imshow("BGR", img1)

        img2 = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        cv2.imshow("GRAY", img2)

        img3 = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
        cv2.imshow("HSV", img3)

        img4 = cv2.cvtColor(frame, cv2.COLOR_RGB2HLS)
        cv2.imshow("HLS", img4)

        img5 = cv2.cvtColor(frame, cv2.COLOR_RGB2LAB)
        cv2.imshow("LAB", img5)

        img6 = cv2.cvtColor(frame, cv2.COLOR_RGB2LUV)
        cv2.imshow("LUV", img6)

        if cv2.waitKey(1) == 32:
            break

    camera.release()
    cv2.destroyAllWindows()


main()
