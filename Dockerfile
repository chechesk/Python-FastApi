FROM continuumio/miniconda3

WORKDIR /app

# Copiar los archivos necesarios
COPY env.yml .  
COPY .env .  
COPY app.py . 
COPY . . 

# Crear el entorno con el archivo env.yml
RUN conda env create -f env.yml

# Establecer el entorno Conda como predeterminado para los siguientes pasos
SHELL ["conda", "run", "-n", "pythonapp", "/bin/bash", "-c"]

# Verificar que fastapi y otras dependencias estén instaladas correctamente
RUN echo "Verificando que FastAPI está instalado..."
RUN python -c "import fastapi; print(f'FastAPI version: {fastapi.__version__}')"

# Exponer el puerto donde corre la app FastAPI
EXPOSE 8000

# Ejecutar la aplicación cuando se inicie el contenedor
CMD ["conda", "run", "--no-capture-output", "-n", "pythonapp", "python", "app.py"]
