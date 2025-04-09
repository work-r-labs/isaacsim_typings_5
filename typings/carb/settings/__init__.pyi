"""
Bindings for `carb::settings::ISettings` interface. Settings is a runtime representation of typical configuration formats (like json, toml, xml), it is a nested dictionary of values.
"""
from __future__ import annotations
import carb as carb
from carb.settings._settings import ChangeEventType
from carb.settings._settings import ISettings
from carb.settings._settings import SubscriptionId
from carb.settings._settings import acquire_settings_interface
from functools import lru_cache
from . import _settings
__all__ = ['ChangeEventType', 'ISettings', 'SubscriptionId', 'acquire_settings_interface', 'carb', 'get_settings', 'get_settings_interface', 'lru_cache']
def get_settings() -> _settings.ISettings:
    """
    Returns cached :class:`carb.settings.ISettings` interface (shorthand).
    """
def get_settings_interface(*args, **kwargs):
    """
    Returns cached :class:`carb.settings.ISettings` interface
    """
__copyright__: str = 'Copyright (c) 2020-2021, NVIDIA CORPORATION. All rights reserved.'
__license__: str = '\nNVIDIA CORPORATION and its licensors retain all intellectual property\nand proprietary rights in and to this software, related documentation\nand any modifications thereto. Any use, reproduction, disclosure or\ndistribution of this software and related documentation without an express\nlicense agreement from NVIDIA CORPORATION is strictly prohibited.\n'
