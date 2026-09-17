import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse, HTMLResponse, PlainTextResponse, RedirectResponse
app = FastAPI()

@app.get("/json", response_class=JSONResponse)
def read_json():
    return {
        "msg": "This is JSON"
    }

@app.get("/html", response_class=HTMLResponse)
def read_html():
    return "<h1>This is HTML</h1>"

@app.get("/plain", response_class=PlainTextResponse)
def read_plain():
    return "This is Plain Text"

@app.get("/redirect")
def read_redirect():
    return RedirectResponse(url="/html")

if __name__ == "__main__":
    uvicorn.run("06_custom_responses:app", host="0.0.0.0", port=8000, reload=True)
