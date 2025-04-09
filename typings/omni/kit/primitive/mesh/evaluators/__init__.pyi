"""
This module provides functionality to evaluate different geometric mesh primitives and retrieve their names.
"""
from __future__ import annotations
from omni.kit.primitive.mesh.evaluators.abstract_shape_evaluator import AbstractShapeEvaluator
from omni.kit.primitive.mesh.evaluators.cone import ConeEvaluator
from omni.kit.primitive.mesh.evaluators.cube import CubeEvaluator
from omni.kit.primitive.mesh.evaluators.cylinder import CylinderEvaluator
from omni.kit.primitive.mesh.evaluators.disk import DiskEvaluator
from omni.kit.primitive.mesh.evaluators.plane import PlaneEvaluator
from omni.kit.primitive.mesh.evaluators.sphere import SphereEvaluator
from omni.kit.primitive.mesh.evaluators.torus import TorusEvaluator
import re as re
from . import abstract_shape_evaluator
from . import cone
from . import cube
from . import cylinder
from . import disk
from . import plane
from . import sphere
from . import torus
from . import utils
__all__: list = ['get_geometry_mesh_prim_list', 'AbstractShapeEvaluator']
def _get_all_evaluators():
    ...
def get_geometry_mesh_prim_list():
    """
    Returns a sorted list of all available geometry mesh primitive names.
    
        Returns:
            list of str: Sorted list of geometry mesh primitive names.
    """
_all_evaluators: dict = {'Cone': cone.ConeEvaluator, 'Disk': disk.DiskEvaluator, 'Cube': cube.CubeEvaluator, 'Cylinder': cylinder.CylinderEvaluator, 'Sphere': sphere.SphereEvaluator, 'Torus': torus.TorusEvaluator, 'Plane': plane.PlaneEvaluator}
