import cv2
import numpy as np
from sqlalchemy import column

image = cv2.imread("lenna.png")
cv2.imshow("original image", image)

column, row, channel = image.shape

# 变换矩阵，x放心移动100，y方向移动50
M = np.float32([[1, 0, 100], [0, 1, 50]])
dst=cv2.warpAffine(image, M, (column, row))
cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
