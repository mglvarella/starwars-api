from fastapi import APIRouter, Query
from app.services.swapi_service import fetch_data

router = APIRouter()

@router.get("/")
def get_veichles(page: int = Query(1, ge=1)):
    """
    This endpoint retrieves a paginated list of Star Wars vehicles from the SWAPI.
    """
    params = {"page": page}
    data = fetch_data("vehicles", params)
    return data

@router.get("/{veichle_id}")
def get_veichle(veichle_id: int):
    """
    This endpoint retrieves details of a specific Star Wars vehicle by its ID from the SWAPI.
    """
    data = fetch_data(f"vehicles/{veichle_id}")
    return data