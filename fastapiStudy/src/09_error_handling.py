import uvicorn
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id == 42:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
            headers={"X-Error": "There was an error"}
        )
    return {"item_id": item_id}

if __name__ == "__main__":
    uvicorn.run("09_error_handling:app", host="0.0.0.0", port=8000, reload=True)
