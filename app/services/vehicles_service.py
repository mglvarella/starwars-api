from app.clients.swapi_client import fetch_data

class VehiclesService:
    @staticmethod
    async def fetch_vehicles(params: dict | None = None):
        return await fetch_data("vehicles", params)

    @staticmethod
    async def fetch_vehicle_by_id(vehicle_id: int):
        return await fetch_data(f"vehicles/{vehicle_id}")
