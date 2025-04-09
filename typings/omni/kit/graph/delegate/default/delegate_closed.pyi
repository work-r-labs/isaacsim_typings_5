from __future__ import annotations
import omni.kit.graph.delegate.default.delegate_full
from omni.kit.graph.delegate.default.delegate_full import GraphNodeDelegateFull
import omni.kit.widget.graph.abstract_graph_node_delegate
from omni.kit.widget.graph.abstract_graph_node_delegate import GraphNodeDescription
from omni import ui
__all__ = ['GraphNodeDelegateClosed', 'GraphNodeDelegateFull', 'GraphNodeDescription', 'LINE_VISIBLE_MIN', 'TEXT_VISIBLE_MIN', 'ui']
class GraphNodeDelegateClosed(omni.kit.graph.delegate.default.delegate_full.GraphNodeDelegateFull):
    """
    
        The delegate with the Omniverse design for the nodes of the closed state.
        
    """
    def __init__(self, scale_factor = 1.0):
        ...
    def node_background(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription):
        ...
    def node_footer(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription):
        """
        Called to create widgets of the bottom of the node
        """
    def node_header(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription):
        """
        Called to create widgets of the top of the node
        """
    def node_header_input(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription):
        """
        Called to create the left part of the header that will be used as input when the node is collapsed
        """
    def node_header_output(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription):
        """
        Called to create the right part of the header that will be used as output when the node is collapsed
        """
LINE_VISIBLE_MIN: float = 0.4
TEXT_VISIBLE_MIN: float = 0.7
