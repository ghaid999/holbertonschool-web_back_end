#!/usr/bin/env python3
"""Pagination helper."""


def index_range(page: int, page_size: int) -> tuple:
    """Return the index range for a page."""
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
