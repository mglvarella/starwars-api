from fastapi import APIRouter, Query
from app.services.species_service import SpeciesService

router = APIRouter()

@router.get("/")
async def get_species(
    page: int = Query(1, ge=1),
    search: str | None = Query(default=None, description="Search species by name")
):
    """
    This endpoint retrieves a paginated list of Star Wars species from the SWAPI.
    """
    params = {"page": page}
    if search:
        params["search"] = search

    return await SpeciesService.fetch_species(params)

@router.get("/{species_id}")
async def get_specie(species_id: int):
    """
    This endpoint retrieves details of a specific Star Wars species by its ID from the SWAPI.
    """
    return await SpeciesService.fetch_species_by_id(species_id)