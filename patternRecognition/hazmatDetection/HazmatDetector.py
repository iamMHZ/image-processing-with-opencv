import cv2
import os


class Hazmat_detector:

    def __init__(self):
        self.__hazmat_list = list()

    def add_to_list(self, hazmat):
        self.__hazmat_list.append(hazmat)

    def get_hazmat_list(self):
        return self.__hazmat_list

    def calculate_features(self, hazmat):
        pass


    def read_templates(self , path):
        pass

