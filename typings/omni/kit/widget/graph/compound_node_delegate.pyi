"""
This module provides delegate classes for compound nodes and their input/output nodes with associated context menus in a graph widget.
"""
from __future__ import annotations
import omni.kit.widget.graph.abstract_graph_node_delegate
from omni.kit.widget.graph.abstract_graph_node_delegate import GraphNodeDescription
from omni.kit.widget.graph.abstract_graph_node_delegate import GraphPortDescription
import omni.kit.widget.graph.graph_node_delegate_full
from omni.kit.widget.graph.graph_node_delegate_full import GraphNodeDelegateFull
from omni import ui
__all__: list = ['CompoundNodeDelegate', 'CompoundInputOutputNodeDelegate']
class CompoundInputOutputNodeDelegate(omni.kit.widget.graph.graph_node_delegate_full.GraphNodeDelegateFull):
    """
    The delegate for the input/output nodes of the compound.
    
        This class extends the GraphNodeDelegateFull and provides custom functionality for input/output nodes, such as creating context menus for port interactions that allow the user to connect, disconnect, remove, and reorder ports.
        
    """
    def _CompoundInputOutputNodeDelegate__on_menu(self, model: GraphModel, node: typing.Any, port: typing.Any):
        ...
    def __init__(self):
        """
        Initializes the CompoundInputOutputNodeDelegate with a default context menu.
        """
    def destroy(self):
        """
        Release any resources and references held by the delegate.
        """
    def port(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription, port_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphPortDescription):
        ...
    def port_input(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription, port_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphPortDescription):
        """
        Create the UI representation for an input port and attach the context menu trigger to it.
        
                Args:
                    model: The graph model.
                    node_desc (GraphNodeDescription): The description of the node to which the port belongs.
                    port_desc (GraphPortDescription): The description of the port.
        """
    def port_output(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription, port_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphPortDescription):
        """
        Create the UI representation for an output port and attach the context menu trigger to it.
        
                Args:
                    model: The graph model.
                    node_desc (GraphNodeDescription): The description of the node to which the port belongs.
                    port_desc (GraphPortDescription): The description of the port.
        """
class CompoundNodeDelegate(omni.kit.widget.graph.graph_node_delegate_full.GraphNodeDelegateFull):
    """
    The delegate for the compound nodes.
    
        This class provides functionality to represent and interact with compound nodes within a graph-based UI. It inherits from GraphNodeDelegateFull to utilize its comprehensive set of features tailored for graph node representation and interaction.
    
        Args:
            scale_factor (float): A factor used to scale the node's appearance in the graph.
    """
