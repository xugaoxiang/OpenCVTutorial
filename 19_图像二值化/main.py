import cv2
import numpy as np

image = cv2.imread('lenna.png')
cv2.imshow("original image", image)

h, w = image.shape[:2]

# 转换为灰度图像
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
h, w = gray.shape

# 取均值作为阈值
T = cv2.mean(gray)[0]
print("T: {}".format(T))

binary = np.zeros((h, w), dtype=np.uint8)
for row in range(h):
    for col in range(w):
        pv = gray[row, col]
        if pv > T:
            binary[row, col] = 255
        else:
            binary[row, col] = 0

cv2.imshow("binary", binary)

cv2.waitKey(0)
cv2.destroyAllWindows()