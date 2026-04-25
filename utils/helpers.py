def parse_price(price_str: str) -> float:
    """Convert a string like '$29.99' to the float 29.99."""
    return float(price_str.replace("$", "").strip())


def format_price(price_float: float) -> str:
    """Convert 29.99 back to '$29.99'."""
    return f"${price_float:.2f}"
