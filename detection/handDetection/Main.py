from HandDetection import *
import cv2

histogram = calculate_histogram(0)

camera = cv2.VideoCapture(0)

while camera.isOpened():
    ret, frame = camera.read(0)
    frame = cv2.flip(frame, 1)

    # apply_back_projection(frame, histogram)
    is_found = detect_object(frame, histogram)

    if is_found:
        cv2.imshow("frame", frame)
    if cv2.waitKey(1) == 32:
        break

cv2.destroyAllWindows()
camera.release()
