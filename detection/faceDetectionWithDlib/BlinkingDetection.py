import cv2
import dlib


def main():
    cap = cv2.VideoCapture(0)

    face_detector = dlib.get_frontal_face_detector()
    landmark_predictor = dlib.shape_predictor()

    while cap.isOpened():
        _, frame = cap.read()

        cv2.imshow("original", frame)

        key = cv2.waitKey(1)
        if key == 32:
            cv2.destroyAllWindows()
            cap.release()
            break


main()
