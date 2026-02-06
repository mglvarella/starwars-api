class Pagination:
    DEFAULT_PAGE_SIZE = 10

    @staticmethod
    def paginate(results: list, page: int, page_size: int = DEFAULT_PAGE_SIZE) -> dict:
        total = len(results)
        start = (page - 1) * page_size
        end = start + page_size
        paginated_results = results[start:end]
        
        has_next = end < total
        has_previous = page > 1
        
        return {
            "count": total,
            "next": f"?page={page + 1}" if has_next else None,
            "previous": f"?page={page - 1}" if has_previous else None,
            "results": paginated_results
        }
