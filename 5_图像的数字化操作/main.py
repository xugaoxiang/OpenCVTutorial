import cv2
import numpy as np

# image的数据类型是 <class 'numpy.ndarray'>
image = cv2.imread('lenna.png')

cv2.imshow('original image', image)

# 图像克隆
image_copy = np.copy(image)
cv2.imshow('copy image', image_copy)

# 赋值，将特定区域设置成白色
image[100:200, 100:300, :] = 255
cv2.imshow("region white image", image)

# 黑色图像
image_black = np.zeros(image.shape, image.dtype)
cv2.imshow("black image", image_black)

# 蓝色图像
image_blue = np.ones(image.shape, dtype=np.uint8)
# BGR序列，分别对应0~2
image_blue[:, :, 0] = 255
cv2.imshow("blue image", image_blue)

cv2.waitKey(0)
cv2.destroyAllWindows()
