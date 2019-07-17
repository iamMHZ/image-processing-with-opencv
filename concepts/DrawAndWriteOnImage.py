import cv2


def main():
    imageLocation = "D:\Programming\database of image\lake.tif"

    windowName = "Drawing"
    # creating a window for showing the image
    cv2.namedWindow(windowName, cv2.WINDOW_FREERATIO)
    # read the image:
    image = cv2.imread(imageLocation)

    # drawing shapes:

    cv2.line(image, (0, 20), (300, 300), (0, 255, 100), 5)
    cv2.circle(image, (300, 100), 90, (255, 0, 20), -1)
    cv2.circle(image, (135, 120), 50, (0, 0, 120), 6)
    cv2.rectangle(image, (50, 150), (100, 250), (0, 0, 220), 5)

    # putting texts:
    text = "I AM 'MHZ'"
    cv2.putText(image, text, (20, 420), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 100, 255), 5)

    # showing image
    cv2.imshow(windowName, image)
    # write the the image to the disk:
    cv2.imwrite("C:\\Users\hMd\\Desktop\\result.jpg", image)
    cv2.waitKey(0)


main()
