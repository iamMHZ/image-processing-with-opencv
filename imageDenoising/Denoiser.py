import cv2
import numpy as np

"""
    created by MHZ 
"""


# denoising techniques  are based on the documentation :
# TODO :  please read the following  docs: https://docs.opencv.org/trunk/d5/d69/tutorial_py_non_local_means.html
# TODO :  https://docs.opencv.org/3.0-beta/modules/imgproc/doc/filtering.html
# TODO : add methods for denoising Video streams use methods like : cv2.fastNlMeansDenoisingMulti()

class Denoiser:

    def __init__(self, image_path):
        self.__image_path = image_path
        self.__image = cv2.imread(image_path)

    def get_image_path(self):
        return self.__image_path

    def get_image(self):
        return self.__image

    def set_image_path(self, new_path):
        self.__image_path = new_path
        self.__image = cv2.imread(self.__image_path)

    def colored_image_denoiser(self):
        frame = np.copy(self.__image)
        denoised_image = cv2.fastNlMeansDenoisingColored(frame)
        self.__show_result(denoised_image, "denoising result")

    def gray_scale_denoiser(self):
        # make a copy of original image:
        frame = np.copy(self.__image)

        height, width, channels = frame.shape

        #    if the image itself is not gray scale  so we must convert it:
        if channels > 1:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        denoised_image = cv2.fastNlMeansDenoising(frame)

        self.__show_result(denoised_image, "denoising gray scale image")

    def __show_result(self, image, window_name):
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        cv2.imshow(window_name, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # TODO: instead of just having kernel_size variable  you can have kernel_width and kernel_height
    # functions input kernel size must be an odd number
    def apply_blur_filter(self, kernel_size):
        blurred_image = cv2.blur(self.__image, (kernel_size, kernel_size))
        self.__show_result(blurred_image, 'blurred')

    def apply_box_filter(self, ddepth, kernel_size):
        """
        :param ddepth: Desired depth of the destination image.
        """

        box_filtered_image = cv2.boxFilter(self.__image, ddepth, (kernel_size, kernel_size))
        self.__show_result(box_filtered_image, "box filter")

    def apply_dilate(self, kernel_size, number_of_iterations):
        # create a rectangular kernel
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
        dilated_image = cv2.dilate(self.__image, kernel=kernel, iterations=number_of_iterations)

        self.__show_result(dilated_image, "apply_dilation")

    def apply_erode(self, kernel_size, number_of_iterations):
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
        eroded_image = cv2.erode(self.__image, kernel, iterations=number_of_iterations)
        self.__show_result(eroded_image, "erode")

    def apply_binary_threshold(self, min_value, max_value):
        gray = cv2.cvtColor(self.__image, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, min_value, max_value, cv2.THRESH_BINARY)
        self.__show_result(thresh, "binary threshold")

    def apply_binary_invert_threshold(self, min_value, max_value):
        gray = cv2.cvtColor(self.__image, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, min_value, max_value, cv2.THRESH_BINARY_INV)
        self.__show_result(thresh, "binary invert threshold")

    def apply_filter_2d(self, ddepth, kernel):
        filtered_image = cv2.filter2D(self.__image, ddepth, kernel)
        self.__show_result(filtered_image, "custom filter")

    def apply_gaussian_blur(self, kernel_size, sigma_x, sigma_y):
        """
        :param sigma_x: Gaussian kernel standard deviation in X direction.
        :param sigma_y: Gaussian kernel standard deviation in Y direction; if sigmaY is zero,
                        it is set to be equal to sigmaX,
                        if both sigmas are zeros, they are computed from kernel_size.width and kernel_size.height , respectively
        """
        gaussian_filter = cv2.GaussianBlur(self.__image, (kernel_size, kernel_size), sigmaX=sigma_x, sigmaY=sigma_y)
        self.__show_result(gaussian_filter, "Gaussian_filter")

    def apply_median_blur(self, kernel_size):
        median_blur = cv2.medianBlur(self.__image, kernel_size)
        self.__show_result(median_blur, "median blur")

    def apply_closing_morphological_transform(self, kernel_size, number_of_iterations):
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
        closing = cv2.morphologyEx(self.__image, cv2.MORPH_CLOSE, kernel, iterations=number_of_iterations)
        self.__show_result(closing, "closing")

    def apply_opening_morphological_transform(self, kernel_size, number_of_iterations):
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
        closing = cv2.morphologyEx(self.__image, cv2.MORPH_OPEN, kernel, iterations=number_of_iterations)
        self.__show_result(closing, "opening")

    def apply_gradient_morphological_transform(self, kernel_size, number_of_iterations):
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
        closing = cv2.morphologyEx(self.__image, cv2.MORPH_GRADIENT, kernel, iterations=number_of_iterations)
        self.__show_result(closing, "gradient")

    def apply_black_hat_morphological_transform(self, kernel_size, number_of_iterations):
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
        closing = cv2.morphologyEx(self.__image, cv2.MORPH_BLACKHAT, kernel, iterations=number_of_iterations)
        self.__show_result(closing, "black hat")

    def apply_top_hat_morphological_transform(self, kernel_size, number_of_iterations):
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
        closing = cv2.morphologyEx(self.__image, cv2.MORPH_TOPHAT, kernel, iterations=number_of_iterations)
        self.__show_result(closing, "top hat")

    def apply_laplacian(self, ddepth, kernel_size):
        laplacian = cv2.Laplacian(self.__image, ddepth, kernel_size)
        self.__show_result(laplacian, "laplacian")

    # Blurs an image and downsamples it:
    # video about downsampleing : https://www.youtube.com/watch?v=emuKA3tBDBw
    # https://docs.opencv.org/3.1.0/dc/dff/tutorial_py_pyramids.html
    def apply_blur_and_downsampling(self):
        result = cv2.pyrDown(self.__image)
        self.__show_result(result, "blur and downsample")

    # Upsamples an image and then blurs it:
    def apply_blur_and_downsampling(self):
        result = cv2.pyrUp(self.__image)
        self.__show_result(result, "blur and downsample")
