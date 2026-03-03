from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn as uv

from pydantic import BaseModel

app = FastAPI()

class EchoRequest (BaseModel):
    text: str
    repeat: int

class EchoResponse (BaseModel):
    result: str
    character_count: int

origin = [
    "http://localhost:8000",
    "http://127.0.0.1:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origin,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.post("/echo")
async def echo_error_messages(req: EchoRequest):
    if req.repeat > 10:
        raise HTTPException(
            status_code = 400,
            detail = "Repeat count cannot exceed 10."
        )
    if not req.text:
        raise HTTPException(
            status_code =  400,
            detail = "Text cannot be empty."
        )

    result = req.text * req.repeat
    character_count = len(result)

    return EchoResponse(
        result = result,
        character_count = character_count
    )

if __name__ == "__main__":
    uv.run(app)