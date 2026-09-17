from pathlib import Path

import uvicorn

from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

def write_log(message: str):
    with open("./logFile/log.txt", "a") as log:
        log.write(message)

@app.get("/")
async def read_root(background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, "root endpoint was accessed")
    return {"message": "Hello World"}

if __name__=="__main__":
    uvicorn.run(f"{Path(__file__).stem}:app", host="0.0.0.0", port=8000, reload=True)