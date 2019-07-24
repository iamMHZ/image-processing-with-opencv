# import cv2
# import numpy as np
#
# camera = cv2.VideoCapture(0)
#
# # while camera.isOpened():
# _, frame = camera.read()
#
# cv2.imshow("frame", frame)
#
# mask = np.zeros(frame.shape[:2], np.uint8)
#
# bgdModel = np.zeros((1, 65), np.float64)
# fgdModel = np.zeros((1, 65), np.float64)
#
# cv2.grabCut(frame, mask, (50, 50, 450, 290), bgdModel, fgdModel, 6, cv2.GC_INIT_WITH_RECT)
#
# mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
# frame = frame * mask2[:, :, np.newaxis]
# cv2.waitKey()
# # if cv2.waitKey(1) == 32:
# #     break
#
# cv2.destroyAllWindows()
# camera.release()
