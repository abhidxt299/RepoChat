from fastapi import FastAPI
import uvicorn as uv

app = FastAPI()
@app.get("/hello")

def read_root():
    return {
        "message": "Hello, World!"
    }

if __name__ == "__main__":
    uv.run(app)