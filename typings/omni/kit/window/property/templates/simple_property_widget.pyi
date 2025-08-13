"""

SimplePropertyWidget class.
"""
from __future__ import annotations
import asyncio as asyncio
import carb as carb
import dataclasses
from dataclasses import dataclass
import functools as functools
import omni as omni
from omni.kit.async_engine.async_engine import run_coroutine
from omni.kit.widget.highlight_label.highlight_label import HighlightLabel
from omni.kit.window.property.property_widget import PropertyWidget
from omni.kit.window.property.style import get_style
from omni.kit.window.property.templates.header_context_menu import GroupHeaderContextMenu
from omni.kit.window.property.templates.header_context_menu import GroupHeaderContextMenuEvent
from omni import ui
import traceback as traceback
import typing
__all__: list = ['LABEL_WIDTH', 'LABEL_WIDTH_LIGHT', 'LABEL_HEIGHT', 'HORIZONTAL_SPACING', 'build_frame_header', 'SimplePropertyWidget', 'GroupHeaderContextMenu', 'GroupHeaderContextMenuEvent', 'PropertyWidget', 'ButtonItem']
class ButtonItem:
    """
    
        A dataclass for a button item.
        
    """
    __dataclass_fields__: typing.ClassVar[dict]  # value = {'text': Field(name='text',type=<class 'str'>,default='',default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'icon': Field(name='icon',type=<class 'str'>,default='',default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'width': Field(name='width',type=<class 'int'>,default=0,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'height': Field(name='height',type=<class 'int'>,default=0,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'enabled': Field(name='enabled',type=<class 'bool'>,default=True,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'callback_fn': Field(name='callback_fn',type=<built-in function callable>,default=None,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'identifier': Field(name='identifier',type=<class 'str'>,default='',default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD)}
    __dataclass_params__: typing.ClassVar[dataclasses._DataclassParams]  # value = _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False)
    __hash__: typing.ClassVar[None] = None
    __match_args__: typing.ClassVar[tuple] = ('text', 'icon', 'width', 'height', 'enabled', 'callback_fn', 'identifier')
    callback_fn = None
    enabled: typing.ClassVar[bool] = True
    height: typing.ClassVar[int] = 0
    icon: typing.ClassVar[str] = ''
    identifier: typing.ClassVar[str] = ''
    text: typing.ClassVar[str] = ''
    width: typing.ClassVar[int] = 0
    def __eq__(self, other):
        ...
    def __init__(self, text: str = '', icon: str = '', width: int = 0, height: int = 0, enabled: bool = True, callback_fn: callable = None, identifier: str = '') -> None:
        ...
    def __repr__(self):
        ...
class SimplePropertyWidget(omni.kit.window.property.property_widget.PropertyWidget):
    """
    
        SimplePropertyWidget provides a simple vertical list of "Label" -> "Value widget" pair layout.
        
    """
    @staticmethod
    def _delayed_rebuild(*args, **kwargs):
        ...
    def __init__(self, title: str, collapsed: bool = False, collapsable: bool = True):
        """
        Initialize class function
        
                Args:
                    collapsed (bool): Default Collapsed state of frame.
                    collapsable (collapsable): Created frame is CollapsibleFrame/Frame.
                
        """
    def _build_frame(self):
        ...
    def _build_frame_header(self, collapsed, text: str, group_id: str = None):
        ...
    def _build_frame_header_with_buttons(self, collapsed, text: str, group_id: str, button_list: list):
        ...
    def _on_filter_changed(self, model: omni.ui._ui.AbstractValueModel):
        """
        
                Called when filter changes. Default calls request_rebuild().
                Derived classes can override to optimize by selectively changing property visibility.
        
                Args:
                    model (ui.AbstractValueModel): model.
                
        """
    def add_item(self, label: str, value):
        """
        
                This function is supposed to be called inside of build_items function.
                Adds a "Label" -> "Value widget" pair item to the widget. "value" will be an uneditable string in a StringField.
        
                Args:
                    label (str): The label text of the entry.
                    value: The value to be stringified and displayed in a StringField.
                
        """
    def add_item_with_model(self, label: str, model, editable: bool = False, identifier: str = None):
        """
        
                This function is supposed to be called inside of build_items function.
                Adds a "Label" -> "Value widget with model" pair item to the widget. "value" will be an editable string in a
                StringField backed by supplied model.
        
                Args:
                    label (str): The label text of the entry.
                    model: The model to be used by the string field.
                    editable: If the StringField generated from model should be editable. Default is False.
                
        """
    def add_label(self, label: str):
        """
        
                Add a Label with a highlight text based on current filter
        
                Args:
                    label (str): Name of label.
                
        """
    def build_impl(self):
        """
        See PropertyWidget.build_impl.
        """
    def build_items(self):
        """
        
                When derived from SimplePropertyWidget, override this function to build your items.
                
        """
    def clean(self):
        """
        
                See PropertyWidget.clean
                
        """
    def on_collapsed_changed(self, collapsed):
        """
        Update collapsed state.
        
                Args:
                    collapsed (bool): New state of collapsed frame.
                
        """
    def on_new_payload(self, payload, ignore_large_selection = False) -> bool:
        """
        
                See PropertyWidget.on_new_payload
                
        """
    def request_rebuild(self):
        """
        
                Request the widget to rebuild.
                It will be rebuilt on next frame.
                
        """
    def reset(self):
        """
        
                See PropertyWidget.reset
                
        """
def build_frame_header(collapsed, text: str, group_id: str = None):
    """
    Custom header for CollapsibleFrame
    
        Args:
            collapsed (bool): Default collapsed state.
            text (str): Name of CollapsibleFrame.
            group_id (str): Group identifier, which is passed to GroupHeaderContextMenuEvent.
        
    """
def build_frame_header_with_buttons(collapsed, text: str, group_id: str, button_list: list):
    """
    Custom header for CollapsibleFrame
    
        Args:
            collapsed (bool): Default collapsed state.
            text (str): Name of CollapsibleFrame.
            group_id (str): Group identifier, which is passed to GroupHeaderContextMenuEvent.
        
    """
def handle_exception(func):
    """
    
        Decorator to print exception in async functions.
        
    """
HORIZONTAL_SPACING: int = 4
LABEL_HEIGHT: int = 18
LABEL_WIDTH: int = 160
LABEL_WIDTH_LIGHT: int = 235
