from __future__ import annotations
import argparse as argparse
import builtins as builtins
import carb as carb
import faulthandler as faulthandler
import omni as omni
import os as os
import re as re
import signal as signal
import sys as sys
import time as time
import typing
__all__ = ['SimulationApp', 'argparse', 'builtins', 'carb', 'faulthandler', 'omni', 'os', 're', 'signal', 'sys', 'time']
class SimulationApp:
    """
    Helper class to launch Omniverse Toolkit.
    
        Omniverse loads various plugins at runtime which cannot be imported unless
        the Toolkit is already running. Thus, it is necessary to launch the Toolkit first from
        your python application and then import everything else.
    
        Usage:
    
        .. code-block:: python
    
            # At top of your application
            from isaacsim.simulation_app import SimulationApp
            config = {
                 width: "1280",
                 height: "720",
                 headless: False,
            }
            simulation_app = SimulationApp(config)
    
            # Rest of the code follows
            ...
            simulation_app.close()
    
        Note:
                The settings in :obj:`DEFAULT_LAUNCHER_CONFIG` are overwritten by those in :obj:`config`.
    
        Arguments:
            config (dict): A dictionary containing the configuration for the app. (default: None)
            experience (str): Path to the application config loaded by the launcher (default: "", will load apps/isaacsim.kit if left blank)
        
    """
    DEFAULT_LAUNCHER_CONFIG: typing.ClassVar[dict] = {'headless': True, 'hide_ui': None, 'active_gpu': None, 'physics_gpu': 0, 'multi_gpu': True, 'max_gpu_count': None, 'sync_loads': True, 'width': 1280, 'height': 720, 'window_width': 1440, 'window_height': 900, 'display_options': 3094, 'subdiv_refinement_level': 0, 'renderer': 'RaytracedLighting', 'anti_aliasing': 3, 'samples_per_pixel_per_frame': 64, 'denoiser': True, 'max_bounces': 4, 'max_specular_transmission_bounces': 6, 'max_volume_bounces': 4, 'open_usd': None, 'fast_shutdown': True, 'profiler_backend': list(), 'create_new_stage': True, 'extra_args': list(), 'experience': '/home/chris/isaacsim/apps/isaacsim.exp.base.python.kit'}
    def __del__(self):
        """
        Destructor for the class.
        """
    def __init__(self, launch_config: dict = None, experience: str = '') -> None:
        ...
    def _prepare_ui(self) -> None:
        """
        Dock the windows in the UI if they exist.
        """
    def _set_render_settings(self, default: bool = False) -> None:
        """
        Set render settings to those in config.
        
                Note:
                    This should be used in case a new stage is opened and the desired config needs
                    to be re-applied.
        
                Args:
                    default (bool, optional): Whether to setup RTX default or non-default settings. Defaults to False.
                
        """
    def _start_app(self) -> None:
        """
        Launch the Omniverse application.
        """
    def _wait_for_viewport(self) -> None:
        ...
    def close(self, wait_for_replicator = True) -> None:
        """
        Close the running Omniverse Toolkit.
        """
    def is_exiting(self) -> bool:
        """
        
                bool: True if close() was called previously, False otherwise
                
        """
    def is_running(self) -> bool:
        """
        
                bool: convenience function to see if app is running. True if running, False otherwise
                
        """
    def reset_render_settings(self):
        """
        Reset render settings to those in config.
        
                Note:
                    This should be used in case a new stage is opened and the desired config needs
                    to be re-applied.
                
        """
    def set_setting(self, setting: str, value) -> None:
        """
        
                Set a carbonite setting
        
                Args:
                    setting (str): carb setting path
                    value: value to set the setting to, type is used to properly set the setting.
                
        """
    def update(self) -> None:
        """
        
                Convenience function to step the application forward one frame
                
        """
    @property
    def app(self) -> omni.kit.app.IApp:
        """
        
                omni.kit.app.IApp: omniverse kit application object
                
        """
    @property
    def context(self) -> omni.usd.UsdContext:
        """
        
                omni.usd.UsdContext: the current USD context
                
        """
