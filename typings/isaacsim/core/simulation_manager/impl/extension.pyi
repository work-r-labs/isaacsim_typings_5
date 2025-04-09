from __future__ import annotations
import carb as carb
from isaacsim.core.simulation_manager import _simulation_manager
import isaacsim.core.simulation_manager._simulation_manager
from isaacsim.core.simulation_manager.impl.isaac_events import IsaacEvents
from isaacsim.core.simulation_manager.impl.simulation_manager import SimulationManager
import omni as omni
__all__ = ['Extension', 'IsaacEvents', 'SimulationManager', 'acquire_simulation_manager_interface', 'carb', 'omni']
class Extension(omni.ext._extensions.IExt):
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id):
        ...
def acquire_simulation_manager_interface():
    ...
_simulation_manager_interface: isaacsim.core.simulation_manager._simulation_manager.ISimulationManager  # value = <isaacsim.core.simulation_manager._simulation_manager.ISimulationManager object>
