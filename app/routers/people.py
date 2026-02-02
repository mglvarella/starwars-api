from fastapi import APIRouter, Query
from app.services.people_service import PeopleService

router = APIRouter()

@router.get("/")
def get_people(
    page: int = Query(1, ge=1),
    search: str | None = Query(default=None, description="Search people by name")
):
    """
    This endpoint retrieves a paginated list of Star Wars people from the SWAPI.
    """
    params = {"page": page}
    if search:
        params["search"] = search

    return PeopleService.fetch_people(params)

@router.get("/{person_id}")
def get_person(person_id: int):
    """
    This endpoint retrieves details of a specific Star Wars person by their ID from the SWAPI.
    """
    return PeopleService.fetch_person_by_id(person_id)