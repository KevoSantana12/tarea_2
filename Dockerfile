# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /python-docker

# Copiar el archivo de requisitos y instalar dependencias
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copiar todo el código de la aplicación al contenedor
COPY . .

# Exponer el puerto en el que Gunicorn servirá la aplicación
EXPOSE 8000

# Comando para ejecutar Gunicorn, sirviendo la aplicación en 0.0.0.0:8000
CMD ["gunicorn", "wsgi:app", "-b", "0.0.0.0:8000"]
