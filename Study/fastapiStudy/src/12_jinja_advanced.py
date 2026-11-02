import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from jinja2 import Environment, select_autoescape, FileSystemLoader

app = FastAPI()

env = Environment(
    loader=FileSystemLoader('./templates'),
    autoescape=select_autoescape(['html']),
    extensions=['jinja2.ext.do']
)

templates = Jinja2Templates(env=env)

@app.get("/do_example")
def do_example(request: Request):
    return templates.TemplateResponse(request=request, name="index06.html")

@app.get("/inherit")
def template_inherit(request:Request):
    my_text = "FastAPI와 Jinja2를 이용한 예시입니다."
    return templates.TemplateResponse(request=request, name="extends.html", context={"text": my_text})

@app.get("/multi_block")
def multi_block(request: Request):
    return templates.TemplateResponse(request=request, name="index03.html")

@app.get("/include_example")
def include_example(request: Request):
    return templates.TemplateResponse(request=request, name="index04.html")

@app.get("/import_example")
def import_example(request: Request):
    return templates.TemplateResponse(request=request, name="index05.html")

if __name__ == "__main__":
    uvicorn.run("12_jinja_advanced:app", host="0.0.0.0", port=8000, reload=True)
