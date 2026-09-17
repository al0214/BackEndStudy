import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="./templates")

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse(request = request, name="main.html")

@app.get("/02/")
def read_root_01(request: Request):
    return templates.TemplateResponse(request=request, name="index02.html", context={"name":"John"})

@app.get("/safe")
def read_root_safe(request:Request):
    my_variable_with_html = "<h1>Hello, FastAPI!</h1>"
    return templates.TemplateResponse(request=request, name="index_with_safe.html", context={"my_variable_with_html": my_variable_with_html})

@app.get("/user/{username}")
def get_user(request: Request, username: str):
    return templates.TemplateResponse(request=request, name="index01.html", context={"username": username})

@app.get("/greet")
def get_user(request: Request, time_of_day: str):
    return templates.TemplateResponse(request=request, name="indexIf.html", context={"time_of_day": time_of_day})

@app.get("/items")
def read_items(request: Request):
    my_items = ["apple", "banana", "cherry"]
    return templates.TemplateResponse(request=request, name="indexFor.html", context={"items": my_items})

@app.get("/dynamic_items/")
def dynamic_items(request:Request, item_list: str = ""):
    items = item_list.split(",")
    return templates.TemplateResponse(request=request, name="indexList.html", context={"items": items})

if __name__ == "__main__":
    uvicorn.run("10_jinja_templates:app", host="0.0.0.0", port=8000, reload=True)
