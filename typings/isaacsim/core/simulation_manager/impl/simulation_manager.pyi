from __future__ import annotations
import carb as carb
import collections
from collections import OrderedDict
import isaacsim.core.simulation_manager._simulation_manager
from isaacsim.core.simulation_manager.impl.isaac_events import IsaacEvents
from isaacsim.core.utils import numpy as np_utils
from isaacsim.core.utils.prims import get_prim_at_path
from isaacsim.core.utils.prims import is_prim_path_valid
from isaacsim.core.utils.stage import get_current_stage
from isaacsim.core.utils.stage import get_current_stage_id
from isaacsim.core.utils import torch as torch_utils
from isaacsim.core.utils import warp as warp_utils
import omni as omni
from pxr import PhysxSchema
import typing
import weakref as weakref
__all__: list[str] = ['IsaacEvents', 'OrderedDict', 'PhysxSchema', 'SimulationManager', 'carb', 'get_current_stage', 'get_current_stage_id', 'get_prim_at_path', 'is_prim_path_valid', 'np_utils', 'omni', 'torch_utils', 'warp_utils', 'weakref']
class SimulationManager:
    """
    This class provide functions that take care of many time-related events such as
        warm starting simulation in order for the physics data to be retrievable.
        Adding/ removing callback functions that gets triggered with certain events such as a physics step,
        on post reset, on physics ready..etc.
    """
    _assets_loaded: typing.ClassVar[bool] = True
    _assets_loaded_callback: typing.ClassVar[carb.eventdispatcher._eventdispatcher.ObserverGuard]  # value = <carb.eventdispatcher._eventdispatcher.ObserverGuard object>
    _assets_loading_callback: typing.ClassVar[carb.eventdispatcher._eventdispatcher.ObserverGuard]  # value = <carb.eventdispatcher._eventdispatcher.ObserverGuard object>
    _backend: typing.ClassVar[str] = 'numpy'
    _callbacks: typing.ClassVar[dict] = {}
    _callbacks_enabled: typing.ClassVar[dict] = {'warm_start': True, 'on_stop': True, 'post_warm_start': True, 'stage_open': True}
    _carb_settings: typing.ClassVar[carb.settings._settings.ISettings]  # value = <carb.settings._settings.ISettings object>
    _default_physics_scene_idx: typing.ClassVar[int] = -1
    _message_bus: typing.ClassVar[carb.eventdispatcher._eventdispatcher.IEventDispatcher]  # value = <carb.eventdispatcher._eventdispatcher.IEventDispatcher object>
    _on_stop_callback: typing.ClassVar[carb.events._events.ISubscription]  # value = <carb.events._events.ISubscription object>
    _physics_scene_apis: typing.ClassVar[collections.OrderedDict]  # value = OrderedDict()
    _physics_sim_view = None
    _physics_sim_view__warp = None
    _physx_interface: typing.ClassVar[omni.physx.bindings._physx.PhysX]  # value = <omni.physx.bindings._physx.PhysX object>
    _physx_sim_interface: typing.ClassVar[omni.physx.bindings._physx.IPhysxSimulation]  # value = <omni.physx.bindings._physx.IPhysxSimulation object>
    _post_warm_start_callback: typing.ClassVar[carb.eventdispatcher._eventdispatcher.ObserverGuard]  # value = <carb.eventdispatcher._eventdispatcher.ObserverGuard object>
    _simulation_manager_interface: typing.ClassVar[isaacsim.core.simulation_manager._simulation_manager.ISimulationManager]  # value = <isaacsim.core.simulation_manager._simulation_manager.ISimulationManager object>
    _simulation_view_created: typing.ClassVar[bool] = False
    _stage_open_callback: typing.ClassVar[carb.eventdispatcher._eventdispatcher.ObserverGuard]  # value = <carb.eventdispatcher._eventdispatcher.ObserverGuard object>
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
    def _get_physics_scene_api(cls, physics_scene: str = None):
        ...
    @classmethod
    def _initialize(cls) -> None:
        ...
    @classmethod
    def _setup_on_stop_callback(cls) -> None:
        ...
    @classmethod
    def _setup_post_warm_start_callback(cls) -> None:
        ...
    @classmethod
    def _setup_stage_open_callback(cls) -> None:
        ...
    @classmethod
    def _setup_warm_start_callback(cls) -> None:
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
        """
        Deregisters a callback which was previously registered using register_callback.
        
                Args:
                    callback_id: The ID of the callback returned by register_callback to deregister.
                
        """
    @classmethod
    def enable_all_default_callbacks(cls, enable: bool = True) -> None:
        """
        Enable or disable all default callbacks.
                Default callbacks are: warm_start, on_stop, post_warm_start, stage_open.
        
                Args:
                    enable: Whether to enable all callbacks.
                
        """
    @classmethod
    def enable_ccd(cls, flag: bool, physics_scene: str = None) -> None:
        """
        Enables Continuous Collision Detection (CCD).
        
                Args:
                    flag (bool): enables or disables CCD on the PhysicsScene.
                    physics_scene (str, optional): physics scene prim path.
        
                Raises:
                    Exception: If the prim path registered in context doesn't correspond to a valid prim path currently.
                
        """
    @classmethod
    def enable_fabric(cls, enable):
        """
        Enables or disables physics fabric integration and associated settings.
        
                Args:
                    enable: Whether to enable or disable fabric.
                
        """
    @classmethod
    def enable_fabric_usd_notice_handler(cls, stage_id, flag):
        """
        Enables or disables the fabric usd notice handler.
        
                Args:
                    stage_id: The stage ID to enable or disable the handler for.
                    flag: Whether to enable or disable the handler.
                
        """
    @classmethod
    def enable_gpu_dynamics(cls, flag: bool, physics_scene: str = None) -> None:
        """
        Enables gpu dynamics pipeline, required for deformables for instance.
        
                Args:
                    flag (bool): enables or disables gpu dynamics on the PhysicsScene. If flag is true, CCD is disabled.
                    physics_scene (str, optional): physics scene prim path.
        
                Raises:
                    Exception: If the prim path registered in context doesn't correspond to a valid prim path currently.
                
        """
    @classmethod
    def enable_on_stop_callback(cls, enable: bool = True) -> None:
        """
        Enable or disable the on stop callback.
        
                Args:
                    enable: Whether to enable the callback.
                
        """
    @classmethod
    def enable_post_warm_start_callback(cls, enable: bool = True) -> None:
        """
        Enable or disable the post warm start callback.
        
                Args:
                    enable: Whether to enable the callback.
                
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
    def enable_stage_open_callback(cls, enable: bool = True) -> None:
        """
        Enable or disable the stage open callback.
                Note: This also enables/disables the assets loading and loaded callbacks. If disabled, assets_loading() will always return True.
        
                Args:
                    enable: Whether to enable the callback.
                
        """
    @classmethod
    def enable_usd_notice_handler(cls, flag):
        """
        Enables or disables the usd notice handler.
        
                Args:
                    flag: Whether to enable or disable the handler.
                
        """
    @classmethod
    def enable_warm_start_callback(cls, enable: bool = True) -> None:
        """
        Enable or disable the warm start callback.
        
                Args:
                    enable: Whether to enable the callback.
                
        """
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
    def get_default_callback_status(cls) -> dict:
        """
        Get the status of all default callbacks.
                Default callbacks are: warm_start, on_stop, post_warm_start, stage_open.
        
                Returns:
                    Dictionary with callback names and their enabled status.
                
        """
    @classmethod
    def get_default_physics_scene(cls) -> str:
        ...
    @classmethod
    def get_num_physics_steps(cls):
        ...
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
    def get_simulation_time(cls):
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
    def initialize_physics(cls) -> None:
        ...
    @classmethod
    def is_ccd_enabled(cls, physics_scene: str = None) -> bool:
        """
        Checks if Continuous Collision Detection (CCD) is enabled.
        
                Args:
                    physics_scene (str, optional): physics scene prim path.
        
                Raises:
                    Exception: If the prim path registered in context doesn't correspond to a valid prim path currently.
        
                Returns:
                    bool: True if CCD is enabled, otherwise False.
                
        """
    @classmethod
    def is_default_callback_enabled(cls, callback_name: str) -> bool:
        """
        Check if a specific default callback is enabled.
                Default callbacks are: warm_start, on_stop, post_warm_start, stage_open.
        
                Args:
                    callback_name: Name of the callback to check.
        
                Returns:
                    Whether the callback is enabled.
                
        """
    @classmethod
    def is_fabric_enabled(cls, enable):
        """
        Checks if fabric is enabled.
        
                Args:
                    enable: Whether to check if fabric is enabled.
        
                Returns:
                    bool: True if fabric is enabled, otherwise False.
                
        """
    @classmethod
    def is_fabric_usd_notice_handler_enabled(cls, stage_id):
        """
        Checks if fabric usd notice handler is enabled.
        
                Args:
                    stage_id: The stage ID to check.
        
                Returns:
                    bool: True if fabric usd notice handler is enabled, otherwise False.
                
        """
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
    def is_paused(cls):
        ...
    @classmethod
    def is_simulating(cls):
        ...
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
    def register_callback(cls, callback: callable, event, order: int = 0, name: str = None):
        """
        Registers a callback to be triggered when a specific event occurs.
        
                Args:
                    callback: The callback function to register.
                    event: The event to trigger the callback.
                    order: The order in which the callback should be triggered.
                    name: The name of the callback.
        
                Returns:
                    int: The ID of the callback.
                
        """
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
    def set_default_physics_scene(cls, physics_scene_prim_path: str):
        ...
    @classmethod
    def set_physics_dt(cls, dt: float = 0.016666666666666666, physics_scene: str = None) -> None:
        """
        Sets the physics dt on the physics scene provided.
        
                Args:
                    dt (float, optional): physics dt. Defaults to 1.0/60.0.
                    physics_scene (str, optional): physics scene prim path. Defaults to first physics scene found in the stage.
        
                Raises:
                    Exception: If the prim path registered in context doesn't correspond to a valid prim path currently.
                    ValueError: Physics dt must be a >= 0.
                    ValueError: Physics dt must be a <= 1.0.
                
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
    @classmethod
    def step(cls, render: bool = False):
        ...
