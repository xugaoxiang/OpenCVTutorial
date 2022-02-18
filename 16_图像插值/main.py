import cv2

image = cv2.imread('lenna.png')
cv2.imshow("original image", image)

h, w = image.shape[:2]

dst = cv2.resize(image, (w*2, h*2), fx=0.75, fy=0.75, interpolation=cv2.INTER_NEAREST)
cv2.imshow("INTER_NEAREST", dst)

dst = cv2.resize(image, (w*2, h*2), interpolation=cv2.INTER_LINEAR)
cv2.imshow("INTER_LINEAR", dst)

dst = cv2.resize(image, (w*2, h*2), interpolation=cv2.INTER_AREA)
cv2.imshow("INTER_AREA", dst)

dst = cv2.resize(image, (w*2, h*2), interpolation=cv2.INTER_CUBIC)
cv2.imshow("INTER_CUBIC", dst)

dst = cv2.resize(image, (w*2, h*2), interpolation=cv2.INTER_LANCZOS4)
cv2.imshow("INTER_LANCZOS4", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()