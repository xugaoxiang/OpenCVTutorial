import cv2
import numpy as np

image = cv2.imread('lenna.png')
cv2.imshow("original image", image)

h, w = image.shape[:2]

# T = 127
#
# # 转换为灰度图像
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# h, w = gray.shape
# T = cv2.mean(gray)[0]
# print("current threshold value : ", T)
#
# # 二值图像
# binary = np.zeros((h, w), dtype=np.uint8)
# for row in range(h):
#     for col in range(w):
#         pv = gray[row, col]
#         if pv > T:
#             binary[row, col] = 255
#         else:
#             binary[row, col] = 0
# cv2.imshow("binary", binary)

# 阈值下界
lowerb = (127, 127, 127)
# 阈值上界
upperb = (127, 127, 127)

# 图像二值化
mask = cv2.inRange(image, lowerb, upperb)

cv2.namedWindow("mask", flags= cv2.WINDOW_NORMAL | cv2.WINDOW_FREERATIO)
cv2.imshow('mask', mask)

cv2.waitKey(0)
cv2.destroyAllWindows()