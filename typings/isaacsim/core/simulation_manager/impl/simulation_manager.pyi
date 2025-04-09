from __future__ import annotations
import carb as carb
import collections
from collections import OrderedDict
import isaacsim.core.simulation_manager._simulation_manager
from isaacsim.core.simulation_manager.impl.isaac_events import IsaacEvents
from isaacsim.core.utils import numpy as np_utils
from isaacsim.core.utils import torch as torch_utils
from isaacsim.core.utils import warp as warp_utils
import omni as omni
from pxr import PhysxSchema
import typing
import weakref as weakref
__all__ = ['IsaacEvents', 'OrderedDict', 'PhysxSchema', 'SimulationManager', 'carb', 'np_utils', 'omni', 'torch_utils', 'warp_utils', 'weakref']
class SimulationManager:
    """
    This class provide functions that take care of many time-related events such as
        warm starting simulation in order for the physics data to be retrievable.
        Adding/ removing callback functions that gets triggered with certain events such as a physics step,
        on post reset, on physics ready..etc.
    """
    _assets_loaded: typing.ClassVar[bool] = True
    _assets_loading_callback: typing.ClassVar[carb.events._events.ISubscription]  # value = <carb.events._events.ISubscription object>
    _backend: typing.ClassVar[str] = 'numpy'
    _callbacks: typing.ClassVar[dict] = {}
    _carb_settings: typing.ClassVar[carb.settings._settings.ISettings]  # value = <carb.settings._settings.ISettings object>
    _message_bus: typing.ClassVar[carb.events._events.IEventStream]  # value = <carb.events._events.IEventStream object>
    _on_stop_callback: typing.ClassVar[carb.events._events.ISubscription]  # value = <carb.events._events.ISubscription object>
    _physics_scene_apis: typing.ClassVar[collections.OrderedDict]  # value = OrderedDict()
    _physics_sim_view = None
    _physx_interface: typing.ClassVar[omni.physx.bindings._physx.PhysX]  # value = <omni.physx.bindings._physx.PhysX object>
    _physx_sim_interface: typing.ClassVar[omni.physx.bindings._physx.IPhysxSimulation]  # value = <omni.physx.bindings._physx.IPhysxSimulation object>
    _post_warm_start_callback: typing.ClassVar[carb.events._events.ISubscription]  # value = <carb.events._events.ISubscription object>
    _simulation_manager_interface: typing.ClassVar[isaacsim.core.simulation_manager._simulation_manager.ISimulationManager]  # value = <isaacsim.core.simulation_manager._simulation_manager.ISimulationManager object>
    _stage_open_callback: typing.ClassVar[carb.events._events.ISubscription]  # value = <carb.events._events.ISubscription object>
    _timeline: typing.ClassVar[omni.timeline._timeline.Timeline]  # value = <omni.timeline._timeline.Timeline object>
    _warm_start_callback: typing.ClassVar[carb.events._events.ISubscription]  # value = <carb.events._events.ISubscription object>
    _warmup_needed: typing.ClassVar[bool] = True
    @staticmethod
    def _create_simulation_view(event) -> None:
        ...
    @staticmethod
    def _on_stop(event) -> None:
        ...
    @staticmethod
    def _post_stage_open(event) -> None:
        ...
    @staticmethod
    def _track_physics_scenes() -> None:
        ...
    @staticmethod
    def _warm_start(event) -> None:
        ...
    @classmethod
    def _clear(cls) -> None:
        ...
    @classmethod
    def _get_backend_utils(cls) -> str:
        ...
    @classmethod
    def _initialize(cls) -> None:
        ...
    @classmethod
    def assets_loading(cls) -> bool:
        """
        Checks if textures are loaded.
        
                Returns:
                    bool: True if textures are loading and not done yet, otherwise False.
                
        """
    @classmethod
    def deregister_callback(cls, callback_id):
        ...
    @classmethod
    def enable_fabric(cls, enable):
        ...
    @classmethod
    def enable_fabric_usd_notice_handler(cls, stage_id, flag):
        ...
    @classmethod
    def enable_gpu_dynamics(cls, flag: bool, physics_scene: str = None) -> None:
        """
        Enables gpu dynamics pipeline, required for deformables for instance.
        
                Args:
                    flag (bool): enables or disables gpu dynamics on the PhysicsScene.
                    physics_scene (str, optional): physics scene prim path.
        
                Raises:
                    Exception: If the prim path registered in context doesn't correspond to a valid prim path currently.
                
        """
    @classmethod
    def enable_stablization(cls, flag: bool, physics_scene: str = None) -> None:
        """
        Enables additional stabilization pass in the solver.
        
                Args:
                    flag (bool): enables or disables stabilization on the PhysicsScene
                    physics_scene (str, optional): physics scene prim path.
        
                Raises:
                    Exception: If the prim path registered in context doesn't correspond to a valid prim path currently.
                
        """
    @classmethod
    def enable_usd_notice_handler(cls, flag):
        ...
    @classmethod
    def get_backend(cls) -> str:
        ...
    @classmethod
    def get_broadphase_type(cls, physics_scene: str = None) -> str:
        """
        Gets current broadcast phase algorithm type.
        
                Args:
                    physics_scene (str, optional): physics scene prim path.
        
                Raises:
                    Exception: If the prim path registered in context doesn't correspond to a valid prim path currently.
        
                Returns:
                    str: Broadcast phase algorithm used.
                
        """
    @classmethod
    def get_physics_dt(cls, physics_scene: str = None) -> str:
        """
        
                 Returns the current physics dt.
        
                Args:
                    physics_scene (str, optional): physics scene prim path.
        
                Raises:
                    Exception: If the prim path registered in context doesn't correspond to a valid prim path currently.
        
                Returns:
                    float: physics dt.
                
        """
    @classmethod
    def get_physics_sim_device(cls) -> str:
        ...
    @classmethod
    def get_physics_sim_view(cls):
        ...
    @classmethod
    def get_solver_type(cls, physics_scene: str = None) -> str:
        """
        Gets current solver type.
        
                Args:
                    physics_scene (str, optional): physics scene prim path.
        
                Raises:
                    Exception: If the prim path registered in context doesn't correspond to a valid prim path currently.
        
                Returns:
                    str: solver used for simulation.
                
        """
    @classmethod
    def is_fabric_enabled(cls, enable):
        ...
    @classmethod
    def is_fabric_usd_notice_handler_enabled(cls, stage_id):
        ...
    @classmethod
    def is_gpu_dynamics_enabled(cls, physics_scene: str = None) -> bool:
        """
        Checks if Gpu Dynamics is enabled.
        
                Args:
                    physics_scene (str, optional): physics scene prim path.
        
                Raises:
                    Exception: If the prim path registered in context doesn't correspond to a valid prim path currently.
        
                Returns:
                    bool: True if Gpu Dynamics is enabled, otherwise False.
                
        """
    @classmethod
    def is_stablization_enabled(cls, physics_scene: str = None) -> bool:
        """
        Checks if stabilization is enabled.
        
                Args:
                    physics_scene (str, optional): physics scene prim path.
        
                Raises:
                    Exception: If the prim path registered in context doesn't correspond to a valid prim path currently.
        
                Returns:
                    bool: True if stabilization is enabled, otherwise False.
                
        """
    @classmethod
    def register_callback(cls, callback: callable, event):
        ...
    @classmethod
    def set_backend(cls, val: str) -> None:
        ...
    @classmethod
    def set_broadphase_type(cls, val: str, physics_scene: str = None) -> None:
        """
        Broadcast phase algorithm used in simulation.
        
                Args:
                    val (str): type of broadcasting to be used, can be "MBP".
                    physics_scene (str, optional): physics scene prim path.
        
                Raises:
                    Exception: If the prim path registered in context doesn't correspond to a valid prim path currently.
                
        """
    @classmethod
    def set_physics_sim_device(cls, val) -> None:
        ...
    @classmethod
    def set_solver_type(cls, solver_type: str, physics_scene: str = None) -> None:
        """
        solver used for simulation.
        
                Args:
                    solver_type (str): can be "TGS" or "PGS".
                    physics_scene (str, optional): physics scene prim path.
        
                Raises:
                    Exception: If the prim path registered in context doesn't correspond to a valid prim path currently.
                
        """
