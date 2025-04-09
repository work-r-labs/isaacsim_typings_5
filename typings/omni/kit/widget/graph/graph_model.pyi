"""
This module defines the GraphModel class used for managing the data structure and interactions within a graph widget, following the model-view pattern.
"""
from __future__ import annotations
import enum
from enum import Enum
from enum import IntFlag
from enum import auto
import typing
__all__: list = ['GraphModel']
class GraphModel:
    """
    The base class for the Graph model.
    
        The model is the central component of the graph widget. It is the
        application's dynamic data structure, independent of the user interface,
        and it directly manages the data. It follows closely model–view pattern.
        It defines the standard interface to be able to interoperate with the
        components of the model-view architecture. It is not supposed to be
        instantiated directly. Instead, the user should subclass it to create a
        new model.
    
        The model manages two kinds of data elements. Node and port are the
        atomic data elements of the model. Both node and port can have any number
        of sub-ports and any number of input and output connections.
    
        There is no specific Python type for the elements of the model. Since
        Python has dynamic types, the model can return any object as a node or a
        port. When the widget needs to get a property of the node, it provides
        the given node back to the model.
    
        Example:
    
        .. code:: python
    
           class UsdShadeModel(GraphModel):
               @property
               def nodes(self, prim=None):
                   # Return Usd.Prim in a list
                   return [stage.GetPrimAtPath(selection)]
    
               @property
               def name(self, item=None):
                   # item here is Usd.Prim because UsdShadeModel.nodes returns
                   # Usd.Prim
                   return item.GetPath().name
    
           # Accessing nodes and properties example
           model = UsdShadeModel()
    
           # UsdShadeModel decides the type of nodes. It's a list with Usd.Prim
           nodes = model.nodes
    
           for node in nodes:
               # The node is accessed through evaluation of self[key]. It will
               # return the proxy object that redirects its properties back to
               # model. So the following line will call UsdShadeModel.name(node).
               name = model[node].name
               print(f"The model has node {name}")
        
    """
    class ExpansionState(enum.Enum):
        """
        Enum for node expansion states.
        """
        CLOSED: typing.ClassVar[GraphModel.ExpansionState]  # value = <ExpansionState.CLOSED: 2>
        MINIMIZED: typing.ClassVar[GraphModel.ExpansionState]  # value = <ExpansionState.MINIMIZED: 1>
        OPEN: typing.ClassVar[GraphModel.ExpansionState]  # value = <ExpansionState.OPEN: 0>
    class PreviewState(enum.IntFlag):
        """
        Enum flags for node preview states.
        """
        CACHED: typing.ClassVar[GraphModel.PreviewState]  # value = <PreviewState.CACHED: 2>
        LARGE: typing.ClassVar[GraphModel.PreviewState]  # value = <PreviewState.LARGE: 4>
        NONE: typing.ClassVar[GraphModel.PreviewState]  # value = <PreviewState.NONE: 0>
        OPEN: typing.ClassVar[GraphModel.PreviewState]  # value = <PreviewState.OPEN: 1>
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
    class _ItemProxy:
        """
        
                The proxy that allows accessing the nodes and ports of the model
                through evaluation of self[key]. This proxy object redirects its
                properties to the model that has properties like this:
        
                class Model:
                   @property
                   def name(self, item):
                       pass
        
                   @name.setter
                   def name(self, value, item):
                       pass
        
                
        """
        def __getattr__(self, attr):
            """
            
                        Called when the default attribute access fails with an
                        AttributeError.
                        
            """
        def __init__(self, model, item):
            """
            Save model and item to be able to redirect the properties
            """
        def __setattr__(self, attr, value):
            """
            
                        Called when an attribute assignment is attempted. This is called
                        instead of the normal mechanism (i.e. store the value in the
                        instance dictionary).
                        
            """
    DISPLAY_NAME = None
    @staticmethod
    def has_nodes(obj):
        """
        Checks whether the model can currently build the graph network using the provided object.
        
                Args:
                    obj: The object to check for nodes.
        
                Returns:
                    bool: True if nodes are present; otherwise, False.
        """
    def __getitem__(self, item):
        """
        Called to implement evaluation of self[key]
        """
    def __init__(self):
        """
        Initialize the GraphModel, setting up events for item changes, node changes, and selection changes.
        """
    def _item_changed(self, item = None):
        """
        Call the event object that has the list of functions
        """
    def _rebuild_node(self, item = None, full = False):
        """
        Call the event object that has the list of functions
        """
    def _selection_changed(self):
        """
        Call the event object that has the list of functions
        """
    def can_connect(self, source, target):
        """
        Determines if a connection between source and target is allowed.
        
                Args:
                    source: The starting point of the connection.
                    target: The end point of the connection.
        
                Returns:
                    bool: True if the connection is possible; otherwise, False.
        """
    def destroy(self):
        """
        Perform any necessary cleanup when the GraphModel is destroyed.
        """
    def position_begin_edit(self, item):
        """
        Invoked when a user starts dragging the node.
        
                Args:
                    item: The item being edited.
        """
    def position_end_edit(self, item):
        """
        Invoked when a user has finished dragging the node and released the mouse.
        
                Args:
                    item: The item that was edited.
        """
    def size_begin_edit(self, item):
        """
        Invoked when a user starts resizing the node.
        
                Args:
                    item: The item being resized.
        """
    def size_end_edit(self, item):
        """
        Invoked when a user has finished resizing the node and released the mouse.
        
                Args:
                    item: The item that was resized.
        """
    def special_select_widget(self, node, node_widget):
        """
        Provides a special selection widget for the node if necessary.
        
                Args:
                    node: The node for which the selection widget is to be provided.
                    node_widget: The widget corresponding to the node.
        
                Returns:
                    A widget to be used for the node's selection, or None if the default node_widget should be used.
        """
    def subscribe_item_changed(self, fn):
        """
        Subscribes a callback function to item change events.
        
                Args:
                    fn: The callback function to be invoked when an item changes.
        
                Returns:
                    An _EventSubscription object that will automatically unsubscribe when destroyed.
        """
    def subscribe_node_changed(self, fn):
        """
        Subscribes a callback function to node change events.
        
                Args:
                    fn: The callback function to be invoked when a node changes.
        
                Returns:
                    An _EventSubscription object that will automatically unsubscribe when destroyed.
        """
    def subscribe_selection_changed(self, fn):
        """
        Subscribes a callback function to selection change events.
        
                Args:
                    fn: The callback function to be invoked when the selection changes.
        
                Returns:
                    An _EventSubscription object that will automatically unsubscribe when destroyed.
        """
    @property
    def add_empty_input_port(self, item) -> bool:
        """
        Create IsolationGraphModel.EmptyPort for IsolationGraphModel.InputNode's.
        
                Returns:
                    Defines whether or not an empty port should be created.
        """
    @property
    def add_empty_output_port(self, item) -> bool:
        """
        Create IsolationGraphModel.EmptyPort for IsolationGraphModel.OutputNode's.
        
                Returns:
                    Defines whether or not an empty port should be created.
        """
    @property
    def description(self, item):
        """
        The text label that is displayed on the backdrop in the node graph.
        
                Returns:
                    The description text of the item.
        """
    @description.setter
    def description(self, value, item = None):
        """
        Sets the description of the item.
        
                Args:
                    value: The new description text.
                    item: The item whose description is being set.
        """
    @property
    def display_color(self, item):
        """
        Gets the display color of the item.
        
                Returns:
                    The display color of the item.
        """
    @display_color.setter
    def display_color(self, value, item = None):
        """
        Sets the display color of the item.
        
                Args:
                    value: The new color value.
                    item: The item whose display color is being set.
        """
    @property
    def expansion_state(self, item = None) -> GraphModel.ExpansionState:
        """
        Gets the expansion state of the item.
        
                Returns:
                    The expansion state of the item.
        """
    @expansion_state.setter
    def expansion_state(self, value: GraphModel.ExpansionState, item = None):
        """
        Sets the expansion state of the item.
        
                Args:
                    value: The new expansion state.
                    item: The item whose expansion state is being set.
        """
    @property
    def icon(self, item) -> typing.Union[str, typing.Any, NoneType]:
        """
        Gets the icon of the image.
        
                Returns:
                    The icon of the item, which can be a string or any other type.
        """
    @icon.setter
    def icon(self, value: typing.Union[str, typing.Any, NoneType], item = None):
        """
        Sets the icon of the image.
        
                Args:
                    value: The new icon value, which can be a string or any other type.
                    item: The item whose icon is being set.
        """
    @property
    def inputs(self, item):
        """
        Gets the inputs of the item.
        
                Returns:
                    The inputs of the item.
        """
    @inputs.setter
    def inputs(self, value, item = None):
        """
        Sets the inputs of the item.
        
                Args:
                    value: The new inputs value.
                    item: The item whose inputs are being set.
        """
    @property
    def name(self, item) -> str:
        """
        Gets the name of the item.
        
                Returns:
                    The name of the item.
        """
    @name.setter
    def name(self, value: str, item = None):
        """
        Sets the name of the item.
        
                Args:
                    value: The new name.
                    item: The item whose name is being set.
        """
    @property
    def nodes(self, item = None):
        """
        Gets the nodes of the item.
        
                Returns:
                    The nodes of the item.
        """
    @property
    def outputs(self, item):
        """
        Gets the outputs of the item.
        
                Returns:
                    The outputs of the item.
        """
    @outputs.setter
    def outputs(self, value, item = None):
        """
        Sets the outputs of the item.
        
                Args:
                    value: The new outputs value.
                    item: The item whose outputs are being set.
        """
    @property
    def ports(self, item = None):
        """
        Gets the ports of the item.
        
                Returns:
                    The ports of the item.
        """
    @ports.setter
    def ports(self, value, item = None):
        """
        Sets the ports of the item.
        
                Args:
                    value: The new ports value.
                    item: The item whose ports are being set.
        """
    @property
    def position(self, item = None):
        """
        Gets the position of the item.
        
                Returns:
                    The position of the item.
        """
    @position.setter
    def position(self, value, item = None):
        """
        Sets the position of the item.
        
                Args:
                    value: The new position value.
                    item: The item whose position is being set.
        """
    @property
    def preview(self, item) -> typing.Union[str, typing.Any, NoneType]:
        """
        Gets the preview of the image.
        
                Returns:
                    The preview of the item, which can be a string or any other type.
        """
    @preview.setter
    def preview(self, value: typing.Union[str, typing.Any, NoneType], item = None):
        """
        Sets the preview of the image.
        
                Args:
                    value: The new preview value, which can be a string or any other type.
                    item: The item whose preview is being set.
        """
    @property
    def preview_state(self, item) -> GraphModel.PreviewState:
        """
        Gets the state of the preview of the node.
        
                Returns:
                    The preview state of the item.
        """
    @preview_state.setter
    def preview_state(self, value: GraphModel.PreviewState, item = None):
        """
        Sets the state of the preview of the node.
        
                Args:
                    value: The new preview state.
                    item: The item whose preview state is being set.
        """
    @property
    def selection(self):
        """
        Gets the current selection list.
        
                Returns:
                    The current selection list.
        """
    @selection.setter
    def selection(self, value: list):
        """
        Sets the selection list.
        
                Args:
                    value: The new selection list.
        """
    @property
    def size(self, item):
        """
        The node size. Is used for nodes like Backdrop.
        
                Returns:
                    The size of the item.
        """
    @size.setter
    def size(self, value, item = None):
        """
        The node position setter.
        
                Args:
                    value: The new size value.
                    item: The item whose size is being set.
        """
    @property
    def stacking_order(self, item):
        """
        This value is a hint when an application cares about the visibility
                of a node and whether each node overlaps another.
        
                Returns:
                    An integer representing the stacking order.
        """
    @property
    def type(self, item):
        """
        Gets the type of the item.
        
                Returns:
                    The type of the item.
        """
