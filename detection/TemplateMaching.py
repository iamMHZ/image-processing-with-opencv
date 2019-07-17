import cv2

image = cv2.imread('C:\\Users\hMd\Desktop\image.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

template = cv2.imread('C:\\Users\hMd\Desktop\\template.jpg')
gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

w, h  = gray_template.shape

# Apply template Matching
res = cv2.matchTemplate(gray_image, gray_template, cv2.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

cv2.rectangle(image, top_left, bottom_right, 0, 2)

cv2.imshow('template', template)
# cv2.imshow('src', image)
cv2.imshow('result', image)

cv2.waitKey(0)
