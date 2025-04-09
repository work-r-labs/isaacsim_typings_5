from __future__ import annotations
import carb as carb
from functools import partial
import omni as omni
from omni.kit.usd.layers._impl.layer_utils import LayerUtils
from omni.kit.widget.layers.layer_item import LayerItem
from omni.kit.widget.layers.layer_model_utils import LayerModelUtils
from omni.kit.widget.layers.prim_spec_item import PrimSpecItem
from omni.kit.widget.layers.prim_spec_item import PrimSpecSpecifier
from omni.kit.widget.layers.singleton import Singleton
from omni import ui
from pxr import Sdf
import weakref as weakref
__all__ = ['ContextMenu', 'ContextMenuEvent', 'LayerItem', 'LayerModelUtils', 'LayerUtils', 'PrimSpecItem', 'PrimSpecSpecifier', 'Sdf', 'Singleton', 'carb', 'omni', 'partial', 'ui', 'weakref']
class ContextMenu:
    """
     Context menu for the layers widget
    """
    @staticmethod
    def _get_content_window():
        ...
    @staticmethod
    def _get_layer_item(objects) -> omni.kit.widget.layers.layer_item.LayerItem:
        ...
    @staticmethod
    def _get_prim_spec_item(objects):
        ...
    @staticmethod
    def _stage_window_object(objects: dict) -> dict:
        ...
    @staticmethod
    def add_menu(menu_list):
        """
        
                Add the menu to the end of the context menu. Return the object that
                should be alive all the time. Once the returned object is destroyed,
                the added menu is destroyed as well.
                
        """
    @staticmethod
    def can_be_set_as_authoring_target(objects):
        """
        
                Check if the selected item can be set as authoring target.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def can_delete_prim(objects):
        """
        
                Check if the selected item can be deleted.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def can_edit_root_layer(objects):
        """
        
                Check if selected tree view can edit root layer.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def can_edit_sublayer(objects):
        """
        
                Check if selected layer item can edit sublayer.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def can_edit_sublayer_parent(objects):
        """
        
                Check if selected layer item's parent can edit sublayer.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def can_flatten_sublayers(objects):
        """
        
                Check if selected layer item can flatten sublayer.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def can_merge_layer_down(objects):
        """
        
                Check if the selected layer item can be merged down.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def can_not_edit_sublayer(objects):
        """
        
                Check if selected layer item can edit sublayer.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def can_set_as_edit_target(objects):
        """
        
                Check if selected layer can set as edit target.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def copy_layer_url(objects):
        """
        Deprecated.
        """
    @staticmethod
    def copy_url(objects):
        """
        
                Copy the selected item's url to clipboard.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def create_anonymous_sublayer(objects):
        """
        
                Create anonymous sublayer for selected layer item.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
                
        """
    @staticmethod
    def create_sublayer(objects, anonymous = False):
        """
        
                Create sublayer for selected layer item.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def find_in_browser(objects):
        """
        
                Navigate to selected layer's file if found it in content browser.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def flatten_sublayers(objects):
        """
        
                Faltten selected layer item.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
                
        """
    @staticmethod
    def has_any_items_selected(objects):
        """
        
                Check any items selected.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
                    
                Returns:
                    bool: True if any item selected, otherwise False.    
                
        """
    @staticmethod
    def has_no_layers_locked(objects):
        """
        
                Check if the selected item has not layers locked.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def has_payload_or_reference(objects: dict):
        """
        
                checks if prim has references
                
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def has_sublayers(objects):
        """
        
                Check if the selected stage has sublayers.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def insert_sublayer(objects):
        """
        
                Insert sublayer into selected layer item.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
                
        """
    @staticmethod
    def is_anonymous_layer(objects):
        """
        
                Check if the selected layer item  is anonymous layer.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def is_authoring_layer(objects):
        """
        
                Check if the selected item is authoring layer.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def is_auto_authoring_mode(objects):
        """
        
                Check if the selected item is in auto authoring mode.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def is_auto_authoring_or_spec_linking_mode(objects):
        """
        
                Check if the selected item is in spec linking mode or auto authoring mode.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def is_edit_layer(objects):
        """
        
                Check if the selected item is edit layer item.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def is_from_session_layer_tree(objects):
        """
        
                Check if the selected item is from session layer tree.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def is_item_expaned(objects):
        """
        Unused.
        """
    @staticmethod
    def is_layer_and_parent_unmuted(objects):
        """
        
                Check if the selected layer item is muted and parent muted.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def is_layer_dirty(objects):
        """
        
                Check if the selected layer item is dirty.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def is_layer_item(objects):
        """
        
                Check if the selected item is layer item.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool: True if selected item is layer item, otherwise True.  
                
        """
    @staticmethod
    def is_layer_locked(objects):
        """
        
                Check if the selected layer item is locked.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def is_layer_locked_by_other(objects):
        """
        Deprecated.
        """
    @staticmethod
    def is_layer_not_locked(objects):
        """
        
                Check if the selected layer item is not locked.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def is_layer_not_locked_by_other(objects):
        """
        
                Check if the selected layer item is not locked by other.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def is_layer_or_parent_muted(objects):
        """
        
                Check if the selected layer item is muted or parent muted.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def is_layer_read_only(objects):
        """
        
                Check if the selected layer item is not locked.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def is_layer_writable(objects):
        """
        
                Check if the selected layer item is writable.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def is_live_session_layer(objects):
        """
        
                Check if selected layer item is live session layer.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def is_live_syncing_layer(objects):
        """
        
                Check if selected layer item is live syncing layer.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def is_material(objects):
        """
        
                Check if the selected item's type is material.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def is_missing_layer(objects):
        """
        
                Check if the selected item is missing layer.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def is_not_anonymous_layer(objects):
        """
        
                Check if the selected layer item is not anonymous layer.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def is_not_authoring_layer(objects):
        """
        
                Check if the selected item is not authoring layer.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def is_not_auto_authoring_and_spec_linking_mode(objects):
        """
        
                Check if the selected item is not in spec linking mode and auto authoring mode.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def is_not_edit_layer(objects):
        """
        
                Check if the selected item is not edit layer item.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def is_not_from_session_layer_tree(objects):
        """
        
                Check if the selected item is not from session layer tree.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def is_not_live_layer(objects):
        """
        
                Check if selected layer item is not live syncing layer.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def is_not_live_session_layer(objects):
        """
        
                Check if selected layer item is not live session layer.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def is_not_missing_layer(objects):
        """
        
                Check if the selected item is not missing layer.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def is_not_omni_layer(objects):
        """
        
                Check if the selected item is not omniverse layer.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def is_not_reserved_layer(objects):
        """
        
                Check if the selected item is not reserved layer.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def is_omni_layer(objects):
        """
        
                Check if the selected item is omniverse layer.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def is_prim_spec_item(objects):
        """
        
                Check if the selected item is prim spec item.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool: True if selected item is prim spec item, otherwise True.  
                
        """
    @staticmethod
    def is_reserved_layer(objects):
        """
        
                Check if the selected item is reserved layer.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def is_spec_linking_mode(objects):
        """
        
                Check if the selected item is in spec linking mode.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def merge_down_one(objects):
        """
        
                Merge selected layer items down to one.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
                
        """
    @staticmethod
    def no_items_selected(objects):
        """
        
                Check any items selected.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool: False if any item selected, otherwise True.  
                
        """
    @staticmethod
    def prim_delete(objects):
        """
        
                Delete selected prim spec item.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
                
        """
    @staticmethod
    def refresh_reference_payload_name(objects: dict):
        """
        
                checks if prims have references/payload and returns name
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def reload_layer(objects):
        """
        
                Reload selected layer item.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
                
        """
    @staticmethod
    def remove_layer(objects):
        """
        
                Remove selected layer item.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
                
        """
    @staticmethod
    def save_layer(objects):
        """
        
                Save selected layer.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
                
        """
    @staticmethod
    def save_layer_as(objects):
        """
        
                Save selected layer, it will open a file picker dialog to select save path.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
                
        """
    @staticmethod
    def save_layer_as_and_replace(objects):
        """
        
                Save selected layer, it will open a file picker dialog to select save path,
                and overwrite the exist layer file.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
                
        """
    @staticmethod
    def set_authoring_layer(objects):
        """
        
                Set the selected layer as authoring layer.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def set_edit_layer(objects):
        """
        
                Set the selected layer as default edit layer.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    @staticmethod
    def show_open_close_tree(objects):
        """
        
                Toggle tree from a specific layer/prim item.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
                
        """
    def __init__(self, usd_context):
        """
        
                Initializes the ContextMenu with a specific USD context.
        
                Args:
                    usd_context(omni.usd.UsdContext): The USD context to be associated with this context menu.
                
        """
    def clear_all_linked_prims(self, objects):
        """
        
                Clear all the linked prims from a specific layer item.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
                
        """
    def has_selections(self, objects):
        """
        
                If the usd context has selectetions.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool: True if any thing selected in usd context, otherwise False.  
                
        """
    def is_over_specifier(self, objects):
        """
        
                Check if the selected prim item's specifier is 'OVER_ONLY'.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
        
                Returns:
                    bool
                
        """
    def link_selected_prims(self, objects):
        """
        
                Link the selected prims to a specific layer item.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
                
        """
    def link_selected_prims_with_hierarchy(self, objects):
        """
        
                Link the selected prims to a specific layer item with hierarchy.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
                
        """
    def move_prims(self, objects):
        """
        
                Move selected prim spec item.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
                
        """
    def on_mouse_event(self, event):
        """
        Handles mouse events and show context menu  based on the event type.
        
                Args:
                    event: An event object containing details about the mouse event.
        
                Returns:
                    None if the module is not found or if the event type is not ACTIVATE.
                
        """
    def select_linked_prims(self, objects):
        """
        
                Select the linked prims from a specific layer item.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
                
        """
    def unlink_selected_prims(self, objects):
        """
        
                Unlink the selected prims to a specific layer item.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
                
        """
    def unlink_selected_prims_with_hierarchy(self, objects):
        """
        
                Unlink the selected prims to a specific layer item with hierarchy.
        
                Args:
                    objects (dict): A dictionary containing selected item information.
                
        """
class ContextMenuEvent:
    """
    The object comatible with ContextMenu
    """
    def __init__(self, item: weakref, expanded = None):
        ...
