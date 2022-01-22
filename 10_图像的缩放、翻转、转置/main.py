import cv2

image = cv2.imread("lenna.png")
cv2.imshow("original image", image)

# 缩放，指定宽高
image_sized_pixel = cv2.resize(image, (200, 200))
cv2.imshow('sized pixel image', image_sized_pixel)

# 缩放，按比例
image_sized_p = cv2.resize(image, None, fx=0.5, fy=0.5)
cv2.imshow('sized percent image', image_sized_p)

# 翻转
# flipcode为0是垂直方向翻转
# flipcode为正数时是水平方向翻转，一般取值1
# flipcode为负数时，2个方向都进行翻转，一般取值-1
image_flip = cv2.flip(image, flipCode=-1)
cv2.imshow('flip image', image_flip)

# 转置，将图像的x坐标和y坐标互换
image_transpose = cv2.transpose(image)
cv2.imshow('transpose image', image_transpose)

cv2.waitKey(0)
cv2.destroyAllWindows()
