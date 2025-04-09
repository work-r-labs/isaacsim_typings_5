"""
A module providing VecAttributeModel, a UI model for editing vector attributes with mathematical operations support.
"""
from __future__ import annotations
from omni import ui
import omni.ui._ui
from pxr import Gf
import weakref as weakref
__all__ = ['Gf', 'VecAttributeModel', 'ui', 'weakref']
class VecAttributeModel(omni.ui._ui.AbstractItemModel):
    """
    A class representing a model for vector attributes with editable string fields.
    
        This model is designed to parse string values for vector attributes, allowing for
        mathematical operations to be performed on the vector's components. It uses
        internal string models to represent float values as strings. It provides
        callbacks for beginning and ending edit operations on vector components.
    
            Args:
                default_value: The default value to initialize each component of the vector.
                begin_edit_callback (Callable[[None], None]): Optional; a callback function
                    that is invoked when editing of a component begins.
                end_edit_callback (Callable[[Gf.Vec3d], None]): Optional; a callback function
                    that is invoked when editing of a component ends, receiving the edited
                    value as an argument.
    """
    def __init__(self, default_value, begin_edit_callback: typing.Callable[[NoneType], NoneType] = None, end_edit_callback: typing.Callable[[pxr.Gf.Vec3d], NoneType] = None):
        """
        Initializer for VecAttributeModel.
        """
    def _on_value_changed(self, item):
        ...
    def begin_edit(self, item):
        """
        Begins the editing process for the given item.
        
                Args:
                    item: The item that is being edited.
        """
    def end_edit(self, model):
        """
        Ends the editing process for the given model.
        
                Args:
                    model: The model that was being edited.
        """
    def get_item_children(self, item):
        """
        Get the child items of a given item.
        
                Args:
                    item: The item whose children are to be retrieved.
        """
    def get_item_value_model(self, item, column_id):
        """
        Gets the value model for a given item and column.
        
                Args:
                    item: The item for which the value model is needed.
                    column_id: The identifier for the column.
        """
