import cv2
import os

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Failed to open camera")
    raise SystemExit(1)

os.makedirs("test_outputs", exist_ok=True)

for i in range(10):
    ret, frame = cap.read()
    if not ret:
        print("Failed to read frame")
        break

    print(f"Frame {i}: shape={frame.shape}")
    cv2.imwrite(f"test_outputs/frame_{i}.jpg", frame)

cap.release()
print("Camera test complete. Saved frames to test_outputs/")
