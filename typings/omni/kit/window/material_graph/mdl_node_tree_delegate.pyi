from __future__ import annotations
from functools import partial
import omni.kit.graph.editor.core.graph_editor_core_tree_delegate
from omni.kit.graph.editor.core.graph_editor_core_tree_delegate import GraphEditorCoreTreeDelegate
from omni import ui
import omni.ui.color_utils
import pathlib
from pathlib import Path
__all__ = ['CURRENT_PATH', 'GraphEditorCoreTreeDelegate', 'ICON_PATH', 'ICON_SIZE', 'ITEM_SIZE', 'MdlNodeTreeDelegate', 'Path', 'SECTION_HEIGHT', 'cl', 'partial', 'ui']
class MdlNodeTreeDelegate(omni.kit.graph.editor.core.graph_editor_core_tree_delegate.GraphEditorCoreTreeDelegate):
    """
    The delegate for TreeView of the MDL shader panel
    """
    def __init__(self, flat = False):
        ...
    def build_branch(self, model, item, column_id, level, expanded):
        """
        Create a branch widget that opens or closes subtree
        """
    def build_icon_with_tooltip(self, model, item, column_id, level, expanded):
        ...
    def build_item_widget(self, model, item, column_id, level, expanded):
        """
         build the widget for the items 
        """
    def build_section_icon(self, model, item, column_id, level, expanded):
        """
        this function is used as the base class function to be override by inherited ones,
                so that we can add icon in front of the section item
        """
    def build_section_widget(self, model, item, column_id, level, expanded):
        ...
    def build_widget(self, model, item, column_id, level, expanded):
        ...
    def filter_by_text(self, filter_name_text: str):
        """
        Saves the filtering text to use it when drawing the item
        """
CURRENT_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.window.material_graph-1.8.19/omni/kit/window/material_graph')
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.window.material_graph-1.8.19/icons')
ICON_SIZE: int = 25
ITEM_SIZE: int = 50
SECTION_HEIGHT: int = 30
cl: omni.ui.color_utils.ColorShade  # value = <omni.ui.color_utils.ColorShade object>
