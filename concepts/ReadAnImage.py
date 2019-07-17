import cv2


# using named window for reading an image:
def readImage(imgPath):
    img = cv2.imread(imgPath)
    # cv2.imshow("showImage", img)
    cv2.namedWindow('Lena', cv2.WINDOW_FREERATIO)
    cv2.imshow('Lena', img)
    cv2.waitKey(0)
    cv2.destroyWindow('Lena')

# flag cv2.COLOR_BGR@RGB
def readImageWithColorConversions(path):
    image = cv2.imread(path, cv2.COLOR_BGR2RGB)
    cv2.imshow("color conversion",image)
    cv2.waitKey(0)


# write the grayScale version of image to disk

def writeImage(imgPath):
    img = cv2.imread(imgPath, 0)
    cv2.imwrite("C:\\Users\hMd\\Desktop\\result.jpg", img)


def main():
    path = "D:\Programming\database of image\lena_color_256.tif"
    readImage(path)

    writeImage(path)

    readImageWithColorConversions(path)


    img = cv2.imread(path)
    print(type(img))

main()
