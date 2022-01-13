# 导入模块
import cv2

# 读取图片文件
image = cv2.imread('lenna.png')

# 指定窗口
cv2.namedWindow("show image", cv2.WINDOW_AUTOSIZE)

# 开窗口显示
cv2.imshow('show image', image)

# 保存成文件
cv2.imwrite('copy.png', image)

# 接收键盘输入,相当于是一个loop循环
cv2.waitKey(0)

# 删除创建的所有窗口，删除特定窗口cv2.destroyWindow(winname=**)
cv2.destroyAllWindows()
