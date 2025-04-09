"""
This module defines a set of UI styles and color palettes for components in the omni.kit.widget.nucleus_connector package, providing consistency and theming across the user interface.
"""
from __future__ import annotations
from omni import ui
import pathlib
from pathlib import Path
import typing
__all__ = ['CURRENT_PATH', 'Colors', 'DATA_PATH', 'ICON_PATH', 'Path', 'UI_STYLES', 'ui']
class Colors:
    """
    A class that defines a palette of colors for UI components.
    
        This class contains static attributes representing various colors used in the UI design, each defined as a shade with optional light variations. The colors include backgrounds, borders, button states, text, warnings, URLs, images, progress elements, and alert panes. They are meant to ensure consistency and theme coherence across the user interface.
        
    """
    AlertPaneBackground: typing.ClassVar[str] = 'shade:4282006074;light=4281480244'
    Background: typing.ClassVar[str] = 'shade:4280492319;light=4283650900'
    Border: typing.ClassVar[str] = 'shade:4288782753;light=4292927712'
    ButtonHovered: typing.ClassVar[str] = 'shade:4288322202;light=4288322202'
    ButtonSelected: typing.ClassVar[str] = 'shade:4288322202;light=4288322202'
    Image: typing.ClassVar[str] = 'shade:4289243304;light=4289243304'
    InfoPaneBorder: typing.ClassVar[str] = 'shade:4291401548;light=4291401548'
    ProgressBackground: typing.ClassVar[str] = 'shade:4280557855;light=4280557855'
    ProgressBar: typing.ClassVar[str] = 'shade:4291401548;light=4291401548'
    ProgressBorder: typing.ClassVar[str] = 'shade:4281480244;light=4281480244'
    Text: typing.ClassVar[str] = 'shade:4288782753;light=4292927712'
    TextWarn: typing.ClassVar[str] = 'shade:4281545633;light=4281545696'
    Url: typing.ClassVar[str] = 'shade:4293438795;light=4292870144'
    WarningPaneBorder: typing.ClassVar[str] = 'shade:4281435795;light=4281435795'
CURRENT_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.widget.nucleus_connector-1.1.10+d02c707b/omni/kit/widget/nucleus_connector')
DATA_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.widget.nucleus_connector-1.1.10+d02c707b/data')
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.widget.nucleus_connector-1.1.10+d02c707b/data/icons')
UI_STYLES: dict  # value = {'Dialog': {'background_color': 'shade:4280492319;light=4283650900', 'margin_width': 8, 'margin_height': 8}, 'Image': {'background_color': 0, 'margin': 0, 'padding': 0, 'color': 'shade:4289243304;light=4289243304', 'alignment': <Alignment.CENTER: 72>}, 'QrCode': {'background_color': 0, 'margin': 10, 'padding': 0, 'alignment': <Alignment.CENTER: 72>}, 'Image.Label': {'color': 'shade:4288782753;light=4292927712', 'alignment': <Alignment.CENTER: 72>}, 'ProgressBar': {'background_color': 'shade:4280557855;light=4280557855', 'border_width': 2, 'border_radius': 0, 'border_color': 'shade:4281480244;light=4281480244', 'color': 'shade:4291401548;light=4291401548', 'margin': 0, 'padding': 0, 'alignment': <Alignment.LEFT_CENTER: 66>}, 'ProgressBar.Frame': {'background_color': 4280492319, 'margin': 0, 'padding': 0}, 'ProgressBar.Puck': {'background_color': 'shade:4291401548;light=4291401548', 'margin': 2}, 'StringField.Url': {'color': 'shade:4293438795;light=4292870144', 'background_color': 0}, 'Label': {'color': 'shade:4288782753;light=4292927712'}, 'Label.Code': {'color': 'shade:4288782753;light=4292927712', 'alignment': <Alignment.CENTER: 72>, 'font_size': 40}, 'Label.TimeRemaining': {'color': 'shade:4293438795;light=4292870144'}, 'Label.Expired': {'color': 'shade:4281545633;light=4281545696', 'alignment': <Alignment.CENTER: 72>}, 'AlertPane': {'background_color': 'shade:4282006074;light=4281480244', 'color': 'shade:4288782753;light=4292927712', 'margin': 0, 'border_radius': 0.0}, 'AlertPane::info': {'border_color': 'shade:4291401548;light=4291401548', 'border_width': 2}, 'AlertPane::warn': {'border_color': 'shade:4281435795;light=4281435795', 'border_width': 2}, 'AlertPane.Content': {'background_color': 0, 'margin_width': 8, 'margin_height': 12}, 'AlertPanePane.Clear': {'background_color': 0, 'border_radius': 0.0, 'border_color': 'shade:4288782753;light=4292927712', 'border_width': 1, 'margin': 0, 'padding': 2}, 'AlertPane.Clear:hovered': {'background_color': 'shade:4288322202;light=4288322202'}, 'AlertPane.Clear.Image': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.widget.nucleus_connector-1.1.10+d02c707b/data/icons/close.svg', 'color': 'shade:4288782753;light=4292927712'}}
