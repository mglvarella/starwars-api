from app.clients.swapi_client import fetch_data
from app.services.filters.people_filters import PeopleFilters

class PeopleService:
    @staticmethod
    async def fetch_people(params: dict):
        people = await fetch_data("people")
        if params:
            people = PeopleFilters.define_filters(people, params)
        return people         

    @staticmethod
    async def fetch_person_by_id(person_id: int):
        return await fetch_data(f"people/{person_id}")