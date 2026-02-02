from fastapi import APIRouter, Query
from app.services.films_service import FilmsService

router = APIRouter()

@router.get("/")
def get_films(
    page: int = Query(1, ge=1),
    search: str | None = Query(default=None, description="Search films by title")
):
    """
    This endpoint retrieves a paginated list of Star Wars films from the SWAPI.
    """
    params = {"page": page}
    if search:
        params["search"] = search
    
    return FilmsService.fetch_films(params)

@router.get("/{film_id}")
def get_film(film_id: int):
    """
    This endpoint retrieves details of a specific Star Wars film by its ID from the SWAPI.
    """
    return FilmsService.fetch_film_by_id(film_id)