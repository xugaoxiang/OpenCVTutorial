import cv2
import numpy as np

imgname = "lenna.png"

image = cv2.imread(imgname, cv2.IMREAD_COLOR)

height, width = image.shape[:2]

src = np.array([[0, 0],  [width-5, 0],  [0, height-5], [width-5, height-5]], np.float32)
dst = np.array([[100,100], [width/3, 10], [100, height-5], [width-5, height-5]], np.float32)

M = cv2.getPerspectiveTransform(src, dst)
dst = cv2.warpPerspective(image, M, (width, height), borderValue=125)

cv2.imshow("dst image", dst)

cv2.imshow("original image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()