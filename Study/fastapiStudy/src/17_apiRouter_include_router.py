from http.client import HTTPException

import uvicorn
from fastapi import FastAPI, APIRouter, Depends, HTTPException
from fastapi.middleware.trustedhost import TrustedHostMiddleware

app = FastAPI()

def common_dependency():
    return "This is a common dependency"

parent_router = APIRouter(
    prefix="/parent",
    tags=["parent"],
    dependencies=[Depends(common_dependency)]
)

@parent_router.get("/item")
def read_parent_item():
    return {
        "message" : "This is an item from the parent router"
    }

child_router = APIRouter()

@child_router.get("/item")
def read_child_item(common: str = Depends(common_dependency)):
    return {
        "message" : "This is an item from the child router",
        "common" : common
    }

parent_router.include_router(child_router, prefix="/child")

app.include_router(parent_router)

if __name__=="__main__":
    uvicorn.run("17_apiRouter_include_router:app", host="0.0.0.0", port=8000, reload=True)