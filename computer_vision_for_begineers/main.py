import cv2

# The function cv2.imread() is used to load an image from a specified file path
image = cv2.imread("Ganesh.jpg")
# Display image
cv2.imshow("Original Image: ", image)
# Keep the window open until and key is pressed
cv2.waitKey(0)
# closes the window
cv2.destroyAllWindows()
