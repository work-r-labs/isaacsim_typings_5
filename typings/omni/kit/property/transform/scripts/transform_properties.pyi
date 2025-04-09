"""
Provides a custom extension to manipulate USD property widgets for transformations in Omniverse Kit.
"""
from __future__ import annotations
import carb as carb
from functools import partial
import omni as omni
from omni.kit.property.transform.scripts import transform_builder
from omni.kit.property.transform.scripts.transform_widget import TransformAttributeWidget
from omni.kit.property.transform.scripts import xform_op_utils
from omni.kit.property.usd.prim_selection_payload import PrimSelectionPayload
from pathlib import Path
import pxr.Tf
from pxr import Tf
from pxr import Usd
from pxr import UsdGeom
__all__: list = ['TransformPropertyExtension']
class TransformPropertyExtension(omni.ext._extensions.IExt):
    """
    A class designed to extend the functionality of USD property widgets in Omniverse Kit.
    
        This extension adds context menu options and a custom widget to manipulate transformation properties of USD prims. It enables adding, disabling, deleting, and enabling various transformation operations like translate, rotate, scale, and pivot directly from the property window's context menu. It also handles the startup and shutdown processes for registering and unregistering the custom widget and menu items.
        
    """
    def __init__(self):
        """
        Initializes the TransformPropertyExtension object.
        """
    def _add_xform_op(self, payload: omni.kit.property.usd.prim_selection_payload.PrimSelectionPayload, add_translate_op: bool, add_rotate_xyz_op: bool, add_orient_op: bool, add_scale_op: bool, add_transform_op: bool, add_pivot = False):
        ...
    def _prim_is_type(self, objects: dict, prim_type: pxr.Tf.Type) -> bool:
        """
        
                Checks if prims are given class/schema
                
        """
    def _register_context_menu(self):
        ...
    def _register_widget(self):
        ...
    def _unregister_context_menu(self):
        ...
    def _unregister_widget(self):
        ...
    def on_shutdown(self):
        """
        Called when the extension is shut down.
        """
    def on_startup(self, ext_id):
        """
        Called when the extension is started.
        
                Args:
                    ext_id (str): The ID of the extension being started.
        """
