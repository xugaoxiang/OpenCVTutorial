import cv2

image = cv2.imread('lenna.png')
cv2.imshow("original image", image)

# 分离出通道
mv = cv2.split(image)
print(type(mv))

# 操作蓝色通道
mv[0][:, :] = 0
# 合并通道
dst_b = cv2.merge(mv)
cv2.imshow('dst_b image', dst_b)

# 操作绿色通道
mv[1][:, :] = 0
dst_g = cv2.merge(mv)
cv2.imshow('dst_g image', dst_g)

# 操作红色通道
mv[2][:, :] = 0
dst_r = cv2.merge(mv)
cv2.imshow('dst_r image', dst_r)

# image是输入，dst_r是输出，第三个参数fromTo，也就是将输入image的红色通道拷贝到输出dst_r的绿色通道。如果是多个通道拷贝的话，fromTo可以是 [2,0, 1,1, 0,2]，意思就是将输入的rgb拷贝到输出的bgr
cv2.mixChannels(image, dst_r, fromTo=[2, 1])
cv2.imshow('dst_mixChannels', dst_r)

cv2.waitKey(0)
cv2.destroyAllWindows()