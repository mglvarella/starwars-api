from fastapi import FastAPI
from app.routers import films, people, planets, species, starships, veichles

app = FastAPI()

app.include_router(films.router, prefix="/films", tags=["films"])
app.include_router(species.router, prefix="/species", tags=["species"])
app.include_router(people.router, prefix="/people", tags=["people"])
app.include_router(planets.router, prefix="/planets", tags=["planets"])
app.include_router(starships.router, prefix="/starships", tags=["starships"])
app.include_router(veichles.router, prefix="/vehicles", tags=["vehicles"])