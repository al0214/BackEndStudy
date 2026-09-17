import csv
import io
from pathlib import Path
import uvicorn

from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

def csv_streamer():
    data = [["name", "age"], ['alice', 32], ["bob", 29]]
    output = io.StringIO()
    writer = csv.writer(output)
    for row in data:
        writer.writerow(row)
        yield output.getvalue() # 여기에서 스트리밍 응답을 사용하면, 중간 결과를 응답해줄 수 있음
        output.flush()
        output.truncate(0)
        output.seek(0)

@app.get("/csv")
def get_csv():
    return StreamingResponse(
        csv_streamer(),
        headers={"Content-Type": "text/csv"}
    )

# 스트리밍 응답 기본 문법
def data_generator():
    for i in range(100):
        yield f"data chunk {i}\n"

@app.get("/stream")
def stream_data():
    generator = data_generator()
    return StreamingResponse(generator, media_type="text/plain")


if __name__=="__main__":
    uvicorn.run(f"{Path(__file__).stem}:app", host="0.0.0.0", port=8000, reload=True)