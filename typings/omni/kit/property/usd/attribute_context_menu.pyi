from __future__ import annotations
import carb as carb
import contextlib as contextlib
from functools import partial
import omni as omni
from omni.kit.property.usd.usd_attribute_model import GfVecAttributeModel
from omni.kit.property.usd.usd_attribute_model import MdlEnumAttributeModel
from omni.kit.property.usd.usd_attribute_model import TfTokenAttributeModel
from omni.kit.property.usd.usd_attribute_model import UsdAttributeModel
from omni.kit.property.usd.usd_model_base import UsdBase
from omni.kit.usd.layers._impl.extension import get_layers
from omni.kit.usd.layers._omni_kit_usd_layers import LayerEditMode
from pxr import Sdf
import typing
import weakref as weakref
__all__: list = list()
class AttributeContextMenu:
    """
    
        Attribute context menu.
        
    """
    _instance: typing.ClassVar[AttributeContextMenu]  # value = <omni.kit.property.usd.attribute_context_menu.AttributeContextMenu object>
    @classmethod
    def get_instance(cls):
        """
        
                Get the instance of the attribute context menu.
                
        """
    def __del__(self):
        """
        
                Delete the attribute context menu.
                
        """
    def __init__(self):
        """
        
                Initialize the attribute context menu.
                
        """
    def _link_attributes(self, link_or_unlink, layer_identifier, objects):
        """
        
                Link attributes.
        
                Args:
                    link_or_unlink (bool): Whether to link or unlink.
                    layer_identifier (str): The layer identifier.
                
        """
    def _lock_attributes(self, lock_or_unlock, objects):
        """
        
                Lock attributes.
        
                Args:
                    lock_or_unlock (bool): Whether to lock or unlock.
                
        """
    def _register_context_menus(self):
        """
        
                Register the context menus.
                
        """
    def _register_copy_paste_menus(self):
        """
        
                Register the copy paste menus.
                
        """
    def _register_copy_prop_path_menu(self):
        """
        
                Register the copy property path menu.
                
        """
    def _register_delete_prop_menu(self):
        """
        
                Register the delete property menu.
                
        """
    def destroy(self):
        """
        
                Destroy the attribute context menu.
                
        """
    def on_mouse_event(self, event: AttributeContextMenuEvent):
        """
        
                On mouse event.
        
                Args:
                    event (AttributeContextMenuEvent): The event.
                
        """
class AttributeContextMenuEvent:
    """
    
        Event for the attribute context menu.
        
    """
    def __init__(self, widget, attribute_paths, stage, time_code, model, comp_index):
        ...
