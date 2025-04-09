from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.async_engine.async_engine import run_coroutine
from omni.kit import notification_manager as nm
from omni.kit.usd import layers
from omni.kit.usd.layers._impl.layer_utils import LayerUtils
from omni.kit.widget.layers.globals import LayerGlobals
from omni.kit.widget.layers.layer_item import LayerItem
from omni.kit.widget.layers.layer_model_utils import LayerModelUtils
from omni.kit.widget.layers.path_utils import PathUtils
from omni.kit.widget.layers.prim_spec_item import PrimSpecItem
from omni import ui
import os as os
from pxr import Sdf
from pxr import Tf
from pxr import Trace
from pxr import Usd
__all__: list = ['LayerModel']
class LayerModel(omni.ui._ui.AbstractItemModel):
    """
    Class representing the Layer Model.
    """
    @staticmethod
    def _handle_pending_prim_specs(*args, **kwargs):
        ...
    @staticmethod
    def _load_sublayers(*args, **kwargs):
        ...
    @staticmethod
    def _on_attach(*args, **kwargs):
        """
        Called when opening a new stage
        """
    @staticmethod
    def _on_stage_event(*args, **kwargs):
        ...
    @staticmethod
    def filter_by_text(*args, **kwargs):
        """
        
                Specify the filter string that is used to reduce the model.
                
                Args:
                    filter_name_text(str): String used to filter layer's name text.
                
        """
    @staticmethod
    def find_all_specs(*args, **kwargs):
        """
        
                Return the list of all the parent nodes and the node representing the given path.
        
                Args:
                    paths(List[Sdf.Path]): Paths to find specs.
        
                Returns:
                    Tuble(LayerItem, List[PrimSpecItem])
                
        """
    def __init__(self, usd_context, layer_settings = None):
        """
        
                Initialize.
                
                Args:
                    usd_context(omni.usd.UsdContext): The USD context for the layers.
                    layer_settings(LayerSettings): The layer settings.
                
        """
    def _cache_sublayer(self, layer_item: omni.kit.widget.layers.layer_item.LayerItem):
        ...
    def _clear(self):
        ...
    def _clear_sublayer_cache(self):
        ...
    def _gather_all_sublayer_descendants(self, item: omni.kit.widget.layers.layer_item.LayerItem):
        ...
    def _initialize_subscriptions(self):
        ...
    def _is_sublayer_cached(self, layer_item: omni.kit.widget.layers.layer_item.LayerItem):
        ...
    def _on_default_edit_layer_update(self):
        ...
    def _on_detach(self):
        """
        Called when close the stage
        """
    def _on_layer_edit_mode_update(self):
        ...
    def _on_layer_events(self, event: carb.events._events.IEvent):
        ...
    def _on_layer_lock_update(self):
        ...
    def _on_layer_muteness_changed(self):
        ...
    def _on_layer_muteness_scope_changed(self):
        ...
    def _on_prim_spec_changed(self, layer_identifier: str, prim_spec_paths: typing.List[str]):
        ...
    def _on_spec_links_changed(self, spec_paths: typing.List[str]):
        ...
    def _on_spec_locks_changed(self, spec_paths: typing.List[str]):
        ...
    def _on_sublayer_changed(self):
        ...
    def _on_update(self, _):
        ...
    def _remove_cached_sublayer(self, layer_item: omni.kit.widget.layers.layer_item.LayerItem):
        ...
    def _reset_root(self):
        ...
    def _update_default_edit_layer(self, default_edit_layer):
        ...
    def _update_dirtiness(self):
        ...
    def _update_edit_target(self, layer_identifier: str):
        ...
    def add_dirtiness_listener(self, fn: typing.Callable[[], NoneType]):
        """
        
                Add a dirtiness listener.
        
                Args:
                    fn (Callable[[], None]): The function to be added as a dirtiness listener.
                
        """
    def add_layer_muteness_scope_listener(self, fn: typing.Callable[[], NoneType]):
        """
        
                Add a muteness scope listener.
        
                Args:
                    fn (Callable[[], None]): The function to be added as a muteness scope listener.
                
        """
    def add_stage_attach_listener(self, fn: typing.Callable[[bool], NoneType]):
        """
        
                Add a stage attachment listener.
        
                Args:
                    fn (Callable[[bool], None]): The function to be added as a stage attachment listener.
                
        """
    def can_item_have_children(self, item):
        """
        
                Check if an item can have children.
        
                Args:
                    item(omni.ui.AbstractItem): The item to check.
                
        """
    def destroy(self):
        """
        Destroys the LayerModel instance.
        """
    def drop(self, target_item, source, drop_location = -1):
        """
        
                Reimplemented from AbstractItemModel. Called when dropping something to the item.
        
                Args:
                    target_item(:obj:'LayerItem'): The target item to drop onto.
                    source(:obj:'LayerItem'): The source item being dragged.
                    drop_location(int): The location to drop the item (default: -1).
                
        """
    def drop_accepted(self, target_item, source, drop_location = -1):
        """
        
                Reimplemented from AbstractItemModel. Called to highlight target when drag and drop.
                Returns whether the drop is accepted.
        
                Args:
                    target_item(:obj:'LayerItem'): The target item to drop onto.
                    source(:obj:'LayerItem'): The source item being dragged.
                    drop_location(int): The location to drop the item (default: -1).
        
                Returns:
                    bool: True if the drop is accepted, False otherwise.
                
        """
    def flatten_all_layers(self):
        """
         Flatten all layers if there is not layer locked. 
        """
    def get_all_dirty_layer_identifiers(self, include_omni_layers = True, include_local_layers = True):
        """
        
                Returns a list of all dirty layer identifiers.
        
                Args:
                    include_omni_layers(bool): Whether to include Omni layers (default: True).
                    include_local_layers(bool): Whether to include local layers (default: True).
        
                Returns:
                    List[str]
                
        """
    def get_drag_mime_data(self, item):
        """
        
                Returns Multipurpose Internet Mail Extensions (MIME) data for be able to drop this item somewhere.
                
                Args:
                    item(:obj:'omni.ui.AbstractItem'): The target item to drop.
        
                Returns:
                    str
                
        """
    def get_item_children(self, item):
        """
        
                Get the children of an item, reimplemented from AbstractItemModel.
        
                Args:
                    item(omni.ui.AbstractItem): The item whose children are to be retrieved.
        
                Returns:
                    List: A list containing the children of the item.
                
        """
    def get_item_value_model(self, item, column_id):
        """
        
                Reimplemented from AbstractItemModel.
                Returns the value model for the given item and column ID.
        
                Args:
                    item(:obj:'LayerItem'): The item to get the value model for.
                    column_id(int): The column ID to get the value model for.
        
                Returns:
                    omni.ui.AbstractValueModel
                
        """
    def get_item_value_model_count(self, item):
        """
        
                Reimplemented from AbstractItemModel, returns the number of value models for the given item.
        
                Args:
                    item: The item to get the value model count for.
        
                Returns:
                    int: The number of value models (7).
        """
    def get_layer_item_by_identifier(self, layer_identifier):
        """
        
                Find the first layer item that has the identifier
        
                Args:
                    layer_identifier(str): The identifier of the layer item to find.
        
                Returns:
                    :obj:'LayerItem': The first layer item with the given identifier, or None if not found.
                
        """
    def has_any_layers_locked(self):
        """
        
                Checks if any layers are locked.
        
                Returns:
                    bool: True if any layers are locked, False otherwise.
                
        """
    def has_dirty_layers(self, include_omni_layers = True, include_local_layers = True):
        """
        
                Checks if there are any dirty layers in the current stage.
        
                Args:
                    include_omni_layers (bool, optional): Whether to include omni layers.
                                                        Defaults to True.
                    include_local_layers (bool, optional): Whether to include local layers.
                                                        Defaults to True.
        
                Returns:
                    bool: True if there are any dirty layers, False otherwise.
                
        """
    def has_outdated_layers(self):
        """
        
                Checks if there are any outdated layers in the sublayers cache.
        
                Returns:
                    bool: True if there are any outdated layers, False otherwise.
                
        """
    def refresh(self):
        """
        Force full re-update
        """
    def save_layers(self, layer_identifiers, on_save_done: typing.Callable[[bool, str, typing.List[str]], NoneType] = None):
        """
        
                Saves multiple layers asynchronously and executes a callback on completion.
        
                Args:
                    layer_identifiers (List[str]): A list of identifiers for the layers to be saved.
                    on_save_done (Callable[[bool, str, List[str]], None], optional): A callback function to be called upon
                        completion of the save operation. The function singature is: on_save_done(bool, str, List[str]).
                
        """
    def set_edit_target(self, layer_item: omni.kit.widget.layers.layer_item.LayerItem, saved = False):
        """
        
                Sets the edit target with the given layer item's identifier.
        
                Args:
                    layer_item (:obj:'LayerItem'): The LayerItem to set as the edit target.
                    saved (bool): Whether the edit target has been saved (default: False).
                
        """
    @property
    def auto_authoring_mode(self):
        """
        
                If the edit mode is 'AUTO_AUTHORING'.
        
                Returns:
                    bool: True if the edit mode is 'AUTO_AUTHORING', False otherwise.
                
        """
    @auto_authoring_mode.setter
    def auto_authoring_mode(self, value):
        """
        
                Setter method for the 'auto_authoring_mode' property.
                This property sets the edit mode based on the given value.
        
                Args:
                    value (bool): True to set layers to auto authoring mode, False to normal mode.
                
        """
    @property
    def default_edit_layer(self):
        """
        
                The default edit layer. (Only useful when edit mode is AUTO_AUTHORING or SPECS_LINKING).
        
                Returns:
                    str: The default edit layer.
                
        """
    @default_edit_layer.setter
    def default_edit_layer(self, value):
        """
        
                Setter method for the 'default_edit_layer' property.
                This property sets the default edit layer.
        
                Args:
                    value (str): The new value for the 'default_edit_layer' property.
                
        """
    @property
    def global_muteness_scope(self):
        """
        
                If the layers' muteness scope is global.
        
                Returns:
                    bool: True if the layers' muteness scope is global, False otherwise.
                
        """
    @global_muteness_scope.setter
    def global_muteness_scope(self, value: bool):
        """
        
                Setter method for the 'global_muteness_scope' property.
        
                Args:
                    value (bool): The new value for the layers muteness scope.
                
        """
    @property
    def is_in_live_session(self):
        """
        
                If the layer is in live session.
        
                Returns:
                    bool: True if the stage is in live session, False otherwise.
                
        """
    @property
    def normal_mode(self):
        """
        
                If the edit mode is 'NORMAL'.
        
                Returns:
                    bool: True if the edit mode is 'NORMAL', False otherwise.
                
        """
    @property
    def root_layer_item(self):
        """
        
                Root layer item.
        
                Returns:
                    :obj:'LayerItem'.
                
        """
    @property
    def session_layer_item(self):
        """
        
                The session layer item
        
                Returns:
                    :obj:'LayerItem'.
                
        """
    @property
    def spec_linking_mode(self):
        """
        
                If the edit mode is 'SPECS_LINKING'.
        
                Returns:
                    bool: True if the edit mode is 'SPECS_LINKING', False otherwise.
                
        """
    @spec_linking_mode.setter
    def spec_linking_mode(self, value):
        """
        
                Setter method for the 'spec_linking_mode' property.
                This property sets the edit mode based on the given value.
        
                Args:
                    value (bool): True to set layers to spec linking mode, False to normal mode.
                
        """
    @property
    def usd_context(self):
        """
        
                UsdContext corresponding to this model.
        
                Returns:
                    :obj:'omni.usd.UsdContext'.
                
        """
