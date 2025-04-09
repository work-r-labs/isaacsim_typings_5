from __future__ import annotations
import asyncio as asyncio
import omni as omni
from omni.kit.widget.graph.graph_view import GraphView
from pxr import UsdShade
__all__: list = ['MaterialGraphView']
class MaterialGraphView(omni.kit.widget.graph.graph_view.GraphView):
    def _MaterialGraphView__serialize_positions(self):
        """
        Serialze updated positions to models
        """
    def __init__(self, **kwargs):
        ...
    def get_bbox_of_nodes(self, nodes: list):
        """
        Get the bounding box of nodes.
                   This is a copy of the same method in the super class,
                   the only difference is the fallback value returned in the 
                   else clause.  These values center the material node in the 
                   graph.
                
        """
    def layout_all(self):
        """
        Reset positions of all the nodes in the model
        """
