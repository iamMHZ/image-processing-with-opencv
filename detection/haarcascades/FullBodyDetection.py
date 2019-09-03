import cv2


def main():
    # load haarcascades classifier
    upper_body_classifier = cv2.CascadeClassifier(
        "D:\Programming\opencv\sources\data\haarcascades\haarcascade_fullbody.xml")

    camera = cv2.VideoCapture(0)

    while camera.isOpened():
        check, frame = camera.read()

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        bodies = upper_body_classifier.detectMultiScale(gray_frame)

        # draw body areas:
        for x, y, w, h in bodies:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
            print(x, y, w, h)

        cv2.imshow(' Result ', frame)

        if cv2.waitKey(1) == 32:
            cv2.destroyAllWindows()
            camera.release()
            break


main()
