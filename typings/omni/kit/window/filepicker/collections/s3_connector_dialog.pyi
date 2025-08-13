from __future__ import annotations
import asyncio as asyncio
import carb as carb
import omni as omni
from omni.kit.window.popup_dialog.dialog import PopupDialog
from omni.kit.window.popup_dialog.form_dialog import FormDialog
from omni.kit.window.popup_dialog.form_dialog import FormWidget
from omni import ui
import pathlib
import typing
from typing import Any
__all__: list[str] = ['AlertPane', 'Any', 'Colors', 'FormDialog', 'FormWidget', 'ICON_PATH', 'PopupDialog', 'S3ConnectorDialog', 'UI_STYLES', 'asyncio', 'carb', 'omni', 'ui']
class AlertPane:
    """
    A class representing an alert pane within an application dialog.
    
        This pane can be used to display informational messages or warnings to the user in a stylized format.
    
        Args:
            width: int
                The width of the alert pane in pixels.
    """
    Info: typing.ClassVar[int] = 0
    Warn: typing.ClassVar[int] = 1
    def __init__(self, width: int = 400):
        ...
    def _build_ui(self, width: int = 400):
        ...
    def destroy(self):
        ...
    def hide(self):
        ...
    def show(self, msg: str = '', alert_type: int = 0):
        ...
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
class S3ConnectorDialog(omni.kit.window.popup_dialog.dialog.PopupDialog):
    """
    The main connection dialog for establishing Nucleus connections.
    
        This dialog provides a user interface to add new Omniverse connections with an optional name. It manages the UI elements and tasks associated with the connection process, such as displaying progress, handling cancellations, and showing alerts.
        
    """
    def __del__(self):
        ...
    def __init__(self):
        ...
    def _build_ui(self):
        ...
    def _on_cancel_fn(self):
        ...
    def cancel_task(self):
        """
        Cancels the managed task
        """
    def destroy(self):
        ...
    def get_value(self, name: str) -> str:
        ...
    def hide(self):
        ...
    def run_cancellable_task(self, task: typing.Coroutine) -> typing.Any:
        """
        Manages running and cancelling the given task
        """
    def set_value(self, name: str, value: str):
        ...
    def show(self, name: str = None, url: str = None):
        """
        Shows the dialog after resetting to a default state
        """
    def show_alert(self, msg: str = '', alert_type: int = 0):
        ...
    @property
    def frame(self):
        ...
    @property
    def visible(self) -> bool:
        ...
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/videos/isaacsim/_build/linux-x86_64/release/extscache/omni.kit.window.filepicker-2.13.3+8131b85d/icons/NvidiaDark')
UI_STYLES: dict  # value = {'Dialog': {'background_color': 'shade:4280492319;light=4283650900', 'margin_width': 8, 'margin_height': 8}, 'Image': {'background_color': 0, 'margin': 0, 'padding': 0, 'color': 'shade:4289243304;light=4289243304', 'alignment': <Alignment.CENTER: 72>}, 'QrCode': {'background_color': 0, 'margin': 10, 'padding': 0, 'alignment': <Alignment.CENTER: 72>}, 'Image.Label': {'color': 'shade:4288782753;light=4292927712', 'alignment': <Alignment.CENTER: 72>}, 'ProgressBar': {'background_color': 'shade:4280557855;light=4280557855', 'border_width': 2, 'border_radius': 0, 'border_color': 'shade:4281480244;light=4281480244', 'color': 'shade:4291401548;light=4291401548', 'margin': 0, 'padding': 0, 'alignment': <Alignment.LEFT_CENTER: 66>}, 'ProgressBar.Frame': {'background_color': 4280492319, 'margin': 0, 'padding': 0}, 'ProgressBar.Puck': {'background_color': 'shade:4291401548;light=4291401548', 'margin': 2}, 'StringField.Url': {'color': 'shade:4293438795;light=4292870144', 'background_color': 0}, 'Label': {'color': 'shade:4288782753;light=4292927712'}, 'Label.Code': {'color': 'shade:4288782753;light=4292927712', 'alignment': <Alignment.CENTER: 72>, 'font_size': 40}, 'Label.TimeRemaining': {'color': 'shade:4293438795;light=4292870144'}, 'Label.Expired': {'color': 'shade:4281545633;light=4281545696', 'alignment': <Alignment.CENTER: 72>}, 'AlertPane': {'background_color': 'shade:4282006074;light=4281480244', 'color': 'shade:4288782753;light=4292927712', 'margin': 0, 'border_radius': 0.0}, 'AlertPane::info': {'border_color': 'shade:4291401548;light=4291401548', 'border_width': 2}, 'AlertPane::warn': {'border_color': 'shade:4281435795;light=4281435795', 'border_width': 2}, 'AlertPane.Content': {'background_color': 0, 'margin_width': 8, 'margin_height': 12}, 'AlertPanePane.Clear': {'background_color': 0, 'border_radius': 0.0, 'border_color': 'shade:4288782753;light=4292927712', 'border_width': 1, 'margin': 0, 'padding': 2}, 'AlertPane.Clear:hovered': {'background_color': 'shade:4288322202;light=4288322202'}, 'AlertPane.Clear.Image': {'image_url': '/home/chris/videos/isaacsim/_build/linux-x86_64/release/extscache/omni.kit.window.filepicker-2.13.3+8131b85d/icons/NvidiaDark/close.svg', 'color': 'shade:4288782753;light=4292927712'}}
