import cv2


def main():
    eye_cascade = cv2.CascadeClassifier(
        "D:\Programming\opencv\sources\data\haarcascades\haarcascade_eye_tree_eyeglasses.xml")

    camera = cv2.VideoCapture(0)

    # number of all faces in video
    while camera.isOpened():

        check, frame = camera.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)

        # eye detextion
        eyes = eye_cascade.detectMultiScale(gray)
        for x, y, w, h in eyes:
            eye = frame[y:y + h, x:x + w]
            eye_gray = cv2.cvtColor(eye, cv2.COLOR_BGR2GRAY)
            eye_gray = cv2.GaussianBlur(eye_gray, (5, 5), 0)
            flag, eye_thresh = cv2.threshold(eye_gray, 50, 250, cv2.THRESH_BINARY_INV)

            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
            # eye_thresh = cv2.dilate(eye_thresh, kernel)

            contoures, hierachy = cv2.findContours(eye_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            cv2.drawContours(eye, contoures, -1, (0, 255, 0))

            cv2.imshow("eye", eye_thresh)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 150), 1)

        cv2.imshow("face", frame)

        if cv2.waitKey(1) == 32:
            break

    camera.release()
    cv2.destroyAllWindows()


main()
