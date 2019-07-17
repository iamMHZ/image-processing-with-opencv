import cv2


def main():
    win_name = "LIVE VIDEO"
    cv2.namedWindow(win_name)

    camera = cv2.VideoCapture(0)
    

    while camera.isOpened():
        # read a frame from camera:
        flag, frame = camera.read()
        # color conversion:
        img = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
        # show the image:
        cv2.imshow(win_name, img)
        # if Esc key is pressed :
        if cv2.waitKey(1) == 27:
            camera.release()
            cv2.destroyAllWindows()
            break


main()
