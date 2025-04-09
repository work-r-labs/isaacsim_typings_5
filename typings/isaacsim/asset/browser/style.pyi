from __future__ import annotations
import omni.ui.color_utils
import pathlib
from pathlib import Path
__all__ = ['CONTEXT_MENU_STYLE', 'CURRENT_PATH', 'ICON_PATH', 'PROPERTY_STYLE', 'Path', 'cl']
CONTEXT_MENU_STYLE: dict  # value = {'Menu': {'background_color': 'context_menu_background_color', 'color': 'context_menu_text', 'border_radius': 2}, 'Menu.Item': {'background_color': 0, 'margin': 0}, 'Separator': {'background_color': 0, 'color': 'context_menu_separator'}}
CURRENT_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/exts/isaacsim.asset.browser/isaacsim/asset/browser')
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/exts/isaacsim.asset.browser/icons')
PROPERTY_STYLE: dict = {'RadioButton': {'background_color': 0, 'padding': 0}, 'RadioButton.Image': {'image_url': '/home/chris/isaacsim/exts/isaacsim.asset.browser/icons/radio_off.svg'}, 'RadioButton.Image:checked': {'image_url': '/home/chris/isaacsim/exts/isaacsim.asset.browser/icons/radio_on.svg'}}
cl: omni.ui.color_utils.ColorShade  # value = <omni.ui.color_utils.ColorShade object>
