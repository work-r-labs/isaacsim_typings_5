from __future__ import annotations
import asyncio as asyncio
from carb import log_info
from carb import log_warn
import omni as omni
from omni.kit.window.filepicker.style import get_style
from omni import ui
from omni.ui import scene as sc
import os as os
import pathlib
__all__ = ['AnimatedDots', 'ICON_ROOT', 'LoadingPane', 'SingletonTask', 'Spinner', 'asyncio', 'exec_after_redraw', 'get_style', 'get_user_folders_dict', 'log_info', 'log_warn', 'omni', 'os', 'sc', 'ui']
class AnimatedDots:
    def __del__(self):
        ...
    def __init__(self, period: int = 30, phase: int = 3, width: int = 10, height: int = 20):
        """
        
                Initialize the event loop. 
                
                Keyword Args:
                    period(int): The time between updates in seconds (30)
                    phase(int): The phase of the update ( 0 - 3 )
                    width(int): The width of the UI ( default 10 )
                    height(int): The height of the UI ( default 20 )
                
        """
    def _build_ui(self, width: int = 0, height: int = 0):
        ...
    def _inf_loop(self):
        ...
class LoadingPane(SingletonTask):
    """
     A loading pane frame used to play during loading file from remote
    """
    def __init__(self, frame):
        ...
    def _build_ui(self):
        ...
    def destroy(self):
        """
        Destroy the loading frame. 
        """
    def hide(self):
        """
         Hide the loading frame.
        """
    def show(self):
        """
          Show the loading frame. 
        """
class SingletonTask:
    def __del__(self):
        ...
    def __init__(self):
        ...
    def cancel_task(self):
        """
         Cancel the task associated with this task if any. 
        """
    def destroy(self):
        """
         Called when the task is no longer needed. 
        """
    def run_task(self, task: typing.Coroutine) -> typing.Any:
        """
        
                Run a task and return its result. 
                Args:
                    task (Coroutine): The task to run. Must be a coroutine.
                
                Returns: 
                    Any: The result of the task. 
                
        """
class Spinner(omni.ui_scene._scene.Manipulator):
    """
     An ov logo rotator with a given speed.
    """
    def __init__(self, rotation_speed: int = 2):
        ...
    def on_build(self):
        ...
def exec_after_redraw(callback: typing.Callable, wait_frames: int = 2) -> typing.Any:
    """
    
        Execute a function after redrawing the dialog. 
        This is useful for unit tests where you want to wait for a dialog to be redrawn 
        and then call it in the next update frame.
        
        Args:
            callback (Callable): The function to execute after redrawing the dialog.
                       Function signature is void callback().
             
        Keyword Args:
            wait_frames (int): The number of frames to wait before executing the callback.
                       default value is 2.
        
        Returns: 
            :obj: 'asyncio.Task': future that will fire when the callback is executed.
        
    """
def get_user_folders_dict() -> dict:
    """
    
        Gets dictionary of user folders.
    
        Returns:
            dict: dictionary of user folders as name path pairs.
        
    """
ICON_ROOT: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.window.filepicker-2.11.7+d02c707b/icons')
