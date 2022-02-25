import cv2
import numpy as np

image = cv2.imread('lenna.png')
cv2.imshow("original image", image)

h, w = image.shape[:2]

# 获取ROI,/表示浮点数除法，返回值是float，而//表示整数除法
cy = h // 2
cx = w // 2

# ROI区域提取
roi = image[cy-200:cy+200, cx-100:cx+100, :]
cv2.imshow("roi", roi)

# ROI区域的复制
roi_copy = np.copy(roi)

# 修改ROI
roi[:, :, 0] = 0
cv2.imshow("roi modify", roi)

# modify copy roi
roi_copy[:, :, 2] = 0
cv2.imshow("roi_copy", roi_copy)

# 这时的image已经被修改了，也就是roi会影响到原图，但roi的拷贝不影响
cv2.imshow("image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()