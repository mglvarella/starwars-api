from app.clients.swapi_client import fetch_data, fetch_all_data
from app.services.filters.people_filters import PeopleFilters
from app.utils.ordering import Ordering
from app.utils.pagination import Pagination

class PeopleService:
    @staticmethod
    async def fetch_people(default_params: dict, personalized_params: dict, ordering_params: dict = None):
        has_custom_filters = any(v for v in personalized_params.values()) if personalized_params else False
        has_ordering = ordering_params and ordering_params.get("order_by")
        
        if has_custom_filters or has_ordering:
            all_results = await fetch_all_data("people", default_params)
            
            if has_custom_filters:
                all_results = PeopleFilters.filter_results(all_results, personalized_params)
            
            if has_ordering:
                all_results = Ordering.sort_results(
                    all_results,
                    ordering_params.get("order_by"),
                    ordering_params.get("order_direction", "asc")
                )
            
            page = default_params.get("page", 1)
            return Pagination.paginate(all_results, page)
        
        return await fetch_data("people", default_params)

    @staticmethod
    async def fetch_person_by_id(person_id: int):
        return await fetch_data(f"people/{person_id}")