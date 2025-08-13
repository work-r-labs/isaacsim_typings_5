"""

        Isaac Sim Core Nodes Module
        
        This module provides core functionality for simulation time management and tracking.
        It offers methods to query various time metrics in the simulation:
        
        - Simulation time (sim time)
        - Monotonic simulation time
        - System (real-world) time
        - Physics step count
        
        These time functions can be queried for the current state or for specific
        points in time using RationalTime objects or (deprecated) stage with history (swh) frame numbers.
        
        Usage:
            # Import the module
            from isaacsim.core.nodes.bindings import _isaacsim_core_nodes
            
            # Acquire the interface
            core_nodes = _isaacsim_core_nodes.acquire_interface()
            
            # Get current time metrics
            sim_time = core_nodes.get_sim_time()
            monotonic_time = core_nodes.get_sim_time_monotonic()
            system_time = core_nodes.get_system_time()
            
            # Get time metrics for a specific frame
            frame_sim_time = core_nodes.get_sim_time_at_time((0, 0))
            
            # Get physics step count
            steps = core_nodes.get_physics_num_steps()
            
            # Timeline control affects time metrics and physics steps
            timeline = omni.timeline.get_timeline_interface()
            timeline.play()  # Start simulation, physics steps will increment
            timeline.stop()  # Stop simulation, physics steps reset to 0
    
"""
from __future__ import annotations
import typing
__all__: list[str] = ['CoreNodes', 'acquire_interface', 'release_interface']
class CoreNodes:
    def get_physics_num_steps(self) -> int:
        """
                        Gets the number of physics steps completed since simulation start.
        
                        This counter is reset to zero when the timeline is stopped.
        
                        Returns:
                            int: The number of physics steps completed.
        
                        @deprecated: This method is deprecated and will be removed in a future release.
                        Please use isaacsim.core.simulation_manager.get_num_physics_steps() instead.
        """
    def get_sim_time(self) -> float:
        """
                        Gets the current simulation time in seconds.
        
                        Returns:
                            float: The current simulation time in seconds.
        
                        @deprecated: This method is deprecated and will be removed in a future release.
                        Please use isaacsim.core.simulation_manager.get_simulation_time() instead.
        """
    @typing.overload
    def get_sim_time_at_time(self, arg0: ...) -> float:
        """
                        Gets simulation time in seconds at a specific rational time.
        
                        Args:
                            time (omni.fabric.RationalTime): The rational time to query.
        
                        Returns:
                            float: The simulation time in seconds at the specified time.
        
                        @deprecated: This method is deprecated and will be removed in a future release.
                        Please use isaacsim.core.simulation_manager.get_simulation_time_at_time() instead.
        """
    @typing.overload
    def get_sim_time_at_time(self, arg0: tuple[int, int]) -> float:
        """
                        Gets simulation time in seconds at a specific rational time.
        
                        Args:
                            time (tuple): A tuple of (numerator, denominator) representing the rational time.
        
                        Returns:
                            float: The simulation time in seconds at the specified time.
        
                        @deprecated: This method is deprecated and will be removed in a future release.
                        Please use isaacsim.core.simulation_manager.get_simulation_time_at_time() instead.
        """
    def get_sim_time_monotonic(self) -> float:
        """
                        Gets a monotonically increasing simulation time in seconds.
        
                        This time is guaranteed to always increase, unlike regular simulation time
                        which can be reset or modified by timeline operations.
        
                        Returns:
                            float: The monotonic simulation time in seconds.
        
                        @deprecated: This method is deprecated and will be removed in a future release.
                        Please use isaacsim.core.simulation_manager.get_simulation_monotonic() instead.
        """
    @typing.overload
    def get_sim_time_monotonic_at_time(self, arg0: ...) -> float:
        """
                        Gets monotonic simulation time in seconds at a specific rational time.
        
                        Args:
                            time (omni.fabric.RationalTime): The rational time to query.
        
                        Returns:
                            float: The monotonic simulation time in seconds at the specified time.
        
                        @deprecated: This method is deprecated and will be removed in a future release.
                        Please use isaacsim.core.simulation_manager.get_simulation_time_monotonic_at_time() instead.
        """
    @typing.overload
    def get_sim_time_monotonic_at_time(self, arg0: tuple[int, int]) -> float:
        """
                        Gets monotonic simulation time in seconds at a specific rational time.
        
                        Args:
                            time (tuple): A tuple of (numerator, denominator) representing the rational time.
        
                        Returns:
                            float: The monotonic simulation time in seconds at the specified time.
        
                        @deprecated: This method is deprecated and will be removed in a future release.
                        Please use isaacsim.core.simulation_manager.get_simulation_time_monotonic_at_time() instead.
        """
    def get_system_time(self) -> float:
        """
                        Gets the current system (real-world) time in seconds.
        
                        Returns:
                            float: The current system time in seconds.
        
                        @deprecated: This method is deprecated and will be removed in a future release.
                        Please use isaacsim.core.simulation_manager.get_system_time() instead.
        """
    @typing.overload
    def get_system_time_at_time(self, arg0: ...) -> float:
        """
                        Gets system (real-world) time in seconds at a specific rational time.
        
                        Args:
                            time (omni.fabric.RationalTime): The rational time to query.
        
                        Returns:
                            float: The system time in seconds at the specified time.
        
                        @deprecated: This method is deprecated and will be removed in a future release.
                        Please use isaacsim.core.simulation_manager.get_system_time_at_time() instead.
        """
    @typing.overload
    def get_system_time_at_time(self, arg0: tuple[int, int]) -> float:
        """
                        Gets system (real-world) time in seconds at a specific rational time.
        
                        Args:
                            time (tuple): A tuple of (numerator, denominator) representing the rational time.
        
                        Returns:
                            float: The system time in seconds at the specified time.
        
                        @deprecated: This method is deprecated and will be removed in a future release.
                        Please use isaacsim.core.simulation_manager.get_system_time_at_time() instead.
        """
def acquire_interface(plugin_name: str = None, library_path: str = None) -> CoreNodes:
    ...
def release_interface(arg0: CoreNodes) -> None:
    ...
