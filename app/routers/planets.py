from fastapi import APIRouter, Query
from app.services.swapi_service import fetch_data

router = APIRouter()

@router.get("/")
def get_planets(page: int = Query(1, ge=1)):
    """
    This endpoint retrieves a paginated list of Star Wars planets from the SWAPI.
    """
    params = {"page": page}
    data = fetch_data("planets", params)
    return data

@router.get("/{planet_id}")
def get_planet(planet_id: int):
    """
    This endpoint retrieves details of a specific Star Wars planet by its ID from the SWAPI.
    """
    data = fetch_data(f"planets/{planet_id}")
    return data