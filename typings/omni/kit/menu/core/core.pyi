"""

Core menu class. Used by omni.kit.menu.utils and omni.kit.context_menu to build menus.
"""
from __future__ import annotations
import carb as carb
import collections as collections
import copy as copy
import omni as omni
from omni import ui
from pathlib import Path
import typing
__all__: list = ['has_delegate_func', 'DictReadOnly', 'IconMenuBaseDelegate', 'uiMenu', 'uiMenuItem', 'MenuEventType']
class DictReadOnly(collections.abc.Mapping):
    """
    Read-only dictionary. Prevents accidental write-backs to dictionary.
    
        Args:
            data (dict): The dictionary to be wrapped in a read-only interface.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __getitem__(self, key):
        ...
    def __init__(self, data):
        """
        Initializes the DictReadOnly instance.
        """
    def __ior__(self, *args, **kwargs):
        ...
    def __iter__(self):
        ...
    def __len__(self):
        ...
    def __or__(self, other):
        ...
    def __readonly__(self, *args, **kwargs):
        ...
    def __str__(self) -> str:
        ...
    def copy(self):
        """
        Creates a shallow copy of the read-only dictionary.
        
                Returns:
                    DictReadOnly: A new DictReadOnly instance with copied data.
                
        """
    def merge_dict(self, other):
        """
        Merges another dictionary into the current read-only dictionary.
        
                Args:
                    other (dict): The dictionary to merge with the current dictionary.
        
                Returns:
                    DictReadOnly: A new DictReadOnly instance with merged data.
                
        """
class IconMenuBaseDelegate(omni.ui._ui.MenuDelegate):
    """
    Icon Menu Delegate class.
    
        Keyword Args:
            background_color (int): Background color of the menu.
            background_selected_color (int): Background color when an item is selected.
            icon_size (float): Size of the icons.
            text_size (float): Size of the text.
            tick_size (float): Size of the tick marks.
            separator_size (list): Size of the separators.
            tick_spacing (list): Spacing of the tick marks.
            margin_size (list): Margin size.
            margin_size_posttick (list): Margin size after the tick mark.
            post_label_spaces (float): Space after the label.
            root_spacing (float): Spacing at the root level.
            submenu_pre_spacing (float): Pre-spacing for submenu items.
            submenu_spacing (float): Spacing for submenu items.
            submenu_icon_size (float): Size of the submenu icons.
            item_spacing (list): Spacing for menu items.
            icon_spacing (list): Spacing for icons.
            hotkey_spacing (list): Spacing for hotkeys.
            color_label_enabled (int): Color of the label when enabled.
            color_label_disabled (int): Color of the label when disabled.
            color_tick_enabled (int): Color of the tick mark when enabled.
            color_tick_disabled (int): Color of the tick mark when disabled.
            color_separator (int): Color of the separators.
            color_icon_enabled (int): Color of the icon when enabled.
            color_icon_disabled (int): Color of the icon when disabled.
            menu_title_text_color (int): Color of the menu title text.
            menu_title_color (int): Color of the menu title.
            menu_title_line_color (int): Color of the menu title line.
            menu_title_text_height (float): Height of the menu title text.
            menu_title_text_spacer (list): Spacer size for the menu title text.
            menu_title_close_icon_size (float): Size of the close icon in the menu title.
            menu_title_close_color (int): Color of the close icon in the menu title.
            menu_headfoot_spacing (float): Menu header & footer spacing.
            show_menu_titles (bool): Whether to show menu titles.
            indent_all_ticks (bool): Whether to indent all tick marks.
        
    """
    def _IconMenuBaseDelegate__update_style(self):
        ...
    def __init__(self, **kwargs):
        """
        Initializes the IconMenuBaseDelegate.
        """
    def _build_item_get_style(self, item: omni.ui._ui.Menu) -> dict:
        ...
    def _build_item_glyph(self, item: omni.ui._ui.Menu):
        ...
    def _build_item_header(self, item: omni.ui._ui.Menu):
        ...
    def _build_item_hotkey(self, item: omni.ui._ui.Menu):
        ...
    def _build_item_label(self, item: omni.ui._ui.Menu):
        ...
    def _build_item_subdir(self, item: omni.ui._ui.Menu):
        ...
    def _build_item_tick(self, item: omni.ui._ui.Menu):
        ...
    def _build_item_title(self, item):
        ...
    def build_item(self, item: omni.ui._ui.Widget):
        """
        Build menu omni.ui for item, only uiMenu or uiMenuItem are handled by this function, anything else is handled by the ui.MenuDelegate base-class. Can be overridden on subclass along with _build_item_header, _build_item_tick, _build_item_glyph, _build_item_label, _build_item_hotkey, _build_item_subdir.
        
                Args:
                    item (ui.Widget): The menu item to build.
        
                Returns:
                    None
                
        """
    def build_status(self, item):
        """
        Builds the footer for a menu item.
        
                Args:
                    item (ui.MenuItem): The menu item for which to build the footer.
        
                Returns:
                    None
                
        """
    def build_title(self, item):
        """
        Builds the header for a menu item.
        
                Args:
                    item (ui.MenuItem): The menu item for which to build the header.
        
                Returns:
                    None
                
        """
    def get_style(self):
        """
        Get current style
        
                Returns:
                    DictReadOnly: The current menu style.
                
        """
    def load_settings(self, extension):
        """
        Loads settings from /exts/{extension}/* which control how menus are built.
        
                Args:
                    extension (str): Extension identifier for settings.
                
        """
class MenuEventType:
    """
    Enum for menu activation events
    
        This class represents different types of events that can trigger the activation of a menu.
        
    """
    ACTIVATE: typing.ClassVar[int] = 0
class uiMenu(omni.ui._ui.Menu):
    """
    ui.Menu subclass. Has glyph, menu_checkable, menu_hotkey_text, submenu and parent_menu properties
    
        Args:
            args: Arguments for the ui.Menu constructor.
    
        Keyword Args:
            glyph: The glyph associated with the menu.
            menu_checkable: If the menu is checkable.
            menu_hotkey_text: The hotkey text for the menu.
            submenu: If the menu is a submenu.
            parent_menu: The parent menu.
        
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes the uiMenu instance.
        """
class uiMenuItem(omni.ui._ui.MenuItem):
    """
    ui.MenuItem subclass. Has glyph, menu_checkable, menu_hotkey_text, and parent_menu properties
    
        Args:
            args: Positional arguments passed to the parent class.
    
        Keyword Args:
            glyph: Custom glyph for the menu item.
            menu_checkable: Indicates if the menu item is checkable.
            menu_hotkey_text: Hotkey text for the menu item.
            parent_menu: Reference to the parent menu.
            radio_group: Radio group to which this menu item belongs.
        
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the uiMenuItem class.
        """
def has_delegate_func(delegate, func_name):
    """
    Checks if delegate class has func_name function.
    
        Args:
            delegate (object): The delegate object to check.
            func_name (str): The name of the function to look for.
    
        Returns:
            bool: True if the delegate has a callable function with the given name, otherwise False.
        
    """
