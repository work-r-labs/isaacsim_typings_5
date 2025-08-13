"""
Omniverse Isaac Sim Simulation Manager Interface

This module provides access to the Simulation Manager which handles events and callbacks
for simulation-related activities, such as physics scene additions and object deletions.
It also manages USD notice handling to track stage changes.
"""
from __future__ import annotations
import typing
__all__: list[str] = ['ISimulationManager', 'acquire_simulation_manager_interface', 'release_simulation_manager_interface']
class ISimulationManager:
    def deregister_callback(self, arg0: int) -> bool:
        """
                        Deregister a previously registered callback.
        
                        Args:
                            callback_id: The unique identifier of the callback to deregister.
        
                        Returns:
                            bool: True if callback was successfully deregistered, False otherwise.
        """
    def enable_fabric_usd_notice_handler(self, arg0: int, arg1: bool) -> None:
        """
                        Enable or disable the USD notice handler for a specific fabric stage.
        
                        Args:
                            stage_id: ID of the fabric stage.
                            flag: True to enable the handler, False to disable.
        """
    def enable_usd_notice_handler(self, arg0: bool) -> None:
        """
                        Enable or disable the USD notice handler.
        
                        Args:
                            flag: True to enable the handler, False to disable.
        """
    def get_callback_iter(self) -> int:
        """
                        Get the current callback iteration counter.
        
                        Returns:
                            int: The current callback iteration counter value.
        """
    def get_num_physics_steps(self) -> int:
        """
                        Get the current physics step count.
        
                        Returns:
                            int: The current physics step count.
        """
    def get_simulation_time(self) -> float:
        """
                        Get the current simulation time.
        
                        Returns:
                            double: The current simulation time.
        """
    @typing.overload
    def get_simulation_time_at_time(self, arg0: ...) -> float:
        """
                        Gets simulation time in seconds at a specific rational time.
        
                        Args:
                            time (omni.fabric.RationalTime): The rational time to query.
        
                        Returns:
                            float: The simulation time in seconds at the specified time.
        """
    @typing.overload
    def get_simulation_time_at_time(self, arg0: tuple[int, int]) -> float:
        """
                        Gets simulation time in seconds at a specific rational time.
        
                        Args:
                            time (tuple): A tuple of (numerator, denominator) representing the rational time.
        
                        Returns:
                            float: The simulation time in seconds at the specified time.
        """
    def get_simulation_time_monotonic(self) -> float:
        """
                        Get the current simulation time. This time does not reset when the simulation is stopped.
        
                        Returns:
                            double: The current simulation time.
        """
    @typing.overload
    def get_simulation_time_monotonic_at_time(self, arg0: ...) -> float:
        """
                        Gets monotonic simulation time in seconds at a specific rational time.
        
                        Args:
                            time (omni.fabric.RationalTime): The rational time to query.
        
                        Returns:
                            float: The monotonic simulation time in seconds at the specified time.
        """
    @typing.overload
    def get_simulation_time_monotonic_at_time(self, arg0: tuple[int, int]) -> float:
        """
                        Gets monotonic simulation time in seconds at a specific rational time.
        
                        Args:
                            time (tuple): A tuple of (numerator, denominator) representing the rational time.
        
                        Returns:
                            float: The monotonic simulation time in seconds at the specified time.
        """
    def get_system_time(self) -> float:
        """
                        Get the current system time.
        
                        Returns:
                            double: The current system time.
        """
    @typing.overload
    def get_system_time_at_time(self, arg0: ...) -> float:
        """
                        Gets system (real-world) time in seconds at a specific rational time.
        
                        Args:
                            time (omni.fabric.RationalTime): The rational time to query.
        
                        Returns:
                            float: The system time in seconds at the specified time.
        """
    @typing.overload
    def get_system_time_at_time(self, arg0: tuple[int, int]) -> float:
        """
                        Gets system (real-world) time in seconds at a specific rational time.
        
                        Args:
                            time (tuple): A tuple of (numerator, denominator) representing the rational time.
        
                        Returns:
                            float: The system time in seconds at the specified time.
        """
    def is_fabric_usd_notice_handler_enabled(self, arg0: int) -> bool:
        """
                        Check if the USD notice handler is enabled for a specific fabric stage.
        
                        Args:
                            stage_id: ID of the fabric stage to check.
        
                        Returns:
                            bool: True if the handler is enabled for the stage, False otherwise.
        """
    def is_paused(self) -> bool:
        """
                        Get the current simulation pause state.
        
                        Returns:
                            bool: True if the simulation is paused, False otherwise.
        """
    def is_simulating(self) -> bool:
        """
                        Get the current simulation pause state.
        
                        Returns:
                            bool: True if the simulation is paused, False otherwise.
        """
    def register_deletion_callback(self, arg0: typing.Callable[[str], None]) -> int:
        """
                        Register a callback for deletion events.
        
                        Args:
                            callback: Function to be called when an object is deleted. Takes a string path parameter.
        
                        Returns:
                            int: Unique identifier for the registered callback.
        """
    def register_physics_scene_addition_callback(self, arg0: typing.Callable[[str], None]) -> int:
        """
                        Register a callback for physics scene addition events.
        
                        Args:
                            callback: Function to be called when a physics scene is added. Takes a string path parameter.
        
                        Returns:
                            int: Unique identifier for the registered callback.
        """
    def reset(self) -> None:
        """
                        Reset the simulation manager to its initial state.
        
                        Calls all registered deletion callbacks with the root path ('/'),
                        clears all registered callbacks, clears the physics scenes list,
                        and resets the callback iterator to 0.
        """
    def set_callback_iter(self, arg0: int) -> None:
        """
                        Set the callback iteration counter.
        
                        Args:
                            val: New value for the callback iteration counter.
        """
def acquire_simulation_manager_interface(plugin_name: str = None, library_path: str = None) -> ISimulationManager:
    ...
def release_simulation_manager_interface(arg0: ISimulationManager) -> None:
    ...
