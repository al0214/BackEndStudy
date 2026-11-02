import uvicorn
from fastapi import FastAPI, Query
from typing import List, Dict

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello"}

@app.get("/items/{item_id}")
def read_item(item_id:int):
    return {"item_id" : item_id}

@app.post("/items/")
def create_item(item: dict):
    return {"item": item}

@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10):
    return {
        "skip": skip, "limit": limit
    }

@app.put("/items/{item_id}")
def update_item(item_id: int, item: dict):
    return {
        "item_id": item_id,
        "updated_item": item
    }

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {
        "message": f"Item {item_id} has been deleted"
    }

if __name__ == "__main__":
    uvicorn.run("01_crud_basics:app", host="0.0.0.0", port=8000, reload=True)
