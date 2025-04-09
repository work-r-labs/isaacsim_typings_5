"""
This module provides the GraphNodeDelegateFull class for creating styled graph node UI elements in NVIDIA Omniverse applications.
"""
from __future__ import annotations
import colorsys as colorsys
from functools import partial
import math as math
import omni.kit.widget.graph.abstract_graph_node_delegate
from omni.kit.widget.graph.abstract_graph_node_delegate import AbstractGraphNodeDelegate
from omni.kit.widget.graph.abstract_graph_node_delegate import GraphConnectionDescription
from omni.kit.widget.graph.abstract_graph_node_delegate import GraphNodeDescription
from omni.kit.widget.graph.abstract_graph_node_delegate import GraphPortDescription
from omni.kit.widget.graph.graph_model import GraphModel
from omni import ui
__all__: list = ['color_to_hex', 'GraphNodeDelegateFull']
class GraphNodeDelegateFull(omni.kit.widget.graph.abstract_graph_node_delegate.AbstractGraphNodeDelegate):
    """
    A delegate class for graph node UI elements with Omniverse design.
    
        This class provides methods for creating and styling various parts of a graph node interface, such as headers, footers, ports, and connections. It extends AbstractGraphNodeDelegate and follows the design conventions of NVIDIA Omniverse applications.
    
        Args:
            scale_factor (float): A multiplier for scaling the UI elements of the graph node.
    """
    def _GraphNodeDelegateFull__build_rectangle(self, radius, width, height, draw_top, style_name, name, style_override = None):
        """
        
                Build rectangle of the specific design.
        
                Args:
                    radius: The radius of round corers. The corners are top-left and
                            bottom-right.
                    width: The width of triangle to cut. The top-right and
                           bottom-left trialgles are cut.
                    height: The height of triangle to cut. The top-right and
                            bottom-left trialgles are cut.
                    draw_top: When false the top corners are straight.
                    style_name: style_type_name_override of each widget
                    name: name of each widget
                    style_override: the style to apply to the top level node
                
        """
    def _GraphNodeDelegateFull__scale(self, value):
        """
        Return the value multiplied by global scale multiplier
        """
    def __init__(self, scale_factor = 1.0):
        """
        Initializes the GraphNodeDelegateFull with an optional scale factor.
        """
    def _common_node_header_top(self, model, node):
        """
        Node header part that is used in both full and closed states
        """
    def connection(self, model, source: omni.kit.widget.graph.abstract_graph_node_delegate.GraphConnectionDescription, target: omni.kit.widget.graph.abstract_graph_node_delegate.GraphConnectionDescription, foreground: bool = False):
        """
        Called to create the connection between ports.
        
                Args:
                    model: The graph model containing the connection data.
                    source (GraphConnectionDescription): Description of the source port of the connection.
                    target (GraphConnectionDescription): Description of the target port of the connection.
                    foreground (bool): Optional flag to draw the connection in the foreground.
        """
    def node_background(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription):
        """
        Called to create widgets of the node background.
        
                Args:
                    model: The graph model containing the node data.
                    node_desc (GraphNodeDescription): Description of the node to create background for.
        """
    def node_footer(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription):
        """
        Called to create widgets of the bottom of the node.
        
                Args:
                    model: The graph model containing the node data.
                    node_desc (GraphNodeDescription): Description of the node to create footer for.
        """
    def node_header(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription):
        """
        Called to create widgets of the top of the node.
        
                Args:
                    model: The graph model containing the node data.
                    node_desc (GraphNodeDescription): Description of the node to create header for.
        """
    def node_header_input(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription):
        """
        Called to create the left part of the header that will be used as input when the node is collapsed.
        
                Args:
                    model: The graph model containing the node data.
                    node_desc (GraphNodeDescription): Description of the node to create header input for.
        """
    def node_header_output(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription):
        """
        Called to create the right part of the header that will be used as output when the node is collapsed.
        
                Args:
                    model: The graph model containing the node data.
                    node_desc (GraphNodeDescription): Description of the node to create header output for.
        """
    def port(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription, port_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphPortDescription):
        """
        Called to create the middle part of the port.
        
                Args:
                    model: The graph model containing the node data.
                    node_desc (GraphNodeDescription): Description of the node containing the port.
                    port_desc (GraphPortDescription): Description of the port.
        """
    def port_input(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription, port_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphPortDescription):
        """
        Called to create the left part of the port that will be used as input.
        
                Args:
                    model: The graph model containing the node data.
                    node_desc (GraphNodeDescription): Description of the node containing the port.
                    port_desc (GraphPortDescription): Description of the port.
        """
    def port_output(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription, port_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphPortDescription):
        """
        Called to create the right part of the port that will be used as output.
        
                Args:
                    model: The graph model containing the node data.
                    node_desc (GraphNodeDescription): Description of the node containing the port.
                    port_desc (GraphPortDescription): Description of the port.
        """
def color_to_hex(color: tuple) -> int:
    """
    Converts a color from floating-point RGB(A) format to a hexadecimal integer.
    
        Args:
            color (tuple): A tuple representing the color in RGB(A) format. Each component is a
                           float in the range [0.0, 1.0], where the optional fourth element is the alpha
                           value. If the alpha value is not provided, it defaults to 1.0 (fully opaque).
    
        Returns:
            int: The color encoded as a hexadecimal integer in the form 0xAARRGGBB, where AA is
                 the alpha component, RR is the red component, GG is the green component, and BB
                 is the blue component.
        
    """
CONNECTION_CURVE: int = 60
LINE_VISIBLE_MIN: float = 0.15
MARGIN_WIDTH: float = 7.5
TEXT_VISIBLE_MIN: float = 0.6
