from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.usd import layers
from omni.kit.usd.layers._impl.layer_utils import LayerUtils
from omni.kit.widget.layers.models.layer_latest_model import LayerLatestModel
from omni.kit.widget.layers.models.layer_live_update_model import LayerLiveUpdateModel
from omni.kit.widget.layers.models.layer_name_model import LayerNameModel
from omni.kit.widget.layers.models.live_session_user_model import LiveSessionUserModel
from omni.kit.widget.layers.models.lock_model import LockModel
from omni.kit.widget.layers.models.muteness_model import MutenessModel
from omni.kit.widget.layers.models.save_model import SaveModel
from omni.kit.widget.layers.path_utils import PathUtils
from omni.kit.widget.layers.prim_spec_item import PrimSpecItem
from omni import ui
import os as os
import pxr.Sdf
from pxr import Sdf
from pxr import Trace
__all__: list = ['LayerItem']
class LayerItem(omni.ui._ui.AbstractItem):
    """
    A single AbstractItemModel item that represents a single sublayer
    """
    @staticmethod
    def _get_item_children(*args, **kwargs):
        ...
    @staticmethod
    def _load_prim_spec_subtree(*args, **kwargs):
        ...
    @staticmethod
    def _prefilter_internal(*args, **kwargs):
        """
        Recursively mark items that meet the filtering rule
        """
    @staticmethod
    def find_all_specs(*args, **kwargs):
        """
        
                Find the child node with given name and return the list of all the
                parent nodes and the found node. It populates the children during
                search.
                
                Args:
                    paths (List[Sdf.Path]): Paths of child prims to find.
                    
                Returns:
                    List[PrimSpecItem]
                
        """
    @staticmethod
    def on_content_changed(*args, **kwargs):
        """
        
                Handles updates to content based on changes in prim spec paths.
        
                Args:
                    changed_prim_spec_paths (List[str]): A list of string paths representing the prims that have changed.
        
                Returns:
                    Tuple[Set[PrimSpecItem], Set[PrimSpecItem]]: Two sets containing updated prim spec items. The first set
                    contains items where flags have been updated, and the second set contains items where children have been
                    updated.
                
        """
    def _LayerItem__update_live_session_user_models(self, live_session):
        ...
    def __init__(self, usd_context, identifier: str, layer: pxr.Sdf.Layer, model, parent_item):
        """
        
                Initializes a new instance of the LayerItem class.
        
                Args:
                    usd_context (omni.usd.UsdContext): The USD context associated with the item.
                    identifier (str): The identifier of the item.
                    layer (Sdf.Layer): The Sdf.Layer object associated with the item.
                    model (LayerModel): The model associated with the item.
                    parent_item (LayerItem): The parent item of the item.
                
        """
    def __repr__(self):
        ...
    def __str__(self):
        ...
    def _clear_cache(self):
        ...
    def _create_all_parent_items(self, item: omni.kit.widget.layers.prim_spec_item.PrimSpecItem, filtered = False):
        ...
    def _get_item_from_cache(self, prim_spec_path: pxr.Sdf.Path, create = False):
        ...
    def _notify_muteness_changed(self):
        ...
    def _on_layer_events(self, event):
        ...
    def _remove_cache_item(self, prim_spec_path):
        ...
    def destroy(self):
        """
        Clean up used model and subscription.
        """
    def get_item_value_model(self, column_id):
        """
        
                Returns the value model associated with the specified column ID.
        
                Args:
                    column_id (int): The ID of the column.
        
                Returns:
                    model(omni.ui.AbstractValueModel): The value model associated with the column.
        
                
        """
    def on_layer_edit_mode_changed(self):
        """
         Notifies all items in the prim specs cache about the change in layer edit mode.
        """
    def on_layer_lock_changed(self):
        """
         Handles the change of layer lock status. 
        """
    def on_layer_outdate_state_changed(self):
        """
        Updates the layer's auto-reload and outdated status based on the current state.
        """
    def on_live_session_state_changed(self):
        """
         Handles the change of live session state.
        """
    def on_muteness_changed(self):
        """
         Handles the change of muteness state.
        """
    def on_muteness_scope_changed(self):
        """
         Handles the change of muteness scope. 
        """
    def prefilter(self, text: str):
        """
        
                Applies prefiltering with the given text.
        
                Args:
                    text (str): The text to be prefiltered.
                
        """
    def reload(self):
        """
         Reload the layer of this layer item. 
        """
    def save(self, on_save_done = None):
        """
         
                Save the layer of this layer item.
                
                Args:
                    on_save_done (Callable, optional): Callback function to be called when save is done. 
                        Signature is fn(bool, str, List[str])->None. Defaults to None. 
                
                
        """
    def update_flags(self):
        """
         Updates the flag attributes of the layer item.
        """
    def update_spec_links_status(self, spec_paths: typing.List[typing.Union[pxr.Sdf.Path, str]]):
        """
        
                Updates the status of spec links for the provided spec paths.
        
                Args:
                    spec_paths (List[Union[str, Sdf.Path]]): The list of spec paths to update.
                
        """
    def update_spec_locks_status(self, spec_paths: typing.List[typing.Union[pxr.Sdf.Path, str]]):
        """
        
                Updates the status of spec locks for the provided spec paths.
        
                Args:
                    spec_paths (List[Union[str, Sdf.Path]]): The list of spec paths to update.
                
        """
    @property
    def absolute_root_spec(self):
        """
        The prim spec that represents the root of prim tree.
        """
    @property
    def add_sublayer(self, sublayer_item):
        """
        
                Adds a sublayer item to the layer item.
        
                Args:
                    sublayer_item(:obj:'LayerItem'): The sublayer item to be added.
                
        """
    @property
    def anonymous(self):
        """
        If this layer is anonymous layer.
        """
    @property
    def auto_reload(self):
        """
        Reload changes automatically.
        """
    @auto_reload.setter
    def auto_reload(self, value):
        ...
    @property
    def base_layer(self):
        """
        
                If this layer is a live session layer, this property can be used to access its
                base layer item.
                
                Returns:
                    :obj:'LayerItem'
                
        """
    @property
    def can_live_update(self):
        """
        Indicates whether the layer supports live updates.
        """
    @property
    def current_live_session(self):
        """
        
                If this layer is in a live session or it's a live session layer, it's to return the live session.
                
                Returns:
                    :obj:'LiveSession'
                
        """
    @property
    def dirty(self):
        """
        If this layer has unsaved changes.
        """
    @dirty.setter
    def dirty(self, value):
        ...
    @property
    def edit_layer_in_auto_authoring_mode(self):
        """
        Indicates whether the layer is being edited in auto-authoring mode.
        """
    @edit_layer_in_auto_authoring_mode.setter
    def edit_layer_in_auto_authoring_mode(self, value):
        """
        
                Sets the edit mode state of the layer and notifies the model if the state changes.
        
                Args:
                    value (bool): The new edit mode state to be set for the layer.
                
        """
    @property
    def editable(self):
        """
        Indicates whether the layer is writable.
        """
    @property
    def filtered(self):
        """
        If this layer item is filtered in the search list.
        """
    @property
    def from_session_layer(self):
        """
        
                If this layer is under the session layer.
        
                Returns:
                    bool
                
        """
    @property
    def globally_muted(self):
        """
        
                Globally mute is the mute value saved in custom data. The muteness of USD
                layer is dependent on the muteness scope (local or global). When it's in global mode,
                the muteness of USD layer is the same as this value.
        
                Returns:
                    bool
                
        """
    @property
    def has_child_edit_layer(self):
        """
        
                Returns whether the layer item has a child with an edit layer.
        
                Returns:
                    bool: True if the layer item has a child with an edit layer, False otherwise.
                
        """
    @property
    def has_child_edit_target(self):
        """
        
                Returns whether the layer item has a child with an edit target.
        
                Returns:
                    bool: True if the layer item has a child with an edit target, False otherwise.
                
        """
    @property
    def has_children(self):
        """
        If this layer item has children.
        """
    @property
    def has_content(self):
        """
        
                Returns whether the layer item has content.
        
                Returns:
                    bool: True if the layer item has content, False otherwise.
                
        """
    @property
    def identifier(self):
        """
        Identifier of this layer item.
        """
    @property
    def is_edit_target(self):
        """
        
                Returns whether layer item is the edit target.
        
                Returns:
                    bool
                
        """
    @is_edit_target.setter
    def is_edit_target(self, value):
        """
        
                Sets the value of the edit target property and notifies the model of the item change.
        
                Args:
                    value (bool): The value to set for edit target property.       
                
        """
    @property
    def is_in_live_session(self):
        """
        
                A layer is in live session means it joins a live session. This is only true when it's
                the base layer of the live session. For live session layer, it's false.
                
                Returns:
                    bool
                
        """
    @property
    def is_live_session_layer(self):
        """
        
                A layer is a live session layer if it's from a live session and it's the root layer
                of that session with extension .live.
                
                Returns:
                    bool
                
        """
    @property
    def is_omni_layer(self):
        """
        
                If the item represents an omni layer.
        
                Returns:
                    bool: True if the item represents an omni layer, False otherwise.
                
        """
    @property
    def is_omni_live_path(self):
        """
        
                If the item represents an omni live layer.
        
                Returns:
                    bool: True if the item represents an omni live layer, False otherwise.
                
        """
    @property
    def latest(self):
        """
        
                If this layer is latest. It only applies to omniverse layer.
                
                Returns:
                    bool       
                
        """
    @property
    def layer(self):
        """
        
                Getter method for the 'layer' property.
        
                Returns:
                    Sdf.Layer: The layer associated with the item.
                
        """
    @property
    def live(self):
        """
        
                If this live is in live sync. It only applies to omniverse layer.
                
                Returns:
                    bool
                
        """
    @property
    def live_session_layer(self):
        """
        
                If this layer is in live session, this property can be used to access its
                corresponding live session layer item.
                
                Returns:
                    :obj:'LayerItem'
                
        """
    @property
    def locally_muted(self):
        """
        
                Local mute is the muteness when it's in local scope.
        
                Returns:
                    bool       
                
        """
    @property
    def locked(self):
        """
        
                Returns the locked status of the layer item.
        
                Returns:
                    bool: True if the layer item is locked, False otherwise.
                
        """
    @locked.setter
    def locked(self, value):
        """
        
                Sets the locked status of the layer item.
        
                Args:
                    value (bool): The locked status to set for the layer item.
                
        """
    @property
    def missing(self):
        """
        Indicates whether the layer is missing.
        """
    @missing.setter
    def missing(self, value):
        """
        
                Sets the missing state of the layer and triggers a model update.
        
                Args:
                    value (bool): The new missing state to be set for the layer.
                
        """
    @property
    def model(self):
        """
        
                Getter method for the 'model' property.
        
                Returns:
                    :obj:'LayerModel': The model associated with the item.
                
        """
    @property
    def muted(self):
        """
        
                If this layer is muted..
                
                Returns:
                    bool
                
        """
    @muted.setter
    def muted(self, value):
        """
        
                Set this layer's is muteness.
        
                Args:
                    value(bool): Muteness to set.
                
        """
    @property
    def muted_or_parent_muted(self):
        """
        
                If this layer is muted or its parent is muted.
                
                Returns:
                    bool
                
        """
    @property
    def name(self):
        """
        Name of this layer item.
        """
    @property
    def outdated(self):
        """
        If this layer item is outdated.
        """
    @property
    def parent(self):
        """
        Parent layer item.
        """
    @property
    def prim_specs(self):
        """
        Prim specs under this layer.
        """
    @property
    def read_only_on_disk(self):
        """
        Indicates whether the layer is read-only on disk.
        """
    @property
    def reserved(self):
        """
        If this is the root or session layer.
        """
    @property
    def selected(self):
        """
        If this layer is selected in layer window.
        """
    @selected.setter
    def selected(self, value):
        """
        
                Sets the selected state of the layer and notifies the model if the state changes.
        
                Args:
                    value (bool): The new selected state to be set for the layer.
                
        """
    @property
    def sublayers(self):
        """
        
                Subayer items under this layer.
        
                Returns:
                    List[LayerItem]
                
        """
    @sublayers.setter
    def sublayers(self, value):
        ...
    @property
    def usd_context(self):
        """
        
                Getter method for the 'usd_context' property.
        
                Returns:
                    Usd.Context: The USD context associated with the item.
                
        """
    @property
    def version(self):
        """
        
                The version of this layer. It only applies to omniverse layer.
                
                Returns:
                    str
                
        """
