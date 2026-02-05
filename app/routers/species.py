from fastapi import APIRouter, Query
from app.services.species_service import SpeciesService

router = APIRouter()

@router.get("/")
async def get_species(
    page: int = Query(1, ge=1),
    search: str | None = Query(default=None, description="Search species by name"),
    order_by: str | None = Query(default=None, description="Field to order results by (e.g., name, classification, average_height)"),
    order_direction: str = Query(default="asc", description="Order direction: 'asc' or 'desc'")
):
    """
    This endpoint retrieves a paginated list of Star Wars species from the SWAPI with optional ordering.
    """
    params = {"page": page}
    if search:
        params["search"] = search

    ordering_params = {
        "order_by": order_by,
        "order_direction": order_direction
    }

    return await SpeciesService.fetch_species(params, ordering_params)

@router.get("/{species_id}")
async def get_specie(species_id: int):
    """
    This endpoint retrieves details of a specific Star Wars species by its ID from the SWAPI.
    """
    return await SpeciesService.fetch_species_by_id(species_id)