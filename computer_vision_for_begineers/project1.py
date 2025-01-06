import cv2

image = cv2.imread("example.jpg")
(h, w) = image.shape[:2]
center = (w // 2, h // 2)
cv2.circle(image, (150, 150), 50, (250, 0, 0), 2)
cv2.rectangle(image, (50, 50), (200, 200), (0, 255, 0), 3)
cv2.line(image, (10, 10), (300, 300), (0, 0, 255))
cv2.putText(
    image,
    "OpenCV Tutorial",
    (50, 50),
    cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
    1,
    (255, 255, 255),
    2,
    cv2.LINE_AA,
)
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
