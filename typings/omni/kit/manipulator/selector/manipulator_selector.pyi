from __future__ import annotations
import carb as carb
import omni as omni
from pxr import Sdf
__all__ = ['ManipulatorSelector', 'Sdf', 'carb', 'omni']
class ManipulatorSelector:
    """
    
        Manages the selection and ordering of manipulators in a USD context. It will auto
        enable/disable each prim manipulator when selection changed.
        
    """
    def __del__(self):
        ...
    def __init__(self, order_manager: ManipulatorOrderManager, usd_context_name: str):
        """
        
                Initialize the ManipulatorSelector.
        
                Args:
                    order_manager (:obj:'ManipulatorOrderManager'): Manager for manipulator orders.
                    usd_context_name (str): Name of the USD context.
                
        """
    def _on_orders_changed(self):
        ...
    def _on_selection_changed(self):
        ...
    def _on_stage_selection_event(self, event: carb.events.IEvent):
        ...
    def _refresh(self):
        ...
    def _sort(self) -> bool:
        ...
    def destroy(self):
        """
         Clean up resources used by the ManipulatorSelector.
        """
    def register_manipulator_instance(self, name: str, manipulator: ManipulatorBase):
        """
        
                Register a prim manipulator instance.
        
                Args:
                    name (str): Name of the manipulator.
                    manipulator (:obj:'ManipulatorBase'): Manipulator instance.
                
        """
    def unregister_manipulator_instance(self, name: str, manipulator: ManipulatorBase):
        """
        
                Unregister a manipulator instance.
        
                Args:
                    name (str): Name of the manipulator.
                    manipulator (:obj:'ManipulatorBase'): Manipulator instance.
                
        """
