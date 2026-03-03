from fastapi import FastAPI, Depends, Query, Path
import uvicorn as uv
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()

class PathParams (BaseModel):
    name: str

class QueryParams (BaseModel):
    query: str = Field(alias="q")
    limit: int = 10

@app.get("/greet/{name}")
async def root(params: Annotated[PathParams, Path()]):
    return {
        "message": f"Hello, {params.name.title()}!"
    }

@app.get("/search")
async def search(query_params: Annotated[QueryParams, Depends()]):
    return {
        "query": query_params.query, 
        "limit": query_params.limit,
        "results": []
    }

if __name__ == "__main__":
    uv.run(app)

