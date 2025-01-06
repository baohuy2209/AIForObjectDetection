import cv2
import numpy as np

# Load the image
image = cv2.imread("example.jpg")  # Replace 'example.jpg' with your image path

# Get image dimensions
(h, w) = image.shape[:2]

# Apply rotation
center = (w // 2, h // 2)
rotation_matrix = cv2.getRotationMatrix2D(
    center, 45, 1.0
)  # Rotate by 45 degrees
rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))

# Apply scaling
scaled_image = cv2.resize(
    image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR
)  # Scale by 1.5x

# Apply translation
translation_matrix = np.float32(
    [[1, 0, 50], [0, 1, 50]]
)  # Translate by 50 pixels in x and y directions
translated_image = cv2.warpAffine(image, translation_matrix, (w, h))

# Display the images with transformations
cv2.imshow("Rotated Image", rotated_image)
cv2.imshow("Scaled Image", scaled_image)
cv2.imshow("Translated Image", translated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
