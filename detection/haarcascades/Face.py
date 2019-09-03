import cv2


def swap_faces(frame, faces):
    if len(faces) >= 2:
        x0, y0, w0, h0 = faces[0].reshape(4)
        x1, y1, w1, h1 = faces[1].reshape(4)

        frame_copy = frame.copy()

        # temp = frame[y0:y0 + h0, x0:x0 + w0]

        frame[y0:y0 + h0, x0:x0 + w0] = cv2.resize(frame[y1:y1 + h1, x1:x1 + w1], (w0, h0),
                                                   interpolation=cv2.INTER_LINEAR)
        frame[y1:y1 + h1, x1:x1 + w1] = cv2.resize(frame_copy[y0:y0 + h0, x0:x0 + w0], (w1, h1),
                                                   interpolation=cv2.INTER_LINEAR)

    return frame


def main():
    face_cascade = cv2.CascadeClassifier(
        "D:\Programming\opencv\sources\data\haarcascades\haarcascade_frontalface_alt2.xml")
    eye_cascade = cv2.CascadeClassifier("D:\Programming\opencv\sources\data\haarcascades\haarcascade_eye.xml")

    camera = cv2.VideoCapture(0)

    # number of all faces in video
    face_counter = 0
    while camera.isOpened():

        check, frame = camera.read()

        # faces = cascade.detectMultiScale(frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # optimization and noise removal
        gray = cv2.equalizeHist(gray)
        # cv2.imshow("gray" , gray)
        faces = face_cascade.detectMultiScale(gray)

        # number of face in each frame
        face_number = len(faces)

        for face in faces:
            x, y, w, h = face.reshape(4)

            # drawing and writing on faces
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, 'face ' + str(face_number), (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))

            # putting the face in the right corner of the frame:
            frame[0:h, 0: w] = frame[y: y + h, x:x + w].copy()

            print(x, y, w, h)

            cv2.imwrite("C:\\Users\hMd\Desktop\\new\\face" + str(face_counter) + ".jpg", frame[y:y + h, x:x + w])

            face_number -= 1
            face_counter += 1

            # swapping faces
            # frame = swap_faces(frame, faces)

        # eye detextion
        eyes = eye_cascade.detectMultiScale(gray)
        for x, y, w, h in eyes:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 150), 1)

        cv2.imshow("face", frame)

        if cv2.waitKey(1) == 32:
            break

    camera.release()
    cv2.destroyAllWindows()


main()
