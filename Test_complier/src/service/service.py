from ultralytics import YOLO
import cv2


model = YOLO('yolov8n.pt')  
source = 0  
cap = cv2.VideoCapture(source)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model.predict(source=frame, save=False, conf=0.3, show=False)

    annotated_frame = results[0].plot()
    cv2.imshow("YOLOv8 Detection", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
