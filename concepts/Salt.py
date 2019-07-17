import cv2
import random


def main():
    original = cv2.imread("D:\Programming\database of image\misc\\4.1.08.tiff")
    noisy = original.copy()

    rows, columns, channels = noisy.shape

    for i in range(rows):
        for j in range(columns):
            array = noisy[i][j]
            rand = random.randrange(0, 160)

            if rand > 120:
                noisy[i][j] = [0, 0, 0]
            elif rand > 100:
                noisy[i][j] = [255, 255, 255]

    denoised = cv2.medianBlur(noisy, 5)


    cv2.imshow("ORIGINAL", original)
    cv2.imshow("NOISY", noisy)
    cv2.imshow("DENOISED", denoised)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


main()
