from app.clients.swapi_client import fetch_data

class SpeciesService:
    @staticmethod
    async def fetch_species(params: dict | None = None):
        return await fetch_data("species", params)

    @staticmethod
    async def fetch_species_by_id(species_id: int):
        return await fetch_data(f"species/{species_id}")
