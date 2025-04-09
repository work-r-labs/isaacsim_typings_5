"""
This module provides user interface components for establishing and managing Nucleus connections in the Omniverse environment.
"""
from __future__ import annotations
import asyncio as asyncio
import carb as carb
import omni as omni
from omni.kit.async_engine.async_engine import run_coroutine
from omni.kit.window.popup_dialog.dialog import PopupDialog
from omni.kit.window.popup_dialog.form_dialog import FormDialog
from omni.kit.window.popup_dialog.form_dialog import FormWidget
from omni import ui
import os as os
import pathlib
import sys as sys
import tempfile as tempfile
import typing
__all__ = ['AlertPane', 'ConnectorDialog', 'DeviceAuthFlowDialog', 'FormDialog', 'FormWidget', 'ICON_PATH', 'LoopProgressBar', 'PopupDialog', 'UI_STYLES', 'asyncio', 'carb', 'omni', 'os', 'run_coroutine', 'sys', 'tempfile', 'ui']
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
class ConnectorDialog(omni.kit.window.popup_dialog.dialog.PopupDialog):
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
    def show_authenticate(self, name: str, url: str):
        """
        Shows the dialog for authentication, when the name and url is already given.
        """
    def show_waiting(self):
        ...
    @property
    def frame(self):
        ...
    @property
    def visible(self) -> bool:
        ...
class DeviceAuthFlowDialog(omni.kit.window.popup_dialog.dialog.PopupDialog):
    """
    A dialog for facilitating device authentication flow.
    
        This class manages the user interface for device authentication, providing a QR code for the user
        to scan and input a code for authentication. It handles countdowns for code expiration and
        retries for expired codes.
    
        Args:
            params (omni.client.AuthDeviceFlowParams): Parameters for device authentication including URL, server, and expiration.
        
    """
    TEMP_DIR: typing.ClassVar[str] = '/tmp/kit_device_auth_qrcode/'
    def __del__(self):
        ...
    def __init__(self, params: omni.client.impl._omniclient.AuthDeviceFlowParams):
        ...
    def _build_ui(self, params: omni.client.impl._omniclient.AuthDeviceFlowParams):
        ...
    def _count_expiration_async(self):
        """
        Counts down the remaining time in seconds before expiration.
        """
    def _generate_qrcode(self, url: str):
        """
        Generates a qrcode from the given url.
        """
    def _on_cancel_fn(self):
        ...
    def _on_retry(self):
        ...
    def destroy(self):
        ...
    def hide(self):
        ...
    def show_expired(self):
        """
        Show the user when the code has expired.
        """
    @property
    def visible(self) -> bool:
        ...
class LoopProgressBar:
    """
    A looping progress bar for visual indication of ongoing processes.
    
        This class creates a graphical progress bar that loops to indicate an ongoing process without a defined end. It is commonly used in UIs to show that an action is taking place.
    
        Args:
            puck_size (int): Size of the moving element in the progress bar.
            period (float): The time it takes for the puck to complete one loop.
    """
    def __del__(self):
        ...
    def __init__(self, puck_size: int = 20, period: float = 120):
        ...
    def _build_ui(self):
        ...
    def _inf_loop(self):
        ...
    def hide(self):
        ...
    def show(self):
        ...
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.widget.nucleus_connector-1.1.10+d02c707b/data/icons')
UI_STYLES: dict  # value = {'Dialog': {'background_color': 'shade:4280492319;light=4283650900', 'margin_width': 8, 'margin_height': 8}, 'Image': {'background_color': 0, 'margin': 0, 'padding': 0, 'color': 'shade:4289243304;light=4289243304', 'alignment': <Alignment.CENTER: 72>}, 'QrCode': {'background_color': 0, 'margin': 10, 'padding': 0, 'alignment': <Alignment.CENTER: 72>}, 'Image.Label': {'color': 'shade:4288782753;light=4292927712', 'alignment': <Alignment.CENTER: 72>}, 'ProgressBar': {'background_color': 'shade:4280557855;light=4280557855', 'border_width': 2, 'border_radius': 0, 'border_color': 'shade:4281480244;light=4281480244', 'color': 'shade:4291401548;light=4291401548', 'margin': 0, 'padding': 0, 'alignment': <Alignment.LEFT_CENTER: 66>}, 'ProgressBar.Frame': {'background_color': 4280492319, 'margin': 0, 'padding': 0}, 'ProgressBar.Puck': {'background_color': 'shade:4291401548;light=4291401548', 'margin': 2}, 'StringField.Url': {'color': 'shade:4293438795;light=4292870144', 'background_color': 0}, 'Label': {'color': 'shade:4288782753;light=4292927712'}, 'Label.Code': {'color': 'shade:4288782753;light=4292927712', 'alignment': <Alignment.CENTER: 72>, 'font_size': 40}, 'Label.TimeRemaining': {'color': 'shade:4293438795;light=4292870144'}, 'Label.Expired': {'color': 'shade:4281545633;light=4281545696', 'alignment': <Alignment.CENTER: 72>}, 'AlertPane': {'background_color': 'shade:4282006074;light=4281480244', 'color': 'shade:4288782753;light=4292927712', 'margin': 0, 'border_radius': 0.0}, 'AlertPane::info': {'border_color': 'shade:4291401548;light=4291401548', 'border_width': 2}, 'AlertPane::warn': {'border_color': 'shade:4281435795;light=4281435795', 'border_width': 2}, 'AlertPane.Content': {'background_color': 0, 'margin_width': 8, 'margin_height': 12}, 'AlertPanePane.Clear': {'background_color': 0, 'border_radius': 0.0, 'border_color': 'shade:4288782753;light=4292927712', 'border_width': 1, 'margin': 0, 'padding': 2}, 'AlertPane.Clear:hovered': {'background_color': 'shade:4288322202;light=4288322202'}, 'AlertPane.Clear.Image': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.widget.nucleus_connector-1.1.10+d02c707b/data/icons/close.svg', 'color': 'shade:4288782753;light=4292927712'}}
