import cv2
import os


class Hazmat:

    def __init__(self, name, path, image, key_points, descriptors):
        # having image or loading it from path ?!!
        # if it is being resize so we better have the image itself too
        self.image = image
        self.key_points = key_points
        self.descriptors = descriptors
        self.name = name
        self.path = path

    # def __str__(self):
    #     return
    #     str('name:  ' + self.name + '\n' + 'path:  ' + self.path + '\n' + 'key points :  ' + str(
    #         self.key_points) + '\n' + 'descriptors : ' + str(self.descriptors) + '\n')
