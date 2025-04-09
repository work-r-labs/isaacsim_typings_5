"""
pybind11 carb.settings bindings
"""
from __future__ import annotations
import carb.dictionary._dictionary
import typing
__all__ = ['ChangeEventType', 'ISettings', 'SubscriptionId', 'acquire_settings_interface']
class ChangeEventType:
    """
    Members:
    
      CREATED : An Item was created
    
      CHANGED : An Item was changed
    
      DESTROYED : An Item was destroyed
    """
    CHANGED: typing.ClassVar[ChangeEventType]  # value = <ChangeEventType.CHANGED: 1>
    CREATED: typing.ClassVar[ChangeEventType]  # value = <ChangeEventType.CREATED: 0>
    DESTROYED: typing.ClassVar[ChangeEventType]  # value = <ChangeEventType.DESTROYED: 2>
    __members__: typing.ClassVar[dict[str, ChangeEventType]]  # value = {'CREATED': <ChangeEventType.CREATED: 0>, 'CHANGED': <ChangeEventType.CHANGED: 1>, 'DESTROYED': <ChangeEventType.DESTROYED: 2>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ISettings:
    """
    
    The Carbonite Settings interface
    
    Carbonite settings are built on top of the carb.dictionary interface (which is also required in order to use this
    interface). Many dictionary functions are replicated in settings, but explicitly use the settings database instead of a
    generic carb.dictionary.Item object.
    
    carb.settings uses keys (or paths) that start with an optional forward-slash and are forward-slash separated (example:
    "/log/level"). The settings database exists as a root-level carb.dictionary.Item (of type ItemType.DICTIONARY) that is
    created and maintained by the carb.settings system (typically through the carb.settings.plugin plugin). The root level
    settings carb.dictionary.Item is accessible through get_settings_dictionary().
    
    Portions of the settings database hierarchy can be subscribed to with subscribe_to_tree_change_events() or individual
    keys may be subscribed to with subscribe_to_tree_change_events().
    """
    def create_dictionary_from_settings(self, path: str = '') -> carb.dictionary._dictionary.Item:
        """
        Takes a snapshot of a portion of the setting database as a dictionary.Item.
        
        Parameters:
            path: An optional path from root to access. "/" or "" is interpreted to be the settings database root.
        """
    def destroy_item(self, arg0: str) -> None:
        """
        Destroys the item at the given path.
        
        Any objects that reference the given path become invalid and their use is undefined behavior.
        
        Parameters:
            path: Settings database key path (i.e. "/log/level").
        """
    def get(self, path: str) -> typing.Any:
        """
        Retrieve the stored value at the supplied path as a Python object.
        
        An array value will be returned as a list. If the value does not exist, None will be returned.
        
        Parameters:
            path: Settings database key path (i.e. "/log/level").
        
        Returns:
            A Python object representing the stored value.
        """
    def get_as_bool(self, arg0: str) -> bool:
        """
        Attempts to get the supplied item as a boolean value, either directly or via conversion.
        
        Parameters:
            path: Settings database key path (i.e. "/log/level").
        
        Returns:
            Boolean: a boolean value representing the stored value. If conversion fails, False is returned.
        """
    def get_as_float(self, arg0: str) -> float:
        """
        Attempts to get the supplied item as a floating-point value, either directly or via conversion.
        
        Parameters:
            path: Settings database key path (i.e. "/log/level").
        
        Returns:
            Float: a floating-point value representing the stored value. If conversion fails, 0.0 is returned.
        """
    def get_as_int(self, arg0: str) -> int:
        """
        Attempts to get the supplied item as an integer, either directly or via conversion.
        
        Parameters:
            path: Settings database key path (i.e. "/log/level").
        
        Returns:
            Integer: an integer value representing the stored value. If conversion fails, 0 is returned.
        """
    def get_as_string(self, arg0: str) -> str:
        """
        Attempts to get the supplied item as a string value, either directly or via conversion.
        
        Parameters:
            path: Settings database key path (i.e. "/log/level").
        
        Returns:
            String: a string value representing the stored value. If conversion fails, "" is returned.
        """
    def get_settings_dictionary(self, path: str = '') -> carb.dictionary._dictionary.Item:
        """
        Access the setting database as a dictionary.Item
        
        Accesses the setting database as a dictionary.Item, which allows use of carb.dictionary functions directly.
        
        WARNING: The root dictionary.Item is owned by carb.settings and must not be altered or destroyed.
        
        Parameters:
            path: An optional path from root to access. "/" or "" is interpreted to be the settings database root.
        """
    def initialize_from_dictionary(self, arg0: carb.dictionary._dictionary.Item) -> None:
        """
        Performs a one-time initialization from a given dictionary.Item.
        
        NOTE: This function may only be called once. Subsequent calls will result in an error message logged.
        
        Parameters:
            dictionary: A dictionary.Item to initialize the settings database from. The items are copied into the root of the settings database.
        """
    def is_accessible_as(self, arg0: carb.dictionary._dictionary.ItemType, arg1: str) -> bool:
        """
        Checks if the item could be accessible as the provided type, either directly or via a cast.
        
        Parameters:
            itemType: carb.dictionary.ItemType to check for.
            path: Settings database key path (i.e. "/log/level").
        
        Returns:
            boolean: True if the item is accessible as the provided type; False otherwise.
        """
    def set(self, path: str, value: typing.Any) -> None:
        """
        Sets the given value at the supplied path.
        
        Parameters:
            path: Settings database key path (i.e. "/log/level").
            value: A Python object. The carb.dictionary.ItemType is inferred from the type of the object; if the type is not supported, the value is ignored. Both tuples and lists are treated as arrays (a special kind of ItemType.DICTIONARY).
        """
    def set_bool(self, arg0: str, arg1: bool) -> None:
        """
        Sets the boolean value at the supplied path.
        
        Parameters:
            path: Settings database key path (i.e. "/log/level").
            value: A boolean value to store.
        """
    def set_bool_array(self, arg0: str, arg1: list[bool]) -> None:
        """
        Sets the given array at the supplied path.
        
        Parameters:
            path: Settings database key path (i.e. "/log/level").
            array: A tuple or list of boolean values.
        """
    def set_default(self, path: str, value: typing.Any) -> None:
        ...
    def set_default_bool(self, arg0: str, arg1: bool) -> None:
        """
        Sets a value at the given path, if and only if one does not already exist.
        
        Parameters:
            path: Settings database key path (i.e. "/log/level").
            value: Value that will be stored at the given path if a value does not already exist there.
        """
    def set_default_float(self, arg0: str, arg1: float) -> None:
        """
        Sets a value at the given path, if and only if one does not already exist.
        
        Parameters:
            path: Settings database key path (i.e. "/log/level").
            value: Value that will be stored at the given path if a value does not already exist there.
        """
    def set_default_int(self, arg0: str, arg1: int) -> None:
        """
        Sets a value at the given path, if and only if one does not already exist.
        
        Parameters:
            path: Settings database key path (i.e. "/log/level").
            value: Value that will be stored at the given path if a value does not already exist there.
        """
    def set_default_string(self, arg0: str, arg1: str) -> None:
        """
        Sets a value at the given path, if and only if one does not already exist.
        
        Parameters:
            path: Settings database key path (i.e. "/log/level").
            value: Value that will be stored at the given path if a value does not already exist there.
        """
    def set_float(self, arg0: str, arg1: float) -> None:
        """
        Sets the floating-point value at the supplied path.
        
        Parameters:
            path: Settings database key path (i.e. "/log/level").
            value: A floating-point value to store.
        """
    def set_float_array(self, arg0: str, arg1: list[float]) -> None:
        """
        Sets the given array at the supplied path.
        
        Parameters:
            path: Settings database key path (i.e. "/log/level").
            array: A tuple or list of floating-point values.
        """
    def set_int(self, arg0: str, arg1: int) -> None:
        """
        Sets the integer value at the supplied path.
        
        Parameters:
            path: Settings database key path (i.e. "/log/level").
            value: An integer value to store.
        """
    def set_int_array(self, arg0: str, arg1: list[int]) -> None:
        """
        Sets the given array at the supplied path.
        
        Parameters:
            path: Settings database key path (i.e. "/log/level").
            array: A tuple or list of integer values.
        """
    def set_string(self, arg0: str, arg1: str) -> None:
        """
        Sets the string value at the supplied path.
        
        Parameters:
            path: Settings database key path (i.e. "/log/level").
            value: A string value.
        """
    def set_string_array(self, arg0: str, arg1: list[str]) -> None:
        """
        Sets the given array at the supplied path.
        
        Parameters:
            path: Settings database key path (i.e. "/log/level").
            array: A tuple or list of strings.
        """
    def subscribe_to_node_change_events(self, arg0: str, arg1: typing.Callable[[carb.dictionary._dictionary.Item, ChangeEventType], None]) -> SubscriptionId:
        """
        Subscribes to node change events about a specific item.
        
        When finished with the subscription, call unsubscribe_to_change_events().
        
        Parameters:
            path: Settings database key path (i.e. "/log/level") to subscribe to.
            eventFn: A function that is called for each change event.
        """
    def subscribe_to_tree_change_events(self, arg0: str, arg1: typing.Callable[[carb.dictionary._dictionary.Item, carb.dictionary._dictionary.Item, ChangeEventType], None]) -> SubscriptionId:
        """
        Subscribes to change events for all items in a subtree.
        
        When finished with the subscription, call unsubscribe_to_change_events().
        
        Parameters:
            path: Settings database key path (i.e. "/log/level") to subscribe to.
            eventFn: A function that is called for each change event.
        """
    def unsubscribe_to_change_events(self, id: SubscriptionId) -> None:
        """
        Unsubscribes from change events.
        
        Parameters:
            id: The handle returned from subscribe_to_tree_change_events() or subscribe_to_node_change_events().
        """
    def update(self, arg0: str, arg1: carb.dictionary._dictionary.Item, arg2: str, arg3: typing.Any) -> None:
        """
        Merges the source dictionary.Item into the settings database.
        
        Destination path need not exist and missing items in the path will be created as ItemType.DICTIONARY.
        
        Parameters:
            path: Settings database key path (i.e. "/log/level"). Used as the destination location within the setting database. "/" is considered to be the root.
            dictionary: A dictionary.Item used as the base of the items to merge into the setting database.
            dictionaryPath: A child path of `dictionary` to use as the root for merging. May be None or an empty string in order to use `dictionary` directly as the root.
            updatePolicy: One of dictionary.UpdateAction to use as the policy for updating.
        """
class SubscriptionId:
    """
    Representation of a subscription
    """
def acquire_settings_interface(plugin_name: str = None, library_path: str = None) -> ISettings:
    ...
