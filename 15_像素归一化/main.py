import cv2
import numpy as np

image = cv2.imread('lenna.png')
cv2.imshow("original image", image)

# 灰度图
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 转换为浮点数类型数组
gray = np.float32(gray)

# NORM_MINMAX，最常用的一种方法，数组的数值会被缩放到一个指定的范围，比如本例中的 0~1
dst = np.zeros(gray.shape, dtype=np.float32)
# 这里alpha=1, beta=0也是ok的
cv2.normalize(gray, dst=dst, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
# 显示原图时，需要将像素值 re-scale 到 0~255
cv2.imshow("NORM_MINMAX", np.uint8(dst*255))

# NORM_INF，无穷范数，每个值除以最大值来进行无穷范数归一化
dst = np.zeros(gray.shape, dtype=np.float32)
cv2.normalize(gray, dst=dst, alpha=1.0, beta=0, norm_type=cv2.NORM_INF)
# 归一化后最大值就是1，所以也是*255
cv2.imshow("NORM_INF", np.uint8(dst*255))

# NORM_L1，1范数，每个值除以它们的和来进行归一化
dst = np.zeros(gray.shape, dtype=np.float32)
cv2.normalize(gray, dst=dst, alpha=1.0, beta=0, norm_type=cv2.NORM_L1)
# 归一化后范围是 0~1，但最大值不是1，所以这里乘以一个足够大的数，你也可以取其它值，不一定是下面这个数。注意到 np.uint8 的最大值是255，因此 re-scale 的范围也是 0~255
cv2.imshow("NORM_L1", np.uint8(dst*20000000))

# NORM_L2，2范数，每个值除以该向量的模长，归一化位单位向量
dst = np.zeros(gray.shape, dtype=np.float32)
cv2.normalize(gray, dst=dst, alpha=1.0, beta=0, norm_type=cv2.NORM_L2)
# 与NORM_L1类似
cv2.imshow("NORM_L2", np.uint8(dst*30000))

cv2.waitKey(0)
cv2.destroyAllWindows()