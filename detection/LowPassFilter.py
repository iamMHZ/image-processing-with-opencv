import cv2


def main():
    camera = cv2.VideoCapture(0)

    while True:
        flag, frame = camera.read()

        #  -1 us the depth and (10,10) is kernel size
        box_filter = cv2.boxFilter(frame, -1, (10, 10))
        blur_filter = cv2.blur(frame, (5, 5))
        gaussian_filter = cv2.GaussianBlur(frame, (13, 13), 0)

        cv2.imshow("Original", frame)
        cv2.imshow("box filter", box_filter)
        cv2.imshow("blur filter", blur_filter)
        cv2.imshow("Gaussian blur filter", gaussian_filter)

        if (cv2.waitKey(1) == 32):
            break

    cv2.destroyAllWindows()
    camera.release()

    kernel = cv2.getGaussianKernel(40, 0)
    print(kernel)


print()

main()
