import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
def read_item(item_id:int) -> dict:
    return {"item_id" : item_id}

@app.get("/users/{user_id}/items/{item_name}")
def read_user_item(user_id:int, item_name:str) -> dict:
    return {
        "user_id": user_id, "item_name": item_name
    }

@app.get("/items/")
def read_items(skip, limit):
    return {"skip": skip, "limit": limit}

@app.get("/itemss/")
def read_items(skip = 0, limit = 10):
    return {"skip": skip, "limit": limit}

@app.get("/getdata/")
def read_items(data:str = "funcoding"):
    return {"data": data}



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)