from ultralytics import YOLO
import cv2

# Configure the tracking parameters and run the tracker
modelo = YOLO('yolov8m.pt')

videoPath = "cars.mp4"
resultado = modelo.predict(source=videoPath, conf=0.5, iou=0.5, show=True, save=True)
