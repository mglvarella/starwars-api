from app.clients.swapi_client import fetch_data

class PeopleService:
    @staticmethod
    async def fetch_people(params: dict):        
        data = await fetch_data("people", params)           
        return data

    @staticmethod
    async def fetch_person_by_id(person_id: int):
        return await fetch_data(f"people/{person_id}")