from fastapi import FastAPI
from app.routers import films

app = FastAPI()

app.include_router(films.router, prefix="/films", tags=["films"])
