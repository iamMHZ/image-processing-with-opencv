# should i use erode or dilate or any nose removal algorithm????
import cv2
import numpy as np

camera = cv2.VideoCapture(0)

while camera.isOpened():
    check, frame = camera.read()

    boundaries = [
        # low and high boundary for  **BGR**  colorSpace:
        # red
        ([17, 15, 100], [50, 56, 200]),
        # blue
        ([86, 31, 4], [220, 88, 50]),
        # yellow
        ([25, 146, 190], [62, 174, 250]),
        # green
        # ([103, 86, 65], [145, 133, 128])
    ]

    for (low, high) in boundaries:
        color = high
        # convert tuple to array because cv2.inRange gets array not tuple
        low = np.array(low, dtype='uint8')
        high = np.array(high, dtype='uint8')

        mask = cv2.inRange(frame, low, high)

        # mask_copy = mask.copy()
        # kernel = np.ones((5, 5), np.uint8)
        # mask = cv2.GaussianBlur(mask, (3, 3), 0)
        # cv2.erode(mask, kernel)
        # cv2.dilate(mask, kernel)

        conts, h = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        cv2.drawContours(frame, conts, -1, color, 3)
        # for i in range(len(conts)):
        #     x, y, w, h = cv2.boundingRect(conts[i])
        #     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow("mask", mask)

    cv2.imshow("frame", frame)

    if cv2.waitKey(1) == 32:
        break

camera.release()
cv2.destroyAllWindows()
