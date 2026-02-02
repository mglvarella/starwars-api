from app.clients.swapi_client import fetch_data

class PlanetsService:
    @staticmethod
    def fetch_planets(params: dict | None = None):
        return fetch_data("planets", params)

    @staticmethod
    def fetch_planet_by_id(planet_id: int):
        return fetch_data(f"planets/{planet_id}")
