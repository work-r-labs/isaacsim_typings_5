from __future__ import annotations
import pxr.Usd
import pxr.UsdGeom
import typing
__all__ = ['IsaacBaseSensor', 'IsaacContactSensor', 'IsaacImuSensor', 'IsaacLightBeamSensor', 'IsaacRtxLidarSensorAPI', 'IsaacRtxRadarSensorAPI', 'Tokens']
class IsaacBaseSensor(pxr.UsdGeom.Xformable):
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class IsaacContactSensor(IsaacBaseSensor):
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateColorAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateRadiusAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSensorPeriodAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateThresholdAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetColorAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetRadiusAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetSensorPeriodAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetThresholdAttr(*args, **kwargs):
        ...
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class IsaacImuSensor(IsaacBaseSensor):
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateAngularVelocityFilterWidthAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLinearAccelerationFilterWidthAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateOrientationFilterWidthAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSensorPeriodAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAngularVelocityFilterWidthAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetLinearAccelerationFilterWidthAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetOrientationFilterWidthAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetSensorPeriodAttr(*args, **kwargs):
        ...
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class IsaacLightBeamSensor(IsaacBaseSensor):
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateCurtainAxisAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateCurtainLengthAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateForwardAxisAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMaxRangeAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMinRangeAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateNumRaysAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetCurtainAxisAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetCurtainLengthAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetForwardAxisAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMaxRangeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMinRangeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetNumRaysAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class IsaacRtxLidarSensorAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class IsaacRtxRadarSensorAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class Tokens(Boost.Python.instance):
    angularVelocityFilterWidth: typing.ClassVar[str] = 'angularVelocityFilterWidth'
    color: typing.ClassVar[str] = 'color'
    curtainAxis: typing.ClassVar[str] = 'curtainAxis'
    curtainLength: typing.ClassVar[str] = 'curtainLength'
    enabled: typing.ClassVar[str] = 'enabled'
    forwardAxis: typing.ClassVar[str] = 'forwardAxis'
    linearAccelerationFilterWidth: typing.ClassVar[str] = 'linearAccelerationFilterWidth'
    maxRange: typing.ClassVar[str] = 'maxRange'
    minRange: typing.ClassVar[str] = 'minRange'
    numRays: typing.ClassVar[str] = 'numRays'
    orientationFilterWidth: typing.ClassVar[str] = 'orientationFilterWidth'
    radius: typing.ClassVar[str] = 'radius'
    sensorPeriod: typing.ClassVar[str] = 'sensorPeriod'
    threshold: typing.ClassVar[str] = 'threshold'
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class _CanApplyResult(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 32
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def whyNot(*args, **kwargs):
        ...
__MFB_FULL_PACKAGE_NAME: str = 'isaacSensorSchema'
