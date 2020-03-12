import cv2
import pickle


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

    # loading recognizer and dictionary of labels
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer.yml')

    labels = {}
    with open('labels.pickle', 'rb') as file:
        original_labels = pickle.load(file)
        labels = {v: k for k, v in original_labels.items()}
    # reversing the dictionary to have access to names with id

    camera = cv2.VideoCapture(0)

    print(labels)

    while camera.isOpened():

        check, frame = camera.read()

        # faces = cascade.detectMultiScale(frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)
        # cv2.imshow("gray" , gray)
        faces = face_cascade.detectMultiScale(gray)

        for face in faces:
            x, y, w, h = face.reshape(4)
            face_region = gray[y:y + h, x:x + w]
            # drawing and writing on faces
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # cv2.putText(frame, 'face ' + str(face_number), (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))

            # print(x, y, w, h)

            # lets recognize the face:
            face_id, confident = recognizer.predict(face_region)
            if confident >= 45:
                person_name = labels[face_id]
                cv2.putText(frame, person_name, (x + 5, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))
                print(person_name, confident)

            # print(face_id, confident)

            cv2.imshow("face", frame)

        if cv2.waitKey(1) == 32:
            break

    camera.release()
    cv2.destroyAllWindows()


main()
