import cv2
import matplotlib.pyplot as plt


def calculate_histogram(camera_code):
    camera = cv2.VideoCapture(camera_code)

    while camera.isOpened():
        ret, frame = camera.read()
        frame = cv2.flip(frame, 1)

        line_location = (30, 40)
        font_scale = 0.6
        cv2.putText(frame, " Place your object the rectangle area and PRESS 'm' ", line_location,
                    cv2.FONT_HERSHEY_DUPLEX, font_scale, (0, 50, 255))

        x, y, w, h = 50, 200, 150, 380
        thickness = 2
        cv2.rectangle(frame, (x, y), (w, h), (0, 255, 0), thickness)

        region_of_interest = frame[y + thickness:h - thickness, x + thickness:w - thickness]

        cv2.imshow("frame", frame)
        cv2.imshow("roi", region_of_interest)

        key = cv2.waitKey(30)
        if key == 32 or key == ord('m'):
            break

    cv2.destroyAllWindows()
    camera.release()

    # easier and better to convert it to hsv and then calculate the histogram for it
    hsv = cv2.cvtColor(region_of_interest, cv2.COLOR_BGR2HSV)
    histogram = cv2.calcHist([hsv], [0, 1], None, [12, 15], [0, 180, 0, 256])

    plt.subplot(1, 2, 1)
    plt.plot(histogram)
    plt.title('non normalized')

    cv2.normalize(histogram, histogram, 0, 255, cv2.NORM_MINMAX)

    plt.subplot(1, 2, 2)
    plt.plot(histogram)
    plt.title('normalized')

    plt.show()

    return histogram


def apply_back_projection(frame, histogram):
    # we calculated the histogram in hsv color space so now we apply back projection
    # on hsv frame

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    back_projection = cv2.calcBackProject([hsv], [0, 1], histogram, [0, 180, 0, 256], 1)

    _, thresh = cv2.threshold(back_projection, 70, 255, cv2.THRESH_BINARY)

    # noise removal :
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15))
    filtered_image = cv2.filter2D(thresh, -1, kernel)

    # instead of defining a kernel we will use the default kernel
    # the default kernel is 3*3 matrix
    kernel = None
    eroded = cv2.erode(filtered_image, kernel, iterations=2)
    dilated = cv2.dilate(eroded, kernel, iterations=2)
    closing = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel)

    mask = cv2.bitwise_and(frame, frame, mask=closing)
    # cv2.imshow("masked", mask)
    return closing, mask, thresh


def detect_object(frame, histogram):
    object_area, mask, threshold = apply_back_projection(frame, histogram)

    contours, hierachy = cv2.findContours(object_area, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame, contours, -1, (0, 255, 0))

    # finding the largest contour in image:
    max_area = 0
    cnt = None
    index = 0

    for (i, c) in enumerate(contours):
        area = cv2.contourArea(c)
        if area > max_area:
            max_area = area
            cnt = contours[i]
            index = i

    if cnt is not None:
        cv2.drawContours(frame, contours, index, (0, 255, 0))
        return True
    else:
        return False
