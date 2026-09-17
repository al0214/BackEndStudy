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
    uvicorn.run("05_response_model:app", host="0.0.0.0", port=8000, reload=True)
