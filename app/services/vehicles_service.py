from app.clients.swapi_client import fetch_data
from app.utils.ordering import Ordering

class VehiclesService:
    @staticmethod
    async def fetch_vehicles(params: dict | None = None, ordering_params: dict = None):
        response = await fetch_data("vehicles", params)
        if ordering_params:
            response = Ordering.apply_ordering(
                response,
                ordering_params.get("order_by"),
                ordering_params.get("order_direction", "asc")
            )
        return response

    @staticmethod
    async def fetch_vehicle_by_id(vehicle_id: int):
        return await fetch_data(f"vehicles/{vehicle_id}")
