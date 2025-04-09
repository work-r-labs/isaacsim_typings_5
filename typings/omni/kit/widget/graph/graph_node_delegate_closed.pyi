"""
This module provides the `GraphNodeDelegateClosed` class, a specialized delegate for representing closed state graph nodes with the Omniverse design.
"""
from __future__ import annotations
import omni.kit.widget.graph.abstract_graph_node_delegate
from omni.kit.widget.graph.abstract_graph_node_delegate import GraphNodeDescription
import omni.kit.widget.graph.graph_node_delegate_full
from omni.kit.widget.graph.graph_node_delegate_full import GraphNodeDelegateFull
from omni import ui
__all__: list = ['GraphNodeDelegateClosed']
class GraphNodeDelegateClosed(omni.kit.widget.graph.graph_node_delegate_full.GraphNodeDelegateFull):
    """
    A specialized delegate for representing closed state graph nodes in Omniverse design.
    
        Args:
            scale_factor (float): The factor by which the node's UI is scaled.
    """
    def __init__(self, scale_factor = 1.0):
        """
        Initializes the closed graph node delegate with a scaling factor.
        """
    def node_footer(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription):
        """
        Creates widgets at the bottom of the node. This method intentionally does nothing for closed nodes.
        """
    def node_header(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription):
        """
        Creates widgets at the top of the node.
        
                Args:
                    model: The data model for the graph.
                    node_desc (GraphNodeDescription): The description of the graph node.
        """
    def node_header_input(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription):
        """
        Creates the left part of the header to be used as input when the node is collapsed.
        
                Args:
                    model: The data model for the graph.
                    node_desc (GraphNodeDescription): The description of the graph node.
        """
    def node_header_output(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription):
        """
        Creates the right part of the header to be used as output when the node is collapsed.
        
                Args:
                    model: The data model for the graph.
                    node_desc (GraphNodeDescription): The description of the graph node.
        """
LINE_VISIBLE_MIN: float = 0.15
TEXT_VISIBLE_MIN: float = 0.6
