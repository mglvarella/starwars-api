from fastapi import APIRouter, Query, HTTPException
from app.services.people_service import PeopleService
from pydantic import ValidationError

router = APIRouter()

@router.get("/")
async def get_people(
    page: int = Query(1, description="Page number"),
    search: str | None = Query(default=None, description="Search people by name"),
    gender: str | None = Query(default=None, description="Filter by gender (male, female, etc.)"),
    order_by: str | None = Query(default=None, description="Field to order results by (e.g., name, height, mass)"),
    order_direction: str = Query(default="asc", description="Order direction: 'asc' or 'desc'")
):
    """
    This endpoint retrieves a list of Star Wars people with personalized filters and ordering.
    Validation is handled at the service layer.
    """
    default_params = {
        "page": page,
        "search": search
    }

    personalized_params = {
        "gender": gender
    }
    
    ordering_params = {
        "order_by": order_by,
        "order_direction": order_direction
    }
    
    try:
        return await PeopleService.fetch_people(default_params, personalized_params, ordering_params)
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