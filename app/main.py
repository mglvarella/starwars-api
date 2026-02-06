from fastapi import FastAPI, Depends
from app.routers import films, people, planets, species, starships, vehicles
from app.utils.security import get_api_key

app = FastAPI(
    title="Star Wars API - PowerOfData",
    redirect_slashes=True
)

api_key_dependency = [Depends(get_api_key)]

app.include_router(films.router, prefix="/films", tags=["films"], dependencies=api_key_dependency)
app.include_router(species.router, prefix="/species", tags=["species"], dependencies=api_key_dependency)
app.include_router(people.router, prefix="/people", tags=["people"], dependencies=api_key_dependency)
app.include_router(planets.router, prefix="/planets", tags=["planets"], dependencies=api_key_dependency)
app.include_router(starships.router, prefix="/starships", tags=["starships"], dependencies=api_key_dependency)
app.include_router(vehicles.router, prefix="/vehicles", tags=["vehicles"], dependencies=api_key_dependency)