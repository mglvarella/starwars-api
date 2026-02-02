from app.clients.swapi_client import fetch_data

class VehiclesService:
    @staticmethod
    def fetch_vehicles(params: dict | None = None):
        return fetch_data("vehicles", params)

    @staticmethod
    def fetch_vehicle_by_id(vehicle_id: int):
        return fetch_data(f"vehicles/{vehicle_id}")
