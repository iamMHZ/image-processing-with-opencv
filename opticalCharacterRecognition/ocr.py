import cv2
import pytesseract
from PIL import Image
import numpy as np
import os


# image_path = 'test4.jpg'

# image = cv2.imread(image_path)
# img = cv2.imread(image_path)
# print(pytesseract.image_to_string(img, lang='eng'))
# # OR explicit beforehand converting
# print(pytesseract.image_to_string(Image.open(image_path), lang='eng'))


def ocr(directory_path):
    window_name = 'detection'
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

    for root, dirs, files in os.walk(directory_path):
        for name in files:
            file_path = os.path.join(root, name)
            if file_path.endswith('png') or file_path.endswith('jpg'):
                # print(file_path, end="\n\n")
                image = cv2.imread(str(file_path))
                height, width, channels = image.shape

                cv2.imshow(window_name, image)
                text = pytesseract.image_to_string(image, lang='eng')
                text = 'Output : ' + text
                print(text)
                text_shower = np.ones((400, 1024))
                cv2.putText(text_shower, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255))

                cv2.imshow('Output Text', text_shower)
                key = cv2.waitKey(1)
                if key == 32:
                    cv2.destroyAllWindows()
                    return


path = 'D:\Programming\database of image\RoboticPatterns'

ocr(path)
