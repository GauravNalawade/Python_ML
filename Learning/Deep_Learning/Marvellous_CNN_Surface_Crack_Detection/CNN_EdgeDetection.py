import cv2
import numpy as np

from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import (
    preprocess_input,
    decode_predictions
)

# Load pretrained CNN
model = MobileNetV2(weights="imagenet")

# Start webcam
cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # OpenCV BGR → RGB
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # MobileNetV2 input size
    img_resized = cv2.resize(img, (224,224))

    # (224,224,3) → (1,224,224,3)
    x = np.expand_dims(img_resized, axis=0).astype(np.float32)

    # MobileNet preprocessing
    x = preprocess_input(x)

    # Prediction
    preds = model.predict(x, verbose=0)

    decoded = decode_predictions(preds, top=1)[0][0]

    label = f"{decoded[1]}: {decoded[2] * 100:.1f}%"

    # Display prediction
    cv2.putText(
        frame,
        label,
        (16,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )

    cv2.imshow("CNN Classification", frame)

    # Press q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()