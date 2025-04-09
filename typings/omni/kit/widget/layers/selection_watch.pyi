from __future__ import annotations
import omni as omni
from omni.kit.widget.layers.layer_item import LayerItem
from omni.kit.widget.layers.prim_spec_item import PrimSpecItem
from pxr import Sdf
from pxr import Trace
import weakref as weakref
__all__: list = ['SelectionWatch']
class SelectionWatch:
    """
    
        The object that update selection in TreeView when the scene selection is
        changed and updated scene selection when TreeView selection is changed.
        
    """
    select_with_command = ...
    @staticmethod
    def _on_kit_selection_changed(*args, **kwargs):
        """
        Send the selection from Kit to TreeView
        """
    @staticmethod
    def _on_widget_selection_changed(*args, **kwargs):
        """
        Send the selection from TreeView to Kit
        """
    def __init__(self, usd_context, tree_view, tree_view_delegate):
        ...
    def _on_stage_event(self, event):
        """
        Called by stage_event_stream
        """
    def add_layer_selection_changed_fn(self, fn):
        ...
    def destroy(self):
        ...
    def get_current_focused_layer_item(self):
        ...
    def remove_layer_selection_changed_fn(self, fn):
        ...
    def set_current_focused_layer_item(self, layer_item):
        ...
    def set_tree_view(self, tree_view, tree_view_delegate):
        """
        Replace TreeView that should show the selection
        """
