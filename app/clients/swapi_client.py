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

    @staticmethod
    async def fetch_all(endpoint: str, params: dict | None = None):
        client = await SwapiClient.get_client()
        all_results = []
        clean_params = {k: v for k, v in (params or {}).items() if k not in ["page"]}
        clean_params["page"] = 1
        
        try:
            while True:
                response = await client.get(
                    f"{BASE_URL}/{endpoint}/",
                    params=clean_params
                )
                response.raise_for_status()
                data = response.json()
                all_results.extend(data.get("results", []))
                
                if not data.get("next"):
                    break
                clean_params["page"] += 1
            
            return all_results
        except httpx.HTTPError as e:
            raise RuntimeError(f"Error fetching data from SWAPI: {e}")

async def fetch_data(endpoint: str, params: dict | None = None):
    return await SwapiClient.fetch(endpoint, params)

async def fetch_all_data(endpoint: str, params: dict | None = None):
    return await SwapiClient.fetch_all(endpoint, params)

