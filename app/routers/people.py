from fastapi import APIRouter, Query
from app.services.swapi_service import fetch_data

router = APIRouter()

@router.get("/")
def get_people(page: int = Query(1, ge=1)):
    """
    This endpoint retrieves a paginated list of Star Wars people from the SWAPI.
    """
    params = {"page": page}
    data = fetch_data("people", params)
    return data

@router.get("/{person_id}")
def get_person(person_id: int):
    """
    This endpoint retrieves details of a specific Star Wars person by their ID from the SWAPI.
    """
    data = fetch_data(f"people/{person_id}")
    return data