import cv2

image1 = cv2.imread("lenna.png")
cv2.imshow("original image1", image1)

image2 = cv2.imread("kobe.png")
cv2.imshow("original image2", image2)

image_and = cv2.bitwise_and(image1, image2)
cv2.imshow("image and", image_and)

image_or = cv2.bitwise_or(image1, image2)
cv2.imshow("image or", image_or)

image_xor = cv2.bitwise_xor(image1, image2)
cv2.imshow("image xor", image_xor)

cv2.waitKey(0)
cv2.destroyAllWindows()
