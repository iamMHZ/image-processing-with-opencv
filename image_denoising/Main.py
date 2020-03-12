import numpy as np
from Denoiser import *

image_path = "D:\Programming\database of image\QR\\(1).jpg"
denoiser = Denoiser(image_path)

# denoiser.colored_image_denoiser()

# denoiser.gray_scale_denoiser()

# denoiser.gray_scale_denoiser()
# denoiser.apply_blur_filter(7 )

# denoiser.apply_box_filter(-1,21)
# denoiser.apply_dilate(kernel_size=7 , number_of_iterations=3)

# denoiser.apply_erode(kernel_size=5, number_of_iterations=2

# denoiser.apply_binary_threshold(min_value=170, max_value=255)

# kernel = np.array([[1, 1, 1], [1, -10, 1], [1, 1, 1]], dtype=np.uint8)
# denoiser.apply_filter_2d(-1,kernel)

# denoiser.apply_gaussian_blur(17, 0, 0)

# denoiser.apply_median_blur(7)

# denoiser.apply_closing_morphological_transform(17,20)

# denoiser.apply_opening_morphological_transform(17, 20)

# denoiser.apply_gradient_morphological_transform(17,20)

# denoiser.apply_top_hat_morphological_transform(17, 20)


# denoiser.apply_black_hat_morphological_transform(17, 20)

# denoiser.apply_laplacian(-1, None)

denoiser.apply_blur_and_downsampling()