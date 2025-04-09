from __future__ import annotations
import carb as carb
from carb.variant._variant import IVariant
from carb.variant._variant import acquire_variant_interface
from functools import lru_cache
from . import _variant
__all__ = ['IVariant', 'acquire_variant_interface', 'carb', 'get_variant', 'get_variant_interface', 'lru_cache']
def get_variant() -> _variant.IVariant:
    """
    Returns cached :class:`carb.variant.IVariant` interface (shorthand).
    """
def get_variant_interface(*args, **kwargs):
    """
    Returns cached :class:`carb.variant.IVariant` interface
    """
__copyright__: str = 'Copyright (c) 2022, NVIDIA CORPORATION. All rights reserved.'
__license__: str = '\nNVIDIA CORPORATION and its licensors retain all intellectual property\nand proprietary rights in and to this software, related documentation\nand any modifications thereto. Any use, reproduction, disclosure or\ndistribution of this software and related documentation without an express\nlicense agreement from NVIDIA CORPORATION is strictly prohibited.\n'
