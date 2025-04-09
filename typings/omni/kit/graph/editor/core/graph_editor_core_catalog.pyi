from __future__ import annotations
from omni.kit.graph.editor.core.graph_editor_core_tree_delegate import GraphEditorCoreTreeDelegate
from omni.kit.widget.searchfield.searchfield import SearchField
from omni import ui
import omni.ui._ui
__all__: list = ['GraphEditorCoreCatalog']
class GraphEditorCoreCatalog:
    """
    The common widget for Graph extensions
    """
    def _GraphEditorCoreCatalog__filter_by_text(self, filter_name_text: str):
        """
        Called when the user changes the search field
        """
    def _GraphEditorCoreCatalog__on_expansion(self, item, expanded):
        ...
    def _GraphEditorCoreCatalog__on_mouse_pressed(self, x, y, button, modifier):
        """
        Called by TreeView when mouse pressed
        """
    def __init__(self, model: omni.ui._ui.AbstractItemModel, delegate: omni.ui._ui.AbstractItemDelegate = None, on_context_menu_fn: typing.Optional[typing.Callable[[typing.List[omni.ui._ui.AbstractItem]], NoneType]] = None, **kwargs):
        ...
    def _on_build(self):
        """
        Create a pannel used to create new nodes
        """
    def destroy(self):
        ...
