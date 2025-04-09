from __future__ import annotations
import pxr.Usd
import pxr.UsdGeom
import typing
__all__ = ['Generic', 'Lidar', 'RangeSensor', 'Tokens', 'UltrasonicArray', 'UltrasonicEmitter', 'UltrasonicFiringGroup', 'UltrasonicMaterialAPI']
class Generic(RangeSensor):
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateSamplingRateAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateStreamingAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetSamplingRateAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetStreamingAttr(*args, **kwargs):
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
class Lidar(RangeSensor):
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateEnableSemanticsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateHighLodAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateHorizontalFovAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateHorizontalResolutionAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateRotationRateAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateVerticalFovAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateVerticalResolutionAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateYawOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetEnableSemanticsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetHighLodAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetHorizontalFovAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetHorizontalResolutionAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetRotationRateAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetVerticalFovAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetVerticalResolutionAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetYawOffsetAttr(*args, **kwargs):
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
class RangeSensor(pxr.UsdGeom.Xformable):
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateDrawLinesAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateDrawPointsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMaxRangeAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMinRangeAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetDrawLinesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetDrawPointsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMaxRangeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMinRangeAttr(*args, **kwargs):
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
    adjacencyList: typing.ClassVar[str] = 'adjacencyList'
    attenuationAlpha: typing.ClassVar[str] = 'attenuationAlpha'
    drawLines: typing.ClassVar[str] = 'drawLines'
    drawPoints: typing.ClassVar[str] = 'drawPoints'
    emitterModes: typing.ClassVar[str] = 'emitterModes'
    emitterPrims: typing.ClassVar[str] = 'emitterPrims'
    enableSemantics: typing.ClassVar[str] = 'enableSemantics'
    enabled: typing.ClassVar[str] = 'enabled'
    firingGroups: typing.ClassVar[str] = 'firingGroups'
    highLod: typing.ClassVar[str] = 'highLod'
    horizontalFov: typing.ClassVar[str] = 'horizontalFov'
    horizontalResolution: typing.ClassVar[str] = 'horizontalResolution'
    maxRange: typing.ClassVar[str] = 'maxRange'
    minRange: typing.ClassVar[str] = 'minRange'
    numBins: typing.ClassVar[str] = 'numBins'
    perRayIntensity: typing.ClassVar[str] = 'perRayIntensity'
    receiverModes: typing.ClassVar[str] = 'receiverModes'
    rotationRate: typing.ClassVar[str] = 'rotationRate'
    samplingRate: typing.ClassVar[str] = 'samplingRate'
    streaming: typing.ClassVar[str] = 'streaming'
    useBRDF: typing.ClassVar[str] = 'useBRDF'
    useDistAttenuation: typing.ClassVar[str] = 'useDistAttenuation'
    useUSSMaterialsForBRDF: typing.ClassVar[str] = 'useUSSMaterialsForBRDF'
    ussBase_color: typing.ClassVar[str] = 'uss:base_color'
    ussMetallic: typing.ClassVar[str] = 'uss:metallic'
    ussPerceptualRoughness: typing.ClassVar[str] = 'uss:perceptualRoughness'
    ussReflectance: typing.ClassVar[str] = 'uss:reflectance'
    verticalFov: typing.ClassVar[str] = 'verticalFov'
    verticalResolution: typing.ClassVar[str] = 'verticalResolution'
    yawOffset: typing.ClassVar[str] = 'yawOffset'
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class UltrasonicArray(RangeSensor):
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateAttenuationAlphaAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateEmitterPrimsRel(*args, **kwargs):
        ...
    @staticmethod
    def CreateFiringGroupsRel(*args, **kwargs):
        ...
    @staticmethod
    def CreateHorizontalFovAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateHorizontalResolutionAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateNumBinsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateUseBRDFAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateUseDistAttenuationAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateUseUSSMaterialsForBRDFAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateVerticalFovAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateVerticalResolutionAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAttenuationAlphaAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetEmitterPrimsRel(*args, **kwargs):
        ...
    @staticmethod
    def GetFiringGroupsRel(*args, **kwargs):
        ...
    @staticmethod
    def GetHorizontalFovAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetHorizontalResolutionAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetNumBinsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetUseBRDFAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetUseDistAttenuationAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetUseUSSMaterialsForBRDFAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetVerticalFovAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetVerticalResolutionAttr(*args, **kwargs):
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
class UltrasonicEmitter(pxr.UsdGeom.Xformable):
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateAdjacencyListAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreatePerRayIntensityAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateYawOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAdjacencyListAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetPerRayIntensityAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetYawOffsetAttr(*args, **kwargs):
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
class UltrasonicFiringGroup(pxr.Usd.Typed):
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateEmitterModesAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateReceiverModesAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetEmitterModesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetReceiverModesAttr(*args, **kwargs):
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
class UltrasonicMaterialAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateBase_colorAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMetallicAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreatePerceptualRoughnessAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateReflectanceAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetBase_colorAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMetallicAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetPerceptualRoughnessAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetReflectanceAttr(*args, **kwargs):
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
__MFB_FULL_PACKAGE_NAME: str = 'rangeSensorSchema'
