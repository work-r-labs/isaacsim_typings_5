from __future__ import annotations
from isaacsim.core.utils.stage import get_stage_units
from isaacsim.core.utils.transformations import get_relative_transform
import numpy
import numpy as np
import pxr.Usd
from pxr import Usd
from pxr import UsdGeom
import pxr.UsdGeom
__all__ = ['Usd', 'UsdGeom', 'get_mesh_vertices_relative_to', 'get_relative_transform', 'get_stage_units', 'np']
def get_mesh_vertices_relative_to(mesh_prim: pxr.UsdGeom.Mesh, coord_prim: pxr.Usd.Prim) -> numpy.ndarray:
    """
    Get vertices of the mesh prim in the coordinate system of the given prim.
    
        Args:
            mesh_prim (UsdGeom.Mesh): mesh prim to get the vertice points.
            coord_prim (Usd.Prim): prim used as relative coordinate.
    
        Returns:
            np.ndarray: vertices of the mesh in the coordinate system of the given prim. Shape is (N, 3).
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.mesh as mesh_utils
            >>> import isaacsim.core.utils.stage as stage_utils
            >>>
            >>> # 1 stage unit length cube centered at (0.0, 0.0, 0.0)
            >>> mesh_prim = stage_utils.get_current_stage().GetPrimAtPath("/World/Cube")
            >>> # 1 stage unit diameter sphere centered at (1.0, 1.0, 1.0)
            >>> coord_prim = stage_utils.get_current_stage().GetPrimAtPath("/World/Sphere")
            >>>
            >>> mesh_utils.get_mesh_vertices_relative_to(mesh_prim, coord_prim)
            [[-1.5 -1.5 -0.5]
             [-0.5 -1.5 -0.5]
             [-1.5 -0.5 -0.5]
             [-0.5 -0.5 -0.5]
             [-1.5 -1.5 -1.5]
             [-0.5 -1.5 -1.5]
             [-1.5 -0.5 -1.5]
             [-0.5 -0.5 -1.5]]
        
    """
