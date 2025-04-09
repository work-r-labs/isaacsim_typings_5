"""
This module defines UI styles and functions to retrieve style dictionaries for various UI components in the omni.kit.window.extensions package.
"""
from __future__ import annotations
import carb as carb
from functools import lru_cache
from omni.kit.window.extensions.common import get_icons_path
from omni import ui
import omni.ui.color_utils
__all__: list = list()
def get_style(instance):
    """
    Fetches the style definition for the given instance's class.
    
        Args:
            instance (Any): The instance whose class style is to be fetched.
    
        Returns:
            Dict: The style dictionary associated with the instance's class.
    """
def get_styles(*args, **kwargs):
    ...
CATEGORY_ICON_SIZE: tuple = (70, 70)
EXT_ICON_SIZE: tuple = (70, 70)
EXT_ICON_SIZE_LARGE: tuple = (100, 100)
EXT_ITEM_TITLE_BAR_H: int = 27
EXT_LIST_ITEMS_MARGIN_H: int = 3
EXT_LIST_ITEM_H: int = 106
EXT_LIST_ITEM_ICON_ZONE_W: int = 87
cl: omni.ui.color_utils.ColorShade  # value = <omni.ui.color_utils.ColorShade object>
