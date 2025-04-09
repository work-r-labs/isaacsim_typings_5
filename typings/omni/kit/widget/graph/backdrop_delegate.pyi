"""
This module provides a `BackdropDelegate` class for implementing node backdrop UI elements in the Omniverse graph widget.
"""
from __future__ import annotations
import omni.kit.widget.graph.abstract_graph_node_delegate
from omni.kit.widget.graph.abstract_graph_node_delegate import GraphNodeDescription
import omni.kit.widget.graph.graph_node_delegate_full
from omni.kit.widget.graph.graph_node_delegate_full import GraphNodeDelegateFull
from omni import ui
__all__: list = ['BackdropDelegate']
class BackdropDelegate(omni.kit.widget.graph.graph_node_delegate_full.GraphNodeDelegateFull):
    """
    A class for implementing node backdrop UI elements in the Omniverse graph widget.
    
        This delegate class extends the functionality of GraphNodeDelegateFull to provide a custom backdrop UI for graph nodes.
    
        Args:
            scale_factor (float): The factor by which the UI elements are scaled.
        
    """
    def node_background(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription):
        """
        Creates widgets that make up the node background.
        
                Args:
                    model: The graph model that contains the node data.
                    node_desc (GraphNodeDescription): The graphical description of the node.
        
                Raises:
                    Exception: If an error occurs in the underlying UI toolkit.
        """
    def node_footer(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription):
        """
        A placeholder for creating widgets at the bottom of the node.
        
                Args:
                    model: The graph model that contains the node data.
                    node_desc (GraphNodeDescription): The graphical description of the node.
        """
    def node_header(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription):
        """
        Creates widgets to display at the top of the node.
        
                Args:
                    model: The graph model that contains the node data.
                    node_desc (GraphNodeDescription): The graphical description of the node.
        """
LINE_VISIBLE_MIN: float = 0.15
TEXT_VISIBLE_MIN: float = 0.6
