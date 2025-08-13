from __future__ import annotations
import omni as omni
from omni.kit.property.usd.usd_model_base import UsdBase
from omni.kit.property.usd.usd_model_items import AllowedTokenItem
from omni import ui
from pxr import Sdf
from pxr import Usd
import pxr.Usd
import typing
__all__: list = ['VariantSetModel', 'SelectVariantPrimCommand']
class SelectVariantPrimCommand(omni.kit.commands.command.Command):
    """
    
        Select the variant prim.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, prim_path: str, vset_name: str, var_name: str, usd_context_name: str = ''):
        """
        
                Initialize the command.
        
                Args:
                    prim_path (str): The path of the prim.
                    vset_name (str): The name of the variant set.
                    var_name (str): The name of the variant.
                    usd_context_name (str): The name of the usd context.
                
        """
    def do(self):
        """
        
                Do the command.
                
        """
    def undo(self):
        """
        
                Undo the command.
                
        """
class VariantSetModel(omni.ui._ui.AbstractItemModel, omni.kit.property.usd.usd_model_base.UsdBase):
    """
    
        Model for the variant set.
        
    """
    def __init__(self, stage: pxr.Usd.Stage, object_paths: typing.List[pxr.Sdf.Path], variant_set_name: str, self_refresh: bool):
        ...
    def _current_index_changed(self, model):
        """
        
                The current index changed.
        
                Args:
                    model (ui.SimpleIntModel): The model of the current index.
                
        """
    def _get_variant_set(self):
        """
        
                Get the variant set.
        
                Returns:
                    Usd.VariantSet: The variant set.
                
        """
    def _on_dirty(self):
        """
        
                The dirty event.
                
        """
    def _read_value(self, obj: pxr.Usd.Object, time_code: pxr.Usd.TimeCode):
        """
        
                Read the value.
        
                Args:
                    obj (Usd.Object): The object to read the value from.
                    time_code (Usd.TimeCode): The time code to read the value from.
        
                Returns:
                    str: The value.
                
        """
    def _update_value(self, force = False):
        """
        
                Update the value.
        
                Args:
                    force (bool): Whether to force the update.
                
        """
    def _update_variant_names(self):
        """
        
                Update the variant names.
                
        """
    def begin_edit(self, item = None):
        """
        
                Begin the edit of the item.
        
                Args:
                    item (AbstractItem): The item to begin the edit of.
                
        """
    def clean(self):
        ...
    def end_edit(self, item = None):
        """
        
                End the edit of the item.
        
                Args:
                    item (AbstractItem): The item to end the edit of.
                
        """
    def get_item_children(self, item):
        """
        
                Get the children of the item.
        
                Args:
                    item (AbstractItem): The item to get the children of.
        
                Returns:
                    List[AbstractItem]: The children of the item.
                
        """
    def get_item_value_model(self, item, column_id):
        """
        
                Get the value model of the item.
        
                Args:
                    item (AbstractItem): The item to get the value model of.
                    column_id (int): The column id of the item.
        
                Returns:
                    AbstractItem: The value model of the item.
                
        """
    def set_value(self, value, comp = -1):
        """
        
                Set the value of the item.
        
                Args:
                    value (str): The value to set.
                    comp (int): The component to set.
                
        """
