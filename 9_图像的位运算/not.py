import cv2

image = cv2.imread("lenna.png")
cv2.imshow("original image", image)

dst = cv2.bitwise_not(image)
cv2.imshow("dst image", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
