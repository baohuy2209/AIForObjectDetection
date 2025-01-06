import cv2

image = cv2.imread("example.jpg")
resized_image = cv2.resize(image, (1050, 1610))

cv2.imshow("Resized image", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
