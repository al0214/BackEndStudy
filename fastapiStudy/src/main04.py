import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

class Image(BaseModel):
    url: str
    name: str

class Item(BaseModel):
    name: str
    description: str
    image: Image

@app.post("/items/")
def create_item(item: Item):
    return {
        "item" : item.model_dump()
    }

if __name__ == "__main__":
    uvicorn.run("main04:app", host="0.0.0.0", port=8000, reload=True)