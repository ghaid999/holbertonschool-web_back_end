#!/usr/bin/env python3
"""Task 9"""

from typing import Iterable, Tuple, List


def element_length(lst: Iterable[str]) -> List[Tuple[str, int]]:
    """Return a list of tuples containing each element and its length."""
    return [(i, len(i)) for i in lst]
