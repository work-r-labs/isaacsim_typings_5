"""
This module provides a class to isolate and manage a sub-graph within a larger graph model, including functionality for adding, editing, and connecting nodes and ports in the isolated section.
"""
from __future__ import annotations
import omni.kit.widget.graph.graph_model
from omni.kit.widget.graph.graph_model import GraphModel
from omni.kit.widget.graph.graph_model_batch_position_helper import GraphModelBatchPositionHelper
__all__: list = ['IsolationGraphModel']
class IsolationGraphModel:
    """
    A model class to isolate and manage a sub-graph within a larger graph model.
    
        This class provides functionality to create and manage a sub-graph within a larger graph model. It allows for the isolation of a section of a graph model, enabling operations such as adding, editing, and connecting nodes and ports within this isolated section, without affecting the rest of the graph model.
    
        Args:
            model (GraphModel): The graph model from which the sub-graph is isolated.
            root: The root node of the sub-graph to be isolated.
    """
    class EmptyPort:
        """
        Is used by the model for an empty port
        """
        @staticmethod
        def get_type_name() -> str:
            """
            The string type that goes the source model abd view
            """
        def __init__(self, parent: typing.Union[ForwardRef('IsolationGraphModel.InputNode'), ForwardRef('IsolationGraphModel.OutputNode')]):
            ...
    class InputNode:
        """
        
                Is used by the model for the input node. This node represents input
                ports of the compound node and it's placed to the subnetwork of the
                compound.
                
        """
        @staticmethod
        def get_type_name() -> str:
            """
            The string type that goes the source model and view
            """
        def __getattr__(self, attr):
            ...
        def __hash__(self):
            ...
        def __init__(self, model: omni.kit.widget.graph.graph_model.GraphModel, source):
            ...
        @property
        def __delattr__(self, *args):
            ...
        @property
        def __dir__(self, *args):
            ...
        @property
        def __eq__(self, *args):
            ...
        @property
        def __format__(self, *args):
            ...
        @property
        def __ge__(self, *args):
            ...
        @property
        def __gt__(self, *args):
            ...
        @property
        def __init_subclass__(self, *args):
            ...
        @property
        def __le__(self, *args):
            ...
        @property
        def __lt__(self, *args):
            ...
        @property
        def __ne__(self, *args):
            ...
        @property
        def __reduce__(self, *args):
            ...
        @property
        def __reduce_ex__(self, *args):
            ...
        @property
        def __repr__(self, *args):
            ...
        @property
        def __sizeof__(self, *args):
            ...
        @property
        def __str__(self, *args):
            ...
        @property
        def __subclasshook__(self, *args):
            ...
        @property
        def ports(self) -> typing.Optional[typing.List[typing.Any]]:
            """
            The list of ports of this node. It only has input ports from the compound node.
            """
    class MagicWrapperMeta(type):
        """
        
                Python always looks in the class (and parent classes) __dict__ for
                magic methods and __getattr__ doesn't work, but since we want to
                override them, we need to use this trick with proxy property.
        
                It makes the class looking like the source object.
        
                See https://stackoverflow.com/questions/9057669 for details.
                
        """
        @classmethod
        def __init__(cls, name, bases, dct):
            ...
    class OutputNode:
        """
        
                Is used by the model for the ouput node. This node represents output
                ports of the comound node and it's placed to the subnetwork of the
                compound.
                
        """
        @staticmethod
        def get_type_name() -> str:
            """
            The string type that goes the source model and view
            """
        def __getattr__(self, attr):
            ...
        def __hash__(self):
            ...
        def __init__(self, model: omni.kit.widget.graph.graph_model.GraphModel, source):
            ...
        @property
        def __delattr__(self, *args):
            ...
        @property
        def __dir__(self, *args):
            ...
        @property
        def __eq__(self, *args):
            ...
        @property
        def __format__(self, *args):
            ...
        @property
        def __ge__(self, *args):
            ...
        @property
        def __gt__(self, *args):
            ...
        @property
        def __init_subclass__(self, *args):
            ...
        @property
        def __le__(self, *args):
            ...
        @property
        def __lt__(self, *args):
            ...
        @property
        def __ne__(self, *args):
            ...
        @property
        def __reduce__(self, *args):
            ...
        @property
        def __reduce_ex__(self, *args):
            ...
        @property
        def __repr__(self, *args):
            ...
        @property
        def __sizeof__(self, *args):
            ...
        @property
        def __str__(self, *args):
            ...
        @property
        def __subclasshook__(self, *args):
            ...
        @property
        def ports(self) -> typing.Optional[typing.List[typing.Any]]:
            """
            The list of ports of this node. It only has output ports from the compound node.
            """
    class _IsolationItemProxy(omni.kit.widget.graph.graph_model.GraphModel._ItemProxy):
        """
        
                The proxy class that redirects the model calls from view to the
                source model or to the isolation model.
                
        """
        display_color: typing.Optional[typing.Tuple[float]]
        position: typing.Optional[typing.Tuple[float]]
        size: typing.Optional[typing.Tuple[float]]
        def __init__(self, model: omni.kit.widget.graph.graph_model.GraphModel, item: typing.Any, isolation_model: IsolationGraphModel):
            ...
        def __setattr__(self, attr, value):
            """
            
                        Called when an attribute assignment is attempted. This is called
                        instead of the normal mechanism (i.e. store the value in the
                        instance dictionary).
                        
            """
        def is_empty_port(self, item: IsolationGraphModel.EmptyPort = None) -> bool:
            """
            True if the current redirection is related to the empty port
            """
        def is_input_node(self, item: typing.Union[ForwardRef('IsolationGraphModel.InputNode'), ForwardRef('IsolationGraphModel.OutputNode')] = None) -> bool:
            """
            True if the current redirection is related to the input node
            """
        def is_output_node(self, item: typing.Union[ForwardRef('IsolationGraphModel.InputNode'), ForwardRef('IsolationGraphModel.OutputNode')] = None) -> bool:
            """
            True if the current redirection is related to the output node
            """
        @property
        def icon(self) -> typing.Any:
            """
            Redirects call to the source model if it's the model of the source model
            """
        @property
        def inputs(self) -> typing.Optional[typing.List[typing.Any]]:
            ...
        @inputs.setter
        def inputs(self, value: typing.List[typing.Any]):
            ...
        @property
        def name(self) -> str:
            """
            Redirects call to the source model if it's the model of the source model
            """
        @name.setter
        def name(self, value: str):
            ...
        @property
        def outputs(self) -> typing.Optional[typing.List[typing.Any]]:
            ...
        @property
        def ports(self) -> typing.Optional[typing.List[typing.Any]]:
            """
            Redirects call to the source model if it's the model of the source model
            """
        @ports.setter
        def ports(self, value: typing.List[typing.Any]):
            ...
        @property
        def preview(self) -> typing.Any:
            """
            Redirects call to the source model if it's the model of the source model
            """
        @property
        def preview_state(self) -> omni.kit.widget.graph.graph_model.GraphModel.PreviewState:
            """
            Redirects call to the source model if it's the model of the source model
            """
        @preview_state.setter
        def preview_state(self, value: omni.kit.widget.graph.graph_model.GraphModel.PreviewState):
            ...
        @property
        def stacking_order(self) -> int:
            ...
        @property
        def type(self) -> str:
            """
            Redirects call to the source model if it's the model of the source model
            """
    def __getattr__(self, attr):
        """
        Pretend it's self._model
        """
    def __getitem__(self, item):
        """
        Called to implement evaluation of self[key]
        """
    def __init__(self, model: omni.kit.widget.graph.graph_model.GraphModel, root):
        """
        Initializes the IsolationGraphModel.
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
    def add_input_or_output(self, position: typing.Tuple[float], is_input: bool = True):
        """
        Adds an input or output node to the isolation graph.
        
                Args:
                    position (Tuple[float]): The position where the node should be added.
                    is_input (bool, optional): Whether the node is an input node. Defaults to True.
        """
    def can_connect(self, source: typing.Any, target: typing.Any):
        """
        Checks if a connection between the source and target can be made.
        
                Args:
                    source (Any): The source of the connection.
                    target (Any): The target of the connection.
        
                Returns:
                    bool: True if the connection is possible, False otherwise.
        """
    def clear_caches(self):
        """
        Clears the internal caches of the model.
        """
    def destroy(self):
        """
        Destroys the model, clearing all internal data and subscriptions.
        """
    def position_begin_edit(self, item: typing.Any):
        """
        Begins the edit operation for the position of an item.
        
                Args:
                    item (Any): The item whose position is being edited.
        """
    def position_end_edit(self, item: typing.Any):
        """
        Ends the edit operation for the position of an item.
        
                Args:
                    item (Any): The item whose position edit operation is being ended.
        """
    def subscribe_item_changed(self, fn):
        """
        Subscribes to item changed events.
        
                Args:
                    fn (Callable): The function to be called when an item changes.
        
                Returns:
                    _EventSubscription: An object that will automatically unsubscribe when destroyed.
        """
    def subscribe_node_changed(self, fn):
        """
        Subscribes to node changed events.
        
                Args:
                    fn (Callable): The function to be called when a node changes.
        
                Returns:
                    _EventSubscription: An object that will automatically unsubscribe when destroyed.
        """
    def subscribe_selection_changed(self, fn):
        """
        Subscribes to selection changed events.
        
                Args:
                    fn (Callable): The function to be called when the selection changes.
        
                Returns:
                    _EventSubscription: An object that will automatically unsubscribe when destroyed.
        """
    @property
    def nodes(self, item: typing.Any = None):
        """
        It's only called to get the nodes from the top level
        
                Returns:
                    Optional[List[Any]]: A list of nodes at the top level, if any.
        """
    @property
    def selection(self) -> typing.Optional[typing.List[typing.Any]]:
        """
        Gets the current selection.
        
                Returns:
                    Optional[List[Any]]: The currently selected items.
        """
    @selection.setter
    def selection(self, value: typing.Optional[typing.List[typing.Any]]):
        """
        Sets the selection, filtering out input and output nodes.
        
                Args:
                    value (Optional[List[Any]]): The items to be selected.
        """
def _get_ports_recursive(model, root):
    """
    Recursively get all the ports
    """
