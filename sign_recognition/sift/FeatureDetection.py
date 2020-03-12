import os
import cv2
import numpy


# this function returns a
def load_images(path):
    image_paths = list()

    for root, dirs, files in os.walk(path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if file_path.endswith('png') or file_path.endswith('jpg'):
                image_paths.append(file_path)


def detect_features_and_descriptors(image, feature_detector):
    key_points, descriptors = feature_detector.detectAndCompute(image, None)

    return key_points, descriptors


def main():
    camera = cv2.VideoCapture(0)
    h = camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
    w = camera.get(cv2.CAP_PROP_FRAME_WIDTH)

    image = cv2.imread("peroxide.png", cv2.IMREAD_GRAYSCALE)

    image = cv2.resize(image, (int(h), int(w)))

    # this algorithm is patented :(
    # sift_obj = cv2.xfeatures2d.SIFT_create()

    # ؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟
    feature_detector = cv2.ORB.create(3000)

    test_image_kp, test_image_desc = detect_features_and_descriptors(image, feature_detector)

    # ؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟
    bf = cv2.BFMatcher()

    while True:

        _, frame = camera.read()
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        key_points, descriptors = detect_features_and_descriptors(gray_frame, feature_detector)
        # features = cv2.drawKeypoints(gray_frame, key_points, gray_frame)

        # ؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟
        matches = bf.knnMatch(test_image_desc, descriptors, k=2)
        good_points = []
        for m, n in matches:
            if m.distance < 0.6 * n.distance:
                good_points.append(m)
        img3 = cv2.drawMatches(image, test_image_kp, gray_frame, key_points, good_points, gray_frame, flags=2)

        win_name = "features"
        cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
        cv2.imshow(win_name, img3)
        if cv2.waitKey(1) == 32:
            cv2.destroyAllWindows()
            camera.release()
            break


main()
