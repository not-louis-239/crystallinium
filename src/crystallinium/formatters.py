def format_time(s: float, /) -> str:
    """Format a time in seconds to a human-readable string."""
    hours = s // 3600
    minutes = (s // 60) % 60
    seconds = (s % 60) // 1
    return f"{hours:02}:{minutes:02}:{seconds:02}"
