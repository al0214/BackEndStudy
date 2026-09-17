import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi.middleware.trustedhost import TrustedHostMiddleware

app = FastAPI()

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=['example.com', "localhost", "127.0.0.1"]
)

router = APIRouter()

@router.get("/items/")
def read_items_from_router():
    return {"message": "You are accessing the API from an allowed host via router."}

app.include_router(router, prefix="/api")

@app.get("/hello/")
def read_users():
    return {"message": "Hello World"}




if __name__=="__main__":
    uvicorn.run("15_apiRouter_middleware:app", host="0.0.0.0", port=8000, reload=True)