from __future__ import annotations
from isaacsim.core.api.materials.physics_material import PhysicsMaterial
from isaacsim.core.api.materials.preview_surface import PreviewSurface
from isaacsim.core.api.materials.visual_material import VisualMaterial
import isaacsim.core.prims.impl.single_geometry_prim
from isaacsim.core.prims.impl.single_geometry_prim import SingleGeometryPrim
import isaacsim.core.prims.impl.single_rigid_prim
from isaacsim.core.prims.impl.single_rigid_prim import SingleRigidPrim
from isaacsim.core.utils.prims import get_prim_at_path
from isaacsim.core.utils.prims import is_prim_path_valid
from isaacsim.core.utils.stage import get_current_stage
from isaacsim.core.utils.string import find_unique_string_name
import numpy as np
from pxr import Gf
from pxr import UsdGeom
__all__ = ['DynamicSphere', 'FixedSphere', 'Gf', 'PhysicsMaterial', 'PreviewSurface', 'SingleGeometryPrim', 'SingleRigidPrim', 'UsdGeom', 'VisualMaterial', 'VisualSphere', 'find_unique_string_name', 'get_current_stage', 'get_prim_at_path', 'is_prim_path_valid', 'np']
class DynamicSphere(isaacsim.core.prims.impl.single_rigid_prim.SingleRigidPrim, FixedSphere):
    """
    High level wrapper to create/encapsulate a dynamic sphere
    
        .. note::
    
            Dynamic spheres (Sphere shape) have collisions (Collider API) and rigid body dynamics (Rigid Body API)
    
        Args:
            prim_path (str): prim path of the Prim to encapsulate or create
            name (str, optional): shortname to be used as a key by Scene class.
                                    Note: needs to be unique if the object is added to the Scene.
                                    Defaults to "dynamic_sphere".
            position (Optional[Sequence[float]], optional): position in the world frame of the prim. shape is (3, ).
                                                            Defaults to None, which means left unchanged.
            translation (Optional[Sequence[float]], optional): translation in the local frame of the prim
                                                            (with respect to its parent prim). shape is (3, ).
                                                            Defaults to None, which means left unchanged.
            orientation (Optional[Sequence[float]], optional): quaternion orientation in the world/ local frame of the prim
                                                            (depends if translation or position is specified).
                                                            quaternion is scalar-first (w, x, y, z). shape is (4, ).
                                                            Defaults to None, which means left unchanged.
            scale (Optional[Sequence[float]], optional): local scale to be applied to the prim's dimensions. shape is (3, ).
                                                    Defaults to None, which means left unchanged.
            visible (bool, optional): set to false for an invisible prim in the stage while rendering. Defaults to True.
            color (Optional[np.ndarray], optional): color of the visual shape. Defaults to None, which means 50% gray
            radius (Optional[float], optional): sphere radius. Defaults to None.
            visual_material (Optional[VisualMaterial], optional): visual material to be applied to the held prim.
                                    Defaults to None. If not specified, a default visual material will be added.
            physics_material (Optional[PhysicsMaterial], optional): physics material to be applied to the held prim.
                                    Defaults to None. If not specified, a default physics material will be added.
            mass (Optional[float], optional): mass in kg. Defaults to None.
            density (Optional[float], optional): density. Defaults to None.
            linear_velocity (Optional[np.ndarray], optional): linear velocity in the world frame. Defaults to None.
            angular_velocity (Optional[np.ndarray], optional): angular velocity in the world frame. Defaults to None.
    
        Example:
    
        .. code-block:: python
    
            >>> from isaacsim.core.api.objects import DynamicSphere
            >>> import numpy as np
            >>>
            >>> # create a red dynamic sphere of mass 1kg at the given path
            >>> prim = DynamicSphere(prim_path="/World/Xform/Sphere", color=np.array([1.0, 0.0, 0.0]), mass=1.0)
            >>> prim
            <isaacsim.core.api.objects.sphere.DynamicSphere object at 0x7f4deaf8f010>
        
    """
    def __init__(self, prim_path: str, name: str = 'dynamic_sphere', position: typing.Optional[numpy.ndarray] = None, translation: typing.Optional[numpy.ndarray] = None, orientation: typing.Optional[numpy.ndarray] = None, scale: typing.Optional[numpy.ndarray] = None, visible: typing.Optional[bool] = None, color: typing.Optional[numpy.ndarray] = None, radius: typing.Optional[numpy.ndarray] = None, visual_material: typing.Optional[isaacsim.core.api.materials.visual_material.VisualMaterial] = None, physics_material: typing.Optional[isaacsim.core.api.materials.physics_material.PhysicsMaterial] = None, mass: typing.Optional[float] = None, density: typing.Optional[float] = None, linear_velocity: typing.Optional[typing.Sequence[float]] = None, angular_velocity: typing.Optional[typing.Sequence[float]] = None) -> None:
        ...
