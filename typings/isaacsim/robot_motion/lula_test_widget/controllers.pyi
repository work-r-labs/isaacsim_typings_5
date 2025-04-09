from __future__ import annotations
import carb as carb
import isaacsim.core.api.controllers.base_controller
from isaacsim.core.api.controllers.base_controller import BaseController
from isaacsim.core.api import objects
import isaacsim.core.utils.types
from isaacsim.core.utils.types import ArticulationAction
import isaacsim.robot_motion.motion_generation.articulation_kinematics_solver
from isaacsim.robot_motion.motion_generation.articulation_kinematics_solver import ArticulationKinematicsSolver
import isaacsim.robot_motion.motion_generation.articulation_trajectory
from isaacsim.robot_motion.motion_generation.articulation_trajectory import ArticulationTrajectory
import isaacsim.robot_motion.motion_generation.path_planner_visualizer
from isaacsim.robot_motion.motion_generation.path_planner_visualizer import PathPlannerVisualizer
import numpy as np
import numpy
import typing
__all__ = ['ArticulationAction', 'ArticulationKinematicsSolver', 'ArticulationTrajectory', 'BaseController', 'KinematicsController', 'LulaController', 'PathPlannerController', 'PathPlannerVisualizer', 'TrajectoryController', 'carb', 'np', 'objects']
class KinematicsController(LulaController):
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, name: str, art_kinematics: isaacsim.robot_motion.motion_generation.articulation_kinematics_solver.ArticulationKinematicsSolver):
        ...
    def forward(self, target_end_effector_position: numpy.ndarray, target_end_effector_orientation: typing.Optional[numpy.ndarray] = None) -> isaacsim.core.utils.types.ArticulationAction:
        ...
class LulaController(isaacsim.core.api.controllers.base_controller.BaseController):
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self):
        ...
    def forward(self, target_end_effector_position: numpy.ndarray, target_end_effector_orientation: typing.Optional[numpy.ndarray] = None) -> isaacsim.core.utils.types.ArticulationAction:
        ...
class PathPlannerController(LulaController):
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, name: str, path_planner_visualizer: isaacsim.robot_motion.motion_generation.path_planner_visualizer.PathPlannerVisualizer, cspace_interpolation_max_dist: float = 0.5, frames_per_waypoint: int = 30):
        ...
    def add_obstacle(self, obstacle: isaacsim.core.api.objects, static: bool = False) -> None:
        ...
    def forward(self, target_end_effector_position: numpy.ndarray, target_end_effector_orientation: typing.Optional[numpy.ndarray] = None) -> isaacsim.core.utils.types.ArticulationAction:
        ...
    def make_new_plan(self, target_end_effector_position: numpy.ndarray, target_end_effector_orientation: typing.Optional[numpy.ndarray] = None) -> None:
        ...
    def remove_obstacle(self, obstacle: isaacsim.core.api.objects) -> None:
        ...
    def reset(self) -> None:
        ...
class TrajectoryController(LulaController):
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, name: str, art_trajectory: isaacsim.robot_motion.motion_generation.articulation_trajectory.ArticulationTrajectory):
        ...
    def forward(self, target_end_effector_position: numpy.ndarray, target_end_effector_orientation: typing.Optional[numpy.ndarray] = None):
        ...
