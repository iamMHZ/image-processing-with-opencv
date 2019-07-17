import cv2


def main():
    camera = cv2.VideoCapture(0)

    while camera.isOpened():
        _, frame = camera.read()

        # output = cv2.kmeans(frame , 3 , )
        cv2.imshow("frame ", frame)
        if (cv2.waitKey(1) == 32):
            break

    camera.release()
    cv2.destroyAllWindows()


main()
