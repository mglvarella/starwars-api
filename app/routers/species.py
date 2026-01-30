from fastapi import APIRouter, Query
from app.services.swapi_service import fetch_data

router = APIRouter()

@router.get("/")
def get_species(page: int = Query(1, ge=1, description="Page number for pagination")):
    """
    Retrieve a list of species from the SWAPI.
    """
    params = {"page": page}
    data = fetch_data("species", params)
    return data

@router.get("/{species_id}")
def get_species_by_id(species_id: int):
    """
    Retrieve details of a specific species by its ID from the SWAPI.
    """
    data = fetch_data(f"species/{species_id}")
    return data