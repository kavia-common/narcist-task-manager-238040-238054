"""
Minimal, side-effect-free helper module.

This repository primarily contains a React frontend, but this file was added per request.
"""

from __future__ import annotations


# PUBLIC_INTERFACE
def add(a: float, b: float) -> float:
    """Return the sum of two numbers.

    Args:
        a: First addend.
        b: Second addend.

    Returns:
        The sum of `a` and `b`.

    Notes:
        - This function is intentionally small and safe (no I/O, no mutation of global state).
        - Uses `float` typing to accept ints and floats naturally.
    """
    return a + b
