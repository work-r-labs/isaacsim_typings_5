from __future__ import annotations
import colorsys as colorsys
from functools import partial
import math as math
import omni.kit.widget.graph.abstract_graph_node_delegate
from omni.kit.widget.graph.abstract_graph_node_delegate import AbstractGraphNodeDelegate
from omni.kit.widget.graph.abstract_graph_node_delegate import GraphConnectionDescription
from omni.kit.widget.graph.abstract_graph_node_delegate import GraphNodeDescription
from omni.kit.widget.graph.abstract_graph_node_delegate import GraphNodeLayout
from omni.kit.widget.graph.abstract_graph_node_delegate import GraphPortDescription
from omni.kit.widget.graph.graph_model import GraphModel
from omni import ui
import omni.ui.color_utils
import typing
__all__ = ['AbstractGraphNodeDelegate', 'CONNECTION_CURVE', 'GraphConnectionDescription', 'GraphModel', 'GraphNodeDelegateFull', 'GraphNodeDescription', 'GraphNodeLayout', 'GraphPortDescription', 'LINE_VISIBLE_MIN', 'TEXT_VISIBLE_MIN', 'cl', 'colorsys', 'math', 'partial', 'ui']
class GraphNodeDelegateFull(omni.kit.widget.graph.abstract_graph_node_delegate.AbstractGraphNodeDelegate):
    """
    
        The delegate with the Omniverse design.
        
    """
    PREVIEW_SIZE: typing.ClassVar[int] = 175
    def _GraphNodeDelegateFull__build_rectangle(self, radius, width, height, draw_top, style_name, name, style_override = None):
        """
        
                Build rectangle of the specific design.
        
                Args:
                    radius: The radius of round corners. The corners are top-left and
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
        ...
    def _common_node_header_top(self, model, node):
        """
        Node header part that is used in both full and closed states
        """
    def _common_node_node_background(self, model, node, draw_icon: bool):
        """
        Called to create widgets of the node background
        """
    def _display_color_style(self, display_color, style_name: str, style_field: str, fallback = None):
        ...
    def _icon(self, model, node, style_name, **kwargs):
        ...
    def connection(self, model, source: omni.kit.widget.graph.abstract_graph_node_delegate.GraphConnectionDescription, target: omni.kit.widget.graph.abstract_graph_node_delegate.GraphConnectionDescription, foreground: bool = False):
        """
        Called to create the connection between ports
        """
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
    def port(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription, port_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphPortDescription):
        """
        Called to create the middle part of the port
        """
    def port_input(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription, port_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphPortDescription):
        """
        Called to create the left part of the port that will be used as input
        """
    def port_output(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription, port_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphPortDescription):
        """
        Called to create the right part of the port that will be used as output
        """
CONNECTION_CURVE: int = 60
LINE_VISIBLE_MIN: float = 0.4
TEXT_VISIBLE_MIN: float = 0.7
cl: omni.ui.color_utils.ColorShade  # value = <omni.ui.color_utils.ColorShade object>
