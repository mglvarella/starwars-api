from app.clients.swapi_client import fetch_data, fetch_all_data
from app.services.filters.starships_filters import StarshipsFilters
from app.utils.ordering import Ordering
from app.utils.pagination import Pagination

class StarshipsService:
    @staticmethod
    async def fetch_starships(params: dict, ordering_params: dict = None):
        has_custom_filters = params.get("max_speed") is not None
        has_ordering = ordering_params and ordering_params.get("order_by")
        
        if has_custom_filters or has_ordering:
            all_results = await fetch_all_data("starships", params)
            
            if has_custom_filters:
                all_results = StarshipsFilters.filter_results(all_results, params)
            
            if has_ordering:
                all_results = Ordering.sort_results(
                    all_results,
                    ordering_params.get("order_by"),
                    ordering_params.get("order_direction", "asc")
                )
            
            page = params.get("page", 1)
            return Pagination.paginate(all_results, page)
        
        return await fetch_data("starships", params)

    @staticmethod
    async def fetch_starship_by_id(starship_id: int):
        return await fetch_data(f"starships/{starship_id}")

