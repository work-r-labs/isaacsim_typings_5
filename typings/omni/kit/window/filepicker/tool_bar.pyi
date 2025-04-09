from __future__ import annotations
import carb as carb
from carb import log_warn
from omni.kit.widget.browser_bar.widget import BrowserBar
import omni.kit.widget.filebrowser.model
from omni.kit.widget.filebrowser.model import FileBrowserItem
from omni.kit.window.filepicker.config_button import ConfigButton
from omni.kit.window.filepicker.style import get_style
from omni.kit.window.popup_dialog.form_dialog import FormDialog
from omni.kit.window.popup_dialog.input_dialog import InputDialog
from omni.kit.window.popup_dialog.message_dialog import MessageDialog
from omni import ui
import pathlib
import typing
__all__: list = ['ToolBar']
class ToolBar:
    SAVED_SETTINGS_OPTIONS_MENU: typing.ClassVar[str] = '/persistent/app/omniverse/filepicker/options_menu'
    def __init__(self, **kwargs):
        ...
    def _build_ui(self):
        ...
    def _build_widgets(self):
        ...
    def _on_toggle_bookmark(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem):
        ...
    def destroy(self):
        """
         Destroy the widget. 
        """
    def set_bookmarked(self, true_false: bool):
        """
        
                Set whether or not the bookmark image should be shown.
        
                Args:
                    true_false (bool): True if the bookmark image should be shown else False.
                
        """
    def set_config_value(self, name: str, value: bool):
        """
        
                Set a value for a config button.
        
                Args:
                    name (str): The name of the value to set.
                    value (bool): The value to set for the name.
                
        """
    def set_path(self, path: str):
        """
        
                Sets the path to search for.
        
                Args:
                    path (str): The path to search
                
        """
    def set_search_delegate(self, delegate):
        """
        
                Sets a custom search delegate for the tool bar.
        
                Args:
                    delegate (:obj:`SearchDelegate`): Object that creates the search widget.
                
        """
    @property
    def bookmarked(self) -> bool:
        """
        
                Whether or not the current path is bookmarked.
        
                Returns:
                    bool: True if the current path is bookmarked else False.
                
        """
    @property
    def config_values(self):
        """
        
                Returns the values of the configuration button.
        
                Returns:
                    Dict[str, bool]:  A dictionary of the configuration button values
                
        """
    @property
    def path(self) -> str:
        """
        
                Path to the currently displayed file.
        
                Returns:
                    str: Path to the currently displayed file or None if there is no browser bar.
                
        """
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.window.filepicker-2.11.7+d02c707b/icons/NvidiaDark')
