# should i use erode or dilate or any nose removal algorithm
import cv2

camera = cv2.VideoCapture(0)

while camera.isOpened():
    check, frame = camera.read()

    frame_copy = frame.copy()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    low = (45, 65, 20)
    high = (70, 255, 200)

    mask = cv2.inRange(frame, low, high)

    output = cv2.bitwise_and(frame_copy, frame_copy, mask=mask)

    conts, h = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(frame, conts, -1, (255, 0, 0), 3)
    # for i in range(len(conts)):
    #     x, y, w, h = cv2.boundingRect(conts[i])
    #     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow("frame", frame)
    cv2.imshow("bitwise and", output)
    cv2.imshow("mask", mask)

    if cv2.waitKey(1) == 32:
        break

camera.release()
cv2.destroyAllWindows()
