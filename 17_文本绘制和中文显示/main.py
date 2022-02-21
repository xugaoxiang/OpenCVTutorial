import cv2

image = cv2.imread('lenna.png')

text = 'Hello OpenCV-Python!'
dst = cv2.putText(image, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 50, 50))
cv2.imshow('dst image', dst, )

cv2.waitKey(0)
cv2.destroyAllWindows()