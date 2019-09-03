import cv2
import numpy as np


def show_result(window_name, frame, millis):
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.imshow(window_name, frame)
    key = cv2.waitKey(millis)
    if key == 32:
        cv2.destroyAllWindows()


def object_detection_yolo(frame):
    # loading YOLO:
    net = cv2.dnn.readNet('yolov3.weights', 'yolov3.cfg')

    labels = list()

    with open('coco.names', 'r') as file:
        for line in file.readlines():
            labels.append(line.strip())

    # print(labels)

    # ???????
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    height, width, channels = frame.shape

    blobs = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, False)
    # for blob in blobs:
    #     for n, img in enumerate(blob):
    #         show_result(str(n), img)

    net.setInput(blobs)
    outputs = net.forward(output_layers)

    # print(outputs)

    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > 0.3:
                print(labels[class_id])

                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # cv2.circle(frame, (center_x, center_y), 100, (0, 0, 255),5)

                #             rectangle coordinates
                x = int(center_x - (w / 2))
                y = int(center_y - (h / 2))

                # cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
                cv2.putText(frame, str(labels[class_id]), (x + 30, y + 30), cv2.FONT_ITALIC, 4, (0, 0, 255), 5)

    # show_result('result', frame, 0)
    # show_result('result', frame, 1)

    return frame


def start_live_object_recognition():
    camera = cv2.VideoCapture(0)

    while True:
        _, frame = camera.read()

        result = object_detection_yolo(frame)

        cv2.imshow('result', result)

        key = cv2.waitKey(1)
        if key == 32:
            cv2.destroyAllWindows()
            camera.release()
            break


# call to functions:
# image = cv2.imread('testImage2.jpg')
# result = object_detection_yolo(image)
# show_result('result', result, 0)

start_live_object_recognition()
