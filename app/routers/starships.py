from fastapi import APIRouter, HTTPException, Query
from pydantic_core import ValidationError
from app.services.starships_service import StarshipsService

router = APIRouter()

@router.get("/")
async def get_starships(
    page: int = Query(1, ge=1),
    search: str | None = Query(default=None, description="Search starships by name"),
    max_speed: int | None = Query(default=None, description="Filter starships by maximum speed")
):
    """
    This endpoint retrieves a paginated list of Star Wars starships from the SWAPI.
    """
    params = {
        "page": page,
        "search": search,
        "max_speed": max_speed
        }
    
    try:
        return await StarshipsService.fetch_starships(params)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{starship_id}")
async def get_starship(starship_id: int):
    """
    This endpoint retrieves details of a specific Star Wars starship by its ID from the SWAPI.
    """
    return await StarshipsService.fetch_starship_by_id(starship_id)