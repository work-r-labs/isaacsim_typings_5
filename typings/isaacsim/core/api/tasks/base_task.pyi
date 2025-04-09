from __future__ import annotations
import isaacsim.core.api.scenes.scene
from isaacsim.core.api.scenes.scene import Scene
from isaacsim.core.api.simulation_context.simulation_context import SimulationContext
import numpy as np
__all__ = ['BaseTask', 'Scene', 'SimulationContext', 'np']
class BaseTask:
    """
    This class provides a way to set up a task in a scene and modularize adding objects to stage,
        getting observations needed for the behavioral layer, calculating metrics needed about the task,
        calling certain things pre-stepping, creating multiple tasks at the same time and much more.
    
        Checkout the required tutorials at
        https://docs.omniverse.nvidia.com/app_isaacsim/app_isaacsim/overview.html
    
        Args:
            name (str): needs to be unique if added to the World.
            offset (Optional[np.ndarray], optional): offset applied to all assets of the task.
        
    """
    def __init__(self, name: str, offset: typing.Optional[numpy.ndarray] = None) -> None:
        ...
    def _move_task_objects_to_their_frame(self):
        ...
    def calculate_metrics(self) -> dict:
        """
        [summary]
        
                Raises:
                    NotImplementedError: [description]
                
        """
    def cleanup(self) -> None:
        """
        Called before calling a reset() on the world to removed temporary objects that were added during
                simulation for instance.
                
        """
    def get_description(self) -> str:
        """
        [summary]
        
                Returns:
                    str: [description]
                
        """
    def get_observations(self) -> dict:
        """
        Returns current observations from the objects needed for the behavioral layer.
        
                Raises:
                    NotImplementedError: [description]
        
                Returns:
                    dict: [description]
                
        """
    def get_params(self) -> dict:
        """
        Gets the parameters of the task.
                   This is defined differently for each task in order to access the task's objects and values.
                   Note that this is different from get_observations.
                   Things like the robot name, block name..etc can be defined here for faster retrieval.
                   should have the form of params_representation["param_name"] = {"value": param_value, "modifiable": bool}
        
                Raises:
                    NotImplementedError: [description]
        
                Returns:
                    dict: defined parameters of the task.
                
        """
    def get_task_objects(self) -> dict:
        """
        [summary]
        
                Returns:
                    dict: [description]
                
        """
    def is_done(self) -> bool:
        """
        Returns True of the task is done.
        
                Raises:
                    NotImplementedError: [description]
                
        """
    def post_reset(self) -> None:
        """
        Calls while doing a .reset() on the world.
        """
    def pre_step(self, time_step_index: int, simulation_time: float) -> None:
        """
        called before stepping the physics simulation.
        
                Args:
                    time_step_index (int): [description]
                    simulation_time (float): [description]
                
        """
    def set_params(self, *args, **kwargs) -> None:
        """
        Changes the modifiable parameters of the task
        
                Raises:
                    NotImplementedError: [description]
                
        """
    def set_up_scene(self, scene: isaacsim.core.api.scenes.scene.Scene) -> None:
        """
        Adding assets to the stage as well as adding the encapsulated objects such as SingleXFormPrim..etc
                   to the task_objects happens here.
        
                Args:
                    scene (Scene): [description]
                
        """
    @property
    def device(self):
        ...
    @property
    def name(self) -> str:
        """
        [summary]
        
                Returns:
                    str: [description]
                
        """
    @property
    def scene(self) -> isaacsim.core.api.scenes.scene.Scene:
        """
        Scene of the world
        
                Returns:
                    Scene: [description]
                
        """
