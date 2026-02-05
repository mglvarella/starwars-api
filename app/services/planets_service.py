from app.clients.swapi_client import fetch_data
from app.utils.ordering import Ordering

class PlanetsService:
    @staticmethod
    async def fetch_planets(params: dict | None = None, ordering_params: dict = None):
        response = await fetch_data("planets", params)
        if ordering_params:
            response = Ordering.apply_ordering(
                response,
                ordering_params.get("order_by"),
                ordering_params.get("order_direction", "asc")
            )
        return response

    @staticmethod
    async def fetch_planet_by_id(planet_id: int):
        return await fetch_data(f"planets/{planet_id}")
