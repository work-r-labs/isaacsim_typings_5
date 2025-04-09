from __future__ import annotations
import carb as carb
__all__ = ['MANIPULATOR_ORDERS_SETTING_PATH', 'ManipulatorOrderManager', 'carb']
class ManipulatorOrderManager:
    """
      A manager class that manages the order of prim manipulators.
    """
    def __del__(self):
        ...
    def __init__(self):
        """
         Constructor. 
        """
    def _on_setting_changed(self, tree_item, changed_item, event_type):
        ...
    def _refresh_orders(self):
        ...
    def destroy(self):
        """
         Destroys ManipulatorOrderManager's instance.
        """
    def subscribe_to_orders_changed(self, fn: typing.Callable) -> int:
        """
        
                Subscribes a function to be called when the manipulators' orders change.
        
                Args:
                    fn (Callable): The function to be called when the manipulators' orders change.
                        The funcion's signatrue is: void fn()
        
                Returns:
                    int: A unique identifier for the change function.
                
        """
    def unsubscribe_to_orders_changed(self, id: int):
        """
        
                Unsubscribes a function from being called when the manipulators' orders change.
        
                Args:
                    id (int): The unique identifier of the function to be removed.
                
        """
    @property
    def orders_dict(self) -> typing.Dict[str, int]:
        """
        
                Get the order dictionary containing the manipulator orders.
        
                Returns:
                    Dict[str, int]: A dictionary mapping manipulators' names to their orders.
                
        """
MANIPULATOR_ORDERS_SETTING_PATH: str = '/persistent/exts/omni.kit.manipulator.selector/orders'
