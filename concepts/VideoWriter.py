import cv2
import numpy as np


def main():
    path = "C:\\Users\hMd\Desktop\\output.mp4"  # .avi is better : no error
    codec = cv2.VideoWriter.fourcc("X", "V", "I", "D")
    frame_rate = 30
    resolution = (640, 480)

    video_writer_into_disk = cv2.VideoWriter(path, codec, frame_rate, resolution)

    camera = cv2.VideoCapture(0)
    while True:
        flag, frame = camera.read()

        video_writer_into_disk.write(frame)

        cv2.imshow("LIVE", frame)
        if cv2.waitKey(1) == 32:
            break

    camera.release()
    cv2.destroyAllWindows()
    video_writer_into_disk.release()


main()
