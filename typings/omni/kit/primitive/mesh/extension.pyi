"""
This module contains the PrimitiveMeshExtension class for extending primitive mesh functionality in the Omni application.
"""
from __future__ import annotations
import omni as omni
from omni.kit.primitive.mesh.mesh_actions import deregister_actions
from omni.kit.primitive.mesh.mesh_actions import register_actions
from pxr import Usd
__all__: list = ['PrimitiveMeshExtension']
class PrimitiveMeshExtension(omni.ext._extensions.IExt):
    """
    A class designed to extend the functionality of primitive meshes within the Omni application.
    
        This class is an extension interface for Omni that allows for the registration and deregistration of mesh-related actions. It initializes a mesh generator, which can be used to create and manipulate mesh primitives. The `on_startup` method handles the extension startup logic, including the mesh generator's menu registration. The `on_shutdown` method ensures that any registered actions are properly deregistered and the mesh generator is destroyed if it exists.
        
    """
    def __init__(self):
        """
        Initializes the PrimitiveMeshExtension instance.
        """
    def on_shutdown(self):
        """
        Executes the shutdown routine and cleans up resources.
        """
    def on_startup(self, ext_id):
        """
        Executes the startup routine for the extension.
        
                Args:
                    ext_id (str): Identifier of the extension.
        """
