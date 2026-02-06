from typing import Literal

class Ordering:

    @staticmethod
    def apply_ordering(
        response: dict, 
        order_by: str | None, 
        order_direction: Literal["asc", "desc"] = "asc"
    ) -> dict:
        if not order_by:
            return response
        
        results = response.get("results", [])
        
        if not results:
            return response
        
        if order_by not in results[0]:
            return response
        
        reverse = order_direction.lower() == "desc"
        
        sorted_results = sorted(
            results,
            key=lambda x: Ordering._get_sort_key(x.get(order_by)),
            reverse=reverse
        )
        
        response["results"] = sorted_results
        return response

    @staticmethod
    def sort_results(
        results: list,
        order_by: str | None,
        order_direction: Literal["asc", "desc"] = "asc"
    ) -> list:
        if not order_by or not results:
            return results
        
        if order_by not in results[0]:
            return results
        
        reverse = order_direction.lower() == "desc"
        
        return sorted(
            results,
            key=lambda x: Ordering._get_sort_key(x.get(order_by)),
            reverse=reverse
        )

    @staticmethod
    def _get_sort_key(value):
        if value is None or str(value).lower() in ("unknown", "n/a", "none"):
            return (1, "")

        try:
            cleaned = str(value).replace(",", "")
            return (0, float(cleaned))
        except (ValueError, TypeError):
            return (0, str(value).lower())

