import cv2


def on_mouse_clicked(event, x, y, flags, params):
    if event == cv2.EVENT_RBUTTONDOWN:
        # cv2.putText(params, 'mhz', (x, y), cv2.FONT_HERSHEY_COMPLEX, 16, (0, 100, 255), 55)
        print('MOUSE CLICKED')


def main():
    window_name = 'window'
    cv2.namedWindow(window_name)
    cv2.setMouseCallback(window_name, on_mouse_clicked)

    camera = cv2.VideoCapture(0)

    while camera.isOpened():
        _, frame = camera.read()

        cv2.imshow(window_name, frame)

        if cv2.waitKey(1) == 32:
            break

    camera.release()
    cv2.destroyAllWindows()


main()
