"""

A menu to set datetime format.
"""
from __future__ import annotations
import carb as carb
from functools import partial
import omni as omni
from omni import ui
__all__: list = ['DatetimeFormatMenu']
class DatetimeFormatMenu:
    """
    
        Menu to set datetime format.
    
        Args:
            value_changed_fn(Callable): function to call when datetime format changed. Function Signature:
                void value_changed_fn()
        
    """
    def __init__(self, value_changed_fn: typing.Callable[[], NoneType] = None):
        ...
    def _build_dateformat_items(self):
        ...
    def _on_datetime_format_changed(self, item, event_type):
        ...
    def destroy(self):
        """
        Destructor
        """
    def show_at(self, x: float, y: float):
        """
         Show the menu at the given position. 
        """
    @property
    def visible(self):
        """
         Return True if the menu is visible. 
        """
    @visible.setter
    def visible(self, value: bool):
        """
         Set visibility of the menu. 
        """
def get_datetime_format():
    """
     Get datetime from settings. 
    """
DATETIME_FORMATS: list = ['MM/DD/YYYY', 'DD.MM.YYYY', 'DD-MM-YYYY', 'YYYY-MM-DD', 'YYYY/MM/DD', 'YYYY.MM.DD']
DATETIME_FORMAT_SETTING: str = '/persistent/app/datetime/format'
