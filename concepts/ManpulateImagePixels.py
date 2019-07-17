import cv2


def main():
    image_location = "D:\Programming\database of image\peppers_color.tif"
    image = cv2.imread(image_location)

    image_copy = image.copy()

    # for row in image_copy:
    #     for col in row:
    #         for x in col:
    #             if x < 150:
    #                 image_copy[row, col] = 255
    #     #         print(x)
    #     #     print("\n")
    #     # print("\n")
    #
    # cv2.imshow("Original", image)
    # cv2.imshow("Changed", image_copy)

    width, height, channels = image.shape[:]

    # for row in width:
    #     for col in height:
    #         if image[row, col] > 170:
    #             image[row, col] = 0

    # x = 0
    # y=0
    # while x <width:
    #     while y<height:
    #
    #         if image[x, y , 0] > 170:
    #             image[x, y , 0] = 0
    #         y +=1
    #     x+=1

    # image[:] = (255, 255, 255)
    cv2.imshow("Manipulated", image)
    cv2.waitKey(0)


main()
