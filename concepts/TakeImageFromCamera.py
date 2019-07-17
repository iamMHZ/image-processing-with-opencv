import cv2
import matplotlib.pyplot as plt


def main():
    # create an object of VideoCapture class an open the webCam
    camera = cv2.VideoCapture(0)

    if camera.isOpened():
        # Capture a frame
        # read function has multiple returns
        flag, frame = camera.read()

        # convert it to format that we wanted:
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # write the image on disk:
        cv2.imwrite("C:\\Users\hMd\Desktop\\output.jpg" , frame)

        # show it
        cv2.imshow('WEBCAM', frame)
        camera.release()
        cv2.waitKey(0)

    else:
        print("CANNOT OPEN THE WEBCAM")


main()
