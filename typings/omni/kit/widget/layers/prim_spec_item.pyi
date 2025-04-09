from __future__ import annotations
import omni as omni
from omni.kit.usd.layers._impl.layer_utils import LayerUtils
from omni.kit.widget.layers.globals import LayerGlobals
from omni.kit.widget.layers.models.prim_name_model import PrimNameModel
from omni import ui
import pxr.Sdf
from pxr import Sdf
from pxr import Trace
import typing
__all__: list = ['PrimSpecItem']
class PrimSpecItem(omni.ui._ui.AbstractItem):
    """
    A single AbstractItemModel item that represents a single prim
    """
    def _PrimSpecItem__update_flags_internal(self):
        ...
    def __init__(self, usd_context, path: pxr.Sdf.Path, layer_item):
        """
        Initializes a PrimSpecItem object.
        
                Args:
                    usd_context (omni.usd.UsdContext): The USD context.
                    path (Sdf.Path): The path to the prim.
                    layer_item (LayerItem): The layer item.
                
        """
    def __repr__(self):
        ...
    def __str__(self):
        ...
    def _get_name_model(self):
        ...
    def _has_missing_reference_in_layer(self, layer_identifier):
        ...
    def _has_missing_references(self, layer, prim_spec):
        ...
    def _initialize_link_and_lock_states(self):
        ...
    def destroy(self):
        """
        Destroys the item object.
        """
    def get_item_value_model(self, column_id):
        """
        
                Retrieves the value of an item in the model based on the given column ID.
        
                Args:
                    column_id (int): The ID of the column for which to retrieve the item value.
        
                Returns:
                    omni.ui.AbstractValueModel: The value of the item in the model.
                
        """
    def on_layer_edit_mode_changed(self):
        """
        Callback function for handling layer edit mode changes.
        """
    def on_layer_muteness_changed(self):
        """
        Callback function for handling layer muteness changes.
        """
    def update_flags(self):
        """
         Updates the flags for this item object.
        """
    @property
    def children(self):
        """
        List of children.
        """
    @property
    def filtered(self):
        """
        
                If this prim spec is filtered in the search list.
                
                Returns:
                    bool
                
        """
    @filtered.setter
    def filtered(self, value):
        """
        
                Setter method for the 'filtered' property.
        
                Args:
                    value (bool): The new value to set for the 'filtered' property.
                
        """
    @property
    def has_children(self):
        """
        
                If the object has children.
        
                Returns
                    bool
                
        """
    @property
    def has_missing_reference(self):
        """
        If this prim spec includes missing references.
        """
    @property
    def instanceable(self):
        """
        
                If this prim spec is instanceable.
                
                Returns:
                    bool
                
        """
    @property
    def layer(self):
        """
        Handle of Sdf.Layer this prim spec resides in.
        """
    @property
    def layer_item(self):
        """
        
                Gets the relate layer item.
                
                Returns:
                    :obj:'LayerItem'
                
        """
    @property
    def linked(self):
        """
        
                If the object is linked.
        
                Returns:
                    bool: True if the object is linked, False otherwise.
                
        """
    @linked.setter
    def linked(self, value):
        """
        
                Setter method for the 'linked' property.
        
                Args:
                    value (bool): The new value to set for the 'linked' property
                
        """
    @property
    def locked(self):
        """
        
                If the object is locked.
        
                Returns:
                    bool: True if the object is locked, False otherwise.
                
        """
    @locked.setter
    def locked(self, value):
        """
        
                Setter method for the 'locked' property.
        
                Args:
                    value (bool): The new value to set for the 'locked' property
                
        """
    @property
    def name(self):
        """
        Name of this prim spec in stage.
        """
    @property
    def parent(self):
        """
        Parent spec.
        """
    @property
    def path(self):
        """
        Path of this prim spec in stage.
        """
    @property
    def prim_spec(self):
        """
        Handle of Sdf.PrimSpec.
        """
    @property
    def specifier(self):
        """
        Specifier of prim spec.
        """
    @property
    def type_name(self):
        """
        Type name of this prim spec in stage.
        """
class PrimSpecSpecifier:
    DEF_ONLY: typing.ClassVar[int] = 1
    DEF_WITH_PAYLOAD: typing.ClassVar[int] = 3
    DEF_WITH_REFERENCE: typing.ClassVar[int] = 2
    OVER_ONLY: typing.ClassVar[int] = 4
    OVER_WITH_PAYLOAD: typing.ClassVar[int] = 6
    OVER_WITH_REFERENCE: typing.ClassVar[int] = 5
    UNKNOWN: typing.ClassVar[int] = 7
def get_prim_specifier(spec):
    ...
