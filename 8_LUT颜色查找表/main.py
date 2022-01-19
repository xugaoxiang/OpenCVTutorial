import cv2

image = cv2.imread('lenna.png')
cv2.imshow('original image', image)

# 变换到深绿色
dst = cv2.applyColorMap(image, cv2.COLORMAP_DEEPGREEN)
cv2.imshow('dst image', dst)

cv2.waitKey(0)

cv2.destroyAllWindows()
