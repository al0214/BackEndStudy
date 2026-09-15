import uvicorn
from fastapi import FastAPI, Query, Body

app = FastAPI()

@app.get("/items/")
def read_items(item_id: int = Query(...)):
    return {"item_id": item_id}

@app.post("/items/")
def create_item(item: dict = Body(None)):
    return {"item": item}

@app.post("/advenced_items/")
def create_advanced_item(
        item: dict = Body(
            default=None,
            example={"key": "value"},
            media_type="application/json",
            alias="item_alias",
            title="Sample Item",
            description="This is a sample item",
            deprecated=False
        )):
    return {"item": item}


if __name__ == "__main__":
    uvicorn.run("main09:app", host="0.0.0.0", port=8000, reload=True)