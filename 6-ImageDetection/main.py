from ultralytics import YOLO

# Simple Image Inference
# model = YOLO()
# result = model("data/lesson.JPG")
# result[0].show()

# Simple Video Inference
model = YOLO()
model.predict(source="/Users/mehmetbilen/Documents/GitHub/moving-obj-detection/tests/resources/raw_videos/people.avi",save=True)
