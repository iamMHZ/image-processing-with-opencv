import cv2
import time


def main():
    camera = cv2.VideoCapture(0)

    # flag, frame = camera.read()

    # time.sleep(0.5)

    while camera.isOpened():
        flag, frame = camera.read()

        frame1 = cv2.cvtColor(frame.copy(), cv2.COLOR_BGR2RGB)

        (R, G, B) = cv2.split(frame1)

        cv2.imshow("ORIGINAL", frame)
        cv2.imshow("RED CHANNEL", R)
        cv2.imshow("BLUE CHANNEL", B)
        cv2.imshow("GREEN CHANNEL", G)

        if cv2.waitKey(1) == 32:
            break

    camera.release()
    cv2.destroyAllWindows()


main()
