from fastapi import APIRouter, Query, HTTPException
from app.services.people_service import PeopleService
from pydantic import ValidationError

router = APIRouter()

@router.get("/")
async def get_people(
    page: int = Query(1, description="Page number"),
    search: str | None = Query(default=None, description="Search people by name"),
    gender: str | None = Query(default=None, description="Filter by gender (male, female, etc.)"),
    eye_color: str | None = Query(default=None, description="Filter by eye color"),
    hair_color: str | None = Query(default=None, description="Filter by hair color")
):
    """
    This endpoint retrieves a list of Star Wars people with personalized filters.
    Validation is handled at the service layer.
    """
    params = {
        "page": page,
        "search": search,
        "gender": gender,
        "eye_color": eye_color,
        "hair_color": hair_color
    }
    
    try:
        return await PeopleService.fetch_people(params)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{person_id}")
async def get_person(person_id: int):
    """
    This endpoint retrieves details of a specific Star Wars person by their ID from the SWAPI.
    """
    return await PeopleService.fetch_person_by_id(person_id)