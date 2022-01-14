import cv2

image = cv2.imread('lenna.png')
cv2.imshow('original image', image)

# cv2.COLOR_BGR2GRAY 彩色到灰度
# cv2.GRAY2BGR 灰度到彩色
# cv2.BGR2HSV BGR到HSV
# cv2.HSV2BGR HSV到BGR
# BGR是蓝绿红序列，HSV即色调(Hue)、饱和度(Saturation)和明度(Value)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray image', gray)

cv2.waitKey(0)

cv2.destroyAllWindows()
