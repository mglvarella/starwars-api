from fastapi import APIRouter, Query
from app.services.swapi_service import fetch_data

router = APIRouter()

@router.get("/")
def get_species(page: int = Query(1, ge=1, description="Page number for pagination")):
    """
    Retrieve a list of species from the Star Wars API (SWAPI).
    """
    params = {"page": page}
    data = fetch_data("species", params)
    return data