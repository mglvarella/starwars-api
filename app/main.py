from fastapi import FastAPI, Depends
from app.routers import films, people, planets, species, starships, vehicles
from app.utils.security import get_api_key

app = FastAPI(
    title="Star Wars API - PowerOfData",
    dependencies=[Depends(get_api_key)],
    redirect_slashes=True
)

app.include_router(films.router, prefix="/films", tags=["films"])
app.include_router(species.router, prefix="/species", tags=["species"])
app.include_router(people.router, prefix="/people", tags=["people"])
app.include_router(planets.router, prefix="/planets", tags=["planets"])
app.include_router(starships.router, prefix="/starships", tags=["starships"])
app.include_router(vehicles.router, prefix="/vehicles", tags=["vehicles"])