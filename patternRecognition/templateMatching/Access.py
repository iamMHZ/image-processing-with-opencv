import pathlib
import cv2
import os


# https://docs.python.org/3/library/pathlib.html

def read_directory_files_with_pathlib_module(directory_path):
    path_obj = pathlib.Path(directory_path)

    window_name = 'window'
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

    for sub in path_obj.iterdir():
        if sub.is_dir():
            sub_dir_path = path_obj / sub
            for x in sub_dir_path.iterdir():
                if x.is_file():
                    if x.name.endswith('png') or x.name.endswith('jpg'):
                        print(str(x))
                        image = cv2.imread(str(x))
                        cv2.imshow(window_name, image)
                        if cv2.waitKey(1) == 32:
                            cv2.destroyAllWindows()
                            return


def read_directory_files_with_os_module(path):
    # os.chdir(path)
    window_name = 'window'
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

    for root, dirs, files in os.walk(path):
        for name in files:
            file_path = os.path.join(root, name)
            if file_path.endswith('png') or file_path.endswith('jpg'):
                print(file_path, end="\n\n")
                image = cv2.imread(str(file_path))
                cv2.imshow(window_name, image)
                if cv2.waitKey(1) == 32:
                    cv2.destroyAllWindows()
                    return

read_directory_files_with_os_module("D:\Programming\database of image\RoboticPatterns")

# read_directory_files_with_pathlib_module("D:\Programming\database of image\RoboticPatterns")