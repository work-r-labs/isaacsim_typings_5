"""
Material utility UI for omni.kit.window.content_browser (Bind material) & omni.kit.context_menu (Create/Material).
"""
from __future__ import annotations
import asyncio as asyncio
import carb as carb
import omni as omni
from omni.kit.material.library.material_dialog import MaterialDialogs
from omni.kit.usd import layers
import os as os
from pxr import Gf
from pxr import Sdf
from pxr import Tf
from pxr import Trace
import pxr.Usd
from pxr import Usd
from pxr import UsdGeom
from pxr import UsdShade
from pxr import UsdUtils
__all__: list = ['MaterialUIExtensions']
class MaterialUIExtensions:
    """
    Material utility UI for omni.kit.window.content_browser (Bind material) & omni.kit.context_menu (Create/Material).
    """
    @staticmethod
    def _can_show_content_bind_material(content_url):
        ...
    @staticmethod
    def _content_bind_material(mdl_path):
        ...
    @staticmethod
    def create_material_and_assign(objects: dict, create_fn: typing.Callable, blocking: bool = True) -> None:
        """
        
                create material and bind to prims
        
                Args:
                    objects: (dict): dictionary of prims
                    create_fn: create material function
                    blocking: block and call create_fn
                
        """
    def __del__(self):
        ...
    def __init__(self):
        """
        Material utility UI for omni.kit.window.content_browser (Bind material) & omni.kit.context_menu (Create/Material).
        """
    def _add_content_window_menus(self):
        ...
    def _add_context_menus(self):
        ...
    def _remove_content_window_menus(self):
        ...
    def _remove_context_menus(self):
        ...
    def bind_material_to_prims_dialog(self, stage: pxr.Usd.Stage, prims: list) -> None:
        """
        
                Show bind material to prims dialog.
        
                Args:
                    stage (Usd.Stage): stage
                    prims (list): list of prims to bind material to.
                
        """
