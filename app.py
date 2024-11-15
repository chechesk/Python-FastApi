from fastapi import FastAPI, HTTPException

app = FastAPI()

# Base de datos simulada
fake_db = []

# Modelo de datos
class Item:
    def __init__(self, id: int, name: str, description: str):
        self.id = id
        self.name = name
        self.description = description

#Leer Conexion Raiz 
@app.get("/")
def read_items():
    return{"Welcome API FastApi"}

# Crear un elemento
@app.post("/items/")
def create_item(item_id: int, name: str, description: str):
    if any(item.id == item_id for item in fake_db):
        raise HTTPException(status_code=400, detail="El ID ya existe")
    item = Item(item_id, name, description)
    fake_db.append(item)
    return {"message": "Elemento creado", "item": item.__dict__}

# Leer todos los elementos
@app.get("/items/")
def read_items():
    return {"items": [item.__dict__ for item in fake_db]}

# Leer un elemento por ID
@app.get("/items/{item_id}")
def read_item(item_id: int):
    for item in fake_db:
        if item.id == item_id:
            return {"item": item.__dict__}
    raise HTTPException(status_code=404, detail="Elemento no encontrado")

# Actualizar un elemento
@app.put("/items/{item_id}")
def update_item(item_id: int, name: str, description: str):
    for item in fake_db:
        if item.id == item_id:
            item.name = name
            item.description = description
            return {"message": "Elemento actualizado", "item": item.__dict__}
    raise HTTPException(status_code=404, detail="Elemento no encontrado")

# Eliminar un elemento
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    global fake_db
    fake_db = [item for item in fake_db if item.id != item_id]
    return {"message": "Elemento eliminado"}

# Ejecutar la aplicación
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
