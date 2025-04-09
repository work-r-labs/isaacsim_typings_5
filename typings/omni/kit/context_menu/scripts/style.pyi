from __future__ import annotations
from functools import lru_cache
import omni.ui.color_utils
import omni.ui.constant_utils
__all__: list = list()
MENU_BACKGROUND: str = 'shade:3425314853'
MENU_ITEM_CHECKMARK_COLOR: str = 'shade:4294952756'
MENU_ITEM_MARGIN: str = 'shade:5'
MENU_ITEM_MARGIN_HEIGHT: str = 'shade:3'
MENU_LIGHT: str = 'shade:4292269782'
MENU_MEDIUM: str = 'shade:4285427310'
MENU_SELECTION: str = 'shade:1006618420'
MENU_SELECTION_BORDER: str = 'shade:4294952756'
MENU_STYLE: dict = {'Menu.Title': {'color': 'shade:4280952869', 'background_color': 0}, 'Menu.Title:hovered': {'background_color': 'shade:1006618420', 'border_width': 1, 'border_color': 'shade:4294952756'}, 'Menu.Title:pressed': {'background_color': 'shade:1006618420'}, 'Menu.Item': {'color': 'shade:4292269782', 'margin_width': 'shade:5', 'margin_HEIGHT': 'shade:3'}, 'Menu.Item.CheckMark': {'color': 'shade:4294952756'}, 'Menu.Separator': {'color': 'shade:4285427310', 'margin_HEIGHT': 'shade:3', 'border_width': 1.5}, 'Menu.Window': {'background_color': 'shade:3425314853', 'border_width': 0, 'border_radius': 0, 'background_selected_color': 'shade:1006618420', 'secondary_padding': 1, 'secondary_selected_color': 'shade:4294952756', 'margin': 2}, 'MenuItem': {'background_selected_color': 'shade:1006618420', 'secondary_padding': 1, 'secondary_selected_color': 'shade:4294952756'}}
MENU_TITLE: str = 'shade:4280952869'
cl: omni.ui.color_utils.ColorShade  # value = <omni.ui.color_utils.ColorShade object>
fl: omni.ui.constant_utils.FloatShade  # value = <omni.ui.constant_utils.FloatShade object>
