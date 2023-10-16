from fastapi import FastAPI
from app.routers import travels

app = FastAPI()

app.include_router(travels.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
