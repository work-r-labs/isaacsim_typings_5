"""
This module defines the GraphNode class, which represents a widget for individual graph nodes in a graphical interface.
"""
from __future__ import annotations
import omni.kit.widget.graph.abstract_graph_node_delegate
from omni.kit.widget.graph.abstract_graph_node_delegate import GraphNodeDescription
from omni.kit.widget.graph.abstract_graph_node_delegate import GraphNodeLayout
from omni.kit.widget.graph.abstract_graph_node_delegate import GraphPortDescription
import omni.kit.widget.graph.graph_model
from omni.kit.widget.graph.graph_model import GraphModel
from omni import ui
__all__: list = ['GraphNode']
class GraphNode:
    """
    Represents the Widget for the single node. Uses the model and the
        delegate to fill up its layout.
    
        Args:
            model (GraphModel): The graph model associated with this node.
            item: The item data associated with this node.
            has_input_connection: Indicates if the node has input connections.
            has_output_connection: Indicates if the node has output connections.
            ports (list): List of ports associated with the node.
            delegate: The delegate responsible for node appearance and layout.
    """
    def _GraphNode__build_layout(self):
        """
        
                Build the Node layout with the delegate. See GraphNodeDelegate for info.
                When it's called, it will replace all the sub-widgets.
                
        """
    def _GraphNode__build_port(self, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription, port, port_input_flags, port_output_flags, level: int, relative_position: int, parent_child_count: int, siblings_below: list[int], is_heap: bool):
        """
        The layout for one single port line.
        """
    def __getattr__(self, attr):
        """
        Pretend it's self.__root_frame
        """
    def __init__(self, model: omni.kit.widget.graph.graph_model.GraphModel, item, has_input_connection, has_output_connection, ports: list, delegate):
        """
        Initializes a new instance of the GraphNode.
        """
    def destroy(self):
        """
        Called by extension before destroying this object. It doesn't happen automatically.
                Without this hot reloading doesn't work.
        """
    def rebuild_layout(self):
        """
        Rebuilds the layout of the graph node based on the current node description.
        """
    @property
    def header_frame(self):
        """
        Gets the frame that holds the entire header bar.
        
                Returns:
                    The Frame that holds the entire header bar.
        """
    @property
    def header_input_frame(self):
        """
        Gets the frame that holds the inputs on the left side of the header bar.
        
                Returns:
                    The Frame that holds the inputs on the left side of the header bar.
        """
    @property
    def header_output_frame(self):
        """
        Gets the frame that holds the outputs on the right side of the header bar.
        
                Returns:
                    The Frame that holds the outputs on the right side of the header bar.
        """
    @property
    def port_center_widgets(self):
        """
        Gets the dictionary for port center widgets which contains the port name label and edit fields.
        
                Returns:
                    A dictionary where the key is the port and the value is a ui.Widget or None if the delegate does not return a widget.
                
        """
    @property
    def ports(self):
        """
        Gets the dictionary mapping ports to their frames.
        
                Returns:
                    A dictionary where the key is a port and the value is a tuple of two ui.Widget objects representing the port.
                
        """
    @property
    def selected(self):
        """
        Gets the widget selected style state.
        
                Returns:
                    The selected style state of the widget.
        """
    @selected.setter
    def selected(self, value):
        """
        Sets the widget selected style state.
        
                Args:
                    value (bool): The new selected state to be applied to the widget.
        """
    @property
    def skip_draw_clipped(self):
        """
        Gets the skip_draw_when_clipped property of the root frame.
        
                Returns:
                    The skip_draw_when_clipped property of the root frame.
        """
    @skip_draw_clipped.setter
    def skip_draw_clipped(self, value):
        """
        Sets the skip_draw_when_clipped property of the root frame.
        
                Args:
                    value (bool): The new skip_draw_when_clipped state to be applied to the root frame.
        """
    @property
    def snapping_widgets(self):
        """
        Gets the dictionary of widgets used for snapping connections.
        
                Returns:
                    A dictionary where the key is a port and the value is a tuple with ui.Widget objects used for snapping connections.
                
        """
    @property
    def user_drag(self):
        """
        Gets the dictionary with widgets that follow the mouse cursor when the user creates a connection.
        
                Returns:
                    A dictionary with the port as the key and widget that follows the mouse cursor when the user creates a connection.
                
        """
    @property
    def user_drag_placer(self):
        """
        Gets the dictionary with placers that follow the mouse cursor when the user creates a connection.
        
                Returns:
                    A dictionary with the port as the key and placer that follows the mouse cursor when the user creates a connection.
                
        """
    @property
    def visible(self) -> bool:
        """
        Gets the visibility state of the graph node.
        
                Returns:
                    The visibility state of the graph node.
        """
    @visible.setter
    def visible(self, value: bool):
        """
        Sets the visibility of the graph node.
        
                Args:
                    value (bool): The new visibility state to be applied to the graph node.
        """
