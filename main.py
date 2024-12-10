from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware  # Importar CORSMiddleware
from database import db
from models import Element
from bson import ObjectId

app = FastAPI()

# Configurar CORS para permitir solicitudes desde tu frontend (Angular)
app.add_middleware(
    CORSMiddleware,
    # Permite solicitudes solo desde el frontend en localhost:4200
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    # Permite todos los métodos HTTP (GET, POST, PUT, DELETE)
    allow_methods=["*"],
    allow_headers=["*"],  # Permite todos los encabezados
)


@app.get("/elements/")
async def get_elements():
    elements = await db.elements.find().to_list(None)
    for element in elements:
        element["_id"] = str(element["_id"])
    return elements


@app.get("/elements/{element_id}")
async def get_element(element_id: str):
    try:
        element = await db.elements.find_one({"_id": ObjectId(element_id)})
        if not element:
            raise HTTPException(status_code=404, detail="Element not found")
        element["_id"] = str(element["_id"])
        return element
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=400, detail="Invalid ID format")


@app.post("/elements/")
async def create_element(element: Element):
    result = await db.elements.insert_one(element.dict(by_alias=True))
    return {"id": str(result.inserted_id)}


@app.put("/elements/{element_id}")
async def update_element(element_id: str, element: Element):
    try:
        result = await db.elements.update_one(
            {"_id": ObjectId(element_id)},
            {"$set": element.dict(by_alias=True)}
        )
        if result.modified_count == 0:
            raise HTTPException(
                status_code=404, detail="Element not found or no changes made")
        return {"message": "Element updated successfully"}
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=400, detail="Invalid ID format")


@app.delete("/elements/{element_id}")
async def delete_element(element_id: str):
    try:
        result = await db.elements.delete_one({"_id": ObjectId(element_id)})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Element not found")
        return {"message": "Element deleted successfully"}
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=400, detail="Invalid ID format")

# Los demás endpoints no necesitan cambios en cuanto a CORS


@app.get("/element/atomicName/{name}")
async def get_element_by_name(name: str):
    try:
        element = await db.elements.find_one({"name": name})
        if not element:
            raise HTTPException(
                status_code=404, detail=f"Element with atomic name '{name}' not found")
        element["_id"] = str(element["_id"])
        return element
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="Internal server error")


@app.get("/elements/state/{state}")
async def get_elements_by_state(state: str):
    try:
        elements = await db.elements.find({"standard_state": state}).to_list(100)
        if not elements:
            raise HTTPException(
                status_code=404, detail=f"No elements found in state '{state}'")
        for element in elements:
            element["_id"] = str(element["_id"])
        return elements
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="Internal server error")


@app.get("/element/atomicNumber/{number}")
async def get_element_by_atomic_number(number: int):
    try:
        element = await db.elements.find_one({"atomic_number": str(number)})
        if not element:
            raise HTTPException(
                status_code=404, detail=f"Element with atomic number '{number}' not found")
        element["_id"] = str(element["_id"])
        return element
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="Internal server error")


@app.get("/elements/group/{group}")
async def get_elements_by_group(group: int):
    try:
        elements = await db.elements.find({"group": str(group)}).to_list(100)
        if not elements:
            raise HTTPException(
                status_code=404, detail=f"No elements found in group '{group}'")
        for element in elements:
            element["_id"] = str(element["_id"])
        return elements
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="Internal server error")


@app.get("/elements/period/{period}")
async def get_elements_by_period(period: int):
    try:
        elements = await db.elements.find({"period": str(period)}).to_list(100)
        if not elements:
            raise HTTPException(
                status_code=404, detail=f"No elements found in period '{period}'")
        for element in elements:
            element["_id"] = str(element["_id"])
        return elements
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="Internal server error")
