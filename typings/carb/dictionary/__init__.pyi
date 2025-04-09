from __future__ import annotations
import carb as carb
from carb.dictionary._dictionary import IDictionary
from carb.dictionary._dictionary import ISerializer
from carb.dictionary._dictionary import Item
from carb.dictionary._dictionary import ItemType
from carb.dictionary._dictionary import UpdateAction
from carb.dictionary._dictionary import acquire_dictionary_interface
from carb.dictionary._dictionary import acquire_serializer_interface
from carb.dictionary._dictionary import get_json_serializer
from carb.dictionary._dictionary import get_toml_serializer
from functools import lru_cache
from . import _dictionary
__all__ = ['IDictionary', 'ISerializer', 'Item', 'ItemType', 'UpdateAction', 'acquire_dictionary_interface', 'acquire_serializer_interface', 'carb', 'get_dictionary', 'get_dictionary_interface', 'get_json_serializer', 'get_toml_serializer', 'lru_cache']
def get_dictionary() -> _dictionary.IDictionary:
    """
    Returns cached :class:`carb.dictionary.IDictionary` interface (shorthand).
    """
def get_dictionary_interface(*args, **kwargs):
    """
    Returns cached :class:`carb.dictionary.IDictionary` interface
    """
__copyright__: str = 'Copyright (c) 2020-2021, NVIDIA CORPORATION. All rights reserved.'
__license__: str = '\nNVIDIA CORPORATION and its licensors retain all intellectual property\nand proprietary rights in and to this software, related documentation\nand any modifications thereto. Any use, reproduction, disclosure or\ndistribution of this software and related documentation without an express\nlicense agreement from NVIDIA CORPORATION is strictly prohibited.\n'
