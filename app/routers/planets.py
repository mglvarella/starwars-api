from fastapi import APIRouter, Query
from app.services.planets_service import PlanetsService

router = APIRouter()

@router.get("/")
async def get_planets(
    page: int = Query(1, ge=1),
    search: str | None = Query(default=None, description="Search planets by name")
):
    """
    This endpoint retrieves a paginated list of Star Wars planets from the SWAPI.
    """
    params = {"page": page}
    if search:
        params["search"] = search

    return await PlanetsService.fetch_planets(params)

@router.get("/{planet_id}")
async def get_planet(planet_id: int):
    """
    This endpoint retrieves details of a specific Star Wars planet by its ID from the SWAPI.
    """
    return await PlanetsService.fetch_planet_by_id(planet_id)