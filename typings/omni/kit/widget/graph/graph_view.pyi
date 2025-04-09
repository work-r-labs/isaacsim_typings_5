"""
This module provides the GraphView class for visualizing nodes and their connections in omni.kit.widget.graph.
"""
from __future__ import annotations
import asyncio as asyncio
import carb as carb
import functools as functools
import omni as omni
from omni.kit.widget.graph.abstract_graph_node_delegate import AbstractGraphNodeDelegate
from omni.kit.widget.graph.abstract_graph_node_delegate import GraphConnectionDescription
from omni.kit.widget.graph.graph_layout import SugiyamaLayout
from omni.kit.widget.graph.graph_model import GraphModel
from omni.kit.widget.graph.graph_node import GraphNode
from omni.kit.widget.graph.graph_node_index import GraphNodeDiff
from omni.kit.widget.graph.graph_node_index import GraphNodeIndex
from omni import ui
import traceback as traceback
import typing
__all__: list = ['GraphView']
class GraphView:
    """
    The visualisation layer of omni.kit.widget.graph. It behaves like a
        regular widget and displays nodes and their connections.
    
        Attributes:
            DEFAULT_DISTANCE_BETWEEN_NODES (float): Default space between graph nodes.
    
        Args:
            kwargs (dict): Arbitrary keyword arguments for widget initialization.
            settings (Any): Settings related to graph visualization and interaction.
            rect_corner_start (Any): Starting corner for a selection rectangle.
            rect_corner_end (Any): Ending corner for a selection rectangle.
        
    """
    class _ConnectionDragHandler:
        def _ConnectionDragHandler__completed(self):
            ...
        def __init__(self, start_port):
            ...
        def abort(self):
            ...
        def can_connect(self, target_port):
            ...
        def complete(self):
            ...
        def destroy(self):
            ...
        def hover_begin(self, hover_node, hover_port, hover_widget):
            ...
        def hover_end(self, port = None):
            ...
        def start(self):
            ...
    class _Event(set):
        """
        
                A list of callable objects. Calling an instance of this will cause a
                call to each item in the list in ascending order by index.
                
        """
        def __call__(self, *args, **kwargs):
            """
            Called when the instance is “called” as a function
            """
        def __repr__(self):
            """
            
                        Called by the repr() built-in function to compute the “official”
                        string representation of an object.
                        
            """
    class _EventSubscription:
        """
        
                Event subscription.
        
                _Event has callback while this object exists.
                
        """
        def __del__(self):
            """
            Called by GC.
            """
        def __init__(self, event, fn):
            """
            
                        Save the function, the event, and add the function to the event.
                        
            """
    class _Proxy:
        """
        
                A service proxy object to keep the given object in a central
                location. It's used to keep the delegate and this object is passed to
                the nodes, so when the delegate is changed, it's automatically
                updated in all the nodes.
        
                TODO: Add `set_delegate`. Otherwise it's useless.
                
        """
        def __getattr__(self, attr):
            """
            
                        Called when the default attribute access fails with an
                        AttributeError.
                        
            """
        def __init__(self, reference = None):
            ...
        def __setattr__(self, attr, value):
            """
            
                        Called when an attribute assignment is attempted. This is called
                        instead of the normal mechanism (i.e. store the value in the
                        instance dictionary).
                        
            """
        def set_object(self, reference):
            """
            Replace the object this proxy holds with the new one
            """
    DEFAULT_DISTANCE_BETWEEN_NODES: typing.ClassVar[float] = 50.0
    @staticmethod
    def _GraphView__delayed_build_layout(*args, **kwargs):
        """
        
                Rebuild all the nodes and connections in the next update cycle. It's
                delayed because it's possible that it's called multiple times a
                frame. And we need to create all the widgets only one.
        
                The challenge here is the ability of USD making input-to-input and output-to-output connections. In USD it's
                perfectly fine to have the following network:
        
                A.out --> B.out
                A.in  <-- B.in
        
                So it doesn't matter if the port is input or output. To draw such connections properly and to know which side
                of the node it should connect, we need to find out the direction of the flow in this node network. This is the
                overview of the algorithm to trace the nodes and compute the direction of the flow.
        
                STEP 1. Create the cache of the model and indices to be able to access the cache fast.
        
                STEP 2. Scan all the nodes and find roots. A root is a node that doesn't have an output connected to another
                node.
        
                STEP 3. Trace connections of roots and assign them level. Level is the distance of the node from the root.
                The root has level 0. The nodes connected to root has level one. The next connected nodes have level 2 etc.
                We assume that level is the flow direction. The flow goes from nodes to root.
        
                STEP 4. It's easy to check if the connection goes to the direction opposite to flow. Such connections have
                virtual ports.
                
        """
    def _GraphView__add_force_redraws_to_diff(self, diff: omni.kit.widget.graph.graph_node_index.GraphNodeDiff, graph_node_index: omni.kit.widget.graph.graph_node_index.GraphNodeIndex):
        """
        
                Add the force_redraw_nodes, if any, by adding them to both the nodes_to_add and nodes_to_del sides.
                Also do the same with any connections to the node(s).  By deleting and then adding, it forces a redraw.
                
        """
    def _GraphView__arrange_nodes(self, node_and_level):
        """
        
                Set the the position of the nodes. If the node doesn't have a
                predefined position (TODO), the position is assigned automatically.
                It's async because it waits until the node is created to get its size.
                
        """
    def _GraphView__cache_positions(self):
        """
        Creates cache for all the positions of all the nodes
        """
    def _GraphView__canvas_space(self, x: float, y: float):
        """
        Convert mouse to canvas space
        """
    def _GraphView__disconnect_inputs(self, port):
        """
        Remove connections from port
        """
    def _GraphView__on_item_changed(self, item):
        """
        Called by the model when something is changed
        """
    def _GraphView__on_port_hovered(self, node, port, widget, hovered):
        """
        Called when the mouse pointer enters the area of the port
        """
    def _GraphView__on_selection_changed(self):
        """
        Called by the model when selection is changed
        """
    def _GraphView__on_start_connection(self, node, port, from_is_input, from_widget, to_widget, modifier = None):
        """
        Called when the user starts creating connection
        """
    def _GraphView__rebuild_node(self, item, full = False):
        """
        Rebuild the delegate of the node, this could be used to just update the look of one node
        """
    def _GraphView__rectangle_selection_begin(self, x: float, y: float, button: int, modifier: int):
        """
        Mouse pressed callback
        """
    def _GraphView__rectangle_selection_end(self, x: float, y: float, button: int, modifier: int):
        """
        Mouse released callback
        """
    def _GraphView__rectangle_selection_moved(self, x: float, y: float, modifier: int, pressed: bool):
        """
        Mouse moved callback
        """
    def __getattr__(self, attr):
        """
        Pretend it's self.__root_frame
        """
    def __init__(self, **kwargs):
        """
        
                Initialize a GraphView widget.
        
                Keyword Arguments:
                    `model : GraphModel`
                        Model to display the node graph
        
                    `delegate : AbstractGraphNodeDelegate`
                        Delegate to draw the node
        
                    `virtual_ports : bool`
                        True when the model should use reversed output for better look
                        of the graph.
        
                    `port_grouping : bool`
                        True when the widget should use sub-ports for port grouping.
        
                    `draw_curve_top_layer : bool`
                        When True, connections are drawn in 2 passes.  The "under" layer is for the
                        opaque curve, and the "top" or "over" layer is meant for floating curve anchor
                        decorations that need to be on top of all nodes, like a value display. Its curve
                        should be drawn transparent. False by default, so both layers are not drawn.
        
                    `allow_same_side_connections : bool`
                        When True, connections can happen between two input ports or two output ports. This is only used within
                        one node. We don't support same side connection between different nodes yet.
        
                    All other kwargs are passed to CanvasFrame which is the root widget.
                
        """
    def _clear_selection_next_frame_async(self, model):
        """
        
                Called by background layer to clear selection. The idea is that if no
                node cancels it, then the yser clicked in the background and we need
                to deselect all.
                
        """
    def _on_finish_connection(self):
        """
        Called when the user finishes creating a connection.
        """
    def _on_node_selected(self, model, node, modifier = 0, pressed = True):
        """
        Called when the user is picking to select nodes
        """
    def _on_port_context_menu(self, node, port):
        """
        Open context menu for specific port
        """
    def _on_rectangle_select(self, model, start, end, modifier = 0):
        """
        Called when the user is performing the rectangle selection
        """
    def _on_set_zoom_key_shortcut(self, mouse_button, key):
        """
        allow user to set the key shortcut for the graphView zoom
        """
    def _post_delayed_build_layout(self):
        """
        Call the event object that has the list of functions
        """
    def _pre_delayed_build_layout(self):
        """
        Call the event object that has the list of functions
        """
    def destroy(self):
        """
        Destroy the GraphView and clean up associated resources.
        
                Called by extension before destroying this object. It doesn't happen automatically.
                Without this hot reloading doesn't work.
        """
    def filter_upstream(self, nodes: list):
        """
        Filter the graph to show only nodes upstream of the specified nodes.
        
                Args:
                    nodes (list): A list of nodes to filter by.
                
        """
    def focus_on_nodes(self, nodes: typing.Optional[typing.List[typing.Any]] = None):
        """
        Center the view on the specified nodes.
        
                Args:
                    nodes (Optional[List[Any]]): A list of nodes to focus on. Defaults to None, which will focus on all nodes.
                
        """
    def get_bbox_of_nodes(self, nodes: list):
        """
        Get the bounding box that encompasses the specified nodes.
        
                Args:
                    nodes (list): A list of nodes to calculate the bounding box for.
        
                Returns:
                    A tuple containing the width, height, and position (x, y) of the bounding box.
                
        """
    def layout_all(self):
        """
        Reset positions of all the nodes in the model
        """
    def set_delegate(self, delegate: omni.kit.widget.graph.abstract_graph_node_delegate.AbstractGraphNodeDelegate):
        """
        Set the delegate responsible for drawing nodes.
        
                Args:
                    delegate (AbstractGraphNodeDelegate): The delegate to use for drawing nodes.
                
        """
    def set_expansion(self, state: omni.kit.widget.graph.graph_model.GraphModel.ExpansionState):
        """
        Open, close or minimize all the nodes in the model.
        
                Args:
                    state (GraphModel.ExpansionState): The expansion state to set for all nodes.
                
        """
    def set_model(self, model: omni.kit.widget.graph.graph_model.GraphModel):
        """
        Set the graph model for the view. It will refresh all the content.
        
                Args:
                    model (GraphModel): The graph model to display.
                
        """
    def subscribe_empty_connection_drop(self, fn):
        """
        Subscribe to the event triggered when a connection is dropped on an empty area.
        
                Args:
                    fn (callable): The function to call when the event is triggered.
        
                Returns:
                    An _EventSubscription object that will unsubscribe when destroyed.
                
        """
    def subscribe_post_delayed_build_layout(self, fn):
        """
        Subscribe to the event triggered after a delayed layout build.
        
                Args:
                    fn (callable): The function to call when the event is triggered.
        
                Returns:
                    An _EventSubscription object that will unsubscribe when destroyed.
                
        """
    def subscribe_pre_delayed_build_layout(self, fn):
        """
        Subscribe to the event triggered before a delayed layout build.
        
                Args:
                    fn (callable): The function to call when the event is triggered.
        
                Returns:
                    An _EventSubscription object that will unsubscribe when destroyed.
                
        """
    @property
    def model(self):
        """
        Gets the current graph model.
        
                Returns:
                    The current GraphModel instance.
                
        """
    @model.setter
    def model(self, model):
        """
        Sets the graph model.
        
                Args:
                    model (GraphModel): The GraphModel instance to set.
                
        """
    @property
    def pan_x(self):
        """
        Gets the current horizontal pan position of the graph.
        
                Returns:
                    The horizontal pan position.
                
        """
    @pan_x.setter
    def pan_x(self, value):
        """
        Sets the horizontal pan position of the graph.
        
                Args:
                    value (float): The new horizontal pan position.
                
        """
    @property
    def pan_y(self):
        """
        Gets the current vertical pan position of the graph.
        
                Returns:
                    The vertical pan position.
                
        """
    @pan_y.setter
    def pan_y(self, value):
        """
        Sets the vertical pan position of the graph.
        
                Args:
                    value (float): The new vertical pan position.
                
        """
    @property
    def raster_nodes(self):
        """
        Gets whether node rasterization is enabled.
        
                Returns:
                    A boolean indicating if rasterization is enabled.
                
        """
    @property
    def selection(self):
        """
        Gets the currently selected nodes in the graph.
        
                Returns:
                    A list of the currently selected nodes.
                
        """
    @selection.setter
    def selection(self, value):
        """
        Sets the currently selected nodes in the graph.
        
                Args:
                    value (list): A list of nodes to set as selected.
                
        """
    @property
    def virtual_ports(self):
        """
        Gets whether virtual ports are enabled.
        
                Returns:
                    A boolean indicating if virtual ports are enabled.
                
        """
    @virtual_ports.setter
    def virtual_ports(self, value):
        """
        Sets whether virtual ports should be enabled.
        
                Args:
                    value (bool): The value to set for virtual ports.
                
        """
    @property
    def zoom(self):
        """
        Gets the current zoom level of the graph.
        
                Returns:
                    The current zoom level.
                
        """
    @zoom.setter
    def zoom(self, value):
        """
        Sets the zoom level of the graph.
        
                Args:
                    value (float): The new zoom level.
                
        """
    @property
    def zoom_max(self):
        """
        Gets the maximum zoom level of the graph.
        
                Returns:
                    The maximum zoom level.
                
        """
    @zoom_max.setter
    def zoom_max(self, value):
        """
        Sets the maximum zoom level of the graph.
        
                Args:
                    value (float): The new maximum zoom level.
                
        """
    @property
    def zoom_min(self):
        """
        Gets the minimum zoom level of the graph.
        
                Returns:
                    The minimum zoom level.
                
        """
    @zoom_min.setter
    def zoom_min(self, value):
        """
        Sets the minimum zoom level of the graph.
        
                Args:
                    value (float): The new minimum zoom level.
                
        """
def handle_exception(func):
    """
    
        Decorator to print exception in async functions
    
        TODO: The alternative way would be better, but we want to use traceback.format_exc for better error message.
            result = await asyncio.gather(*[func(*args)], return_exceptions=True)
        
    """
CONNECTION_CURVE: int = 60
FLOATING_DELTA: float = 1e-05
