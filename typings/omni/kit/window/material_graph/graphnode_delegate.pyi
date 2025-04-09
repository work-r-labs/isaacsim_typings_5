from __future__ import annotations
from functools import partial
import omni.kit.graph.delegate.default.delegate
from omni.kit.graph.delegate.default.delegate import GraphNodeDelegate as GraphNodeDelegateBase
import omni.kit.widget.graph.abstract_graph_node_delegate
from omni.kit.widget.graph.abstract_graph_node_delegate import GraphNodeDescription
from omni import ui
import re as re
__all__: list = ['GraphNodeDelegate']
class GraphNodeDelegate(omni.kit.graph.delegate.default.delegate.GraphNodeDelegate):
    def __init__(self):
        ...
    def node_header(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription):
        """
        Called to create widgets of the top of the node
        """
TEXT_VISIBLE_MIN: float = 0.7
