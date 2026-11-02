import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List, Union, TypeVar, Generic

app = FastAPI()

T = TypeVar('T')

class GenericItem(BaseModel, Generic[T]):
    name: str
    content: T

@app.post("/generic_items/")
def create_item(item: GenericItem[int]):
    return {"item": item.model_dump()}

if __name__ == "__main__":
    uvicorn.run("04_generic_models:app", host="0.0.0.0", port=8000, reload=True)
