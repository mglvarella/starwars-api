from app.clients.swapi_client import fetch_data

class StarshipsService:
    @staticmethod
    async def fetch_starships(params: dict | None = None):
        return await fetch_data("starships", params)

    @staticmethod
    async def fetch_starship_by_id(starship_id: int):
        return await fetch_data(f"starships/{starship_id}")
