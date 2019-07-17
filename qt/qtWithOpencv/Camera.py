import cv2


class Camera:

    def __init__(self, camera_code):
        self.camera_code = camera_code
        self.video_capture = cv2.VideoCapture(camera_code)

    def get_frame(self):
        if (self.video_capture.isOpened()):
            _, frame = self.videoCapture.read()
            self.video_capture.release()
            return frame
        else:
            raise Exception('camera is not reachable')

    # def get_frames(self , close_code):

    #     # while self.video_capture.isOpened():
