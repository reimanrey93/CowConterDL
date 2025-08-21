FROM nvidia/cuda:12.2.0-base-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive

# Instala Python, pip y dependencias básicas del sistema
RUN apt update && \
    apt install -y python3 python3-pip git libgl1 libglib2.0-0 && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    pip3 install --upgrade pip

# Copia e instala requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Crea carpeta de trabajo
WORKDIR /workspace

# Terminal interactiva por defecto
CMD ["bash"]
