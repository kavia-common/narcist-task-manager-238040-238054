"""
Minimal, side-effect-free helper module.

This repository primarily contains a React frontend, but this file was added per request.
"""

from __future__ import annotations


# PUBLIC_INTERFACE
def sub(a: float, b: float) -> float:
    """Return the difference of two numbers (a - b).

    Args:
        a: Minuend.
        b: Subtrahend.

    Returns:
        The result of `a - b`.

    Notes:
        - This function is intentionally small and safe (no I/O, no mutation of global state).
        - Uses `float` typing to accept ints and floats naturally.
    """
    return a - b
