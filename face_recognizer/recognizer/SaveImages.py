import cv2
import os


def capture_and_save(folder_path, dir_name):
    os.chdir(folder_path)

    save_path = os.path.join(folder_path, dir_name)
    # checking if the directory was not created before then create the directory;
    if not os.path.isdir(save_path):
        os.mkdir(save_path)

    camera = cv2.VideoCapture(0)
    number = 0
    while True:
        _, frame = camera.read()

        cv2.imshow("show", frame)

        key = cv2.waitKey(1)
        if key == 32:
            cv2.destroyAllWindows()
            camera.release()
            break
        elif key == ord('s'):
            cv2.imwrite(os.path.join(save_path, str(number) + ".jpg"), frame)
            number += 1


dir_name = str(input("ENTER THE PERSON NAME:  "))
folder_path = "D:\\Programming\\database of image\\ImageDataSet\\people"

capture_and_save(folder_path, dir_name)
