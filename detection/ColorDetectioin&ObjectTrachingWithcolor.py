import cv2
from array import *


def main():
    camera = cv2.VideoCapture(0)

    while camera.isOpened():
        flag, frame = camera.read()

        hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Blue
        # low = (100, 50, 50)
        # high = (140, 255, 255)

        # Red
        # low = (0, 7, 100)
        # high = (100, 100, 255)

        # Green
        # low = (20, 50, 50)
        # high = (80, 255, 255)

        # Tested dark red:
        low = (150, 150, 50)
        high = (180, 255, 255)

        # tested yellow:
        # low = (20, 100, 100)
        # high = (30, 255, 255)

        # testing :
        # low = (0, 0, 0)
        # high = (180, 255, 255)

        masked_img = cv2.inRange(hsv_img, low, high)

        detected_area = cv2.bitwise_and(frame, frame, None, masked_img)

        conts, h = cv2.findContours(masked_img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        cv2.drawContours(frame, conts, -1, (255, 0, 0), 3)
        # for i in range(len(conts)):
        #     x, y, w, h = cv2.boundingRect(conts[i])
        #     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.imshow("I", frame)
        cv2.imshow("Am", masked_img)
        cv2.imshow("MHZ", detected_area)

        if cv2.waitKey(1) == 32:
            break

    camera.release()
    cv2.destroyAllWindows()


main()
