import cv2


def get_frame(cap):
    if (cap.isOpened):
        _, frame = cap.read()
        return frame


def get_background_model(backgroundSubtractor):
    pass


def main():
    cap = cv2.VideoCapture(0)
    background_subtractor = cv2.BackgroundSubtractorMOG()
