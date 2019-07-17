import cv2
import _thread
import time


def changed_resolution():
    camera = cv2.VideoCapture(0)
    window_name = "CHANGED RESOLUTION"
    cv2.namedWindow(window_name)

    camera.set(3, 960.0)
    camera.set(4, 720.0)

    while camera.isOpened():

        flag, frame = camera.read()
        cv2.imshow(window_name, frame)

        # hit Esc key to exit:
        if cv2.waitKey(1) == 27:
            break

    camera.release()
    cv2.destroyAllWindows()


def default_resolution():
    camera = cv2.VideoCapture(0)
    window_name = " DEFAULT RESOLUTION"
    cv2.namedWindow(window_name)

    while camera.isOpened():

        flag, frame = camera.read()
        cv2.imshow(window_name, frame)

        # hit space key to exit:
        if cv2.waitKey(1) == 32:
            break

    camera.release()
    cv2.destroyAllWindows()


def main():
    try:
        default_resolution()
        changed_resolution()
        # _thread.start_new_thread(changed_resolution, ())
        # time.sleep(5)
        # _thread.start_new_thread(default_resolution, ())
        # time.sleep(5)

    except:
        print("Exception")


main()
