"""
This module provides the GraphNodeDelegateRouter class for routing graph node delegates based on defined conditions and the GraphNodeDelegateRoutingError exception for handling routing errors.
"""
from __future__ import annotations
from collections import namedtuple
import omni as omni
from omni.kit.widget.graph.abstract_graph_node_delegate import AbstractGraphNodeDelegate
from omni.kit.widget.graph.abstract_graph_node_delegate import GraphConnectionDescription
from omni.kit.widget.graph.abstract_graph_node_delegate import GraphNodeDescription
from omni.kit.widget.graph.abstract_graph_node_delegate import GraphPortDescription
import typing
__all__: list = ['GraphNodeDelegateRoutingError', 'GraphNodeDelegateRouter', 'RoutingCondition']
class GraphNodeDelegateRouter(omni.kit.widget.graph.abstract_graph_node_delegate.AbstractGraphNodeDelegate):
    """
    
        The delegate that keeps multiple delegates and pick them depending on the
        routing conditions.
    
        It's possible to add the routing conditions with `add_route`, and
        conditions could be a type or a lambda expression.
    
        The latest added routing is stronger than previously added. Routing added
        without conditions is the default.
    
        We use type routing to make the specific kind of nodes unique, and also
        we can use the lambda function to make the particular state of nodes
        unique (ex. full/collapsed).
    
        It's possible to use type and lambda routing at the same time.
    
        Usage examples:
    
           delegate.add_route(TextureDelegate(), type="Texture2d")
           delegate.add_route(CollapsedDelegate(), expressipon=is_collapsed)
        
    """
    @staticmethod
    def node_background_v2(*args, **kwargs):
        """
        Creates widgets for the background of a node with an option to draw an icon.
        
                Args:
                    model: The data model associated with the graph.
                    node_desc (GraphNodeDescription): The description of the node.
                    draw_icon (bool): Whether to draw an icon on the node's background.
        
                Returns:
                    The widgets for the node's background.
        """
    def _GraphNodeDelegateRouter__route(self, model, node):
        """
        Return the delegate for the given node
        """
    def __init__(self):
        """
        Initializes the GraphNodeDelegateRouter with an empty routing table.
        """
    def add_route(self, delegate: omni.kit.widget.graph.abstract_graph_node_delegate.AbstractGraphNodeDelegate, type = None, expression = None):
        """
        Adds a delegate with an optional type and/or expression to the routing table.
        
                Args:
                    delegate (AbstractGraphNodeDelegate): The delegate to be added.
                    type (str, optional): The type of the delegate. Defaults to None.
                    expression (callable, optional): A lambda expression to evaluate for routing. Defaults to None.
        """
    def connection(self, model, source: omni.kit.widget.graph.abstract_graph_node_delegate.GraphConnectionDescription, target: omni.kit.widget.graph.abstract_graph_node_delegate.GraphConnectionDescription, foreground: bool = False):
        """
        Creates a graphical connection between two ports.
        
                Args:
                    model: The data model associated with the graph.
                    source (GraphConnectionDescription): The source port description.
                    target (GraphConnectionDescription): The target port description.
                    foreground (bool, optional): If True, draw the connection in the foreground. Defaults to False.
        
                Returns:
                    The created connection widget.
        """
    def destroy(self):
        """
        Destroys all delegates in the routing table.
        """
    def get_node_layout(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription):
        """
        Determines the layout for a given node.
        
                Args:
                    model: The data model associated with the graph.
                    node_desc (GraphNodeDescription): The description of the node.
        
                Returns:
                    The layout for the node.
        """
    def node_background(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription):
        """
        Creates widgets for the background of a node.
        
                Args:
                    model: The data model associated with the graph.
                    node_desc (GraphNodeDescription): The description of the node.
        
                Returns:
                    The widgets for the node's background.
        """
    def node_footer(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription):
        """
        Creates widgets for the bottom of a node.
        
                Args:
                    model: The data model associated with the graph.
                    node_desc (GraphNodeDescription): The description of the node.
        
                Returns:
                    The widgets for the node's footer.
        """
    def node_header(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription):
        """
        Creates widgets for the top of a node.
        
                Args:
                    model: The data model associated with the graph.
                    node_desc (GraphNodeDescription): The description of the node.
        
                Returns:
                    The widgets for the node's header.
        """
    def node_header_input(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription):
        """
        Creates the left part of the node header to be used as input when the node is collapsed.
        
                Args:
                    model: The data model associated with the graph.
                    node_desc (GraphNodeDescription): The description of the node.
        
                Returns:
                    The widgets for the node's header input.
        """
    def node_header_output(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription):
        """
        Creates the right part of the node header to be used as output when the node is collapsed.
        
                Args:
                    model: The data model associated with the graph.
                    node_desc (GraphNodeDescription): The description of the node.
        
                Returns:
                    The widgets for the node's header output.
        """
    def port(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription, port_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphPortDescription):
        """
        Creates the middle part of a port.
        
                Args:
                    model: The data model associated with the graph.
                    node_desc (GraphNodeDescription): The description of the node.
                    port_desc (GraphPortDescription): The description of the port.
        
                Returns:
                    The widget for the port.
        """
    def port_input(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription, port_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphPortDescription):
        """
        Creates the left part of a port to be used as input.
        
                Args:
                    model: The data model associated with the graph.
                    node_desc (GraphNodeDescription): The description of the node.
                    port_desc (GraphPortDescription): The description of the port.
        
                Returns:
                    The widget for the port input.
        """
    def port_output(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription, port_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphPortDescription):
        """
        Creates the right part of a port to be used as output.
        
                Args:
                    model: The data model associated with the graph.
                    node_desc (GraphNodeDescription): The description of the node.
                    port_desc (GraphPortDescription): The description of the port.
        
                Returns:
                    The widget for the port output.
        """
class GraphNodeDelegateRoutingError(Exception):
    """
    Exception raised for errors in the graph node delegate routing process.
    
        This exception indicates that routing for a graph node delegate could not be resolved,
        typically because a default route is not available in the routing table.
    """
class RoutingCondition(tuple):
    """
    RoutingCondition(type, expression, delegate)
    """
    __match_args__: typing.ClassVar[tuple] = ('type', 'expression', 'delegate')
    __slots__: typing.ClassVar[tuple] = tuple()
    _field_defaults: typing.ClassVar[dict] = {}
    _fields: typing.ClassVar[tuple] = ('type', 'expression', 'delegate')
    @staticmethod
    def __new__(_cls, type, expression, delegate):
        """
        Create new instance of RoutingCondition(type, expression, delegate)
        """
    @classmethod
    def _make(cls, iterable):
        """
        Make a new RoutingCondition object from a sequence or iterable
        """
    def __getnewargs__(self):
        """
        Return self as a plain tuple.  Used by copy and pickle.
        """
    def __repr__(self):
        """
        Return a nicely formatted representation string
        """
    def _asdict(self):
        """
        Return a new dict which maps field names to their values.
        """
    def _replace(self, **kwds):
        """
        Return a new RoutingCondition object replacing specified fields with new values
        """
