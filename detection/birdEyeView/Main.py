import cv2


def show_image(frame):
    window_name = "frame"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.imshow(window_name, frame)
    cv2.waitKey()


def find_coordinate_points(image):
    frame = image.copy()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(frame, 70, 255, cv2.THRESH_BINARY)

    contours, hierachy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    # print(contours)
    cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

    # approx = cv2.approxPolyDP(contours[1] , 0.001,True)
    # rc = cv2.minAreaRect(contours[1])
    # box = cv2.boxPoints(rc)
    # print(box)

    show_image(image)


def main():
    image = cv2.imread('QR.jpg')

    find_coordinate_points(image)


main()
