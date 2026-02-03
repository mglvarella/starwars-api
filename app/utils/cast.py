def safe_int(value) -> int | None:
    if value is None:
        return None

    if isinstance(value, int):
        return value

    try:
        return int(str(value).replace(",", ""))
    except (ValueError, TypeError):
        return None
