from __future__ import annotations
import omni.kit.primitive.mesh.evaluators.abstract_shape_evaluator
from omni.kit.primitive.mesh.evaluators.abstract_shape_evaluator import AbstractShapeEvaluator
from omni.kit.primitive.mesh.evaluators.utils import build_int_slider
from omni.kit.primitive.mesh.evaluators.utils import generate_circle_points
from omni.kit.primitive.mesh.evaluators.utils import generate_disk
from omni.kit.primitive.mesh.evaluators.utils import get_int_setting
from omni.kit.primitive.mesh.evaluators.utils import inverse_u
from omni.kit.primitive.mesh.evaluators.utils import inverse_v
from omni.kit.primitive.mesh.evaluators.utils import modify_winding_order
from omni.kit.primitive.mesh.evaluators.utils import transform_point
from pxr import Gf
import typing
__all__ = ['AbstractShapeEvaluator', 'CylinderEvaluator', 'Gf', 'build_int_slider', 'generate_circle_points', 'generate_disk', 'get_int_setting', 'inverse_u', 'inverse_v', 'modify_winding_order', 'transform_point']
class CylinderEvaluator(omni.kit.primitive.mesh.evaluators.abstract_shape_evaluator.AbstractShapeEvaluator):
    SETTING_OBJECT_HALF_SCALE: typing.ClassVar[str] = '/persistent/app/mesh_generator/shapes/cylinder/object_half_scale'
    SETTING_U_SCALE: typing.ClassVar[str] = '/persistent/app/mesh_generator/shapes/cylinder/u_scale'
    SETTING_V_SCALE: typing.ClassVar[str] = '/persistent/app/mesh_generator/shapes/cylinder/v_scale'
    SETTING_W_SCALE: typing.ClassVar[str] = '/persistent/app/mesh_generator/shapes/cylinder/w_scale'
    @staticmethod
    def build_setting_ui():
        ...
    @staticmethod
    def get_default_half_scale():
        ...
    @staticmethod
    def reset_setting():
        ...
    def __init__(self, attributes: dict):
        ...
    def eval(self, **kwargs):
        ...
