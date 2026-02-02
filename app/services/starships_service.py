from app.clients.swapi_client import fetch_data

class StarshipsService:
    @staticmethod
    def fetch_starships(params: dict | None = None):
        return fetch_data("starships", params)

    @staticmethod
    def fetch_starship_by_id(starship_id: int):
        return fetch_data(f"starships/{starship_id}")
