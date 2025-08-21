from ultralytics import YOLO

# 📂 Ruta al archivo data.yaml
dataset_path = r"C:\Users\Reiman\Downloads\ConteoGanado\coeconter-7\data.yaml"

# 📦 Cargar el modelo YOLOv8 base
model = YOLO("yolov8n.pt")  # Puedes cambiar a "yolov8s.pt" si quieres más precisión

print("🚀 Entrenando con 150 epochs")
# 🏋️‍♂️ Entrenar el modelo
model.train(
    data=dataset_path,
    epochs=150,
    imgsz=1280,
    batch=8,
    lr0=0.001,
)

print("✅ ¡Entrenamiento completado exitosamente!")
