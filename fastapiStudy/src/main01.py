import uvicorn
from fastapi import FastAPI, Query
from typing import List, Dict

app = FastAPI()

@app.get("/itmes/")
def read_items(q: List[int] = Query([])):
    return {"q": q}

@app.post("/create-item/")
def create_item(item: Dict[str, int]):
    return item

if __name__ == "__main__":
    uvicorn.run("main01:app", host="0.0.0.0", port=8000, reload=True)