# Usar una imagen base de Python 3.10
FROM python:3.10

# Instalar paquetes del sistema necesarios (ffmpeg)
RUN apt-get update && apt-get install -y ffmpeg

COPY . .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto utilizado por Streamlit
EXPOSE 8501

# Comando para ejecutar la aplicación Streamlit
CMD ["streamlit", "run", "streamlit2.py"]
