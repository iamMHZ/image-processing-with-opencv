import cv2
import os

from patternRecognition.hazmatDetection.Hazmat import Hazmat


class HazmatDetector:

    def __init__(self):
        self.__hazmat_list = list()

    def add_to_list(self, hazmat):
        self.__hazmat_list.append(hazmat)

    def get_hazmat_list(self):
        return self.__hazmat_list

    def calculate_features(self, original_image):

        changed_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

        feature_detector = cv2.ORB.create(30000)
        key_points, descriptors = feature_detector.detectAndCompute(changed_image, None)

        return key_points, descriptors, changed_image

    # prepossessing task
    def read_templates(self, path):
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                file_name = os.path.basename(file_path)
                # checking for image
                if file_name.endswith('.png') or file_name.endswith('.jpg'):
                    # print(file_name)

                    # now lets calculate features and descriptors:
                    image = cv2.imread(file_path)
                    # self.__show_image('image', image)

                    key_points, descriptors, changed_image = self.calculate_features(image)
                    # create hazmat and add it to the list;
                    hazmat = Hazmat(file_name, file_path, changed_image, key_points, descriptors)
                    self.__hazmat_list.append(hazmat)

        # draw features
        # for haz in self.__hazmat_list:
        #     features = cv2.drawKeypoints(haz.image, hazmat.key_points, hazmat.image)
        #     self.__show_image('features', features)

    def __show_image(self, window_name, image):
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        cv2.imshow(window_name, image)
        # key = cv2.waitKey(1000)
        key = cv2.waitKey(1)

    #
    def start_live_hazmat_detection(self, camera_id):

        camera = cv2.VideoCapture(camera_id)

        # TODO implement it with cv2.FlannBasedMatcher
        bf_matcher = cv2.BFMatcher(normType=cv2.NORM_HAMMING)

        while True:
            _, frame = camera.read()
            # frame = cv2.flip(frame, 1)

            # draw a rectangle for region of interest:
            height, width, channels = frame.shape
            w = 150
            h = 200
            x = int((width / 2) - (w / 2))
            y = int((height / 2) - (h / 2))
            color = (0, 255, 0)
            thickness = 2
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, thickness)
            # extract the region of interest
            roi = frame[y + thickness:y + h - thickness, x + thickness:x + w - thickness]
            # self.__show_image('roi', frame)
            # self.__show_image('roi', roi)

            # check matches:
            frame_key_points, frame_descriptors, changed_frame = self.calculate_features(roi)

            # checking with all other hazmat templates that we have in our list:
            founded_name = ""  # a name that will be written on the frame as name of the hazmat that was detected
            for hazmat in self.__hazmat_list:
                hazmat_name = hazmat.name
                hazmat_key_points = hazmat.key_points
                hazmat_descriptors = hazmat.descriptors
                hazmate_image = hazmat.image

                matches = bf_matcher.knnMatch(hazmat_descriptors, frame_descriptors, k=2)

                # finding good matches:
                good_points = []
                for m, n in matches:
                    if m.distance < 0.6 * n.distance:
                        good_points.append(m)

                # condition to demonstrate the minimum matches needed for detection to be true:
                if len(good_points) > 5:
                    founded_name = hazmat_name
                    cv2.putText(frame, founded_name, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

                img = cv2.drawMatches(hazmate_image, hazmat_key_points, changed_frame, frame_key_points, good_points,
                                      changed_frame, flags=2)
                self.__show_image('matches', img)

                key = cv2.waitKey(1)
                if key == 32:
                    camera.release()
                    cv2.destroyAllWindows()
                    return
            self.__show_image('result', frame)
