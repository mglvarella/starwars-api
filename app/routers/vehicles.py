from fastapi import APIRouter, Query
from app.services.vehicles_service import VehiclesService

router = APIRouter()

@router.get("/")
async def get_vehicles(
    page: int = Query(1, ge=1),
    search: str | None = Query(default=None, description="Search vehicles by name"),
    order_by: str | None = Query(default=None, description="Field to order results by (e.g., name, cost_in_credits, length)"),
    order_direction: str = Query(default="asc", description="Order direction: 'asc' or 'desc'")
):
    """
    This endpoint retrieves a paginated list of Star Wars vehicles from the SWAPI with optional ordering.
    """
    params = {"page": page}
    if search:
        params["search"] = search

    ordering_params = {
        "order_by": order_by,
        "order_direction": order_direction
    }

    return await VehiclesService.fetch_vehicles(params, ordering_params)

@router.get("/{vehicle_id}")
async def get_vehicle(vehicle_id: int):
    """
    This endpoint retrieves details of a specific Star Wars vehicle by its ID from the SWAPI.
    """
    return await VehiclesService.fetch_vehicle_by_id(vehicle_id)