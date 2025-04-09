from __future__ import annotations
import omni.kit.graph.delegate.default.delegate_full
from omni.kit.graph.delegate.default.delegate_full import GraphNodeDelegateFull
import omni.kit.widget.graph.abstract_graph_node_delegate
from omni.kit.widget.graph.abstract_graph_node_delegate import GraphNodeDescription
from omni import ui
__all__ = ['BackdropDelegate', 'GraphNodeDelegateFull', 'GraphNodeDescription', 'LINE_VISIBLE_MIN', 'TEXT_VISIBLE_MIN', 'ui']
class BackdropDelegate(omni.kit.graph.delegate.default.delegate_full.GraphNodeDelegateFull):
    """
    
        The delegate with the Omniverse design for the nodes of the closed state.
        
    """
    def node_background(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription):
        """
        Called to create widgets of the node background
        """
    def node_footer(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription):
        ...
    def node_header(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription):
        """
        Called to create widgets of the top of the node
        """
LINE_VISIBLE_MIN: float = 0.4
TEXT_VISIBLE_MIN: float = 0.7
