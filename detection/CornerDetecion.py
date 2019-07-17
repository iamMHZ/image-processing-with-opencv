import cv2


def main():
    camera = cv2.VideoCapture(0)

    while camera.isOpened():
        flag, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        corners = cv2.goodFeaturesToTrack(gray, 50, qualityLevel=0.01, minDistance=1)

        for c in corners:
            x, y = c.reshape(2)
            print(x, y)
            cv2.circle(frame, (x, y), radius=4, color=(0, 255, 120), thickness=2)

        cv2.imshow("FRAME", frame)
        if cv2.waitKey(1) == 32:
            break

    camera.release()
    cv2.destroyAllWindows()


main()
