from app.clients.swapi_client import fetch_data

class FilmsService:
    @staticmethod
    async def fetch_films(params: dict | None = None):
        return await fetch_data("films", params)

    @staticmethod
    async def fetch_film_by_id(film_id: int):
        return await fetch_data(f"films/{film_id}")