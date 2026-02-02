from fastapi import APIRouter, Query
from app.services.starships_service import StarshipsService

router = APIRouter()

@router.get("/")
def get_starships(
    page: int = Query(1, ge=1),
    search: str | None = Query(default=None, description="Search starships by name")
):
    """
    This endpoint retrieves a paginated list of Star Wars starships from the SWAPI.
    """
    params = {"page": page}
    if search:
        params["search"] = search

    return StarshipsService.fetch_starships(params)

@router.get("/{starship_id}")
def get_starship(starship_id: int):
    """
    This endpoint retrieves details of a specific Star Wars starship by its ID from the SWAPI.
    """
    return StarshipsService.fetch_starship_by_id(starship_id)