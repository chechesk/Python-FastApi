CRUD API con FastAPI
Este proyecto es una API básica creada con FastAPI que permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre una lista de elementos.

Características
Crear nuevos elementos
Leer todos los elementos o un elemento específico
Actualizar un elemento existente
Eliminar un elemento por su ID
Documentación generada automáticamente con Swagger UI y Redoc
Requisitos
Python 3.8 o superior
Dependencias listadas en requirements.txt
Instalación
Clona el repositorio:

bash
Copiar código
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
POST	/items/	Crea un nuevo elemento
GET	/items/	Obtiene todos los elementos
GET	/items/{item_id}	Obtiene un elemento por su ID
PUT	/items/{item_id}	Actualiza un elemento existente
DELETE	/items/{item_id}	Elimina un elemento por su ID
Ejemplo de solicitudes
Crear un elemento:
bash
Copiar código
curl -X POST "http://127.0.0.1:8000/items/?item_id=1&name=Item1&description=Primero"
Leer todos los elementos:
bash
Copiar código
curl -X GET "http://127.0.0.1:8000/items/"
Leer un elemento específico:
bash
Copiar código
curl -X GET "http://127.0.0.1:8000/items/1"
Actualizar un elemento:
bash
Copiar código
curl -X PUT "http://127.0.0.1:8000/items/1?name=Item1_Updated&description=Actualizado"
Eliminar un elemento:
bash
Copiar código
curl -X DELETE "http://127.0.0.1:8000/items/1"
Estructura del proyecto
bash
Copiar código
.
├── main.py                # Código principal de la API
├── requirements.txt       # Dependencias del proyecto
├── README.md              # Documentación del proyecto
Contribuciones
¡Las contribuciones son bienvenidas! Siéntete libre de abrir un issue o un pull request en este repositorio.