"""
References widget.
"""
from __future__ import annotations
import asyncio as asyncio
import carb as carb
from functools import lru_cache
from functools import partial
import omni as omni
from omni.kit.async_engine.async_engine import run_coroutine
from omni.kit.property.usd.asset_filepicker import check_paths_with_callback
from omni.kit.property.usd.asset_filepicker import replace_query
from omni.kit.property.usd.asset_filepicker import show_asset_file_picker
from omni.kit.property.usd.prim_selection_payload import PrimSelectionPayload
from omni.kit.property.usd.usd_property_widget import UsdPropertiesWidget
from omni.kit.property.usd.usd_property_widget_builder import UsdPropertiesWidgetBuilder
from omni.kit.property.usd.usd_style import Styles
from omni.kit.property.usd.versioning_helper import VersioningHelper
from omni.kit.usd import layers
from omni import ui
from pxr import Sdf
import pxr.Sdf
from pxr import Tf
from pxr import Usd
import pxr.Usd
from typing import Any
import urllib as urllib
import weakref as weakref
__all__: list = ['TrackEditingStringModel', 'AddPayloadReferenceWindow', 'PayloadReferenceWidget']
class AddPayloadReferenceWindow:
    """
    Add a payload reference window.
    """
    def __init__(self, payload: omni.kit.property.usd.prim_selection_payload.PrimSelectionPayload, on_payref_added_fn: typing.Callable, use_payloads = False):
        ...
    def destroy(self):
        """
        Destroy the payload reference window.
        """
    def set_payload(self, payload: omni.kit.property.usd.prim_selection_payload.PrimSelectionPayload):
        """
        Set the payload.
        """
    def show(self, payrefs: typing.Union[pxr.Sdf.Reference, pxr.Sdf.Payload]):
        """
        Show the payload reference window.
        """
class PayloadReferenceInfo:
    """
    Payload reference information.
    """
    def __init__(self, asset_path_field, prim_path_field, prim_path_field_model, checkpoint_model, reload_widget = None):
        ...
    def destroy(self):
        """
        Destroy the payload reference information.
        """
class PayloadReferenceWidget(omni.kit.property.usd.usd_property_widget.UsdPropertiesWidget):
    """
    Payload reference widget.
    """
    def __init__(self, use_payloads = False):
        ...
    def _build_asset_path_ui(self, payref: typing.Union[pxr.Sdf.Reference, pxr.Sdf.Payload], intro_layer: pxr.Sdf.Layer, highlight: str, from_local_stack = True):
        ...
    def _build_checkpoint_ui(self, payref: typing.Union[pxr.Sdf.Reference, pxr.Sdf.Payload], intro_layer: pxr.Sdf.Layer, highlight: str):
        ...
    def _build_livesync_ui(self, payref: typing.Union[pxr.Sdf.Reference, pxr.Sdf.Payload], intro_layer: pxr.Sdf.Layer, highlight: str):
        ...
    def _build_payload_reference(self, payref: pxr.Sdf.Reference, intro_layer: pxr.Sdf.Layer):
        ...
    def _build_prim_path_ui(self, payref: typing.Union[pxr.Sdf.Reference, pxr.Sdf.Payload], intro_layer: pxr.Sdf.Layer, highlight: str, from_local_stack = True):
        ...
    def _build_remove_payload_reference_button(self, payref, intro_layer):
        ...
    def _is_ref_prim_valid(self, stage, prim, abs_asset_path, ref_prim_path):
        ...
    def _on_add_payload_reference(self, payload: omni.kit.property.usd.prim_selection_payload.PrimSelectionPayload, use_payloads: bool):
        ...
    def _on_layer_event(self, event: carb.events._events.IEvent):
        ...
    def _on_payload_reference_added(self, prim: pxr.Usd.Prim):
        ...
    def _on_payload_reference_checkpoint_edited(self, model_or_item, stage: pxr.Usd.Stage, prim_path: pxr.Sdf.Path, payref: typing.Union[pxr.Sdf.Reference, pxr.Sdf.Payload]):
        ...
    def _on_payload_reference_edited(self, model_or_item, stage: pxr.Usd.Stage, prim_path: pxr.Sdf.Path, payref: typing.Union[pxr.Sdf.Reference, pxr.Sdf.Payload], intro_layer: pxr.Sdf.Layer):
        ...
    def _on_session_list_changed(self, model):
        ...
    def _on_settings_change(self, item, event_type):
        ...
    def _prim_is_selected(self, objects: dict):
        ...
    def _undo_redo_on_change(self, cmds):
        ...
    def _update_session_widget_states(self):
        ...
    def build_impl(self):
        """
        
                See PropertyWidget.build_impl
                
        """
    def build_items(self):
        ...
    def clean(self):
        ...
    def on_collapsed_changed(self, collapsed):
        ...
    def on_new_payload(self, payload):
        """
        See PropertyWidget.on_new_payload
        """
    def reset(self):
        ...
class TrackEditingStringModel(omni.ui._ui.SimpleStringModel):
    """
    Model that calls edited_fn when end_edit or set_value (not when typing).
    """
    def __init__(self, value: str = ''):
        ...
    def _call_edited_fn(self):
        """
        Call the edited functions when the string model is edited.
        """
    def add_edited_fn(self, fn):
        """
        Add a function to be called when the string model is edited.
        """
    def begin_edit(self):
        """
        Begin editing the string model.
        """
    def clear_edited_fn(self):
        """
        Clear the functions to be called when the string model is edited.
        """
    def end_edit(self):
        """
        End editing the string model.
        """
    def set_value(self, value: str):
        """
        Set the value of the string model.
        """
def _get_plus_glyph(*args, **kwargs):
    ...
def anchor_payload_asset_path_to_layer(ref: pxr.Sdf.Payload, intro_layer: pxr.Sdf.Layer, anchor_layer: pxr.Sdf.Layer):
    """
    Anchor a payload asset path to a layer.
    """
def anchor_reference_asset_path_to_layer(ref: pxr.Sdf.Reference, intro_layer: pxr.Sdf.Layer, anchor_layer: pxr.Sdf.Layer):
    """
    Anchor a reference asset path to a layer.
    """
def build_path_field(stage, init_value: str, jump_button: bool, use_payloads: bool, layer: pxr.Sdf.Layer = None, is_live: bool = False, in_session: bool = False, outdated: bool = False, from_local_stack = True, auto_reload: bool = False):
    """
    Build a path field.
    """
def post_notification(message: str, info: bool = False, duration: int = 3, hide_after_timeout: bool = True):
    """
    Post a notification message to the user.
    """
DEFAULT_PRIM_TAG: str = '<Default Prim>'
REF_LABEL_WIDTH: int = 80
