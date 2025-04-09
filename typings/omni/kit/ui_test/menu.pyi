from __future__ import annotations
import logging as logging
from omni.kit.ui_test.common import human_delay
from omni.kit.ui_test.common import wait_n_updates_internal
from omni.kit.ui_test.input import emulate_mouse_click
from omni.kit.ui_test.input import emulate_mouse_move
from omni.kit.ui_test.vec2 import Vec2
from omni import ui
import re as re
__all__ = ['Vec2', 'emulate_mouse_click', 'emulate_mouse_move', 'get_context_menu', 'human_delay', 'logger', 'logging', 're', 'select_context_menu', 'ui', 'wait_n_updates_internal']
def _find_context_menu_item(query, menu_root, find_fn = _find_menu_item):
    ...
def _find_menu_item(query, menu_root):
    ...
def get_context_menu(menu_root: ui.Widget = None, get_all: bool = False):
    ...
def select_context_menu(menu_path: str, menu_root: ui.Widget = None, offset = ..., human_delay_speed: int = 4, find_fn = _find_menu_item):
    """
    Emulate selection of context menu item with mouse.
         
        Supports nested menus separated by `/`:
    
        .. code-block:: python
    
            await ui_test.select_context_menu("Option/Select/All")
    
        This function waits for current menu for some time first. Unless `menu_root` was passed explicitly.
        When there are nested menu mouse moves to each of them and makes human delay for it to open. Then is emulates mouse
        click on final menu item.
        
    """
logger: logging.Logger  # value = <Logger omni.kit.ui_test.menu (DEBUG)>
