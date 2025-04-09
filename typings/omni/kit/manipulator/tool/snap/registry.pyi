from __future__ import annotations
import carb as carb
import sys as sys
import typing
__all__ = ['RegistrationHelper', 'SnapProviderRegistry', 'carb', 'sys']
class RegistrationHelper:
    """
    A helper class for registering provider classes.
    
        This class is responsible for discovering and registering all provider classes that inherit from a specified base class within a given module. It ensures that all providers are registered upon initialization and unregistered when destroyed.
    
        Args:
            module_name: str
                Name of the module where provider classes are located.
            base_class: Type
                The base class type that all providers should inherit from.
    """
    def __del__(self):
        """
        Ensures that the `destroy` method is called upon the deletion of an instance.
        """
    def __init__(self, module_name: str, base_class: Type):
        """
        Initializes the RegistrationHelper and registers all provider classes that inherit from the specified base class within the given module.
        
                Args:
                    module_name (str): The name of the module where provider classes are located.
                    base_class (Type): The base class type that all providers should inherit from.
        """
    def _get_all_provider_classes(self, module_name: str, base_class: Type):
        """
        Internal method to retrieve all provider classes from a module that inherit from a specified base class.
        
                Args:
                    module_name (str): The name of the module to search for provider classes.
                    base_class (Type): The base class type to compare against.
        
                Returns:
                    list: A list of provider class types that were found in the module.
        """
    def destroy(self):
        """
        Unregisters all previously registered provider classes and marks the helper as not registered.
        """
class SnapProviderRegistry:
    """
    A registry for managing SnapProvider instances as a singleton.
    
        This class handles the registration and unregistration of SnapProvider classes,
        which are used for snapping objects in a 3D environment. It allows subscribing and unsubscribing to registry change events,
        enabling other parts of the application to react to changes in the SnapProvider ecosystem.
        
    """
    _SnapProviderRegistry__instance: typing.ClassVar[SnapProviderRegistry]  # value = <omni.kit.manipulator.tool.snap.registry.SnapProviderRegistry object>
    @classmethod
    def get_instance(cls) -> SnapProviderRegistry:
        """
        Gets the singleton instance of the SnapProviderRegistry.
        
                Returns:
                    SnapProviderRegistry: The singleton instance of the registry.
        """
    def __del__(self):
        ...
    def __init__(self):
        """
        Initializes the SnapProviderRegistry singleton instance.
        
                Raises:
                    RuntimeError: If an instance already exists.
        """
    def _notify_registry_changed(self, callback: typing.Callable[[], None] = None):
        """
        Notifies all subscribed callbacks that the registry has changed. If a specific callback is provided, only that callback is notified.
        
                Args:
                    callback (Callable[[], None], optional): A specific callback to notify. If not provided, all subscribers are notified.
                
        """
    def destroy(self):
        """
        Destroys the singleton instance of the SnapProviderRegistry.
        """
    def get_provider_class_by_name(self, name: str) -> Type[SnapProvider]:
        """
        Retrieves a registered SnapProvider class by its name.
        
                Args:
                    name (str): The name of the provider class to retrieve.
        
                Returns:
                    Type[SnapProvider] or None: The provider class if found, otherwise None.
        """
    def register_provider(self, provider_class: Type[SnapProvider]):
        """
        Registers a new SnapProvider class to the registry.
        
                Args:
                    provider_class (Type[SnapProvider]): The class of the provider to be registered.
        
                Raises:
                    ValueError: If a provider with the same name is already registered.
        """
    def subscribe_to_registry_change(self, callback: typing.Callable[[], None]) -> int:
        """
        Subscribes a callback to the event that is triggered when the provider registry changes.
        
                Args:
                    callback (Callable[[], None]): The callback to be invoked when the registry changes. It is called immediately before function returns.
        
                Returns:
                    int: An ID that can be used to unsubscribe the callback later.
        """
    def unregister_provider(self, provider_class: Type[SnapProvider]):
        """
        Unregisters an existing SnapProvider class from the registry.
        
                Args:
                    provider_class (Type[SnapProvider]): The class of the provider to be unregistered.
        """
    def unsubscribe_to_registry_change(self, id: int):
        """
        Unsubscribes a previously subscribed callback from the registry change event.
        
                Args:
                    id (int): The ID returned by subscribe_to_registry_change when the callback was initially subscribed.
        """
    @property
    def providers(self) -> dict[str, Type[SnapProvider]]:
        """
        Gets all provider classes.
        
                Returns:
                    Dict[str, Type[SnapProvider]]: A dictionary mapping provider names to their respective SnapProvider classes.
                
        """
