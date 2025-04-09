from __future__ import annotations
import asyncio as asyncio
import omni as omni
from omni.kit.window.material_graph.graph_widget import GraphWidget
from omni import ui
__all__: list = ['GraphWindow']
class GraphWindow(omni.ui._ui.Window):
    """
    The Graph window
    """
    def __init__(self, title, **kwargs):
        ...
    def _import_prims(self, _, prims, focus = True):
        """
        Create a model and set it to the graph view
        """
    def add_node(self, event):
        """
        Called to create a node that was droppped to the window
        """
    def destroy(self):
        ...
    def on_build_window(self):
        ...
