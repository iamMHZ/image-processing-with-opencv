import cv2
import numpy as np


# denoising techniques  are based on the documentation :
# TODO:  please read the doc: https://docs.opencv.org/trunk/d5/d69/tutorial_py_non_local_means.html


class Denoiser:

    def __init__(self, image_path):
        self.__image_path = image_path
        self.__image = cv2.imread(image_path)

    def get_image_path(self):
        return self.__image_path

    def get_image(self):
        return self.__image

    def colored_image_denoiser(self):
        frame = np.copy(self.__image)
        denoised_image = cv2.fastNlMeansDenoisingColored(frame)
        self.__show_result(denoised_image, "denoising result")

    def gray_scale_denoiser(self):
        # make a copy of original image:
        frame = np.copy(self.__image)

        height, width, channels = self.frame.shape

        #    if the image itself is not gray scale  so we must convert it:
        if channels > 1:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        denoised_image = cv2.fastNlMeansDenoising()

    def __show_result(self, image, window_name):
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        cv2.imshow(window_name, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
