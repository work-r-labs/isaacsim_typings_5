from __future__ import annotations
from omni.kit.manipulator.transform.toolbar_tool import ToolbarTool
import typing
import weakref as weakref
from weakref import ReferenceType
__all__ = ['ReferenceType', 'ToolbarRegistry', 'ToolbarTool', 'weakref']
class ToolbarRegistry:
    """
    A registry for managing toolbar tools in an application.
    
        This class holds a collection of ToolbarTool classes and provides mechanisms to register or unregister these tools, subscribe to changes in the registry, and retrieve a sorted list of registered tools.
    
        
    """
    class Subscription:
        """
        Represents a subscription to the toolbar registry change events.
        
                This class handles the lifecycle of a subscription to the toolbar registry, allowing for the registration and release of callback functions that listen for changes in the toolbar tool registry.
        
                Args:
                    registry: ReferenceType[ToolbarRegistry]
                        A weak reference to the ToolbarRegistry instance.
                    id: str
                        The unique identifier for this subscription.
        """
        def __del__(self):
            ...
        def __init__(self, registry: ReferenceType[ToolbarRegistry], id: str):
            ...
        def release(self):
            ...
    def __init__(self):
        ...
    def _notify_registry_changed(self, callback: typing.Callable[[], None] = None):
        ...
    def register_tool(self, tool_class: Type[ToolbarTool], id: str):
        """
        
                Registers a tool class to the registry.
        
                Args:
                    tool_class (Type[ToolbarTool]): The class of the tool to be registered.
                    id (str): Unique id of the tool. It must not already exist.
                
        """
    def set_sort_key_function(self, key: typing.Callable[[tuple[str, Type[ToolbarTool]]], typing.Any]):
        """
        
                Set a custom key function to sort the registered tool classes.
        
                Args:
                    key (Callable[[Tuple[str, Type[ToolbarTool]]], Any]): key function used for sorting.
        
                
        """
    def subscribe_to_registry_change(self, callback: typing.Callable[[], None]) -> int:
        """
        
                Subscribes to registry changed event. Callback will be called when tool classes are registered or unregistered.
        
                Args:
                    callback (Callable[[], None]): the callback to be called. It is called immediately before function returns.
        
                Return:
                    An Subscription object. Call sub.release() to unsubscribe.
        
                
        """
    def unregister_tool(self, id: str):
        """
        
                Unregisters a tool class using its id.
        
                Args:
                    id (str): The id used in `register_tool`
                
        """
    def unsubscribe_to_registry_change(self, id: int):
        """
        
                Called be Subscription.release to unsubscribe from registry changed event. Do not call this function directly.
                User should use Subscription object to unsubscribe.
        
                Args:
                    id (int): id returned from subscribe_to_registry_change
        
                
        """
    @property
    def tools(self) -> list[Type[ToolbarTool]]:
        """
        Gets a sorted list of all tool classes.
        """
