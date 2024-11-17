from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Usuario
from config import SessionLocal
from pydantic import BaseModel

app = FastAPI()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Modelo Pydantic para la creación y actualización del usuario
class UsuarioBase(BaseModel):
    nombre: str
    email: str
    password: str

# Crear un usuario
@app.post("/usuarios/")
def create_user(user: UsuarioBase, db: Session = Depends(get_db)):
    # Verificar si el usuario ya existe
    db_usuario = db.query(Usuario).filter(Usuario.email == user.email).first()
    if db_usuario:
        raise HTTPException(status_code=400, detail="El usuario ya existe")

    # Crear el nuevo usuario
    new_user = Usuario(nombre=user.nombre, email=user.email)
    new_user.set_password(user.password)  # Establecer la contraseña con hash

    # Agregar a la base de datos
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "Usuario creado", "user": new_user}

# Leer todos los usuarios
@app.get("/usuarios/")
def read_users(db: Session = Depends(get_db)):
    users = db.query(Usuario).all()
    return {"users": users}

# Leer un usuario por ID
@app.get("/usuarios/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(Usuario).filter(Usuario.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"user": user}

# Actualizar un usuario
@app.put("/usuarios/{user_id}")
def update_user(user_id: int, user: UsuarioBase, db: Session = Depends(get_db)):
    db_user = db.query(Usuario).filter(Usuario.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    # Actualizar los campos del usuario
    db_user.nombre = user.nombre
    db_user.email = user.email
    db_user.set_password(user.password)  # Establecer nueva contraseña con hash
    db.commit()
    db.refresh(db_user)
    return {"message": "Usuario actualizado", "user": db_user}

# Eliminar un usuario
@app.delete("/usuarios/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(Usuario).filter(Usuario.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    db.delete(user)
    db.commit()
    return {"message": "Usuario eliminado"}

# Login (Verificación de contraseña)
@app.post("/login/")
def login(email: str, password: str, db: Session = Depends(get_db)):
    # Buscar el usuario por correo electrónico
    db_usuario = db.query(Usuario).filter(Usuario.email == email).first()
    if db_usuario is None:
        raise HTTPException(status_code=400, detail="Correo o contraseña incorrectos")

    # Verificar la contraseña
    if not db_usuario.verify_password(password):
        raise HTTPException(status_code=400, detail="Correo o contraseña incorrectos")

    return {"message": "Inicio de sesión exitoso", "user": db_usuario}

# Ejecutar la aplicación
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
