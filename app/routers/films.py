from fastapi import APIRouter, Query
from app.services.films_service import FilmsService

router = APIRouter()

@router.get("/")
async def get_films(
    page: int = Query(1, ge=1),
    search: str | None = Query(default=None, description="Search films by title"),
    order_by: str | None = Query(default=None, description="Field to order results by (e.g., title, release_date, episode_id)"),
    order_direction: str = Query(default="asc", description="Order direction: 'asc' or 'desc'")
):
    """
    This endpoint retrieves a paginated list of Star Wars films from the SWAPI with optional ordering.
    """
    params = {"page": page}
    if search:
        params["search"] = search
    
    ordering_params = {
        "order_by": order_by,
        "order_direction": order_direction
    }
    
    return await FilmsService.fetch_films(params, ordering_params)

@router.get("/{film_id}")
async def get_film(film_id: int):
    """
    This endpoint retrieves details of a specific Star Wars film by its ID from the SWAPI.
    """
    return await FilmsService.fetch_film_by_id(film_id)

@router.get("/{film_id}/people")
async def get_film_people(
    film_id: int,
    order_by: str | None = Query(default=None, description="Field to order results by (e.g., name, height, mass)"),
    order_direction: str = Query(default="asc", description="Order direction: 'asc' or 'desc'")
):
    """
    This endpoint retrieves all characters from a specific Star Wars film.
    """
    ordering_params = {
        "order_by": order_by,
        "order_direction": order_direction
    }
    return await FilmsService.fetch_film_people(film_id, ordering_params)