from fastapi import APIRouter, Query
from app.services.vehicles_service import VehiclesService

router = APIRouter()

@router.get("/")
def get_vehicles(
    page: int = Query(1, ge=1),
    search: str | None = Query(default=None, description="Search vehicles by name")
):
    """
    This endpoint retrieves a paginated list of Star Wars vehicles from the SWAPI.
    """
    params = {"page": page}
    if search:
        params["search"] = search

    return VehiclesService.fetch_vehicles(params)

@router.get("/{vehicle_id}")
def get_vehicle(vehicle_id: int):
    """
    This endpoint retrieves details of a specific Star Wars vehicle by its ID from the SWAPI.
    """
    return VehiclesService.fetch_vehicle_by_id(vehicle_id)