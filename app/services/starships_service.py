from app.clients.swapi_client import fetch_data
from app.services.filters.starships_filters import StarshipsFilters
from app.utils.ordering import Ordering

class StarshipsService:
    @staticmethod
    async def fetch_starships(params: dict, ordering_params: dict = None):
        response = await fetch_data("starships", params)
        response = StarshipsFilters.define_filters(response, params)
        if ordering_params:
            response = Ordering.apply_ordering(
                response,
                ordering_params.get("order_by"),
                ordering_params.get("order_direction", "asc")
            )
        return response

    @staticmethod
    async def fetch_starship_by_id(starship_id: int):
        return await fetch_data(f"starships/{starship_id}")
