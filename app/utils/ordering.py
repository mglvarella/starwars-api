from typing import Literal

class Ordering:
    """
    Utility class for applying ordering/sorting to API results.
    Works across all endpoints following the same pattern as filters.
    """
    
    @staticmethod
    def apply_ordering(
        response: dict, 
        order_by: str | None, 
        order_direction: Literal["asc", "desc"] = "asc"
    ) -> dict:
        """
        Apply ordering to the results in the response.
        
        Args:
            response: The API response containing a 'results' list
            order_by: The field name to order by
            order_direction: 'asc' for ascending, 'desc' for descending
            
        Returns:
            The response with ordered results
        """
        if not order_by:
            return response
        
        results = response.get("results", [])
        
        if not results:
            return response
        
        # Check if the field exists in the results
        if order_by not in results[0]:
            return response
        
        reverse = order_direction.lower() == "desc"
        
        # Sort with a key function that handles None and mixed types
        sorted_results = sorted(
            results,
            key=lambda x: Ordering._get_sort_key(x.get(order_by)),
            reverse=reverse
        )
        
        response["results"] = sorted_results
        return response
    
    @staticmethod
    def _get_sort_key(value):
        """
        Generate a sort key that handles None, 'unknown', 'n/a' and mixed types.
        Numeric strings are converted to numbers for proper numeric sorting.
        """
        if value is None or str(value).lower() in ("unknown", "n/a", "none"):
            # Return a tuple that sorts these values last
            return (1, "")
        
        # Try to convert to number for numeric sorting
        try:
            # Handle comma-separated numbers like "1,000"
            cleaned = str(value).replace(",", "")
            return (0, float(cleaned))
        except (ValueError, TypeError):
            # Fall back to string sorting
            return (0, str(value).lower())
