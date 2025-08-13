from __future__ import annotations
import asyncio as asyncio
import omni as omni
from omni.kit.window.console.scripts.command_input import CommandInput
from omni.kit.window.console.scripts.console_command import CommandManager
from omni.kit.window.console.scripts.console_toolbar import ConsoleToolbar
from omni.kit.window.console.scripts.log_view import LogView
from omni import ui
__all__: list = ['ConsoleWindow']
class ConsoleWindow(omni.ui._ui.Window):
    """
    The Console window
    
        This class represents a console window in the UI. It provides functionality for displaying and interacting with console output.
        
    """
    def __init__(self):
        """
        Initializes the ConsoleWindow class.
        """
    def _build_ui(self):
        ...
    def _visibility_changed_fn(self, visible):
        ...
    def destroy(self):
        """
        Destroy window
        """
    def set_visibility_changed_listener(self, listener):
        """
        Sets the listener for visibility changes.
        
                Args:
                    listener (function): Callback called when visibility changes.
                
        """
CONSOLE_WINDOW_STYLE: dict  # value = {'Toolbar.Frame': {'padding': 0, 'margin_width': 0}, 'Toolbar.Button': {'stack_direction': <Direction.LEFT_TO_RIGHT: 0>, 'background_color': 0, 'padding': 2.5}, 'Toolbar.Button:hovered': {'background_color': 4281808695}, 'Toolbar.Button:checked': {'background_color': 4281808695}, 'Toolbar.Button.Image': {'color': 4291611852}, 'Toolbar.Button.Image::clear': {'image_url': '${glyphs}/Clear_Log.svg'}, 'Toolbar.Button.Image::open_log': {'image_url': '${glyphs}/Open_Log.svg'}, 'Toolbar.Button.Image::open_folder': {'image_url': '${glyphs}/Open_Folder.svg'}, 'Toolbar.Button.Image::verbose': {'image_url': '${glyphs}/asterisk.svg', 'color': 4286545791}, 'Toolbar.Button.Image::verbose:checked': {'color': 4290361785}, 'Toolbar.Button.Image::info': {'image_url': '${glyphs}/Info_Log.svg', 'color': 4286545791}, 'Toolbar.Button.Image::info:checked': {'color': 4293638777}, 'Toolbar.Button.Label::warning': {'color': 4286545791}, 'Toolbar.Button.Label::warning:checked': {'color': 4283091935}, 'Toolbar.Button.Image::warning': {'image_url': '${glyphs}/Warning_Log.svg', 'color': 4286545791}, 'Toolbar.Button.Image::warning:checked': {'color': 4283091935}, 'Toolbar.Button.Label::error': {'color': 4289376758}, 'Toolbar.Button.Image::error': {'image_url': '${glyphs}/Error_Log.svg', 'color': 4286545791}, 'Toolbar.Button.Image::error:checked': {'color': 4286417656}, 'Toolbar.SearchField': {'background_color': 'shade:4280557855'}, 'Toolbar.SearchField.hint': {'margin_width': 8, 'color': 'shade:4285427310'}, 'LogView': {'background_color': 'shade:4280557855', 'background_selected_color': 4281545523}, 'LogView:selected': {'background_color': 4281545523}, 'LogView.Item.Text': {'margin_height': 1}, 'LogView.Item.Text::verbose': {'color': 4293638777}, 'LogView.Item.Text::info': {'color': 4293638777}, 'LogView.Item.Text::warning': {'color': 4283091935}, 'LogView.Item.Text::error': {'color': 4289376758}, 'LogView.Item.Text::fatal': {'color': 4289376758}, 'CommandField.Hint': {'color': 'shade:4283058762'}}
