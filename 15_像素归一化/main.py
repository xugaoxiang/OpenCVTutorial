import cv2
import numpy as np

image = cv2.imread('lenna.png')
cv2.imshow("original image", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 转换为浮点数类型数组
gray = np.float32(gray)
print(gray)

# scale and shift by NORM_MINMAX
dst = np.zeros(gray.shape, dtype=np.float32)
cv2.normalize(gray, dst=dst, alpha=0, beta=1.0, norm_type=cv2.NORM_MINMAX)
print(dst)
cv2.imshow("NORM_MINMAX", np.uint8(dst*255))

# scale and shift by NORM_INF
dst = np.zeros(gray.shape, dtype=np.float32)
cv2.normalize(gray, dst=dst, alpha=1.0, beta=0, norm_type=cv2.NORM_INF)
print(dst)
cv2.imshow("NORM_INF", np.uint8(dst*255))

# scale and shift by NORM_L1
dst = np.zeros(gray.shape, dtype=np.float32)
cv2.normalize(gray, dst=dst, alpha=1.0, beta=0, norm_type=cv2.NORM_L1)
print(dst)
cv2.imshow("NORM_L1", np.uint8(dst*10000000))

# scale and shift by NORM_L2
dst = np.zeros(gray.shape, dtype=np.float32)
cv2.normalize(gray, dst=dst, alpha=1.0, beta=0, norm_type=cv2.NORM_L2)
print(dst)
cv2.imshow("NORM_L2", np.uint8(dst*10000))

cv2.waitKey(0)
cv2.destroyAllWindows()