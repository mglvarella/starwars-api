from app.clients.swapi_client import fetch_data

class PlanetsService:
    @staticmethod
    async def fetch_planets(params: dict | None = None):
        return await fetch_data("planets", params)

    @staticmethod
    async def fetch_planet_by_id(planet_id: int):
        return await fetch_data(f"planets/{planet_id}")
