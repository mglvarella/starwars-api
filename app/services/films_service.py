from app.clients.swapi_client import fetch_data
from app.utils.ordering import Ordering

class FilmsService:
    @staticmethod
    async def fetch_films(params: dict | None = None, ordering_params: dict = None):
        response = await fetch_data("films", params)
        if ordering_params:
            response = Ordering.apply_ordering(
                response,
                ordering_params.get("order_by"),
                ordering_params.get("order_direction", "asc")
            )
        return response

    @staticmethod
    async def fetch_film_by_id(film_id: int):
        return await fetch_data(f"films/{film_id}")