from __future__ import annotations
import math as math
import omni.kit.primitive.mesh.evaluators.abstract_shape_evaluator
from omni.kit.primitive.mesh.evaluators.abstract_shape_evaluator import AbstractShapeEvaluator
from omni.kit.primitive.mesh.evaluators.utils import build_int_slider
from omni.kit.primitive.mesh.evaluators.utils import get_int_setting
from omni.kit.primitive.mesh.evaluators.utils import transform_point
from pxr import Gf
import typing
__all__ = ['AbstractShapeEvaluator', 'Gf', 'SphereEvaluator', 'build_int_slider', 'get_int_setting', 'math', 'transform_point']
class SphereEvaluator(omni.kit.primitive.mesh.evaluators.abstract_shape_evaluator.AbstractShapeEvaluator):
    SETTING_OBJECT_HALF_SCALE: typing.ClassVar[str] = '/persistent/app/mesh_generator/shapes/shpere/object_half_scale'
    SETTING_U_SCALE: typing.ClassVar[str] = '/persistent/app/mesh_generator/shapes/sphere/u_scale'
    SETTING_V_SCALE: typing.ClassVar[str] = '/persistent/app/mesh_generator/shapes/sphere/v_scale'
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
    def _eval(self, u, v, up_axis):
        ...
    def eval(self, **kwargs):
        ...
