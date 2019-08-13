import cv2

camera = cv2.VideoCapture(0)

while camera.isOpened():
    _, frame = camera.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    fast_feature_detector = cv2.FastFeatureDetector().create()

    key_points = fast_feature_detector.detect(gray, None)

    output = cv2.drawKeypoints(frame, key_points, frame)

    cv2.imshow("keypoints", output)

    key = cv2.waitKey(1)
    if key == 32:
        cv2.destroyAllWindows()
        camera.release()
        break
