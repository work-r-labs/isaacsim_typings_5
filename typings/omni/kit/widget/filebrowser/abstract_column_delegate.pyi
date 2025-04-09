"""

An abstract column delegate class. Subclassed by column delegates used by :obj:`FileBrowserTreeView`.
"""
from __future__ import annotations
import abc as abc
from omni import ui
import typing
__all__: list = ['ColumnItem', 'AbstractColumnDelegate']
class AbstractColumnDelegate:
    """
    
        An abstract object that is used to put the widget to the file browser asynchronously.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset({'build_widget'})
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def build_header(self):
        """
        Build the header
        """
    def build_widget(self, item: ColumnItem):
        """
        
                Build the widget for the given path. Works inside Frame in async
                mode. Once the widget is created, it will replace the content of the
                frame. It allow to await something for a while and create the widget
                when the result is available.
                
        """
    @property
    def initial_width(self):
        """
        The width of the column
        """
class ColumnItem:
    """
     Column Item class to be used with FileBrowserTreeView. 
    """
    def __init__(self, path):
        ...
    @property
    def path(self):
        """
         Path of the item. 
        """
