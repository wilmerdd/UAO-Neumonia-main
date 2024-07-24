FROM python:latest

# Instala dependencias necesarias para Xvfb y Xming
RUN apt-get update && apt-get install -y \
    xvfb \
    x11-xserver-utils \
    x11-apps \
    xfonts-base \
    wget \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update -y && \
    apt-get install python3-opencv -y 

    # Configura la variable de entorno DISPLAY para Xming
ENV DISPLAY=host.docker.internal:0.0

WORKDIR /home/src

COPY . ./
RUN pip install -r requirements.txt

# Ejecuta tu aplicación
CMD ["xvfb-run", "-a", "python", "/app/detector_neumonia.py"]
