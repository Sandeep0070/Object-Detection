from ultralytics import YOLO

import cv2

model=YOLO('../yolo_wieght/yolov8n.pt')
result=model("Image/2.jpg",show=True)
cv2.waitKey(0)