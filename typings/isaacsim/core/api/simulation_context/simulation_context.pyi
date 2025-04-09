from __future__ import annotations
import builtins as builtins
import carb as carb
import gc as gc
from isaacsim.core.api.physics_context.physics_context import PhysicsContext
from isaacsim.core.simulation_manager.impl.isaac_events import IsaacEvents
from isaacsim.core.simulation_manager.impl.simulation_manager import SimulationManager
from isaacsim.core.utils.carb import get_carb_setting
from isaacsim.core.utils.carb import set_carb_setting
from isaacsim.core.utils import numpy as np_utils
from isaacsim.core.utils.prims import get_prim_type_name
from isaacsim.core.utils.prims import is_prim_ancestral
from isaacsim.core.utils.prims import is_prim_no_delete
from isaacsim.core.utils.stage import clear_stage
from isaacsim.core.utils.stage import create_new_stage
from isaacsim.core.utils.stage import create_new_stage_async
from isaacsim.core.utils.stage import get_current_stage
from isaacsim.core.utils.stage import set_stage_units
from isaacsim.core.utils.stage import set_stage_up_axis
from isaacsim.core.utils.stage import update_stage_async
from isaacsim.core.utils import torch as torch_utils
from isaacsim.core.utils import warp as warp_utils
import omni as omni
from pxr import Usd
import typing
__all__ = ['IsaacEvents', 'PhysicsContext', 'SimulationContext', 'SimulationManager', 'Usd', 'builtins', 'carb', 'clear_stage', 'create_new_stage', 'create_new_stage_async', 'gc', 'get_carb_setting', 'get_current_stage', 'get_prim_type_name', 'is_prim_ancestral', 'is_prim_no_delete', 'np_utils', 'omni', 'set_carb_setting', 'set_stage_units', 'set_stage_up_axis', 'torch_utils', 'update_stage_async', 'warp_utils']
class SimulationContext:
    """
    This class provide functions that take care of many time-related events such as
        perform a physics or a render step for instance. Adding/ removing callback functions that
        gets triggered with certain events such as a physics step, timeline event
        (pause or play..etc), stage open/ close..etc.
    
        It also includes an instance of PhysicsContext which takes care of many physics related
        settings such as setting physics dt, solver type..etc.
    
        Args:
            physics_dt (Optional[float], optional): dt between physics steps. Defaults to None.
            rendering_dt (Optional[float], optional):  dt between rendering steps. Note: rendering means
                                                       rendering a frame of the current application and not
                                                       only rendering a frame to the viewports/cameras. So UI
                                                       elements of Isaac Sim will be refreshed with this dt
                                                       as well if running non-headless.
                                                       Defaults to None.
            stage_units_in_meters (Optional[float], optional): The metric units of assets. This will affect gravity value..etc.
                                                      Defaults to None.
            physics_prim_path (Optional[str], optional): specifies the prim path to create a PhysicsScene at,
                                                 only in the case where no PhysicsScene already defined.
                                                 Defaults to "/physicsScene".
            set_defaults (bool, optional): set to True to use the defaults settings
                                            [physics_dt = 1.0/ 60.0,
                                            stage units in meters = 0.01 (i.e in cms),
                                            rendering_dt = 1.0 / 60.0,
                                            gravity = -9.81 m / s
                                            ccd_enabled,
                                            stabilization_enabled,
                                            gpu dynamics turned off,
                                            broadcast type is MBP,
                                            solver type is TGS]. Defaults to True.
            backend (str, optional): specifies the backend to be used (numpy or torch or warp). Defaults to numpy.
            device (Optional[str], optional): specifies the device to be used if running on the gpu with torch or warp backend.
    
        Example:
    
        .. code-block:: python
    
            >>> from isaacsim.core.api import SimulationContext
            >>>
            >>> simulation_context = SimulationContext()
            >>> simulation_context
            <isaacsim.core.api.simulation_context.simulation_context.SimulationContext object at 0x...>
        
    """
    _instance = None
    _sim_context_initialized: typing.ClassVar[bool] = False
    @classmethod
    def __new__(cls, *args, **kwargs) -> SimulationContext:
        """
        Makes the class a singleton.
        
                Returns:
                    SimulationContext: The instance of the simulation context.
                
        """
    @classmethod
    def clear_instance(cls) -> None:
        """
        Delete the simulation context object, if it was instantiated before, and destroy any subscribed callback
        
                Example:
        
                .. code-block:: python
        
                    >>> SimulationContext.clear_instance()
                
        """
    @classmethod
    def instance(cls) -> SimulationContext:
        """
        Get the instance of the class, if it was instantiated before
        
                Returns:
                    SimulationContext: SimulationContext object or None
        
                Example:
        
                .. code-block:: python
        
                    >>> # given that the class has already been instantiated before
                    >>> simulation_context = SimulationContext.instance()
                    >>> simulation_context
                    <isaacsim.core.api.simulation_context.simulation_context.SimulationContext object at 0x...>
                
        """
    def __init__(self, physics_dt: float | None = None, rendering_dt: float | None = None, stage_units_in_meters: float | None = None, physics_prim_path: str = '/physicsScene', sim_params: dict = None, set_defaults: bool = True, backend: str = 'numpy', device: str | None = None) -> None:
        ...
    def _init_stage(self, physics_dt: float | None = None, rendering_dt: float | None = None, stage_units_in_meters: float | None = None, physics_prim_path: str = '/physicsScene', sim_params: dict = None, set_defaults: bool = True, backend: str = 'numpy', device: str | None = None) -> Usd.Stage:
        ...
    def _initialize_stage_async(self, physics_dt: float | None = None, rendering_dt: float | None = None, stage_units_in_meters: float | None = None, physics_prim_path: str = '/physicsScene', sim_params: dict = None, set_defaults: bool = True, device: str | None = None) -> Usd.Stage:
        ...
    def _on_post_physics_ready(self, event):
        ...
    def _physics_timer_callback_fn(self, step_size: int):
        ...
    def _setup_default_callback_fns(self):
        ...
    def _stage_open_callback_fn(self, event):
        ...
    def _timeline_timer_callback_fn(self, event):
        ...
    def add_physics_callback(self, callback_name: str, callback_fn: typing.Callable[[float], None]) -> None:
        """
        Add a callback which will be called before each physics step.
        
                ``callback_fn`` should take a float argument (e.g., ``step_size``)
        
                Args:
                    callback_name (str): should be unique.
                    callback_fn (Callable[[float], None]): [description]
        
                Example:
        
                .. code-block:: python
        
                    >>> def callback_physics(step_size):
                    ...     print("physics callback -> step_size:", step_size)
                    ...
                    >>> simulation_context.add_physics_callback("callback_physics", callback_physics)
                
        """
    def add_render_callback(self, callback_name: str, callback_fn: typing.Callable) -> None:
        """
        Add a callback which will be called after each rendering event such as .render().
        
                ``callback_fn`` should take an argument of type (e.g., ``event``)
        
                Args:
                    callback_name (str): [description]
                    callback_fn (Callable): [description]
        
                Example:
        
                .. code-block:: python
        
                    >>> def callback_render(event):
                    ...     print("render callback -> event:", event)
                    ...
                    >>> simulation_context.add_render_callback("callback_render", callback_render)
                
        """
    def add_stage_callback(self, callback_name: str, callback_fn: typing.Callable) -> None:
        """
        Add a callback which will be called after each stage event such as open/close among others
        
                ``callback_fn`` should take an argument of type ``omni.usd.StageEvent`` (e.g., ``event``)
        
                Args:
                    callback_name (str): [description]
                    callback_fn (Callable[[omni.usd.StageEvent], None]): [description]
        
                Example:
        
                .. code-block:: python
        
                    >>> def callback_stage(event):
                    ...     print("stage callback -> event:", event)
                    ...
                    >>> simulation_context.add_stage_callback("callback_stage", callback_stage)
                
        """
    def add_timeline_callback(self, callback_name: str, callback_fn: typing.Callable) -> None:
        """
        Add a callback which will be called after each timeline event such as play/pause.
        
                ``callback_fn`` should take an argument of type ``omni.timeline.TimelineEvent`` (e.g., ``event``)
        
                Args:
                    callback_name (str): [description]
                    callback_fn (Callable[[omni.timeline.TimelineEvent], None]): [description]
        
                Example:
        
                .. code-block:: python
        
                    >>> def callback_timeline(event):
                    ...     print("timeline callback -> event:", event)
                    ...
                    >>> simulation_context.add_timeline_callback("callback_timeline", callback_timeline)
                
        """
    def clear(self) -> None:
        """
        Clear the current stage leaving the PhysicsScene and /World
        
                Example:
        
                .. code-block:: python
        
                    >>> simulation_context.clear()
                
        """
    def clear_all_callbacks(self) -> None:
        """
        Clear all callbacks which were added using any ``add_*_callback`` method
        
                Example:
        
                .. code-block:: python
        
                    >>> simulation_context.clear_render_callbacks()
                
        """
    def clear_physics_callbacks(self) -> None:
        """
        Remove all registered physics callbacks
        
                Example:
        
                .. code-block:: python
        
                    >>> simulation_context.clear_physics_callbacks()
                
        """
    def clear_render_callbacks(self) -> None:
        """
        Remove all registered render callbacks
        
                Example:
        
                .. code-block:: python
        
                    >>> simulation_context.clear_render_callbacks()
                
        """
    def clear_stage_callbacks(self) -> None:
        """
        Remove all registered stage callbacks
        
                Example:
        
                .. code-block:: python
        
                    >>> simulation_context.clear_stage_callbacks()
                
        """
    def clear_timeline_callbacks(self) -> None:
        """
        Remove all registered timeline callbacks
        
                Example:
        
                .. code-block:: python
        
                    >>> simulation_context.clear_timeline_callbacks()
                
        """
    def get_block_on_render(self) -> bool:
        """
        Get the block on render flag for the simulation thread
        
                Returns:
                    bool: True if one frame lag between any data captured from the render products and the current USD stage is guaranteed by blocking the step call.
        
                Example:
        
                .. code-block:: python
        
                    >>> simulation_context.get_block_on_render()
                    False
                
        """
    def get_physics_context(self) -> PhysicsContext:
        """
        Get the physics context (a class to deal with a physics scene and its settings) instance
        
                Raises:
                    Exception: if there is no stage currently opened
        
                Returns:
                    PhysicsContext: physics context object
        
                Example:
        
                .. code-block:: python
        
                    >>> simulation_context.get_physics_context()
                    <isaacsim.core.api.physics_context.physics_context.PhysicsContext object at 0x...>
                
        """
    def get_physics_dt(self) -> float:
        """
        Get the current physics dt of the physics context
        
                Raises:
                    Exception: if there is no stage currently opened
        
                Returns:
                    float: current physics dt of the PhysicsContext
        
                Example:
        
                .. code-block:: python
        
                    >>> simulation_context.get_physics_dt()
                    0.016666666666666666
                
        """
    def get_rendering_dt(self) -> float:
        """
        Get the current rendering dt
        
                Raises:
                    Exception: if there is no stage currently opened
        
                Returns:
                    float: current rendering dt
        
                Example:
        
                .. code-block:: python
        
                    >>> simulation_context.get_rendering_dt()
                    0.016666666666666666
                
        """
    def initialize_physics(self) -> None:
        """
        Initialize the physics simulation view
        
                Example:
        
                .. code-block:: python
        
                    >>> simulation_context.initialize_physics()
                
        """
    def initialize_simulation_context_async(self) -> None:
        """
        Initialize the simulation context
        
                .. hint::
        
                    This method is intended to be used in the Isaac Sim's Extensions workflow where
                    the Kit application has the control over timing of physics and rendering steps
        
                Example:
        
                .. code-block:: python
        
                    >>> from omni.kit.async_engine import run_coroutine
                    >>>
                    >>> async def task():
                    ...     await simulation_context.initialize_simulation_context_async()
                    ...
                    >>> run_coroutine(task())
                
        """
    def is_playing(self) -> bool:
        """
        Check whether the simulation is playing
        
                Returns:
                    bool: True if the simulator is playing.
        
                Example:
        
                .. code-block:: python
        
                    >>> # given a simulation in play
                    >>> simulation_context.is_playing()
                    True
                
        """
    def is_simulating(self) -> bool:
        """
        Check whether the simulation is running or not
        
                .. warning::
        
                    With deprecation of Dynamic Control Toolbox, this function is not needed
        
                    It can return True if start_simulation is called even if play was pressed/called.
        
                Returns:
                    bool" True if physics simulation is happening.
        
                Example:
        
                .. code-block:: python
        
                    >>> # given a running simulation
                    >>> simulation_context.is_simulating()
                    True
                
        """
    def is_stopped(self) -> bool:
        """
        Check whether the simulation is playing
        
                Returns:
                    bool: True if the simulator is stopped.
        
                Example:
        
                .. code-block:: python
        
                    >>> # given a simulation in play
                    >>> simulation_context.is_stopped()
                    False
                
        """
    def pause(self) -> None:
        """
        Pause the physics simulation
        
                Example:
        
                .. code-block:: python
        
                    >>> simulation_context.pause()
                
        """
    def pause_async(self) -> None:
        """
        Pause the physics simulation
        
                Example:
        
                .. code-block:: python
        
                    >>> from omni.kit.async_engine import run_coroutine
                    >>>
                    >>> async def task():
                    ...     await simulation_context.pause_async()
                    ...
                    >>> run_coroutine(task())
                
        """
    def physics_callback_exists(self, callback_name: str) -> bool:
        """
        Check if a physics callback exists
        
                Args:
                    callback_name (str): callback name
        
                Returns:
                    bool: whether the callback is registered
        
                Example:
        
                .. code-block:: python
        
                    >>> # given a registered callback named 'callback_physics'
                    >>> simulation_context.physics_callback_exists("callback_physics")
                    True
                
        """
    def play(self) -> None:
        """
        Start playing simulation
        
                .. note::
        
                   It does one step internally to propagate all physics handles properly.
        
                Example:
        
                .. code-block:: python
        
                    >>> simulation_context.play()
                
        """
    def play_async(self) -> None:
        """
        Start playing simulation
        
                Example:
        
                .. code-block:: python
        
                    >>> from omni.kit.async_engine import run_coroutine
                    >>>
                    >>> async def task():
                    ...     await simulation_context.play_async()
                    ...
                    >>> run_coroutine(task())
                
        """
    def remove_physics_callback(self, callback_name: str) -> None:
        """
        Remove a physics callback by its name
        
                Args:
                    callback_name (str): callback name
        
                Example:
        
                .. code-block:: python
        
                    >>> # given a registered callback named 'callback_physics'
                    >>> simulation_context.remove_physics_callback("callback_physics")
                
        """
    def remove_render_callback(self, callback_name: str) -> None:
        """
        Remove a render callback by its name
        
                Args:
                    callback_name (str): callback name
        
                Example:
        
                .. code-block:: python
        
                    >>> # given a registered callback named 'callback_render'
                    >>> simulation_context.remove_render_callback("callback_render")
                
        """
    def remove_stage_callback(self, callback_name: str) -> None:
        """
        Remove a stage callback by its name
        
                Args:
                    callback_name (str): callback name
        
                Example:
        
                .. code-block:: python
        
                    >>> # given a registered callback named 'callback_stage'
                    >>> simulation_context.remove_stage_callback("callback_stage")
                
        """
    def remove_timeline_callback(self, callback_name: str) -> None:
        """
        Remove a timeline callback by its name
        
                Args:
                    callback_name (str): callback name
        
                Example:
        
                .. code-block:: python
        
                    >>> # given a registered callback named 'timeline'
                    >>> simulation_context.timeline_callback("timeline")
                
        """
    def render(self) -> None:
        """
        Refresh the Isaac Sim app rendering components including UI elements, viewports and others
        
                .. warning::
        
                    This method is not intended to be used in the Isaac Sim's Extensions workflow
                    since the Kit application has the control over the rendering steps
        
                Example:
        
                .. code-block:: python
        
                    >>> simulation_context.render()
                
        """
    def render_async(self) -> None:
        """
        Refresh the Isaac Sim app rendering components including UI elements, viewports and others
        
                .. hint::
        
                    This method is intended to be used in the Isaac Sim's Extensions workflow where
                    the Kit application has the control over timing of physics and rendering steps
        
                Example:
        
                .. code-block:: python
        
                    >>> from omni.kit.async_engine import run_coroutine
                    >>>
                    >>> async def task():
                    ...     await simulation_context.render_async()
                    ...
                    >>> run_coroutine(task())
                
        """
    def render_callback_exists(self, callback_name: str) -> bool:
        """
        Check if a render callback exists
        
                Args:
                    callback_name (str): callback name
        
                Returns:
                    bool: whether the callback is registered
        
                Example:
        
                .. code-block:: python
        
                    >>> # given a registered callback named 'callback_render'
                    >>> simulation_context.render_callback_exists("callback_render")
                    True
                
        """
    def reset(self, soft: bool = False) -> None:
        """
        Reset the physics simulation view.
        
                .. warning::
        
                    This method is not intended to be used in the Isaac Sim's Extensions workflow since the Kit application
                    has the control over the rendering steps. For the Extensions workflow use the ``reset_async`` method instead
        
                Args:
                    soft (bool, optional): if set to True simulation won't be stopped and start again. It only calls the reset on the scene objects.
        
                Example:
        
                .. code-block:: python
        
                    >>> simulation_context.reset()
                
        """
    def reset_async(self, soft: bool = False) -> None:
        """
        Reset the physics simulation view (asynchronous version).
        
                Args:
                    soft (bool, optional): if set to True simulation won't be stopped and start again. It only calls the reset on the scene objects.
        
                Example:
        
                .. code-block:: python
        
                    >>> from omni.kit.async_engine import run_coroutine
                    >>>
                    >>> async def task():
                    >>>     await simulation_context.reset_async()
                    >>>
                    >>> run_coroutine(task())
                
        """
    def set_block_on_render(self, block: bool) -> None:
        """
        Set block on render flag for the simulation thread
        
                .. note::
        
                    This guarantee a one frame lag between any data captured from the render products and the current USD stage if enabled.
        
                Args:
                    block (bool): True to block the thread until the renderer is done.
        
                Example:
        
                .. code-block:: python
        
                    >>> simulation_context.set_block_on_render(False)
                
        """
    def set_simulation_dt(self, physics_dt: float | None = None, rendering_dt: float | None = None) -> None:
        """
        Specify the physics step and rendering step size to use when stepping and rendering.
        
                Args:
                    physics_dt (float): The physics time-step. None means it won't change the current setting. (default: None).
                    rendering_dt (float):  The rendering time-step. None means it won't change the current setting. (default: None)
        
                .. hint::
        
                    It is recommended that the two values be divisible, with the ``rendering_dt`` being equal to or greater
                    than the ``physics_dt``
        
                Example:
        
                .. code-block:: python
        
                    >>> set physics dt to 120 Hz and rendering dt to 60Hz (2 physics steps for each rendering)
                    >>> simulation_context.set_simulation_dt(physics_dt=1.0 / 120.0, rendering_dt=1.0 / 60.0)
                
        """
    def stage_callback_exists(self, callback_name: str) -> bool:
        """
        Check if a stage callback exists
        
                Args:
                    callback_name (str): callback name
        
                Returns:
                    bool: whether the callback is registered
        
                Example:
        
                .. code-block:: python
        
                    >>> # given a registered callback named 'callback_stage'
                    >>> simulation_context.stage_callback_exists("callback_stage")
                    True
                
        """
    def step(self, render: bool = True) -> None:
        """
        Steps the physics simulation while rendering or without.
        
                .. warning::
        
                    Calling this method with the ``render`` parameter set to True (default value) is not intended to be used
                    in the Isaac Sim's Extensions workflow since the Kit application has the control over the rendering steps
        
                Args:
                    render (bool, optional): Set to False to only do a physics simulation without rendering. Note:
                                             app UI will be frozen (since its not rendering) in this case.
                                             Defaults to True.
        
                Raises:
                    Exception: if there is no stage currently opened
        
                Example:
        
                .. code-block:: python
        
                    >>> simulation_context.step()
                
        """
    def stop(self) -> None:
        """
        Stop the physics simulation
        
                Example:
        
                .. code-block:: python
        
                    >>> simulation_context.stop()
                
        """
    def stop_async(self) -> None:
        """
        Stop the physics simulation
        
                Example:
        
                .. code-block:: python
        
                    >>> from omni.kit.async_engine import run_coroutine
                    >>>
                    >>> async def task():
                    ...     await simulation_context.stop_async()
                    ...
                    >>> run_coroutine(task())
                
        """
    def timeline_callback_exists(self, callback_name: str) -> bool:
        """
        Check if a timeline callback exists
        
                Args:
                    callback_name (str): callback name
        
                Returns:
                    bool: whether the callback is registered
        
                Example:
        
                .. code-block:: python
        
                    >>> # given a registered callback named 'callback_timeline'
                    >>> simulation_context.timeline_callback_exists("callback_timeline")
                    True
                
        """
    @property
    def app(self) -> omni.kit.app.IApp:
        """
        Returns:
                    omni.kit.app.IApp: Omniverse Kit Application interface
        
                Example:
        
                .. code-block:: python
        
                    >>> simulation_context.app
                    <omni.kit.app._app.IApp object at 0x...>
                
        """
    @property
    def backend(self) -> str:
        """
        
                Returns:
                    str: current backend. Supported backends are: ``"numpy"``, ``"torch"`` and ``"warp"``
        
                Example:
        
                .. code-block:: python
        
                    >>> simulation_context.backend
                    numpy
                
        """
    @property
    def backend_utils(self):
        """
        Get the current backend utils module
        
                .. list-table::
                    :header-rows: 1
        
                    * - Backend
                      - Utils module
                    * - ``"numpy"``
                      - ``isaacsim.core.utils.numpy``
                    * - ``"torch"``
                      - ``isaacsim.core.utils.torch``
                    * - ``"warp"``
                      - ``isaacsim.core.utils.warp``
        
                Returns:
                    str: current backend utils module
        
                Example:
        
                .. code-block:: python
        
                    >>> simulation_context.backend_utils
                    <module 'isaacsim.core.utils.numpy'>
                
        """
    @property
    def current_time(self) -> float:
        """
        
                Returns:
                    float: current time (simulated physical time) that have elapsed since the simulation was played
        
                Example:
        
                .. code-block:: python
        
                    >>> # given a running Isaac Sim instance and after 911 physics steps at 60 Hz
                    >>> simulation_context.current_time
                    15.183334125205874
                
        """
    @property
    def current_time_step_index(self) -> int:
        """
        
                Returns:
                    int: current number of physics steps that have elapsed since the simulation was played
        
                Example:
        
                .. code-block:: python
        
                    >>> # given a running Isaac Sim instance and after approximately 15 seconds of physics simulation at 60 Hz
                    >>> simulation_context.current_time_step_index
                    911
                
        """
    @property
    def device(self) -> str:
        """
        
                Returns:
                    str: Device used by the physics context. None for numpy backend
        
                Example:
        
                .. code-block:: python
        
                    >>> simulation_context.device
                    None
                
        """
    @property
    def physics_sim_view(self):
        """
        
                .. note::
        
                    The physics simulation view instance will be only available after initializing the physics
                    (see ``initialize_physics``) or resetting the simulation context (see ``reset``)
        
                Returns:
                    PhysicsContext: Physics simulation view instance
        
                Example:
        
                .. code-block:: python
        
                    >>> simulation_context.physics_sim_view
                    <omni.physics.tensors.impl.api.SimulationView object at 0x...>
                
        """
    @property
    def stage(self) -> Usd.Stage:
        """
        
                Returns:
                    Usd.Stage: current open USD stage
        
                Example:
        
                .. code-block:: python
        
                    >>> simulation_context.stage
                    Usd.Stage.Open(rootLayer=Sdf.Find('anon:0x...:World....usd'),
                                   sessionLayer=Sdf.Find('anon:0x...:World...-session.usda'),
                                   pathResolverContext=<invalid repr>)
                
        """
