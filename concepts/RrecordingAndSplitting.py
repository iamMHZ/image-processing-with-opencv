import cv2
import numpy as np


def main():
    path = "C:\\Users\hMd\Desktop\\output.avi"  # .avi is better : no error
    codec = cv2.VideoWriter.fourcc("X", "V", "I", "D")
    frame_rate = 30
    resolution = (640, 480)

    camera = cv2.VideoCapture(0)
    while True:
        flag, frame = camera.read()

        # get height and length of frame
        height = len(frame)
        width = len(frame[0])
        video_writer_into_disk = cv2.VideoWriter(path, codec, frame_rate, (2 * width, 2 * height))

        zeros = np.zeros((height, width), dtype="uint8")

        (B, G, R) = cv2.split(frame)
        R = cv2.merge([zeros, zeros, R])
        G = cv2.merge([zeros, G, zeros])
        B = cv2.merge([B, zeros, zeros])

        output = np.zeros((height * 2, width * 2, 3), np.uint8)
        output[0:height, 0:width] = frame
        output[0:height, width:width * 2] = R
        output[height:height * 2, width:width * 2] = G
        output[height:height * 2, 0:width] = B

        video_writer_into_disk.write(output)
        cv2.imshow("Output", output)
        cv2.imshow("LIVE", frame)

        if cv2.waitKey(1) == 32:
            break

    video_writer_into_disk.release()
    camera.release()
    cv2.destroyAllWindows()


main()
