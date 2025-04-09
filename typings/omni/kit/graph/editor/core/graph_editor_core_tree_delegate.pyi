from __future__ import annotations
from functools import partial
from omni import ui
import omni.ui._ui
import omni.ui.color_utils
import pathlib
from pathlib import Path
__all__: list = ['GraphEditorCoreTreeDelegate']
class GraphEditorCoreTreeDelegate(omni.ui._ui.AbstractItemDelegate):
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
    def destroy(self):
        ...
    def filter_by_text(self, filter_name_text: str):
        """
        Saves the filtering text to use it when drawing the item
        """
    def set_on_expand_fn(self, fn):
        ...
CURRENT_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.graph.editor.core-1.5.3/omni/kit/graph/editor/core')
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.graph.editor.core-1.5.3/icons')
cl: omni.ui.color_utils.ColorShade  # value = <omni.ui.color_utils.ColorShade object>
