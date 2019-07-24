import cv2


def main():
    image = cv2.imread("D:\Programming\database of image\circle.jpg")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # remove unwanted noises
    gray = cv2.GaussianBlur(gray, (7, 7), 0)
    _, thresh = cv2.threshold(gray, 150, 250, cv2.THRESH_BINARY)

    contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image, contours, -1, (255, 0, 0), 3)

    perimeter = cv2.arcLength(contours[1], True)
    area = cv2.contourArea(contours[1])
    print("Number of contours: ", len(contours))
    print("Perimeter", perimeter)
    print("Area: ", area)

    window_name = "imageWindow"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.imshow(window_name, image)

    cv2.waitKey()


main()
