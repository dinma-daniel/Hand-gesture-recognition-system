import os

model_path = 'hand-gesture-recognition-mediapipe-main/model/keypoint_classifier/keypoint_classifier.tflite'

if not os.path.exists(model_path):
    print(f"Model file not found: {model_path}")
else:
    print(f"Model file found: {model_path}")
