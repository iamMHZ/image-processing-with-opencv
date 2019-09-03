import cv2


def main():
    # load haarcascades classifiers
    face_classifier = cv2.CascadeClassifier(
        "D:\Programming\opencv\sources\data\haarcascades\haarcascade_frontalface_alt2.xml")
    smile_classifier = cv2.CascadeClassifier(
        "D:\Programming\opencv\sources\data\haarcascades\haarcascade_smile.xml")

    camera = cv2.VideoCapture(0)

    while camera.isOpened():
        check, frame = camera.read()

        height, width, channels = frame.shape

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # optimization and noise removal
        gray_frame = cv2.equalizeHist(gray_frame)
        faces = face_classifier.detectMultiScale(gray_frame)

        for face in faces:
            x, y, w, h = face.reshape(4)

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            face_area = gray_frame[y: y + h, x:x + w].copy()
            smiles = smile_classifier.detectMultiScale(face_area, 1.8)

            for sx, sy, sw, sh in smiles:
                # cv2.rectangle(frame, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 2)
                cv2.putText(frame, " *** SMILE *** ", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255))

        cv2.imshow(' Result ', frame)

        if cv2.waitKey(1) == 32:
            cv2.destroyAllWindows()
            camera.release()
            break


main()
