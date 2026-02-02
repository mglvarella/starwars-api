from app.clients.swapi_client import fetch_data

class PeopleService:
    @staticmethod
    def fetch_people(params: dict | None = None):
        """
        Fetches a paginated list of people from SWAPI.
        """
        return fetch_data("people", params)

    @staticmethod
    def fetch_person_by_id(person_id: int):
        """
        Fetches details of a specific person by their ID.
        """
        return fetch_data(f"people/{person_id}")