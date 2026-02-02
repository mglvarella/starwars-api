from app.clients.swapi_client import fetch_data

class SpeciesService:
    @staticmethod
    def fetch_species(params: dict | None = None):
        return fetch_data("species", params)

    @staticmethod
    def fetch_species_by_id(species_id: int):
        return fetch_data(f"species/{species_id}")
