# CRUD API con FastAPI

Este proyecto es una API básica creada con FastAPI que permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre una lista de elementos.

## Características
- Crear nuevos elementos
- Leer todos los elementos o un elemento específico
- Actualizar un elemento existente
- Eliminar un elemento por su ID
- Documentación generada automáticamente con Swagger UI y Redoc

## Requisitos
- Python 3.8 o superior
- Dependencias listadas en `requirements.txt`

## Instalación

### Clona el repositorio:
```bash
git clone https://github.com/tuusuario/tu-repo.git
cd tu-repo
Crea un entorno virtual (opcional pero recomendado):
bash
Copiar código
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
Instala las dependencias:
bash
Copiar código
pip install -r requirements.txt
Ejecución
Ejecuta el servidor FastAPI:
bash
Copiar código
python main.py
Accede a la aplicación en tu navegador:

http://127.0.0.1:8000 - Endpoint base
http://127.0.0.1:8000/docs - Documentación interactiva Swagger
http://127.0.0.1:8000/redoc - Documentación alternativa Redoc
Uso de la API
Endpoints principales
Método	Endpoint	Descripción
POST	/usuarios/	Crea un nuevo elemento
GET	/usuarios/	Obtiene todos los elementos
GET	/usuarios/{user_id}	Obtiene un elemento por su ID
PUT	/usuarios/{user_id}	Actualiza un elemento existente
DELETE	/usuarios/{user_id}	Elimina un elemento por su ID
Ejemplo de solicitudes
Crear un elemento:

bash
Copiar código
curl -X POST "http://127.0.0.1:8000/usuarios/?item_id=1&name=Item1&description=Primero"
Leer todos los elementos:

bash
Copiar código
curl -X GET "http://127.0.0.1:8000/usuarios/"
Leer un elemento específico:

bash
Copiar código
curl -X GET "http://127.0.0.1:8000/usuarios/1"
Actualizar un elemento:

bash
Copiar código
curl -X PUT "http://127.0.0.1:8000/usuarios/1?name=Item1_Updated&description=Actualizado"
Eliminar un elemento:

bash
Copiar código
curl -X DELETE "http://127.0.0.1:8000/usuarios/1"
Estructura del proyecto
bash
Copiar código
.
├── main.py            # Código principal de la API
├── requirements.txt   # Dependencias del proyecto
├── README.md          # Documentación del proyecto
├── Dockerfile         # Archivo para crear la imagen del contenedor
├── docker-compose.yml # Configuración para Docker Compose
├── env.yml            # Entorno Conda
├── .env               # Variables de entorno
Dockerfile
Este proyecto incluye un archivo Dockerfile para crear una imagen del contenedor con FastAPI y las dependencias necesarias:

dockerfile
Copiar código
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

# Verificar que FastAPI y otras dependencias estén instaladas correctamente
RUN echo "Verificando que FastAPI está instalado..."
RUN python -c "import fastapi; print(f'FastAPI version: {fastapi.__version__}')"

# Exponer el puerto donde corre la app FastAPI
EXPOSE 8000

# Ejecutar la aplicación cuando se inicie el contenedor
CMD ["conda", "run", "--no-capture-output", "-n", "pythonapp", "python", "app.py"]
docker-compose.yml
También se incluye un archivo docker-compose.yml para simplificar la ejecución de la API dentro de un contenedor Docker:

yaml
Copiar código
version: '3'

services:
  data:
    container_name: apipython
    restart: always
    build: ./
    ports:
      - "8000:8000"
Contribuciones
¡Las contribuciones son bienvenidas! Siéntete libre de abrir un issue o un pull request en este repositorio.

r
Copiar código

Este bloque incluye todo el contenido del archivo `README.md` junto con el código de los archivos `Do