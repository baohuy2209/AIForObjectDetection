import cv2

# The function cv2.imread() is used to load an image from a specified file path
image = cv2.imread("Ganesh.jpg")
cropped_image = image[0:1000, 0:1000]

cv2.imshow("Cropped Image", cropped_image)
cv2.imwrite("cropped_image.jpg", cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
