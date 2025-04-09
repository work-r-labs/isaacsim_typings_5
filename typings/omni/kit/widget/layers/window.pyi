from __future__ import annotations
import asyncio as asyncio
import carb as carb
import enum
from enum import Enum
from functools import partial
import omni as omni
from omni.kit import notification_manager as nm
from omni.kit.usd import layers
from omni.kit.usd.layers._impl.layer_utils import LayerUtils
from omni.kit.widget.layers.external_drag_drop_helper import destroy_external_drag_drop
from omni.kit.widget.layers.external_drag_drop_helper import setup_external_drag_drop
from omni.kit.widget.layers.layer_delegate import LayerDelegate
from omni.kit.widget.layers.layer_item import LayerItem
from omni.kit.widget.layers.layer_model import LayerModel
from omni.kit.widget.layers.layer_model_utils import LayerModelUtils
from omni.kit.widget.layers.layer_option_button import LayerOptionItem
from omni.kit.widget.layers.layer_option_button import LayerOptionsButton
from omni.kit.widget.layers.models.layer_auto_authoring import LayerAutoAuthoringModel
from omni.kit.widget.layers.models.layer_scope_model import LayerScopeModel
from omni.kit.widget.layers.models.save_all_model import SaveAllModel
from omni.kit.widget.layers.prim_spec_item import PrimSpecItem
from omni.kit.widget.layers.selection_watch import SelectionWatch
from omni.kit.widget.searchfield.searchfield import SearchField
from omni import ui
from pxr import Sdf
import typing
import weakref as weakref
__all__: list = ['LayerWindow']
class LayerWindow:
    """
    The Layer 2 window
    """
    @staticmethod
    def _set_widget_visible(widget: omni.ui._ui.Widget, visible):
        """
        Utility for using in lambdas
        """
    def _LayerWindow__on_option_changed(self, model, item: omni.kit.widget.layers.layer_option_button.LayerOptionItem):
        ...
    def __init__(self, window_name, usd_context):
        ...
    def _clear_filter_types(self):
        ...
    def _filter_by_text(self, filter_text: str):
        """
        Set the search filter string to the models and widgets
        """
    def _is_selection_from_same_layer(self, selection):
        ...
    def _on_dirtiness_changed(self):
        ...
    def _on_layer_events(self, events):
        ...
    def _on_muteness_scope_changed(self):
        ...
    def _on_reload_layers(self):
        ...
    def _on_stage_attached(self, attached: bool):
        ...
    def _toolbar_action(self, weakref_treeview: weakref, weakref_model: weakref, action: int):
        ...
    def _update_delta_button(self):
        ...
    def _update_save_all_button(self):
        ...
    def _visibility_changed_fn(self, visible):
        ...
    def add_layer_selection_changed_fn(self, fn):
        ...
    def destroy(self):
        """
        
                Called by extension before destroying this object. It doesn't happen automatically.
                Without this hot reloading doesn't work.
                
        """
    def get_current_focused_layer_item(self):
        ...
    def get_layer_model(self):
        ...
    def is_visible(self):
        ...
    def remove_layer_selection_changed_fn(self, fn):
        ...
    def set_current_focused_layer_item(self, layer_identifier):
        ...
    def set_visibility_changed_listener(self, listener):
        ...
    def set_visible(self, value):
        ...
    @property
    def layer_view(self):
        ...
class LiveSessionButtonOptions(enum.Enum):
    """
    An enumeration.
    """
    MERGE_AND_QUIT: typing.ClassVar[LiveSessionButtonOptions]  # value = <LiveSessionButtonOptions.MERGE_AND_QUIT: 1>
    QUIT_ONLY: typing.ClassVar[LiveSessionButtonOptions]  # value = <LiveSessionButtonOptions.QUIT_ONLY: 0>
