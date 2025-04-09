from __future__ import annotations
import typing
__all__ = ['Constants', 'c']
class Constants:
    """
    A class containing constants for the transform manipulator settings.
    
        These constants are used for accessing and storing transform manipulator settings such as movement mode, rotation mode, operation type, and various configuration settings related to the manipulator tool.
        
    """
    FREE_ROTATION_ENABLED_SETTING: typing.ClassVar[str] = '/persistent/exts/omni.kit.manipulator.transform/manipulator/freeRotationEnabled'
    FREE_ROTATION_TYPE_CLAMPED: typing.ClassVar[str] = 'Clamped'
    FREE_ROTATION_TYPE_CONTINUOUS: typing.ClassVar[str] = 'Continuous'
    FREE_ROTATION_TYPE_SETTING: typing.ClassVar[str] = '/persistent/exts/omni.kit.manipulator.transform/manipulator/freeRotationType'
    INTERSECTION_THICKNESS_SETTING: typing.ClassVar[str] = '/persistent/exts/omni.kit.manipulator.transform/manipulator/intersectionThickness'
    MANIPULATOR_SCALE_SETTING: typing.ClassVar[str] = '/persistent/exts/omni.kit.manipulator.transform/manipulator/scaleMultiplier'
    OMNI_SCALE_DIR_SETTING: typing.ClassVar[str] = '/persistent/exts/omni.kit.manipulator.transform/manipulator/omniScaleDirection'
    TOOLS_DEFAULT_COLLAPSED_SETTING: typing.ClassVar[str] = '/persistent/exts/omni.kit.manipulator.transform/tools/defaultCollapsed'
    TRANSFORM_MODE_GLOBAL: typing.ClassVar[str] = 'global'
    TRANSFORM_MODE_LOCAL: typing.ClassVar[str] = 'local'
    TRANSFORM_MOVE_MODE_SETTING: typing.ClassVar[str] = '/app/transform/moveMode'
    TRANSFORM_OP_MOVE: typing.ClassVar[str] = 'move'
    TRANSFORM_OP_ROTATE: typing.ClassVar[str] = 'rotate'
    TRANSFORM_OP_SCALE: typing.ClassVar[str] = 'scale'
    TRANSFORM_OP_SELECT: typing.ClassVar[str] = 'select'
    TRANSFORM_OP_SETTING: typing.ClassVar[str] = '/app/transform/operation'
    TRANSFORM_ROTATE_MODE_SETTING: typing.ClassVar[str] = '/app/transform/rotateMode'
c = Constants
