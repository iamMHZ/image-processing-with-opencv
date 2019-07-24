import cv2
#
# camera = cv2.VideoCapture(0)
#
# while True:
#     _, img = camera.read()
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
#     sift = cv2.xfeatures2d.SIFT_create()
#     kp = sift.detect(gray, None)
#     img = cv2.drawKeypoints(img, kp)
#
#     cv2.imshow("image", img)
#
#     if cv2.waitKey(1) == 32:
#         break
#
# cv2.destroyAllWindows()
# camera.release()
