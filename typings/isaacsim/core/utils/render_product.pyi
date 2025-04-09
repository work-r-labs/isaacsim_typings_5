from __future__ import annotations
from isaacsim.core.utils.prims import set_prim_hide_in_stage_window
from isaacsim.core.utils.prims import set_prim_no_delete
from isaacsim.core.utils.stage import get_current_stage
from pxr import Gf
from pxr import Sdf
from pxr import Usd
from pxr import UsdRender
import warnings as warnings
__all__ = ['Gf', 'Sdf', 'Usd', 'UsdRender', 'add_aov', 'create_hydra_texture', 'get_camera_prim_path', 'get_current_stage', 'get_resolution', 'set_camera_prim_path', 'set_prim_hide_in_stage_window', 'set_prim_no_delete', 'set_resolution', 'warnings']
def add_aov(render_product_path: str, aov_name: str):
    """
    Adds an AOV/Render Var to an existing render product
    
        Args:
            render_product_path (str): path to the render product prim
            aov_name (str): Name of the render var we want to add to this render product
    
        Raises:
            RuntimeError: If the render product path is invalid
            RuntimeError: If the renderVar could not be created
            RuntimeError: If the renderVar could not be added to the render product
    
        
    """
def create_hydra_texture(resolution: typing.Tuple[int], camera_prim_path: str):
    ...
def get_camera_prim_path(render_product_path: str):
    """
    Get the current camera for a render product
    
        Args:
            render_product_path (str): path to the render product prim
    
        Raises:
            RuntimeError: If the render product path is invalid
    
        Returns:
            str : Path to the camera prim attached to this render product
        
    """
def get_resolution(render_product_path: str):
    """
    Get resolution for a render product
    
        Args:
            render_product_path (str): path to the render product prim
    
        Raises:
            RuntimeError: If the render product path is invalid
    
        Returns:
            Tuple[int]: (width,height)
        
    """
def set_camera_prim_path(render_product_path: str, camera_prim_path: str):
    """
    Sets the camera prim path for a render product
    
        Args:
            render_product_path (str):  path to the render product prim
            camera_prim_path (str):  path to the camera prim
    
        Raises:
            RuntimeError: If the render product path is invalid
        
    """
def set_resolution(render_product_path: str, resolution: typing.Tuple[int]):
    """
    Set resolution for a render product
    
        Args:
            render_product_path (str): path to the render product prim
            resolution (Tuple[float]): width,height for render product
    
        Raises:
            RuntimeError: If the render product path is invalid
        
    """
