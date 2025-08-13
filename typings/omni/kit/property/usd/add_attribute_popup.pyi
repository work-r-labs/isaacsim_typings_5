from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.property.usd.prim_selection_payload import PrimSelectionPayload
from omni import ui
import pxr.Sdf
from pxr import Sdf
import weakref as weakref
__all__: list = list()
class AddAttributePopup:
    """
    
        Popup for adding an attribute to the selected prims.
        
    """
    def __del__(self):
        """
        
                Delete the popup.
                
        """
    def __init__(self):
        ...
    def click_fn(self, payload: omni.kit.property.usd.prim_selection_payload.PrimSelectionPayload):
        """
        
                Click the popup.
        
                Args:
                    payload (PrimSelectionPayload): The payload of the prim selection.
                
        """
    def destroy(self):
        """
        
                Destroy the popup.
                
        """
    def hide(self):
        """
        
                Hide the popup.
                
        """
    def show_fn(self, objects: dict):
        """
        
                Show the popup.
        
                Args:
                    objects (dict): The objects of the prim selection.
                
        """
class ComboBoxModel(omni.ui._ui.AbstractItemModel):
    """
    
        Model for the combo box.
        
    """
    def __init__(self):
        ...
    def _populate_items(self):
        ...
    def get_item_children(self, item):
        """
        
                Get the children of the item.
        
                Args:
                    item (AbstractItem): The item to get the children of.
                
        """
    def get_item_value_model(self, item, column_id):
        """
        
                Get the value model of the item.
        
                Args:
                    item (AbstractItem): The item to get the value model of.
                    column_id (int): The column id of the item.
                
        """
    def get_selected_item(self):
        """
        
                Get the selected item.
        
                Returns:
                    AbstractItem: The selected item.
                
        """
class ValueTypeNameItem(omni.ui._ui.AbstractItem):
    """
    
        Item for the value type name combo box.
        
    """
    def __init__(self, value_type_name: pxr.Sdf.ValueTypeName, value_type_name_str: str):
        ...
class ValueTypeNameModel(ComboBoxModel):
    """
    
        Model for the value type name combo box.
        
    """
    def _populate_items(self):
        """
        
                Populate the items.
                
        """
class VariabilityItem(omni.ui._ui.AbstractItem):
    """
    
        Item for the variability combo box.
        
    """
    def __init__(self, variability: pxr.Sdf.Variability, variability_str: str):
        ...
class VariabilityModel(ComboBoxModel):
    """
    
        Model for the variability combo box.
        
    """
    def _populate_items(self):
        ...
