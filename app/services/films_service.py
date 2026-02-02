from app.clients.swapi_client import fetch_data

class FilmsService:
    @staticmethod
    def fetch_films(params: dict | None = None):
        return fetch_data("films", params)

    @staticmethod
    def fetch_film_by_id(film_id: int):
        return fetch_data(f"films/{film_id}")