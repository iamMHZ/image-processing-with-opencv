from pyzbar import pyzbar
import cv2


def main():
    image = cv2.imread("barcodeAndQR.jpg")

    barcods = pyzbar.decode(image)

    for barcode in barcods:
        # draw a rectangle around barcode
        x, y, w, h = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

        barcode_data = barcode.data.decode("utf-8")
        barcode_type = barcode.type

        cv2.putText(image, barcode_data + " , " + barcode_type, (x, y - 20), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))

    cv2.imshow("output", image)

    cv2.waitKey(0)


main()
