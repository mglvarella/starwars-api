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