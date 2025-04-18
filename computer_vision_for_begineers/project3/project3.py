import cv2
from fer import FER

emotion_detector = FER()
# Start the webcam feed
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    emotions = emotion_detector.detect_emotions(frame)
    if emotions:
        emotion_data = emotions[0]["emotions"]
        max_emotion = max(emotion_data, key=emotion_data.get)
        (x, y, w, h) = emotions[0]["box"]
        cv2.putText(
            frame,
            max_emotion,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
        )

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow("Emotion Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
