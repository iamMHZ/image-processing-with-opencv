import cv2
import os


class Hazmat:

    def __init__(self, name, image, features, descriptor):
        self.image = image
        self.feature = features
        self.descriptors = descriptor
        self.name = name
