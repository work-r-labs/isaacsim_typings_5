from __future__ import annotations
import carb as carb
from carb.input import KeyboardInput
import logging as logging
from omni.kit.ui_test.common import wait_n_updates_internal
from omni.kit.ui_test.input import emulate_char_press
from omni.kit.ui_test.input import emulate_keyboard
from omni.kit.ui_test.input import emulate_keyboard_press
from omni.kit.ui_test.input import emulate_mouse_drag_and_drop
from omni.kit.ui_test.input import emulate_mouse_move
from omni.kit.ui_test.input import emulate_mouse_move_and_click
from omni.kit.ui_test.vec2 import Vec2
from omni import ui
from omni.ui_query.query import OmniUIQuery
import typing
__all__ = ['KeyboardInput', 'MenuRef', 'OmniUIQuery', 'Vec2', 'WidgetRef', 'WindowRef', 'WindowStub', 'carb', 'emulate_char_press', 'emulate_keyboard', 'emulate_keyboard_press', 'emulate_mouse_drag_and_drop', 'emulate_mouse_move', 'emulate_mouse_move_and_click', 'find', 'find_all', 'find_first', 'get_menubar', 'logger', 'logging', 'menu_click', 'ui', 'wait_n_updates_internal', 'window_stub']
class MenuRef(WidgetRef):
    """
    Reference to `omni.ui.Menu`
    """
    @staticmethod
    def menu_click(path, separator: str = '/', human_delay_speed: int = 2, show: bool = True):
        ...
    def __init__(self, widget: ui.Menu, path: str):
        ...
    def find_menu(self, path: str, ignore_case: bool = False, contains_path: bool = False) -> MenuRef:
        ...
    @property
    def center(self) -> Vec2:
        ...
class WidgetRef:
    """
    Reference to `omni.ui.Widget` and a path it was found with.
    """
    def __init__(self, widget: ui.Widget, path: str, window: ui.Window = None):
        ...
    def __str__(self) -> str:
        ...
    def _wait(self, update_count = 2):
        ...
    def bring_to_front(self):
        """
        Bring window this widget belongs to on top. Currently this is implemented as undock() + focus().
        """
    def click(self, pos: Vec2 = None, right_click = False, double = False, human_delay_speed: int = 2):
        """
        Emulate mouse click on the widget.
        """
    def double_click(self, pos = None, human_delay_speed: int = 2):
        ...
    def drag_and_drop(self, drop_target: Vec2, human_delay_speed: int = 4):
        """
        Drag/drop for widget.centre to `drop_target`
        """
    def find(self, path: str) -> WidgetRef:
        """
        Find omni.ui Widget or Window by search query starting from this widget.
        
                .. code-block:: python
        
                    stage_window = ui_test.find("Stage//Frame/**/ScrollingFrame/TreeView[*].visible==True")
                    label = stage_window.find("**/Label[*].text=='hello'")
                    await label.right_click()
        
        
                Returns:
                    Found Widget or Window wrapped into `WidgetRef` object.
                
        """
    def find_all(self, path: str) -> list[WidgetRef]:
        """
        Find all omni.ui Widget or Window by search query starting from this widget.
        
                .. code-block:: python
        
                    stage_window = ui_test.find("Stage//Frame/**/ScrollingFrame/TreeView[*].visible==True")
                    labels = stage_window.find_all("**/Label[*]")
                    for label in labels:
                        await label.right_click()
        
        
                Returns:
                    List of found Widget or Window wrapped into `WidgetRef` objects.
                
        """
    def find_first(self, path: str) -> WidgetRef:
        """
        Find the first omni.ui Widget or Window by search query starting from this widget.
        
                .. code-block:: python
        
                    stage_window = ui_test.find("Stage//Frame/**/ScrollingFrame/TreeView[*].visible==True")
                    label = stage_window.find_first("**/Label[*]")
                    await label.right_click()
        
        
                Returns:
                    Widget or Window wrapped into `WidgetRef` object.
                
        """
    def focus(self):
        """
        Focus on a window this widget belongs to.
        """
    def input(self, text: str, end_key = ..., human_delay_speed: int = 2):
        """
        Emulate keyboard input of characters (text) into the widget.
        
                It is a helper function for the following sequence:
        
                1. Double click on the widget
                2. Input characters
                3. Press enter
                
        """
    def offset(self, *kwargs) -> Vec2:
        ...
    def right_click(self, pos = None, human_delay_speed: int = 2):
        ...
    def undock(self):
        """
        Undock a window this widget belongs to.
        """
    @property
    def center(self) -> Vec2:
        """
        Center of the widget.
        """
    @property
    def model(self):
        ...
    @property
    def path(self) -> str:
        """
        Path this widget was found with.
        """
    @property
    def position(self) -> Vec2:
        """
        Screen position of widget's top left corner.
        """
    @property
    def realpath(self) -> str:
        """
        Actual unique path to this widget from the window.
        """
    @property
    def size(self) -> Vec2:
        """
        Computed size of the widget.
        """
    @property
    def widget(self) -> ui.Widget:
        ...
    @property
    def window(self) -> ui.Window:
        ...
class WindowRef(WidgetRef):
    """
    Reference to `omni.ui.WindowHandle`
    """
    def __init__(self, widget: ui.WindowHandle, path: str):
        ...
    @property
    def position(self) -> Vec2:
        ...
    @property
    def size(self) -> Vec2:
        ...
class WindowStub:
    """
    stub window class for use with WidgetRef & 
    """
    @staticmethod
    def focus(_):
        ...
    @staticmethod
    def undock(_):
        ...
def _build_widget_ref(widget, path, root_widget) -> WindowRef | WidgetRef:
    ...
def _build_window_ref(path: str) -> WindowRef | None:
    ...
def _find(path: str, root_widget: WidgetRef = None) -> WidgetRef:
    ...
def _find_all(path: str, root_widget: WidgetRef = None) -> list[WidgetRef]:
    ...
def _find_first(path: str, root_widget: WidgetRef = None) -> WidgetRef:
    ...
def find(path: str) -> WidgetRef:
    """
    Find omni.ui Widget or Window by search query. `omni.ui_query` is used under the hood.
    
        Returned object can be used to get actual found item or/and do UI test operations on it.
    
        .. code-block:: python
    
            stage_window = ui_test.find("Stage//Frame/**/ScrollingFrame/TreeView[*].visible==True")
            await stage_window.right_click()
    
            viewport = ui_test.find("Viewport")
            center = viewport.center
            print(center)
    
    
        Returns:
            Found Widget or Window wrapped into `WidgetRef` object.
        
    """
def find_all(path: str) -> list[WidgetRef]:
    """
    Find all omni.ui Widget or Window by search query.
    
        .. code-block:: python
    
            buttons = ui_test.find_all("Stage//Frame/**/Button[*]")
            for button in buttons:
                await button.click()
    
    
        Returns:
            List of found Widget or Window wrapped into `WidgetRef` objects.
        
    """
def find_first(path: str) -> list[WidgetRef]:
    """
    Find first omni.ui Widget or Window by search query.
    
        .. code-block:: python
    
            button = ui_test.find_first("Stage//Frame/**/Button[*]")
            await button.click()
    
    
        Returns:
            Widget or Window wrapped into `WidgetRef` objects.
        
    """
def get_menubar() -> MenuRef:
    ...
def menu_click(path, separator: str = '/', human_delay_speed: int = 2, show: bool = True) -> None:
    ...
logger: logging.Logger  # value = <Logger omni.kit.ui_test.query (DEBUG)>
window_stub: WindowStub  # value = <omni.kit.ui_test.query.WindowStub object>
