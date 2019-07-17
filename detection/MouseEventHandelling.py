import cv2

imageeLocation = "D:\Programming\database of image\sheep.jpg"
image = cv2.imread(imageeLocation)

win_name = "event handlig"
cv2.namedWindow(win_name, cv2.WINDOW_FREERATIO)


def event_handler(event, x, y, flag, param):
    # if event == cv2.EVENT_L:
    #     cv2.circle(image, (x, y), 100, (0, 90, 255), -1)
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.rectangle(image, (x, y), (x + 150, y + 195), (0, 250, 155), -1)
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.putText(image, "MHZ", (x, y), cv2.FONT_HERSHEY_COMPLEX, 5, (0, 100, 255), 5)


# event handling on the window we just created:
cv2.setMouseCallback(win_name, event_handler)


def main():
    while True:
        cv2.imshow(win_name, image)
        if (cv2.waitKey(1) == 27):
            break


main()
