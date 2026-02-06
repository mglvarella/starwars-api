from app.utils.cast import safe_int

class StarshipsFilters:
    @staticmethod
    def define_filters(response: dict, params: dict):
        starships = response["results"]

        maximum_speed = params.get("max_speed")
        if maximum_speed is not None:
            starships = StarshipsFilters.filter_by_maximum_speed(
                starships, maximum_speed
            )

        response["results"] = starships
        return response

    @staticmethod
    def filter_results(results: list, params: dict) -> list:
        maximum_speed = params.get("max_speed")
        if maximum_speed is not None:
            results = StarshipsFilters.filter_by_maximum_speed(results, maximum_speed)
        return results

    @staticmethod
    def filter_by_maximum_speed(starships: list, maximum_speed) -> list:
        max_speed = safe_int(maximum_speed)
        if max_speed is None:
            return starships
        
        result = [ship for ship in starships 
                  if safe_int(ship.get("max_atmosphering_speed")) is not None 
                  and safe_int(ship.get("max_atmosphering_speed")) <= max_speed]

        return result