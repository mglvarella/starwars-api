from app.clients.swapi_client import fetch_data
from app.services.filters.people_filters import PeopleFilters
from app.utils.ordering import Ordering

class PeopleService:
    @staticmethod
    async def fetch_people(default_params: dict, personalized_params: dict, ordering_params: dict = None):
        people = await fetch_data("people", default_params)
        if personalized_params:
            people = PeopleFilters.define_filters(people, personalized_params)
        if ordering_params:
            people = Ordering.apply_ordering(
                people, 
                ordering_params.get("order_by"), 
                ordering_params.get("order_direction", "asc")
            )
        return people         

    @staticmethod
    async def fetch_person_by_id(person_id: int):
        return await fetch_data(f"people/{person_id}")