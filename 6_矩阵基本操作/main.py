import cv2
import numpy as np

m1 = np.array([[1, 2, 3], [4, 5, 6]], np.uint8)
m2 = np.array([[4, 5, 6], [7, 8, 9]], np.uint8)

print(m1)
print(m2)

# 加法
s = m1 + m2
print(s)

# 使用cv2中的方法
s_add = cv2.add(m1, m2, dtype=cv2.CV_32F)
print(s_add)

# 减法运算
s2 = m2 - m1
s3 = m1 - m2
print(s2)
print(s3)

# 矩阵点乘
# 矩阵的点乘即2个矩阵对应位置的数值相乘。矩阵点乘可以使用 `*` 运算符或者 `np.multiply`
s4 = m1 * m2
s5 = np.multiply(m1, m2)
print(s4)
print(s5)

# 矩阵点除
# 矩阵点除和点乘运算类似，对应位置的数值相除
s6 = m2 / m1
print(s6)

# 矩阵乘法
# 可以使用 `numpy.dot` 方法实现矩阵的乘法，要求第一个矩阵的列和第二个矩阵的行一致
m3 = np.array([[1, 2], [3, 4], [5, 6]], np.uint8)
s7 = np.dot(m1, m3)
print(s7)
