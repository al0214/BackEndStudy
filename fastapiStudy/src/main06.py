import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.get("/item/", response_model=Item)
def get_item():
    return {"name": "milk", "price": 3.5}

if __name__ == "__main__":
    uvicorn.run("main06:app", host="0.0.0.0", port=8000, reload=True)

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#
# def get_item_from_db(id):
#     return {
#         "name": "Simple Item",
#         "description": "A simple item description",
#         "price": 50.0,
#         "dis_price": 45.0
#     }
#
# @app.get("/items/{item_id}", response_model=Item)
# def read_item(item_id: int):
#     item = get_item_from_db(item_id)
#     return item


