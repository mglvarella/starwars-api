from app.clients.swapi_client import fetch_data, fetch_all_data
from app.utils.ordering import Ordering
from app.utils.pagination import Pagination

class PlanetsService:
    @staticmethod
    async def fetch_planets(params: dict | None = None, ordering_params: dict = None):
        has_ordering = ordering_params and ordering_params.get("order_by")
        
        if has_ordering:
            all_results = await fetch_all_data("planets", params)
            
            all_results = Ordering.sort_results(
                all_results,
                ordering_params.get("order_by"),
                ordering_params.get("order_direction", "asc")
            )
            
            page = params.get("page", 1) if params else 1
            return Pagination.paginate(all_results, page)
        
        return await fetch_data("planets", params)

    @staticmethod
    async def fetch_planet_by_id(planet_id: int):
        return await fetch_data(f"planets/{planet_id}")

