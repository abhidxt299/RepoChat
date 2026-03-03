from fastapi import FastAPI
import uvicorn as uv
from pydantic import BaseModel

app = FastAPI()

class EchoRequest (BaseModel):
    text: str
    repeat: int

class EchoResponse (BaseModel):
    result: str
    character_count: int

@app.post("/echo", response_model = EchoResponse)
async def echo (req: EchoRequest):
    result = req.text * req.repeat
    character_count = len(result)
    return {
        "result": result,
        "character_count": character_count
    }

if __name__ == "__main__":
    uv.run(app)