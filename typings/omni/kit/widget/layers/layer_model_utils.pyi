from __future__ import annotations
import carb as carb
import omni as omni
from omni.client.utils import utils as clientutils
from omni.kit.async_engine.async_engine import run_coroutine
from omni.kit import notification_manager as nm
from omni.kit.usd.layers._impl.layer_utils import LayerUtils
from omni.kit.widget.prompt.prompt import PromptButtonInfo
from omni.kit.widget.prompt.prompt import PromptManager
from omni.kit.window.file_exporter import get_file_exporter
from omni.kit.window.file_importer import get_file_importer
import os as os
from pxr import Sdf
import weakref as weakref
__all__ = ['LayerModelUtils', 'LayerUtils', 'PromptButtonInfo', 'PromptManager', 'Sdf', 'carb', 'clientutils', 'get_file_exporter', 'get_file_importer', 'nm', 'omni', 'os', 'run_coroutine', 'weakref']
class LayerModelUtils:
    @staticmethod
    def _create_layer(layer_identifier: str):
        ...
    @staticmethod
    def _found_existing_sublayer(layer_item, layer_identifier):
        ...
    @staticmethod
    def _prompt_content_transfer_and_create_layer(weakref_layer_item, file_path, position):
        ...
    @staticmethod
    def _traverse(layer_item, target_layer, source_layer):
        ...
    @staticmethod
    def can_create_layer_to_location(target_layer, drop_location):
        ...
    @staticmethod
    def can_edit_sublayer(layer_item):
        ...
    @staticmethod
    def can_move_layer(target_layer, source_layer, drop_location):
        """
        Checks if it's possible to move source layer to position of target layer.
        """
    @staticmethod
    def can_move_prim_spec_to_layer(target_layer, prim_spec):
        ...
    @staticmethod
    def can_set_as_edit_target(layer_item):
        ...
    @staticmethod
    def create_sublayer(layer_item, position: int, create_anonymous = False):
        ...
    @staticmethod
    def flatten_all_layers(layer_model):
        ...
    @staticmethod
    def insert_sublayer(layer_item, position: int):
        ...
    @staticmethod
    def is_stronger_than(model, target_layer, source_layer):
        """
        Checks if target_layer is stronger than source_layer
        """
    @staticmethod
    def lock_layer(layer_item, locked):
        ...
    @staticmethod
    def merge_layer_down(layer_item):
        ...
    @staticmethod
    def move_layer(target_layer, source_layer, drop_location):
        """
        Moving from source layer to sublayer position of target layer.
        """
    @staticmethod
    def move_prim_spec(model, target_item, prim_item):
        ...
    @staticmethod
    def reload_layer(layer_item):
        ...
    @staticmethod
    def remove_layer(layer_item):
        ...
    @staticmethod
    def remove_layers(layer_items):
        ...
    @staticmethod
    def remove_prim_spec_items(prim_item_list):
        ...
    @staticmethod
    def save_layer(layer_item):
        ...
    @staticmethod
    def save_layer_as(layer_item, replace = False, insert_before = False, on_save_done = None, confirm_before_insert = False):
        """
        Save layer as new layer.
        
                Args:
                    layer_item (LayerItem): Layer item to be saved.
                    replace (bool): After save, if it needs to replace the item to be saved.
                    insert_before (bool): After save, if it needs to be inserted before this item.
                    `replace` and `insert_before` cannot be true at the same time.
                    confirm_before_insert (bool): Before insert, it needs to confirm or not.
                
        """
    @staticmethod
    def save_model(model):
        """
        Saves all dirty layers of this model
        """
    @staticmethod
    def set_auto_authoring_mode(layer_model, enabled):
        ...
def _show_confirm_layer_insert_prompt(layer_identifier, confirm_fn):
    ...
def _show_file_insert_picker(title: str, file_handler, default_location = None, default_filename = None):
    ...
def _show_move_prim_spec_warning_prompt(layer_identifier, confirm_fn):
    ...
def _show_outdated_layer_prompt(layer_identifier, confirm_fn, middle_fn, middle_2_fn, cancel_fn):
    ...
def _show_outdated_layers_prompt(outdated_layers, confirm_fn, middle_fn, cancel_fn):
    ...
def _show_reload_dirty_layer_prompt(layer_identifier, confirm_fn):
    ...
def _show_remove_dirty_layer_prompt(layer_identifier, dirty, confirm_fn, multiple = False):
    ...
def _show_save_error_prompt(layer_identifier):
    ...
def _show_save_file_picker(title: str, file_handler, default_location = None, default_filename = None):
    ...
def _show_transfer_root_content_prompt(confirm_fn, cancel_fn):
    ...
