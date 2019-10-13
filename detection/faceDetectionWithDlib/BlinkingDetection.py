import cv2
import dlib
from math import hypot
import pyttsx3
import threading
import time

face_detector = dlib.get_frontal_face_detector()
landmarks_predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
speechEngine = pyttsx3.init()


def draw_all_landmarks(frame, gray_frame, face):
    landmarks = landmarks_predictor(gray_frame, face)
    for i in range(0, 68):
        x = landmarks.part(i).x
        y = landmarks.part(i).y
        cv2.circle(frame, (x, y), 5, (150, 250, 80), -1)
        # logging.info("landmark : " + str(i) + "location :  " + str(x) + "," + str(y))


def draw_line(frame, point1, point2):
    color = (0, 0, 255)
    cv2.line(frame, point1, point2, color, 1)


def check_blinking(original_frame, face, right_ratio, left_ratio):
    if left_ratio > 4.42 and right_ratio > 4.42:
        draw_face_rectangle(original_frame, face)
        cv2.putText(original_frame, "*** BLINKING ***", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255),3)
        # say("Blinking")


def get_middle(point1, point2):
    middle_point = int((point1[0] + point2[0]) / 2), int((point1[1] + point2[1]) / 2)
    return middle_point


def landmark_to_point(landmarks, landmark_number):
    point = landmarks.part(landmark_number).x, landmarks.part(landmark_number).y

    return point


def get_line_length(point1, point2):
    length = hypot((point1[0] - point2[0]), (point1[1] - point2[1]))

    return length


def detect_blinking(original_frame, gray_frame, face):
    landmarks = landmarks_predictor(gray_frame, face)

    # left_eye :
    # horizontal line:
    point36 = landmark_to_point(landmarks, 36)
    point39 = landmark_to_point(landmarks, 39)

    draw_line(original_frame, point36, point39)
    # vertical line:
    point37 = landmark_to_point(landmarks, 37)
    point38 = landmark_to_point(landmarks, 38)

    point40 = landmark_to_point(landmarks, 40)
    point41 = landmark_to_point(landmarks, 41)

    left_up_middle = get_middle(point37, point38)
    left_down_middle = get_middle(point40, point41)

    draw_line(original_frame, left_up_middle, left_down_middle)

    # right eye :
    # horizontal line:
    point42 = landmark_to_point(landmarks, 42)
    point45 = landmark_to_point(landmarks, 45)

    draw_line(original_frame, point42, point45)
    # vertical line:
    point43 = landmark_to_point(landmarks, 43)
    point44 = landmark_to_point(landmarks, 44)

    point46 = landmark_to_point(landmarks, 46)
    point47 = landmark_to_point(landmarks, 47)

    right_up_middle = get_middle(point43, point44)
    right_down_middle = get_middle(point46, point47)

    draw_line(original_frame, right_up_middle, right_down_middle)

    # blinking detection :
    left_eye_horizontal_line_length = get_line_length(point36, point39)
    left_eye_vertical_line_length = get_line_length(left_up_middle, left_down_middle)

    right_eye_horizontal_line_length = get_line_length(point42, point45)
    right_eye_vertical_line_length = get_line_length(right_up_middle, right_down_middle)

    right_ratio = right_eye_horizontal_line_length / right_eye_vertical_line_length
    left_ratio = left_eye_horizontal_line_length / left_eye_vertical_line_length

    print("right :   " + str(right_ratio))
    print("left :   " + str(left_ratio) + "\n\n")

    check_blinking(original_frame, face, right_ratio, left_ratio)


def say(word):
    threading.Thread(target=lambda a: (speechEngine.say(word),
                                       speechEngine.runAndWait()), args=(word,)).start()


def draw_face_rectangle(frame, face):
    x1 = face.left()
    y1 = face.top()
    x2 = face.right()
    y2 = face.bottom()
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)


def main():
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)

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
