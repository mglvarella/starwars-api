from app.clients.swapi_client import fetch_data, fetch_all_data, SwapiClient
from app.utils.ordering import Ordering
from app.utils.pagination import Pagination
import asyncio

class FilmsService:
    @staticmethod
    async def fetch_films(params: dict | None = None, ordering_params: dict = None):
        has_ordering = ordering_params and ordering_params.get("order_by")
        
        if has_ordering:
            all_results = await fetch_all_data("films", params)
            
            all_results = Ordering.sort_results(
                all_results,
                ordering_params.get("order_by"),
                ordering_params.get("order_direction", "asc")
            )
            
            page = params.get("page", 1) if params else 1
            return Pagination.paginate(all_results, page)
        
        return await fetch_data("films", params)

    @staticmethod
    async def fetch_film_by_id(film_id: int):
        return await fetch_data(f"films/{film_id}")

    @staticmethod
    async def fetch_film_people(film_id: int, ordering_params: dict = None):
        film = await fetch_data(f"films/{film_id}")
        character_urls = film.get("characters", [])
        
        tasks = [SwapiClient.fetch_url(url) for url in character_urls]
        people = await asyncio.gather(*tasks)
        
        if ordering_params and ordering_params.get("order_by"):
            people = Ordering.sort_results(
                list(people),
                ordering_params.get("order_by"),
                ordering_params.get("order_direction", "asc")
            )
        
        return {
            "count": len(people),
            "film": film.get("title"),
            "results": list(people)
        }