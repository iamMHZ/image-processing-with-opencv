import cv2
import dlib
import logging
import numpy as np

face_detector = dlib.get_frontal_face_detector()
landmarks_predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")


def draw_all_landmarks(frame, gray_frame, face):
    landmarks = landmarks_predictor(gray_frame, face)
    for i in range(0, 68):
        x = landmarks.part(i).x
        y = landmarks.part(i).y
        cv2.circle(frame, (x, y), 5, (150, 250, 80), -1)
        # logging.info("landmark : " + str(i) + "location :  " + str(x) + "," + str(y))


def detect_blinking(original_frame, gray_frame, face):
    landmarks = landmarks_predictor(gray_frame, face)

    landmark36 = landmarks.part(36).x, landmarks.part(36).y
    landmark39 = landmarks.part(39).x, landmarks.part(36).y

    cv2.line(original_frame, landmark36, landmark39, (0, 0, 255))


def draw_face_rectangle(frame, face):
    x1 = face.left()
    y1 = face.top()
    x2 = face.right()
    y2 = face.bottom()
    cv2.rectangle(frame, (x1, y1), (x2, y2), (100, 200, 0), 2)


def main():
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        _, frame = cap.read()

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_detector(gray_frame)

        for face in faces:
            # print(face)
            # draw_face_rectangle(frame, face)

            # draw_all_landmarks(frame, gray_frame, face)
            detect_blinking(frame, gray_frame, face)

        cv2.imshow("original", frame)
        key = cv2.waitKey(1)
        if key == 32:
            cv2.destroyAllWindows()
            cap.release()
            break


if __name__ == "__main__":
    main()
