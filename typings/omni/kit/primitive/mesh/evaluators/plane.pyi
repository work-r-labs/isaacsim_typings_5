from __future__ import annotations
import omni.kit.primitive.mesh.evaluators.abstract_shape_evaluator
from omni.kit.primitive.mesh.evaluators.abstract_shape_evaluator import AbstractShapeEvaluator
from omni.kit.primitive.mesh.evaluators.utils import build_int_slider
from omni.kit.primitive.mesh.evaluators.utils import generate_plane
from omni.kit.primitive.mesh.evaluators.utils import get_int_setting
from omni.kit.primitive.mesh.evaluators.utils import inverse_u
from pxr import Gf
import typing
__all__ = ['AbstractShapeEvaluator', 'Gf', 'PlaneEvaluator', 'build_int_slider', 'generate_plane', 'get_int_setting', 'inverse_u']
class PlaneEvaluator(omni.kit.primitive.mesh.evaluators.abstract_shape_evaluator.AbstractShapeEvaluator):
    SETTING_OBJECT_HALF_SCALE: typing.ClassVar[str] = '/persistent/app/mesh_generator/shapes/plane/object_half_scale'
    SETTING_U_SCALE: typing.ClassVar[str] = '/persistent/app/mesh_generator/shapes/plane/u_scale'
    SETTING_V_SCALE: typing.ClassVar[str] = '/persistent/app/mesh_generator/shapes/plane/v_scale'
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
