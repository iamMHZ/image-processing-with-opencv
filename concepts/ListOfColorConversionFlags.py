

import cv2



def main():

    numberOfColorFlags = 0
    for filename in dir(cv2):
        if filename.startswith("COLOR_"):
            print(filename)
            numberOfColorFlags +=1

    print("\nnumber of color conversion flags :"+str(numberOfColorFlags))


main()