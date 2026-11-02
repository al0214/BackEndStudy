import uvicorn
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/users/")
def read_users(q: str = Query(None, max_length=50, deprecated=True)):
    return {"q": q}

@app.get("/items/")
def read_items(internal_query: str = Query(None, alias="search")):
    return {
        "query_handled": internal_query
    }

@app.get("/info/")
def read_info(info: str = Query(None, description="정보를 입력해 주세요.")):
    return {
        "info" : info
    }

if __name__ == "__main__":
    uvicorn.run("07_query_params:app", host="0.0.0.0", port=8000, reload=True)
