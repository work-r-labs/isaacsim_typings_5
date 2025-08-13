from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.property.usd.usd_model_base import UsdBase
from omni.kit.property.usd.usd_model_items import OptionItem
from omni import ui
from pxr import Sdf
from pxr import Usd
import pxr.Usd
__all__: list = ['MetadataObjectModel']
class MetadataObjectModel(omni.ui._ui.AbstractItemModel, omni.kit.property.usd.usd_model_base.UsdBase):
    """
    The value model that is reimplemented in Python to watch a USD paths.
        Paths can be either Attribute or Prim paths
    """
    def __init__(self, stage: pxr.Usd.Stage, object_paths: typing.List[pxr.Sdf.Path], self_refresh: bool, metadata: dict, key: str, default, options: list):
        ...
    def _current_index_changed(self, model):
        """
        
                Handles the change of the current index.
        
                This method updates the value of the current index and triggers an item change event.
        
                Args:
                    model: The model that triggered the change.
                
        """
    def _get_default_value(self, prop, metadata = None):
        """
        
                Retrieves the default value for a property.
        
                This method returns the default value for the given property.
        
                Args:
                    prop: The property to get the default value for.
                    metadata: The metadata to get the default value for.
        
                Returns:
                    The default value for the given property.
                
        """
    def _on_dirty(self):
        """
        
                Handles the dirty state of the model.
        
                This method handles the dirty state of the model and triggers an item change event.
                
        """
    def _read_value(self, obj: pxr.Usd.Object, time_code: pxr.Usd.TimeCode):
        """
        
                Reads the value of the model.
        
                This method reads the value of the model and returns it.
                
        """
    def _update_option(self):
        """
        
                Updates the options for the combobox.
        
                This method updates the options for the combobox and triggers an item change event.
                
        """
    def _update_value(self, force = False):
        """
        
                Updates the value of the model.
        
                This method updates the value of the model and triggers an item change event.
                
        """
    def _write_value(self, objects: list, key: str, value):
        """
        
                Writes the value of the model.
        
                This method writes the value of the model to the objects.
                
        """
    def begin_edit(self):
        """
        
                Begins the edit process.
        
                This method is not supported in MetadataObjectModel.
                
        """
    def clean(self):
        ...
    def end_edit(self):
        """
        
                Ends the edit process.
        
                This method is not supported in MetadataObjectModel.
                
        """
    def get_item_children(self, item):
        """
        
                Retrieves the children of an item.
        
                This method returns the children of the given item.
        
                Args:
                    item: The item to get children for.
        
                Returns:
                    list: A list of children for the given item.
                
        """
    def get_item_value_model(self, item, column_id):
        """
        
                Retrieves the value model for an item.
        
                This method returns the value model for the given item.
        
                Args:
                    item: The item to get the value model for.
                    column_id: The column ID to get the value model for.
        
                Returns:
                    The value model for the given item.
                
        """
    def is_different_from_default(self) -> bool:
        """
        
                Checks if the value is different from the default.
        
                This method checks if the value is different from the default.
        
                Returns:
                    bool: True if the value is different from the default, False otherwise.
                
        """
    def set_default(self, comp = -1):
        """
        
                Sets the default value for the model.
        
                This method sets the default value for the model and triggers an item change event.
                
        """
    def set_value(self, value, comp = -1):
        """
        
                Sets the value of the model.
        
                This method sets the value of the model and triggers an item change event.
                
        """
