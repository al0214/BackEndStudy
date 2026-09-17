import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
router = APIRouter()

@router.get("/items/")
def read_items():
    return {"items": "apple"}

@router.get("/users")
def read_users():
    return {"user": "John"}

app.include_router(router, prefix="/api/v1", tags=["items"])


if __name__=="__main__":
    uvicorn.run("14_apiRouter_basic:app", host="0.0.0.0", port=8000, reload=True)