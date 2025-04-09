from __future__ import annotations
import omni.kit.graph.delegate.default.delegate
from omni.kit.graph.delegate.default.delegate import GraphNodeDelegate
import omni.kit.widget.graph.abstract_graph_node_delegate
from omni.kit.widget.graph.abstract_graph_node_delegate import GraphNodeDescription
from omni.kit.widget.graph.abstract_graph_node_delegate import GraphPortDescription
from omni import ui
__all__ = ['CompoundInputOutputNodeDelegate', 'CompoundNodeDelegate', 'GraphNodeDelegate', 'GraphNodeDescription', 'GraphPortDescription', 'ui']
class CompoundInputOutputNodeDelegate(omni.kit.graph.delegate.default.delegate.GraphNodeDelegate):
    """
    
        The delegate for the input/output nodes of the compound.
        
    """
    def _CompoundInputOutputNodeDelegate__on_menu(self, model: GraphModel, node: typing.Any, port: typing.Any):
        ...
    def __init__(self):
        ...
    def destroy(self):
        ...
    def port(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription, port_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphPortDescription):
        ...
    def port_input(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription, port_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphPortDescription):
        ...
    def port_output(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription, port_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphPortDescription):
        ...
class CompoundNodeDelegate(omni.kit.graph.delegate.default.delegate.GraphNodeDelegate):
    """
    
        The delegate for the compound nodes.
        
    """
