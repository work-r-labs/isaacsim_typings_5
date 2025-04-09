"""
This module provides abstract base classes for graph node delegates, including layout enums, node, port, and connection descriptions.
"""
from __future__ import annotations
import enum
from enum import Enum
from enum import auto
import typing
__all__: list = ['GraphNodeLayout', 'GraphNodeDescription', 'GraphPortDescription', 'GraphConnectionDescription', 'AbstractGraphNodeDelegate']
class AbstractGraphNodeDelegate:
    """
    
        The delegate generates widgets that together form the node using the
        model. The following figure shows the LIST layout of the node. For every
        zone, there is a method that is called to build this zone.
    
        ::
    
            +-------------------------+
            |     node_background     |
            | +---+-------------+---+ |
            | |[A]| node_header |[B]| |
            | +---+-------------+---+ |
            | |[C]|    port     |[D]| |
            | +---+-------------+---+ |
            | |[D]|    port     |[D]| |
            | +---+-------------+---+ |
            | |[E]| node_footer |[F]| |
            | +---+-------------+---+ |
            +-------------------------+
    
        COLUMN layout allows to put input and output ports at the same line:
    
        ::
    
            +-------------------------+
            |     node_background     |
            | +---+-------------+---+ |
            | |[A]| node_header |[B]| |
            | +---+------+------+---+ |
            | |[C]| port | port |[D]| |
            | |   |      |------+---| |
            | |---+------| port |[D]| |
            | |[D]| port |      |   | |
            | +---+------+------+---+ |
            | |[E]| node_footer |[F]| |
            | +---+-------------+---+ |
            +-------------------------+
    
        ::
    
            [A] node_header_input
            [B] node_header_output
            [C] port_input
            [D] port_output
            [E] node_footer_input (TODO)
            [F] node_footer_output (TODO)
        
    """
    def connection(self, model, source_desc: GraphConnectionDescription, target_desc: GraphConnectionDescription, foreground: bool = False):
        """
        Called to create the connection between ports.
        
                Args:
                    model: The model associated with the graph.
                    source_desc (GraphConnectionDescription): The description of the source connection.
                    target_desc (GraphConnectionDescription): The description of the target connection.
                    foreground (bool, optional): If True, the connection is drawn in the foreground. Defaults to False.
        """
    def destroy(self):
        """
        Performs any necessary cleanup before the object is destroyed.
        """
    def get_node_layout(self, model, node_desc: GraphNodeDescription):
        """
        Called to determine the node layout.
        
                Args:
                    model: The model associated with the graph.
                    node_desc (GraphNodeDescription): The description of the node.
        
                Returns:
                    GraphNodeLayout: The layout of the node.
        """
    def node_background(self, model, node_desc: GraphNodeDescription):
        """
        Called to create widgets of the node background.
        
                Args:
                    model: The model associated with the graph.
                    node_desc (GraphNodeDescription): The description of the node.
        """
    def node_footer(self, model, node_desc: GraphNodeDescription):
        """
        Called to create widgets of the bottom of the node.
        
                Args:
                    model: The model associated with the graph.
                    node_desc (GraphNodeDescription): The description of the node.
        """
    def node_header(self, model, node_desc: GraphNodeDescription):
        """
        Called to create widgets of the top of the node.
        
                Args:
                    model: The model associated with the graph.
                    node_desc (GraphNodeDescription): The description of the node.
        """
    def node_header_input(self, model, node_desc: GraphNodeDescription):
        """
        Called to create the left part of the header that will be used as input when the node is collapsed.
        
                Args:
                    model: The model associated with the graph.
                    node_desc (GraphNodeDescription): The description of the node.
        """
    def node_header_output(self, model, node_desc: GraphNodeDescription):
        """
        Called to create the right part of the header that will be used as output when the node is collapsed.
        
                Args:
                    model: The model associated with the graph.
                    node_desc (GraphNodeDescription): The description of the node.
        """
    def port(self, model, node_desc: GraphNodeDescription, port_desc: GraphPortDescription):
        """
        Called to create the middle part of the port.
        
                Args:
                    model: The model associated with the graph.
                    node_desc (GraphNodeDescription): The description of the node.
                    port_desc (GraphPortDescription): The description of the port.
        """
    def port_input(self, model, node_desc: GraphNodeDescription, port_desc: GraphPortDescription):
        """
        Called to create the left part of the port that will be used as input.
        
                Args:
                    model: The model associated with the graph.
                    node_desc (GraphNodeDescription): The description of the node.
                    port_desc (GraphPortDescription): The description of the port.
        """
    def port_output(self, model, node_desc: GraphNodeDescription, port_desc: GraphPortDescription):
        """
        Called to create the right part of the port that will be used as output.
        
                Args:
                    model: The model associated with the graph.
                    node_desc (GraphNodeDescription): The description of the node.
                    port_desc (GraphPortDescription): The description of the port.
        """
class GraphConnectionDescription:
    """
    A class to describe a connection in a graph.
    
        Args:
            node: The node which the connection belongs to.
            port: The port on the node that is connected.
            widget: The widget representing the connection in the UI.
            level: The level of the node in the graph hierarchy.
            is_tangent_reversed (bool): Indicates if the connection's tangent is reversed. Default to False.
        
    """
    def __init__(self, node, port, widget, level, is_tangent_reversed = False):
        """
        Initializes the GraphConnectionDescription with the specified node, port, widget, and level.
        """
class GraphNodeDescription:
    """
    The object that holds the main attributes of the node.
    
        Args:
            node (Any): The central object of the node the description represents.
            connected_source (Optional[Any]): Source object connected to the node, if any.
            connected_target (Optional[Any]): Target object connected to the node, if any.
    """
    def __init__(self, node, connected_source = None, connected_target = None):
        """
        Initialize a new instance of GraphNodeDescription.
        """
class GraphNodeLayout(enum.Enum):
    """
    An enumeration to define node layout types.
    """
    COLUMNS: typing.ClassVar[GraphNodeLayout]  # value = <GraphNodeLayout.COLUMNS: 2>
    HEAP: typing.ClassVar[GraphNodeLayout]  # value = <GraphNodeLayout.HEAP: 3>
    LIST: typing.ClassVar[GraphNodeLayout]  # value = <GraphNodeLayout.LIST: 1>
class GraphPortDescription:
    """
    Represents the description of a graph port with its various characteristics.
    
        Args:
            port: The graphical representation of the port.
            level: The hierarchy level of the port within the graph.
            relative_position: The position of the port relative to its node.
            parent_child_count: The count of either parent or child connections.
            connected_source: The source node this port is connected to, if any.
            connected_target: The target node this port is connected to, if any.
    """
    def __init__(self, port, level, relative_position, parent_child_count, connected_source = None, connected_target = None):
        """
        Initialize a description for a graph port.
        
                Args:
                    port: The port object being described.
                    level: The hierarchical level of the port within the graph.
                    relative_position: The position of the port relative to its node.
                    parent_child_count: The number of children the parent of this port has.
                    connected_source: The source connection of the port, if any.
                    connected_target: The target connection of the port, if any.
        """
