from __future__ import annotations
import gc as gc
import isaacsim.core.api.loggers.data_logger
from isaacsim.core.api.loggers.data_logger import DataLogger
import isaacsim.core.api.scenes.scene
from isaacsim.core.api.scenes.scene import Scene
import isaacsim.core.api.simulation_context.simulation_context
from isaacsim.core.api.simulation_context.simulation_context import SimulationContext
import isaacsim.core.api.tasks.base_task
from isaacsim.core.api.tasks.base_task import BaseTask
from isaacsim.core.simulation_manager.impl.isaac_events import IsaacEvents
from pxr import Usd
import typing
__all__ = ['BaseTask', 'DataLogger', 'IsaacEvents', 'Scene', 'SimulationContext', 'Usd', 'World', 'gc']
class World(isaacsim.core.api.simulation_context.simulation_context.SimulationContext):
    """
    This class inherits from SimulationContext which provides the following.
    
        SimulationContext provide functions that take care of many time-related events such as
        perform a physics or a render step for instance. Adding/ removing callback functions that
        gets triggered with certain events such as a physics step, timeline event
        (pause or play..etc), stage open/ close..etc.
    
        It also includes an instance of PhysicsContext which takes care of many physics related
        settings such as setting physics dt, solver type..etc.
    
        In addition to what is provided from SimulationContext, this class allows the user to add a
        task to the world and it contains a scene object.
    
        To control the default reset state of different objects easily, the object could be added to
        a Scene. Besides this, the object is bound to a short keyword that facilitates objects retrievals,
        like in a dict.
    
        Checkout the required tutorials at
        https://docs.omniverse.nvidia.com/app_isaacsim/app_isaacsim/overview.html
    
        Args:
            physics_dt (Optional[float], optional): dt between physics steps. Defaults to None.
            rendering_dt (Optional[float], optional): dt between rendering steps. Note: rendering means
                                                       rendering a frame of the current application and not
                                                       only rendering a frame to the viewports/ cameras. So UI
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
            device (Optional[str], optional): specifies the device to be used if running on the gpu with torch or warp backends.
    
        Example:
    
        .. code-block:: python
    
            >>> from isaacsim.core.api import World
            >>>
            >>> world = World()
            >>> world
            <isaacsim.core.api.world.world.World object at 0x...>
        
    """
    _world_initialized: typing.ClassVar[bool] = False
    @classmethod
    def clear_instance(cls):
        """
        Delete the world object, if it was instantiated before, and destroy any subscribed callback
        
                Example:
        
                .. code-block:: python
        
                    >>> World.clear_instance()
                
        """
    def __init__(self, physics_dt: typing.Optional[float] = None, rendering_dt: typing.Optional[float] = None, stage_units_in_meters: typing.Optional[float] = None, physics_prim_path: str = '/physicsScene', sim_params: dict = None, set_defaults: bool = True, backend: str = 'numpy', device: typing.Optional[str] = None) -> None:
        ...
    def add_task(self, task: isaacsim.core.api.tasks.base_task.BaseTask) -> None:
        """
        Add a task to the task registry
        
                .. note::
        
                    Tasks should have a unique name
        
                Args:
                    task (BaseTask): task object
        
                Example:
        
                .. code-block:: python
        
                    >>> from isaacsim.core.api.tasks import BaseTask
                    >>>
                    >>> class Task(BaseTask):
                    ...    def get_observations(self):
                    ...        return {'obs': [0]}
                    ...
                    ...    def calculate_metrics(self):
                    ...        return {"reward": 1}
                    ...
                    ...    def is_done(self):
                    ...        return False
                    ...
                    >>> task = Task(name="custom_task")
                    >>> world.add_task(task)
                
        """
    def calculate_metrics(self, task_name: typing.Optional[str] = None) -> None:
        """
        Get metrics from all the tasks that were added
        
                Args:
                    task_name (Optional[str], optional): task name to ask for. Defaults to None, which means all the tasks
        
                Returns:
                    dict: the computed task (or all tasks) metric
        
                Example:
        
                .. code-block:: python
        
                    >>> world.calculate_metrics("custom_task")
                    {'reward': 1}
                
        """
    def clear(self) -> None:
        """
        Clear the current stage leaving the PhysicsScene and /World
        
                Example:
        
                .. code-block:: python
        
                    >>> world.clear()
                
        """
    def get_current_tasks(self) -> typing.List[isaacsim.core.api.tasks.base_task.BaseTask]:
        """
        Get a dictionary of the registered tasks where keys are task names
        
                Returns:
                    List[BaseTask]: registered tasks
        
                Example:
        
                .. code-block:: python
        
                    >>> world.get_current_tasks()
                    {'custom_task': <custom.task.scripts.extension.Task object at 0x...>}
                
        """
    def get_data_logger(self) -> isaacsim.core.api.loggers.data_logger.DataLogger:
        """
        Return the data logger of the world.
        
                Returns:
                    DataLogger: data logger instance
        
                Example:
        
                .. code-block:: python
        
                    >>> world.get_data_logger()
                    <isaacsim.core.api.loggers.data_logger.DataLogger object at 0x...>
                
        """
    def get_observations(self, task_name: typing.Optional[str] = None) -> dict:
        """
        Get observations from all the tasks that were added
        
                Args:
                    task_name (Optional[str], optional): task name to ask for. Defaults to None, which means all the tasks
        
                Returns:
                    dict: the task (or all tasks) observations
        
                Example:
        
                .. code-block:: python
        
                    >>> world.get_observations("custom_task")
                    {'obs': [0]}
                
        """
    def get_task(self, name: str) -> isaacsim.core.api.tasks.base_task.BaseTask:
        """
        Get a task by its name
        
                Example:
        
                .. code-block:: python
        
                    >>> world.get_task("custom_task")
                    <custom.task.scripts.extension.Task object at 0x...>
                
        """
    def initialize_physics(self) -> None:
        """
        Initialize the physics simulation view and each added object to the Scene
        
                Example:
        
                .. code-block:: python
        
                    >>> world.initialize_physics()
                
        """
    def is_done(self, task_name: typing.Optional[str] = None) -> bool:
        """
        Get done from all the tasks that were added
        
                Args:
                    task_name (Optional[str], optional): task name to ask for. Defaults to None, which means all the tasks
        
                Returns:
                    bool: whether the task (or all tasks) is done
        
                Example:
        
                .. code-block:: python
        
                    >>> world.is_done("custom_task")
                    False
                
        """
    def is_tasks_scene_built(self) -> bool:
        """
        Check if the ``set_up_scene`` method was called for each registered task
        
                Example:
        
                .. code-block:: python
        
                    >>> # given a world instance that was rested at some point
                    >>> world.is_tasks_scene_built()
                    True
                
        """
    def reset(self, soft: bool = False) -> None:
        """
        Reset the stage to its initial state and each object included in the Scene to its default state
                    as specified by the ``set_default_state`` and ``__init__`` methods
        
                .. note::
        
                    - All tasks should be added before the first reset is called unless the ``clear`` method was called.
                    - All articulations should be added before the first reset is called unless the ``clear`` method was called.
                    - This method takes care of initializing articulation handles with the first reset called.
                    - This will do one step internally regardless
                    - Call ``post_reset`` on each object in the Scene
                    - Call ``post_reset`` on each Task
        
                    Things like setting PD gains for instance should happen at a Task reset or a Robot reset since
                    the defaults are restored after ``stop`` method is called.
        
                .. warning::
        
                    This method is not intended to be used in the Isaac Sim's Extensions workflow since the Kit application
                    has the control over the rendering steps. For the Extensions workflow use the ``reset_async`` method instead
        
                Args:
                    soft (bool, optional): if set to True simulation won't be stopped and start again. It only calls the reset on the scene objects.
        
                Example:
        
                .. code-block:: python
        
                    >>> world.reset()
                
        """
    def reset_async(self, soft: bool = False) -> None:
        """
        Reset the stage to its initial state and each object included in the Scene to its default state
                    as specified by the ``set_default_state`` and ``__init__`` methods
        
                .. note::
        
                    - All tasks should be added before the first reset is called unless the ``clear`` method was called.
                    - All articulations should be added before the first reset is called unless the ``clear`` method was called.
                    - This method takes care of initializing articulation handles with the first reset called.
                    - This will do one step internally regardless
                    - Call ``post_reset`` on each object in the Scene
                    - Call ``post_reset`` on each Task
        
                    Things like setting PD gains for instance should happen at a Task reset or a Robot reset since
                    the defaults are restored after ``stop`` method is called.
        
                Args:
                    soft (bool, optional): if set to True simulation won't be stopped and start again. It only calls the reset on the scene objects.
        
                Example:
        
                .. code-block:: python
        
                    >>> from omni.kit.async_engine import run_coroutine
                    >>>
                    >>> async def task():
                    ...     await world.reset_async()
                    ...
                    >>> run_coroutine(task())
                
        """
    def reset_async_no_set_up_scene(self, soft: bool = False) -> None:
        """
        Reset the stage to its initial state and each object included in the Scene to its default state
                    as specified by the ``set_default_state`` and ``__init__`` methods
        
                .. note::
        
                    - All tasks should be added before the first reset is called unless the ``clear`` method was called.
                    - All articulations should be added before the first reset is called unless the ``clear`` method was called.
                    - This method takes care of initializing articulation handles with the first reset called.
                    - This will do one step internally regardless
                    - Call ``post_reset`` on each object in the Scene
                    - Call ``post_reset`` on each Task
        
                    Things like setting PD gains for instance should happen at a Task reset or a Robot reset since
                    the defaults are restored after ``stop`` method is called.
        
                Args:
                    soft (bool, optional): if set to True simulation won't be stopped and start again. It only calls the reset on the scene objects.
        
                Example:
        
                .. code-block:: python
        
                    >>> from omni.kit.async_engine import run_coroutine
                    >>>
                    >>> async def task():
                    >>>     await world.reset_async_no_set_up_scene()
                    >>>
                    >>> run_coroutine(task())
                
        """
    def reset_async_set_up_scene(self, soft: bool = False) -> None:
        """
        Reset the stage to its initial state and each object included in the Scene to its default state
                    as specified by the ``set_default_state`` and ``__init__`` methods
        
                .. note::
        
                    - All tasks should be added before the first reset is called unless the ``clear`` method was called.
                    - All articulations should be added before the first reset is called unless the ``clear`` method was called.
                    - This method takes care of initializing articulation handles with the first reset called.
                    - This will do one step internally regardless
                    - Call ``post_reset`` on each object in the Scene
                    - Call ``post_reset`` on each Task
        
                    Things like setting PD gains for instance should happen at a Task reset or a Robot reset since
                    the defaults are restored after ``stop`` method is called.
        
                Args:
                    soft (bool, optional): if set to True simulation won't be stopped and start again. It only calls the reset on the scene objects.
        
                Example:
        
                .. code-block:: python
        
                    >>> from omni.kit.async_engine import run_coroutine
                    >>>
                    >>> async def task():
                    >>>     await world.reset_async_set_up_scene()
                    >>>
                    >>> run_coroutine(task())
                
        """
    def step(self, render: bool = True, step_sim: bool = True) -> None:
        """
        Step the physics simulation while rendering or without.
        
                .. note::
        
                    The ``pre_step`` for each task is called before stepping. This method also update the Bounding Box Cache
                    time for computing bounding box if enabled
        
                .. warning::
        
                    Calling this method with the ``render`` parameter set to True (default value) is not intended to be used
                    in the Isaac Sim's Extensions workflow since the Kit application has the control over the rendering steps
        
                Args:
                    render (bool, optional): Set to False to only do a physics simulation without rendering. Note:
                                             app UI will be frozen (since its not rendering) in this case.
                                             Defaults to True.
                    step_sim (bool): True to step simulation (physics and/or rendering)
        
                Example:
        
                .. code-block:: python
        
                    >>> world.step()
                
        """
    def step_async(self, step_size: typing.Optional[float] = None) -> None:
        """
        Call all functions that should be called pre stepping the physics
        
                .. note::
        
                    The ``pre_step`` for each task is called before stepping. This method also update the Bounding Box Cache
                    time for computing bounding box if enabled
        
                Args:
                    step_size (float): step size
        
                Example:
        
                .. code-block:: python
        
                    >>> from omni.kit.async_engine import run_coroutine
                    >>>
                    >>> async def task():
                    ...     await world.step_async()
                    ...
                    >>> run_coroutine(task())
                
        """
    @property
    def scene(self) -> isaacsim.core.api.scenes.scene.Scene:
        """
        
                Returns:
                    Scene: Scene instance
        
                Example:
        
                .. code-block:: python
        
                    >>> world.scene
                    <isaacsim.core.api.scenes.scene.Scene object at 0x>
                
        """
