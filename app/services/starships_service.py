from app.clients.swapi_client import fetch_data
from app.services.filters.starships_filters import StarshipsFilters

class StarshipsService:
    @staticmethod
    async def fetch_starships(params : dict):
        
        response = await fetch_data("starships", params)
        return StarshipsFilters.define_filters(response, params)

    @staticmethod
    async def fetch_starship_by_id(starship_id: int):
        return await fetch_data(f"starships/{starship_id}")
