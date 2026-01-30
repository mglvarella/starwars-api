from fastapi import APIRouter, Query
from app.services.swapi_service import fetch_data

router = APIRouter()

@router.get("/")
def get_films(
    page: int = Query(1, ge=1),
    search: str | None = Query(default= None, description="Search films by title")
    ):
    """
    This endpoint retrieves a paginated list of Star Wars films from the SWAPI.
    """
    params = {"page": page}
    
    if search:
        params["search"] = search
    
    data = fetch_data("films", params)
    return data


@router.get("/{film_id}")
def get_film(film_id: int):
    """
    This endpoint retrieves details of a specific Star Wars film by its ID from the SWAPI.
    """
    data = fetch_data(f"films/{film_id}")
    return data