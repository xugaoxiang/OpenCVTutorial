# 画直线
import cv2
import numpy as np

image = cv2.imread('lenna.png')

# 从(50, 50)画一条蓝色的直线到(300, 100)， 边界线粗细为3，颜色是BGR序列
cv2.line(image, (50, 50), (300, 100), (255, 0, 0), 3)
cv2.imshow('Draw line', image)

cv2.waitKey(0)

# 删除创建的所有窗口
cv2.destroyAllWindows()


# 画长方形
image = cv2.imread('lenna.png')

# 长方形的左上角坐标(50, 50)，右下角坐标(300, 100)，边框的颜色是蓝色，边界线粗细为3
cv2.rectangle(image, (50, 50), (300, 100), (255, 0, 0), 3)
cv2.imshow('Draw rectangle', image)

cv2.waitKey(0)

# 删除创建的所有窗口
cv2.destroyAllWindows()


# 画圆
image = cv2.imread('lenna.png')

# 圆的中心坐标(80, 80)，半径为50，边框的颜色是蓝色，最后一个参数是边界线粗细为2像素
cv2.circle(image, (80, 80), 50, (255, 0, 0), 2)

# 如果将最后一个参数设置为-1，则是用对应颜色填充圆
cv2.circle(image, (80, 80), 50, (255, 0, 0), -1)

cv2.imshow('Draw circle', image)

cv2.waitKey(0)

# 删除创建的所有窗口
cv2.destroyAllWindows()


# 画椭圆
image = cv2.imread('lenna.png')

# 椭圆的中心坐标(200, 30)，元组(100,10)分别代表长轴和短轴的长度，接下来的0带不动是椭圆的旋转角度，单位是度，然后是椭圆的起始和终止角度，分别是0和50，边框的颜色是蓝色，最后边界线的粗细，与画圆时含义一致
cv2.ellipse(image, (200, 30), (100, 10), 0, 0, 50, (255, 0, 0), -1)
cv2.imshow('Draw ellipse', image)

cv2.waitKey(0)

# 删除创建的所有窗口
cv2.destroyAllWindows()


# 画多边形
image = cv2.imread('lenna.png')

# 多边形的几个顶点坐标
pts = np.array([[20, 20], [40, 10], [70, 50], [60, 80], [30, 100]], np.int32)

# 第一个参数为-1，代表这一维度的长度是根据后面的维度计算出来的
pts = pts.reshape((-1, 1, 2))

# 第三个参数代表几条折线是否闭合，True为闭合
cv2.polylines(image, [pts], True, (255, 0, 0))
cv2.imshow('Draw polylines', image)

cv2.waitKey(0)

# 删除创建的所有窗口
cv2.destroyAllWindows()