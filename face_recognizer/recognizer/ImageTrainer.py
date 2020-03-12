import os
import cv2
import pickle
import numpy as np


def show_image(image):
    window_name = "PREVIEW"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.imshow(window_name, image)
    cv2.waitKey(1)


def start_training(path):
    # defining a dictionary to have both labels and their label_id
    label_dic = {}
    current_id = 0

    training_labels = []
    training_images = []

    face_cascade = cv2.CascadeClassifier(
        "D:\Programming\opencv\sources\data\haarcascades\haarcascade_frontalface_alt2.xml")

    recognizer = cv2.face.LBPHFaceRecognizer_create()

    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".png") or file.endswith("jpg"):
                image_path = os.path.join(root, file)
                label = os.path.basename(os.path.dirname(image_path)).replace(" ", "_").lower()
                print(label, ':', image_path)

                # if current image was not labeled:
                if not label in label_dic:
                    label_dic[label] = current_id
                    current_id += 1

                id = label_dic[label]
                # reading image and converting it to grayScale:
                image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
                # show_image(image)
                # print(type(image))

                # detecting faces and labeling them
                faces = face_cascade.detectMultiScale(image)
                for x, y, w, h in faces:
                    region_of_interest = image[y:y + h, x:x + w]
                    training_images.append(region_of_interest)
                    training_labels.append(id)

    print(label_dic)

    # saving dictionary of labels and the recognizer for using in another python file
    with open("labels.pickle", 'wb') as file:
        pickle.dump(label_dic, file)

    recognizer.train(training_images, np.array(training_labels))
    recognizer.save("trainer.yml")


path = 'D:\Programming\database of image\ImageDataSet\people'
start_training(path)
