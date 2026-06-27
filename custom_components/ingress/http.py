"""HTTP helpers for ingress proxy."""

MIN_COMPRESSED_SIZE = 128


def should_compress(content_type: str) -> bool:
    """Return if we should compress a response."""
    if content_type.startswith("text/event-stream"):
        return False
    if content_type.startswith("image/"):
        return "svg" in content_type
    if content_type.startswith("application/"):
        return (
            "json" in content_type
            or "xml" in content_type
            or "javascript" in content_type
        )
    return not content_type.startswith(("video/", "audio/", "font/"))