class FixedSphere(VisualSphere):
    """
    High level wrapper to create/encapsulate a fixed sphere
    
        .. note::
    
            Fixed spheres (Sphere shape) have collisions (Collider API) but no rigid body dynamics (Rigid Body API)
    
        Args:
            prim_path (str): prim path of the Prim to encapsulate or create
            name (str, optional): shortname to be used as a key by Scene class.
                                    Note: needs to be unique if the object is added to the Scene.
                                    Defaults to "fixed_sphere".
            position (Optional[Sequence[float]], optional): position in the world frame of the prim. shape is (3, ).
                                                            Defaults to None, which means left unchanged.
            translation (Optional[Sequence[float]], optional): translation in the local frame of the prim
                                                            (with respect to its parent prim). shape is (3, ).
                                                            Defaults to None, which means left unchanged.
            orientation (Optional[Sequence[float]], optional): quaternion orientation in the world/ local frame of the prim
                                                            (depends if translation or position is specified).
                                                            quaternion is scalar-first (w, x, y, z). shape is (4, ).
                                                            Defaults to None, which means left unchanged.
            scale (Optional[Sequence[float]], optional): local scale to be applied to the prim's dimensions. shape is (3, ).
                                                    Defaults to None, which means left unchanged.
            visible (bool, optional): set to false for an invisible prim in the stage while rendering. Defaults to True.
            color (Optional[np.ndarray], optional): color of the visual shape. Defaults to None, which means 50% gray
            radius (Optional[float], optional): sphere radius. Defaults to None.
            visual_material (Optional[VisualMaterial], optional): visual material to be applied to the held prim.
                                    Defaults to None. If not specified, a default visual material will be added.
            physics_material (Optional[PhysicsMaterial], optional): physics material to be applied to the held prim.
                                    Defaults to None. If not specified, a default physics material will be added.
    
        Example:
    
        .. code-block:: python
    
            >>> from isaacsim.core.api.objects import FixedSphere
            >>> import numpy as np
            >>>
            >>> # create a red fixed sphere at the given path
            >>> prim = FixedSphere(prim_path="/World/Xform/Sphere", color=np.array([1.0, 0.0, 0.0]))
            >>> prim
            <isaacsim.core.api.objects.sphere.FixedSphere object at 0x7f4e433f2140>
        
    """
    def __init__(self, prim_path: str, name: str = 'fixed_sphere', position: typing.Optional[numpy.ndarray] = None, translation: typing.Optional[numpy.ndarray] = None, orientation: typing.Optional[numpy.ndarray] = None, scale: typing.Optional[numpy.ndarray] = None, visible: typing.Optional[bool] = None, color: typing.Optional[numpy.ndarray] = None, radius: typing.Optional[numpy.ndarray] = None, visual_material: typing.Optional[isaacsim.core.api.materials.visual_material.VisualMaterial] = None, physics_material: typing.Optional[isaacsim.core.api.materials.physics_material.PhysicsMaterial] = None) -> None:
        ...
class VisualSphere(isaacsim.core.prims.impl.single_geometry_prim.SingleGeometryPrim):
    """
    High level wrapper to create/encapsulate a visual sphere
    
        .. note::
    
            Visual spheres (Sphere shape) have no collisions (Collider API) or rigid body dynamics (Rigid Body API)
    
        Args:
            prim_path (str): prim path of the Prim to encapsulate or create
            name (str, optional): shortname to be used as a key by Scene class.
                                    Note: needs to be unique if the object is added to the Scene.
                                    Defaults to "visual_sphere".
            position (Optional[Sequence[float]], optional): position in the world frame of the prim. shape is (3, ).
                                                            Defaults to None, which means left unchanged.
            translation (Optional[Sequence[float]], optional): translation in the local frame of the prim
                                                            (with respect to its parent prim). shape is (3, ).
                                                            Defaults to None, which means left unchanged.
            orientation (Optional[Sequence[float]], optional): quaternion orientation in the world/ local frame of the prim
                                                            (depends if translation or position is specified).
                                                            quaternion is scalar-first (w, x, y, z). shape is (4, ).
                                                            Defaults to None, which means left unchanged.
            scale (Optional[Sequence[float]], optional): local scale to be applied to the prim's dimensions. shape is (3, ).
                                                    Defaults to None, which means left unchanged.
            visible (bool, optional): set to false for an invisible prim in the stage while rendering. Defaults to True.
            color (Optional[np.ndarray], optional): color of the visual shape. Defaults to None, which means 50% gray
            radius (Optional[float], optional): sphere radius. Defaults to None.
            visual_material (Optional[VisualMaterial], optional): visual material to be applied to the held prim.
                                    Defaults to None. If not specified, a default visual material will be added.
    
        Example:
    
        .. code-block:: python
    
            >>> from isaacsim.core.api.objects import VisualSphere
            >>> import numpy as np
            >>>
            >>> # create a red visual sphere at the given path
            >>> prim = VisualSphere(prim_path="/World/Xform/Sphere", color=np.array([1.0, 0.0, 0.0]))
            >>> prim
            <isaacsim.core.api.objects.sphere.VisualSphere object at 0x7f4e3eb3ea70>
        
    """
    def __init__(self, prim_path: str, name: str = 'visual_sphere', position: typing.Optional[typing.Sequence[float]] = None, translation: typing.Optional[typing.Sequence[float]] = None, orientation: typing.Optional[typing.Sequence[float]] = None, scale: typing.Optional[typing.Sequence[float]] = None, visible: typing.Optional[bool] = True, color: typing.Optional[numpy.ndarray] = None, radius: typing.Optional[float] = None, visual_material: typing.Optional[isaacsim.core.api.materials.visual_material.VisualMaterial] = None) -> None:
        ...
    def get_radius(self) -> float:
        """
        Get the sphere radius
        
                Returns:
                    float: sphere radius
        
                Example:
        
                .. code-block:: python
        
                    >>> prim.get_radius()
                    1.0
                
        """
    def set_radius(self, radius: float) -> None:
        """
        Set the sphere radius
        
                Args:
                    radius (float): sphere radius
        
                Example:
        
                .. code-block:: python
        
                    >>> prim.set_radius(2.0)
                
        """
