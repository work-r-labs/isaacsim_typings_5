from __future__ import annotations
import omni as omni
from omni.kit.manipulator.selector.manipulator_order_manager import ManipulatorOrderManager
from omni.kit.manipulator.selector.manipulator_selector import ManipulatorSelector
__all__ = ['ManipulatorOrderManager', 'ManipulatorPrim', 'ManipulatorSelector', 'get_manipulator_selector', 'omni']
class ManipulatorPrim(omni.ext._extensions.IExt):
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id):
        ...
def get_manipulator_selector(usd_context_name: str) -> omni.kit.manipulator.selector.manipulator_selector.ManipulatorSelector:
    """
    
        Factory function that returns an instance of the ManipulatorSelector for a given usd context.
    
        Args:
            usd_context_name (str): The name of the USD context for which to return a ManipulatorSelector object.
    
        Returns:
            :obj: 'ManipulatorSelector'
        
    """
_order_manager: omni.kit.manipulator.selector.manipulator_order_manager.ManipulatorOrderManager  # value = <omni.kit.manipulator.selector.manipulator_order_manager.ManipulatorOrderManager object>
_selectors: dict  # value = {'': <omni.kit.manipulator.selector.manipulator_selector.ManipulatorSelector object>}
