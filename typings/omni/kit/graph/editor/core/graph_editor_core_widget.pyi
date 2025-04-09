from __future__ import annotations
import asyncio as asyncio
import carb as carb
import omni as omni
from omni.kit.graph.delegate.default.delegate import GraphNodeDelegate
from omni.kit.graph.editor.core.graph_editor_core_breadcrumbs import GraphEditorCoreBreadcrumbs
from omni.kit.graph.editor.core.graph_editor_core_catalog import GraphEditorCoreCatalog
from omni.kit.graph.editor.core.graph_editor_core_splitter import GraphEditorCoreSplitter
from omni.kit.widget.graph.graph_view import GraphView
from omni.kit.widget.graph.isolation_graph_model import IsolationGraphModel
from omni import ui
import pathlib
from pathlib import Path
import traceback as traceback
__all__: list = ['GraphEditorCoreWidget']
class GraphEditorCoreWidget:
    """
    The common widget for Graph extensions
    """
    model = ...
    def _GraphEditorCoreWidget__build_navigation(self):
        """
        Create the top panel with the navigation
        """
    def _GraphEditorCoreWidget__on_build(self):
        ...
    def _GraphEditorCoreWidget__on_build_middle(self):
        ...
    def _GraphEditorCoreWidget__on_build_toolbar(self):
        """
        
                    example of self.__toolbar_items
                    self.__toolbar_items = [
                    { "name": "open", "icon": path, "on_clicked": fn},
                    { "name": "save", "icon": path, "on_clicked": fn},
                    { "name": "-"},
                    { "name": "reset", "icon": path, "on_clicked": fn}
                    { "name": "load", "label": "Load"}
                    { "name": "unavailable", "icon": path, "enabled": False, "tooltip": "A tooltip"}
                    ]
                
        """
    def _GraphEditorCoreWidget__on_item_changed(self, item):
        ...
    def _GraphEditorCoreWidget__on_mouse_mouse_double_clicked(self, button):
        ...
    def _GraphEditorCoreWidget__on_mouse_pressed(self, button):
        ...
    def __init__(self, model = None, delegate = None, view_type = omni.kit.widget.graph.graph_view.GraphView, style = None, catalog_model: typing.Optional[omni.ui._ui.AbstractItemModel] = None, catalog_delegate: typing.Optional[omni.ui._ui.AbstractItemDelegate] = None, has_catalog: bool = True, toolbar_items = list(), **kwargs):
        ...
    def _get_graph_view_hovered_position(self) -> typing.Optional[typing.Tuple[float]]:
        """
        Return the position of mouse if self._graph_view is hovered
        """
    def clear_all(self):
        ...
    def destroy(self):
        ...
    def focus_on_nodes(self):
        """
        Zoom and pan to fit all the nodes
        """
    def get_current_graph_item(self):
        ...
    def on_accept_drop(self, drop_data: str):
        """
        Called to check if the widget can accept the drop
        """
    def on_build_breadcrumbs(self):
        ...
    def on_build_catalog(self):
        """
        Create a pannel used to create new nodes
        """
    def on_build_graph(self):
        ...
    def on_build_startup(self):
        ...
    def on_catalog_context_menu(self, items: typing.List[omni.ui._ui.AbstractItem]):
        ...
    def on_drop(self, event: omni.ui._ui.WidgetMouseDropEvent):
        """
        Called when the user dropped something to the window
        """
    def on_key_pressed(self, key, mod, pressed):
        ...
    def on_left_mouse_button_double_clicked(self, items):
        ...
    def on_left_mouse_button_pressed(self, items):
        ...
    def on_right_mouse_button_pressed(self, items):
        ...
    def set_current_compound(self, item, focus = True):
        """
        Changes the current view to show the subgraph of the compound
        """
    def set_toolbar_items(self, items):
        ...
    @property
    def style(self):
        ...
    @style.setter
    def style(self, style):
        """
        Apply the style and mix it with the default one
        """
def is_func_empty(func: typing.Callable) -> bool:
    """
    Return True if the given function has only pass
    """
BACKGROUND: int = 4280492319
BORDER_MISCELLANEOUS: int = 4288183328
BORDER_SELECTED: int = 4294967295
CURRENT_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.graph.editor.core-1.5.3/omni/kit/graph/editor/core')
EXT_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.graph.editor.core-1.5.3')
ICON_BACKGROUND: int = 4281610282
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.graph.editor.core-1.5.3/icons')
NODE_BACKGROUND: int = 4283121724
NODE_BACKGROUND_SELECTED: int = 4286540902
cl: omni.ui.color_utils.ColorShade  # value = <omni.ui.color_utils.ColorShade object>
