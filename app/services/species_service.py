from app.clients.swapi_client import fetch_data
from app.utils.ordering import Ordering

class SpeciesService:
    @staticmethod
    async def fetch_species(params: dict | None = None, ordering_params: dict = None):
        response = await fetch_data("species", params)
        if ordering_params:
            response = Ordering.apply_ordering(
                response,
                ordering_params.get("order_by"),
                ordering_params.get("order_direction", "asc")
            )
        return response

    @staticmethod
    async def fetch_species_by_id(species_id: int):
        return await fetch_data(f"species/{species_id}")
