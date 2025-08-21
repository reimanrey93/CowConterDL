# Entrenamiento de modelo de conteo de ganado 🐄

Este proyecto utiliza YOLOv8 para entrenar un modelo de detección y conteo de ganado a partir de imágenes aéreas. Está preparado para ejecutarse en contenedores Docker aprovechando la aceleración por GPU.

---

## 🧱 Componentes del proyecto

- `train_gpu.py`: script principal de entrenamiento
- `predict_yolo.py`: script para realizar inferencias
- `runs/`: carpeta donde se almacenan los modelos entrenados
- `dataset/`: ubicación esperada del dataset para entrenamiento
- `Dockerfile`: define la imagen de entrenamiento
- `requirements.txt`: librerías necesarias

---

## 🚀 Requisitos

- Docker (con soporte de GPU habilitado)
- GPU NVIDIA (mínimo 8 GB, recomendado 12 GB)
- Drivers CUDA instalados correctamente

---

## 🐳 Instrucciones para construir y ejecutar el contenedor

```bash
# Clonar el repositorio
git clone https://github.com/tuusuario/ConteoGanado.git
cd ConteoGanado

# Construir imagen Docker
docker build -t ndvi-train .

# Ejecutar contenedor con acceso a GPU y volumen montado
docker run --rm --gpus all --shm-size=4g -it -v "${PWD}:/workspace" ndvi-train bash

# Entrar al contenedor y lanzar entrenamiento
python train_gpu.py

#Si estás fuera del contenedor, asegúrate de tener instaladas:
pip install ultralytics==8.3.117
pip install opencv-python-headless

#convinaciones d epar[ametros sugeridas
#| Experimento | `epochs` | `imgsz` | `batch` | `lr0`  | `degrees` | `translate` | `scale` | `fliplr` | `auto_augment` | `erasing` |
| ----------- | -------- | ------- | ------- | ------ | --------- | ----------- | ------- | -------- | -------------- | --------- |
| **Base**    | 150      | 1024    | 2       | 0.001  | 10        | 0.1         | 0.5     | 0.5      | randaugment    | 0.4       |
| Exp 1       | 200      | 1024    | 2       | 0.0015 | 20        | 0.2         | 0.7     | 0.5      | randaugment    | 0.3       |
| Exp 2       | 250      | 1280    | 1       | 0.0008 | 15        | 0.15        | 0.6     | 0.5      | randaugment    | 0.4       |
| Exp 3       | 180      | 1024    | 4       | 0.002  | 10        | 0.1         | 0.5     | 0.7      | randaugment    | 0.5       |
| Exp 4       | 300      | 1024    | 2       | 0.001  | 25        | 0.3         | 0.6     | 0.5      | randaugment    | 0.6       |


