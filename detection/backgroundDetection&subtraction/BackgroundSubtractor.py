import cv2


def get_frame(cap):
    if (cap.isOpened):
        _, frame = cap.read()
        return frame


#
# def get_background_model(frame, background_subtractor):
#     background_model = background_subtractor.apply(image=frame)
#
#     return background_model


def main():
    cap = cv2.VideoCapture(0)
    background_subtractor = cv2.createBackgroundSubtractorMOG2()

    while True:

        frame = get_frame(cap)

        background_model = background_subtractor.apply(frame, learningRate=0.01)

        cv2.imshow('original frame', frame)
        cv2.imshow('background model', background_model)
        cv2.imshow('forground', cv2.cvtColor(background_model, cv2.COLOR_GRAY2BGR) & frame)

        key = cv2.waitKey(1)

        if key == 32:
            cv2.destroyAllWindows()
            cap.release()
            break


main()
