import cv2
import numpy as np

image = cv2.imread("lenna.png")
cv2.imshow("original image", image)

column, row, channel = image.shape

M = cv2.getRotationMatrix2D((column/2,row/2), 45, 1)

dst = cv2.warpAffine(image, M, (column, row))
cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
