"""
Simulated searchable combobox class, used by MaterialListBoxWidget.
"""
from __future__ import annotations
import asyncio as asyncio
import enum
from enum import IntFlag
import omni as omni
from omni.kit.material.library.treeview_model import Constant
from omni import ui
import typing
__all__: list = ['SearchModel', 'SearchWidget']
class SearchModel(omni.ui._ui.AbstractValueModel):
    """
    Simulated searchable combobox model class, used by SearchWidget.
    """
    def __init__(self, modified_fn):
        """
        Initialize class function.
        
                Args:
                    modified_fn (callable): function called when value changed.
                
        """
    def get_value_as_string(self):
        """
        Gets material name as string.
        
                Returns:
                    (str): material name.
                
        """
    def is_in_string(self, string: str):
        """
        Is `string` in SearchModel string, case insensitive.
        
                Args:
                    string (str): string to compare against.
        
                Returns:
                    (bool): True if Is `string` in SearchModel string else False.
                
        """
    def set_value(self, value):
        """
        Set SearchModel string.
        
                Args:
                    value (str): new material name.
                
        """
class SearchWidget:
    """
    Simulated searchable combobox class, used by MaterialListBoxWidget.
    """
    class WidgetFlags(enum.IntFlag):
        """
        build_ui_popup() options
        """
        SHOW_ALL: typing.ClassVar[SearchWidget.WidgetFlags]  # value = <WidgetFlags.SHOW_ALL: 3>
        SHOW_GOTO_BUTTON: typing.ClassVar[SearchWidget.WidgetFlags]  # value = <WidgetFlags.SHOW_GOTO_BUTTON: 2>
        SHOW_OPEN_BUTTON: typing.ClassVar[SearchWidget.WidgetFlags]  # value = <WidgetFlags.SHOW_OPEN_BUTTON: 1>
    def __init__(self, theme: str, icon_path: str, modified_fn: callable = None):
        """
        Initialize class function.
        
                Args:
                    theme (str): theme name, should be "NvidiaDark" or "NvidiaLight". Not wildly supported.
                    icon_path (str): path to icons, if None then omni.kit.material.library/data/icons will be used.
                    modified_fn (callable): modified_fn passed to SearchModel.
                
        """
    def build_ui(self, width: float, search_size: float):
        """
        build_ui for search widget.
        
                Args:
                    width (float): width of ui.StringField widget.
                    search_size (float): size of widget
                
        """
    def build_ui_popup(self, search_size: float, popup_text: str, index: int, update_fn: callable, widget_flags = ..., missing = False):
        """
        Build the UI for the listbox part of the widget.
        
                Args:
                    search_size (float): widget size.
                    popup_text (str): material name selected in combo box.
                    index (int): default index of material name in combo box.
                    update_fn (callable): callback called when ui.TextField string is cleared.
                    widget_flags (WidgetFlags): Can be SHOW_OPEN_BUTTON and/or SHOW_GOTO_BUTTON or None.
                    missing (bool): Material name is missing, text will be red.
        
                Returns:
                        (ui.Widget) name field
                        (ui.Widget) open button
                        (ui.Widget) goto button
                
        """
    def clean(self):
        """
        Clean up widget.
        """
    def destroy(self):
        """
        Destroy class and cleanup.
        """
    def focus(self):
        """
        Focus search text.
        """
    def get_text(self):
        """
        Get material name as string.
        
                Returns:
                    (str) material name.
                
        """
    def set_placeholder_text(self, msg: str):
        """
        Set material placeholder name from string. This is the string displayed when material name is empty.
        
                Args:
                    msg (str): text to use as placeholder.
                
        """
    def set_text(self, new_text: str):
        """
        Set material name from string.
        
                Args:
                    new_text (str): New material name
                
        """
    def update(self, filter_string: str):
        """
        Update placeholder string and clear button.
        
                Args:
                    filter_string (str): current search string.
                
        """
