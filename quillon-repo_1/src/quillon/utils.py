"""Small helpers.

Author: Teodor Bak
"""


def chunk(items, size):
    """Yield successive chunks of `size` items."""
    for i in range(0, len(items), size):
        yield items[i:i + size]
