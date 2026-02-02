import httpx

BASE_URL = "https://swapi.dev/api"

class SwapiClient:
    _client = None

    @classmethod
    async def get_client(cls):
        if cls._client is None or cls._client.is_closed:
            cls._client = httpx.AsyncClient(timeout=10)
        return cls._client

    @staticmethod
    async def fetch(endpoint: str, params: dict | None = None):
        client = await SwapiClient.get_client()
        try:
            response = await client.get(
                f"{BASE_URL}/{endpoint}/",
                params=params
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            raise RuntimeError(f"Error fetching data from SWAPI: {e}")

async def fetch_data(endpoint: str, params: dict | None = None):
    return await SwapiClient.fetch(endpoint, params)
