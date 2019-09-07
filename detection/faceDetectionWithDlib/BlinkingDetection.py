import cv2
import dlib
from math import hypot
import pyttsx3
import threading
import time

face_detector = dlib.get_frontal_face_detector()
landmarks_predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
speackEngine = pyttsx3.init()


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
    if left_ratio > 4.4 and right_ratio > 4.4:
        draw_face_rectangle(original_frame, face)
        cv2.putText(original_frame, "** BLINKING ***", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))
        say("Blinking")


def detect_blinking(original_frame, gray_frame, face):
    landmarks = landmarks_predictor(gray_frame, face)

    # left_eye :
    # horizontal line:
    landmark36 = landmarks.part(36).x, landmarks.part(36).y
    landmark39 = landmarks.part(39).x, landmarks.part(39).y

    draw_line(original_frame, landmark36, landmark39)
    # vertical line:
    landmark37 = landmarks.part(37).x, landmarks.part(37).y
    landmark38 = landmarks.part(38).x, landmarks.part(38).y

    landmark40 = landmarks.part(40).x, landmarks.part(40).y
    landmark41 = landmarks.part(41).x, landmarks.part(41).y

    left_up_middle = get_middle(landmark37, landmark38)
    left_down_middle = get_middle(landmark40, landmark41)

    draw_line(original_frame, left_up_middle, left_down_middle)

    # right eye :
    # horizontal line:
    landmark42 = landmarks.part(42).x, landmarks.part(42).y
    landmark45 = landmarks.part(45).x, landmarks.part(45).y

    draw_line(original_frame, landmark42, landmark45)
    # vertical line:
    landmark43 = landmarks.part(43).x, landmarks.part(43).y
    landmark44 = landmarks.part(44).x, landmarks.part(44).y

    landmark46 = landmarks.part(46).x, landmarks.part(46).y
    landmark47 = landmarks.part(47).x, landmarks.part(47).y

    right_up_middle = get_middle(landmark43, landmark44)
    right_down_middle = get_middle(landmark46, landmark47)

    draw_line(original_frame, right_up_middle, right_down_middle)

    # blinking detection :
    left_eye_horizental_line_length = hypot((landmark36[0] - landmark39[0]), (landmark36[1] - landmark39[1]))
    left_eye_vertical_line_length = hypot((left_up_middle[0] - left_down_middle[0]),
                                          (left_up_middle[1] - left_down_middle[1]))

    right_eye_horizental_line_length = hypot((landmark42[0] - landmark45[0]), (landmark42[1] - landmark45[1]))
    right_eye_vertical_line_length = hypot((right_up_middle[0] - right_down_middle[0]),
                                           (right_up_middle[1] - right_down_middle[1]))

    right_ratio = right_eye_horizental_line_length / right_eye_vertical_line_length
    left_ratio = left_eye_horizental_line_length / left_eye_vertical_line_length

    print("right :   " + str(right_ratio))
    print("left :   " + str(left_ratio))

    check_blinking(original_frame, face, right_ratio, left_ratio)


def get_middle(point1, point2):
    middle_point = int((point1[0] + point2[0]) / 2), int((point1[1] + point2[1]) / 2)
    return middle_point


def say(word):
    threading.Thread(target=lambda a: (speackEngine.say(word),
                                       speackEngine.runAndWait()), args=(word,)).start()


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
