from pyzbar import pyzbar
import cv2


def main():
    camera = cv2.VideoCapture(0)

    while camera.isOpened():
        flag, frame = camera.read()

        barcods = pyzbar.decode(frame)

        for barcode in barcods:
            x, y, w, h = barcode.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

            barcode_data = barcode.data.decode("utf-8")
            barcode_type = barcode.type

            cv2.putText(frame, barcode_type + " : " + barcode_data, (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 0, 255))

        cv2.imshow("OUTPUT", frame)
        if cv2.waitKey(1) == 32:
            break

    cv2.destroyAllWindows()
    camera.release()


main()
