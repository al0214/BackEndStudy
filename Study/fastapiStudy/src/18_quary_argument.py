from pathlib import Path

import uvicorn

from fastapi import FastAPI, APIRouter, Depends, HTTPException
from fastapi.middleware.trustedhost import TrustedHostMiddleware



app = FastAPI()

# 두개으 쿼리 매개변수를 받습니다.
# @app.get("/items/")
# def read_item(skip: int = 0, limit: int = 10):
#     return {
#         "skip": skip,
#         "limit": limit
#     }


@app.get("/items/int/{item_id:int}")
def read_item_with_type(item_id):
    return {"item_id": item_id}

@app.get("/items/{item_id}")
def read_item_with_type(item_id:int):
    return {"item_id": item_id}

@app.get("/files/{sub_path:path}")
def read_file(sub_path: str):
    return {
        "sub_path": sub_path
    }

if __name__=="__main__":
    uvicorn.run(f"{Path(__file__).stem}:app", host="0.0.0.0", port=8000, reload=True)