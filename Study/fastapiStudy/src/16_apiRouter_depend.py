from http.client import HTTPException

import uvicorn
from fastapi import FastAPI, APIRouter, Depends, HTTPException
from fastapi.middleware.trustedhost import TrustedHostMiddleware

app = FastAPI()

def check_token(token: str):
    if token != "my-secret-token":
        raise HTTPException(status_code=401, detail="Unauthorized")
    return token

router = APIRouter(dependencies=[Depends(check_token)])

@router.get("/items/")
def read_items_from_router():
    return {"message": "Access granted, you can view the items."}

@app.get("/public/")
def read_public():
    return {
        "message" : "This is a public endpoint"
    }

app.include_router(router, prefix="/api")

if __name__=="__main__":
    uvicorn.run("16_apiRouter_depend:app", host="0.0.0.0", port=8000, reload=True)