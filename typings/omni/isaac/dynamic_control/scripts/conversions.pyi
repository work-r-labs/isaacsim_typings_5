from __future__ import annotations
import omni.isaac.dynamic_control._dynamic_control
from omni.isaac.dynamic_control import _dynamic_control
import pxr.Gf
from pxr import Gf
__all__ = ['Gf', 'create_transform', 'create_transform_from_mat']
def _vec3d_quatd_to_dctransform(translation: pxr.Gf.Vec3d, quat: pxr.Gf.Quatd) -> omni.isaac.dynamic_control._dynamic_control.Transform:
    ...
def create_transform(translation, rotation) -> omni.isaac.dynamic_control._dynamic_control.Transform:
    ...
def create_transform_from_mat(mat: pxr.Gf.Matrix4d) -> omni.isaac.dynamic_control._dynamic_control.Transform:
    ...
