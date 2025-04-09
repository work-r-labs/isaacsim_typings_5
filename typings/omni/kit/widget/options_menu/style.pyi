"""
This module defines the style options for the options menu widget in the Omni Kit UI, including colors, margins, and icons.
"""
from __future__ import annotations
from omni import ui
import omni.ui.color_utils
import pathlib
from pathlib import Path
__all__ = ['CURRENT_PATH', 'ICON_PATH', 'OPTIONS_MENU_STYLE', 'Path', 'cl', 'ui']
CURRENT_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.widget.options_menu-1.1.6+d02c707b/omni/kit/widget/options_menu')
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.widget.options_menu-1.1.6+d02c707b/data/icons')
OPTIONS_MENU_STYLE: dict  # value = {'Title.Background': {'background_color': 4280492319, 'corner_flag': <CornerFlag.TOP: 3>, 'margin': 0}, 'Title.Header': {'margin_width': 3, 'margin_height': 0}, 'Title.Label': {'background_color': 0, 'color': 'shade:4288782753', 'margin_width': 5}, 'ResetButton': {'background_color': 0}, 'ResetButton:hovered': {'background_color': 'shade:4281611314'}, 'ResetButton.Label': {'color': 'shade:4294952756'}, 'ResetButton.Label:disabled': {'color': 'shade:4285427310'}, 'ResetButton.Label:hovered': {'color': 'shade:4291137818'}, 'MenuItem.Icon': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.widget.options_menu-1.1.6+d02c707b/data/icons/check_solid.svg', 'color': 0, 'margin': 7}, 'MenuItem.Icon:checked': {'color': 'shade:4294952756'}, 'MenuItem.Icon:selected': {'color': 'shade:4280492319'}, 'MenuItem.Icon::disabled:disabled': {'color': 'shade:4285427310', 'margin': 7}, 'MenuItem.Radio': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.widget.options_menu-1.1.6+d02c707b/data/icons/radiomark.svg', 'color': 0, 'margin': 7}, 'MenuItem.Radio:checked': {'color': 'shade:4294952756'}, 'MenuItem.Radio:selected': {'color': 'shade:4280492319'}, 'MenuItem.Label::title': {'color': 'shade:4288782753', 'margin_width': 5}, 'MenuItem.Label:disabled': {'color': 'shade:4285427310'}, 'MenuItem.Separator': {'color': 'shade:4284703586', 'border_width': 1.5}}
cl: omni.ui.color_utils.ColorShade  # value = <omni.ui.color_utils.ColorShade object>
