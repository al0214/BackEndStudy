import csv
import io
from pathlib import Path
import uvicorn

from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Returned Message: {data} From Server")
    except WebSocketDisconnect:
        print("WebSocket disconnected")
        await websocket.close(code=1000)

if __name__=="__main__":
    uvicorn.run(f"{Path(__file__).stem}:app", host="0.0.0.0", port=8000, reload=True)