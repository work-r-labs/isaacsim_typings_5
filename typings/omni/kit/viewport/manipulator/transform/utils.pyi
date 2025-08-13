from __future__ import annotations
import carb as carb
__all__: list[str] = ['carb', 'flatten']
def flatten(*args, **kwds):
    """
    Convert array[4][4] to array[16]
    """
