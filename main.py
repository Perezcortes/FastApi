"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def raiz():
    return {"mensaje": "Prueba muy exitosa"}

@app.get("/saludar")
def saludar(nombre: str = 'lola', dia: str = 'Lunes'):
    return {"mensaje": f"saludos {nombre} hoy es {dia}!!"}
"""
"""
from fastapi import FastAPI
from pydantic import BaseModel


#Define model Item
class Item(BaseModel):
    name: str = "romel"
    age: int

app = FastAPI()

@app.post("/")
def root(elem: Item):
    name = elem.name
    age = elem.age
    return {"message": f"Haz ingresado {name}, tienes {age} años"}
"""
"""
#ejemplo con PUT
from fastapi import FastAPI
from pydantic import BaseModel

# Define model Item
class Item(BaseModel):
    name: str
    description: str

# Define items at application start
items = {"bananas": "Yellow fruit."}

app = FastAPI()

@app.put("/items")
def update_item(item: Item):
    name = item.name
    # Update the description
    items[name] = item.description
    return item
"""
"""
#ejemplo con delete
from fastapi import FastAPI
from pydantic import BaseModel

# Define model Item
class Item(BaseModel):
    name: str

# Define items at application start
items = {"apples", "oranges", "bananas"}

app = FastAPI()

@app.delete("/items")
def delete_item(item: Item):
    name = item.name
    # Delete the item
    items.remove(name)
    return {}
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Definir el modelo Item
class Item(BaseModel):
    name: str

# Definir los elementos al iniciar la aplicación
items = {"apples", "oranges"}

app = FastAPI()

@app.delete("/items")
def delete_item(item: Item):
    name = item.name
    if name in items:
        items.remove(name)
    else:
        # Generar HTTPException con código de estado "no encontrado"
        raise HTTPException(status_code=404, detail="Item not found.")
    return items #para devolver el elemento encontrado y eliminado
