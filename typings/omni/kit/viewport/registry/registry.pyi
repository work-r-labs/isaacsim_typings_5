from __future__ import annotations
__all__: list = ['_make_registry']
class _Factory:
    """
    A wrapper class for a factory function or class with an optional identifier.
    
        This class is used to represent a factory and provide a callable interface, along with a string
        representation, and a property to access the factory's identifier.
    
        Args:
            factory: Callable
                The factory function or class to be wrapped.
            factory_id: str
                The identifier for the factory. Defaults to the class name if not provided.
    """
    def __call__(self, *args, **kwargs):
        """
        Allows the _Factory instance to be called like a function, which calls the wrapped factory.
        
                Args:
                    *args: Variable length argument list to be passed to the factory callable.
                    **kwargs: Arbitrary keyword arguments to be passed to the factory callable.
        
                Returns:
                    The result of the factory callable.
                
        """
    def __init__(self, factory: typing.Callable, factory_id: str = None):
        """
        Initializes the internal factory instance with provided callable and identifier.
        
                Args:
                    factory (Callable): The factory function or class to be wrapped.
                    factory_id (str, optional): The identifier for the factory. If not provided, the class name of the factory will be used.
                
        """
    def __repr__(self) -> str:
        """
        Generates a string representation of the _Factory instance, including its identifier.
        
                Returns:
                    str: A string representation of the _Factory instance.
                
        """
    @property
    def factory_id(self):
        """
        Property that returns the identifier of the factory.
        
                Returns:
                    The factory identifier.
                
        """
def _make_registry():
    """
    Creates and returns the _Registry class.
    
        This function constructs a nested _Registry class that is used to manage the registration and deregistration of
        viewport factories. It provides mechanisms to add or remove factories, invoke callbacks when factories are loaded
        or unloaded, and retrieve factories in a specified order.
    
        Returns:
            _Registry: A class capable of registering and deregistering viewport factories, managing callbacks for factory
                load events, and providing ordered access to the factories.
        
    """
