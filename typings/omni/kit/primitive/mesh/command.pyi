"""
This module provides commands to create various mesh primitives with default transformations in a USD stage.
"""
from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.primitive.mesh.evaluators import _get_all_evaluators
from pxr import Gf
from pxr import Sdf
from pxr import Usd
from pxr import UsdGeom
from pxr import Vt
import typing
__all__: list = ['CreateMeshPrimWithDefaultXformCommand', 'CreateMeshPrimCommand']
class CreateMeshPrimCommand(CreateMeshPrimWithDefaultXformCommand):
    """
    A command class for creating a mesh primitive in a USD stage with default transformations.
    
        This class is a specialized command for generating various types of mesh primitives such as Plane, Sphere, Cone, etc., and applies a default transformation to them. It extends the CreateMeshPrimWithDefaultXformCommand class.
    
        Args:
            prim_type (str): The type of primitive mesh to create. Supported types include 'Plane', 'Sphere', 'Cone', 'Cylinder', 'Disk', 'Torus', 'Cube'.
    
        Keyword Args:
            object_origin (Gf.Vec3f): The position of the mesh center in the stage units.
            u_patches (int): The number of patches for tessellating the U direction.
            v_patches (int): The number of patches for tessellating the V direction.
            w_patches (int): The number of patches for tessellating the W direction; only applies to 'Cone', 'Cylinder', and 'Cube'.
            half_scale (float): Half the size of the mesh in centimeters; if None, it's controlled by settings.
            u_verts_scale (int): Tessellation level multiplier for the U direction.
            v_verts_scale (int): Tessellation level multiplier for the V direction.
            w_verts_scale (int): Tessellation level multiplier for the W direction; for 'Cone' and 'Cylinder', it tessellates the caps, for 'Cube', it tessellates along the z-axis.
            above_ground (bool): If True, offsets the mesh center above the ground plane; applicable when 'object_origin' is not provided. Defaults to False.
            context_name (str): The name of the USD context. Defaults to an empty string.
            prim_path (str): The path where the new primitive will be created. If None, a default path is generated.
            select_new_prim (bool): Whether to select the new primitive after creation. Defaults to True.
            prepend_default_prim (bool): If True, prepends the default primitive name to the newly created prim path. Defaults to True.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, prim_type: str, **kwargs):
        """
        Initializes the command to create a mesh primitive.
        """
class CreateMeshPrimWithDefaultXformCommand(omni.kit.commands.command.Command):
    """
    A command class to create mesh primitives with default transformations in a USD stage.
    
        This command supports creating various types of mesh primitives such as Plane, Sphere, Cone, Cylinder, Disk, Torus, and Cube.
        It also handles setting up default transformations and attributes for the newly created mesh based on persistent settings and keyword arguments provided during initialization.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, prim_type: str, **kwargs):
        """
        
                Creates primitive.
        
                Args:
                    prim_type (str): It supports Plane/Sphere/Cone/Cylinder/Disk/Torus/Cube.
        
                kwargs:
                    object_origin (Gf.Vec3f): Position of mesh center in stage units.
        
                    u_patches (int): The number of patches to tessellate U direction.
        
                    v_patches (int): The number of patches to tessellate V direction.
        
                    w_patches (int): The number of patches to tessellate W direction.
                                     It only works for Cone/Cylinder/Cube.
        
                    half_scale (float): Half size of mesh in centimeters. Default is None, which means it's controlled by settings.
        
                    u_verts_scale (int): Tessellation Level of U. It's a multiplier of u_patches.
        
                    v_verts_scale (int): Tessellation Level of V. It's a multiplier of v_patches.
        
                    w_verts_scale (int): Tessellation Level of W. It's a multiplier of w_patches.
                                         It only works for Cone/Cylinder/Cube.
                                         For Cone/Cylinder, it's to tessellate the caps.
                                         For Cube, it's to tessellate along z-axis.
        
                    above_ground (bool): It will offset the center of mesh above the ground plane if it's True,
                        False otherwise. It's False by default. This param only works when param object_origin is not given.
                        Otherwise, it will be ignored.
                
        """
    def _define_mesh(self, mesh):
        ...
    def do(self):
        """
        Executes the command to create the mesh primitive.
        """
    def undo(self):
        """
        Undoes the creation of the mesh primitive.
        """
PERSISTENT_SETTINGS_PREFIX: str = '/persistent'
