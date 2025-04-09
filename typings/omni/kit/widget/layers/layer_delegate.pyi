from __future__ import annotations
from omni.kit.widget.layers.context_menu import ContextMenu
from omni.kit.widget.layers.context_menu import ContextMenuEvent
from omni.kit.widget.layers.layer_item import LayerItem
from omni.kit.widget.layers.layer_model_utils import LayerModelUtils
from omni.kit.widget.layers.layer_widgets import build_layer_widget
from omni.kit.widget.layers.layer_widgets import build_prim_spec_widget
from omni.kit.widget.layers.prim_spec_item import PrimSpecItem
from omni import ui
import omni.ui._ui
import pathlib
from pathlib import Path
import weakref as weakref
__all__ = ['CURRENT_PATH', 'ContextMenu', 'ContextMenuEvent', 'ICON_PATH', 'LayerDelegate', 'LayerItem', 'LayerModelUtils', 'Path', 'PrimSpecItem', 'build_layer_widget', 'build_prim_spec_widget', 'on_mouse_pressed', 'ui', 'weakref']
class LayerDelegate(omni.ui._ui.AbstractItemDelegate):
    def __init__(self, usd_context):
        ...
    def build_branch(self, model, item, column_id, level, expanded):
        """
        Create a branch widget that opens or closes subtree
        """
    def build_header(self, column_id):
        ...
    def build_widget(self, model, item, column_id, level, expanded):
        """
        Create a widget per item
        """
    def destroy(self):
        ...
    def on_selection_changed(self, selection):
        ...
    def on_stage_attached(self):
        ...
    def set_highlighting(self, enable: bool = None, text: str = None):
        ...
    def set_tree_view(self, tree_view: omni.ui._ui.TreeView):
        ...
def on_mouse_pressed(button, context_menu: weakref, item: weakref, expanded):
    """
    Called when the user press the mouse button on the item
    """
CURRENT_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.widget.layers-1.8.2+d02c707b/omni/kit/widget/layers')
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.widget.layers-1.8.2+d02c707b/icons')
