import httpx

BASE_URL = "https://swapi.dev/api"

class SwapiClient:
    @staticmethod
    async def fetch(endpoint: str, params: dict | None = None):
        async with httpx.AsyncClient(timeout=30) as client:
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
        all_results = []
        clean_params = {k: v for k, v in (params or {}).items() if k not in ["page"]}
        clean_params["page"] = 1
        
        async with httpx.AsyncClient(timeout=30) as client:
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

    @staticmethod
    async def fetch_url(url: str):
        async with httpx.AsyncClient(timeout=30) as client:
            try:
                response = await client.get(url)
                response.raise_for_status()
                return response.json()
            except httpx.HTTPError as e:
                raise RuntimeError(f"Error fetching data from SWAPI: {e}")

async def fetch_data(endpoint: str, params: dict | None = None):
    return await SwapiClient.fetch(endpoint, params)

async def fetch_all_data(endpoint: str, params: dict | None = None):
    return await SwapiClient.fetch_all(endpoint, params)



