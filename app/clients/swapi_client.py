import requests

BASE_URL = "https://swapi.dev/api"

class SwapiClient:
    @staticmethod
    def fetch(endpoint: str, params: dict | None = None):
        try:
            response = requests.get(
                f"{BASE_URL}/{endpoint}/",
                params=params,
                timeout=10
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise RuntimeError(f"Error fetching data from SWAPI: {e}")

def fetch_data(endpoint: str, params: dict | None = None):
    return SwapiClient.fetch(endpoint, params)
