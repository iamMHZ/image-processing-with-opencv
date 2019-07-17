import numpy as np
import cv2

cap = cv2.VideoCapture()
cap.open("rtsp://admin:12345@169.254.4.155:7072/live/h264")

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', ret)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
