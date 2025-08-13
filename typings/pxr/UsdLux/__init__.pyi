from __future__ import annotations
import pxr.Tf
import pxr.Usd
import pxr.UsdGeom
import typing
__all__: list[str] = ['BoundableLightBase', 'CylinderLight', 'DiskLight', 'DistantLight', 'DomeLight', 'DomeLight_1', 'GeometryLight', 'LightAPI', 'LightFilter', 'LightListAPI', 'ListAPI', 'MeshLightAPI', 'NonboundableLightBase', 'PluginLight', 'PluginLightFilter', 'PortalLight', 'RectLight', 'ShadowAPI', 'ShapingAPI', 'SphereLight', 'Tokens', 'VolumeLightAPI']
class BoundableLightBase(pxr.UsdGeom.Boundable):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateColorAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateColorTemperatureAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateDiffuseAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateEnableColorTemperatureAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateExposureAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateFiltersRel(*args, **kwargs):
        ...
    @staticmethod
    def CreateIntensityAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateNormalizeAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSpecularAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetColorAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetColorTemperatureAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetDiffuseAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetEnableColorTemperatureAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetExposureAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetFiltersRel(*args, **kwargs):
        ...
    @staticmethod
    def GetIntensityAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetNormalizeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetSpecularAttr(*args, **kwargs):
        ...
    @staticmethod
    def LightAPI(*args, **kwargs):
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
class CylinderLight(BoundableLightBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateLengthAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateRadiusAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateTreatAsLineAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetLengthAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetRadiusAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetTreatAsLineAttr(*args, **kwargs):
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
class DiskLight(BoundableLightBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateRadiusAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetRadiusAttr(*args, **kwargs):
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
class DistantLight(NonboundableLightBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateAngleAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAngleAttr(*args, **kwargs):
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
class DomeLight(NonboundableLightBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateGuideRadiusAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreatePortalsRel(*args, **kwargs):
        ...
    @staticmethod
    def CreateTextureFileAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateTextureFormatAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetGuideRadiusAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetPortalsRel(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetTextureFileAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetTextureFormatAttr(*args, **kwargs):
        ...
    @staticmethod
    def OrientToStageUpAxis(*args, **kwargs):
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
class DomeLight_1(NonboundableLightBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateGuideRadiusAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreatePoleAxisAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreatePortalsRel(*args, **kwargs):
        ...
    @staticmethod
    def CreateTextureFileAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateTextureFormatAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetGuideRadiusAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetPoleAxisAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetPortalsRel(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetTextureFileAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetTextureFormatAttr(*args, **kwargs):
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
class GeometryLight(NonboundableLightBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateGeometryRel(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetGeometryRel(*args, **kwargs):
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
class LightAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def ConnectableAPI(*args, **kwargs):
        ...
    @staticmethod
    def CreateColorAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateColorTemperatureAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateDiffuseAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateEnableColorTemperatureAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateExposureAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateFiltersRel(*args, **kwargs):
        ...
    @staticmethod
    def CreateInput(*args, **kwargs):
        ...
    @staticmethod
    def CreateIntensityAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMaterialSyncModeAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateNormalizeAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateOutput(*args, **kwargs):
        ...
    @staticmethod
    def CreateShaderIdAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateShaderIdAttrForRenderContext(*args, **kwargs):
        ...
    @staticmethod
    def CreateSpecularAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetColorAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetColorTemperatureAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetDiffuseAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetEnableColorTemperatureAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetExposureAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetFiltersRel(*args, **kwargs):
        ...
    @staticmethod
    def GetInput(*args, **kwargs):
        ...
    @staticmethod
    def GetInputs(*args, **kwargs):
        ...
    @staticmethod
    def GetIntensityAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetLightLinkCollectionAPI(*args, **kwargs):
        ...
    @staticmethod
    def GetMaterialSyncModeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetNormalizeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetOutput(*args, **kwargs):
        ...
    @staticmethod
    def GetOutputs(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetShaderId(*args, **kwargs):
        ...
    @staticmethod
    def GetShaderIdAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetShaderIdAttrForRenderContext(*args, **kwargs):
        ...
    @staticmethod
    def GetShadowLinkCollectionAPI(*args, **kwargs):
        ...
    @staticmethod
    def GetSpecularAttr(*args, **kwargs):
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
class LightFilter(pxr.UsdGeom.Xformable):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def ConnectableAPI(*args, **kwargs):
        ...
    @staticmethod
    def CreateInput(*args, **kwargs):
        ...
    @staticmethod
    def CreateOutput(*args, **kwargs):
        ...
    @staticmethod
    def CreateShaderIdAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateShaderIdAttrForRenderContext(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetFilterLinkCollectionAPI(*args, **kwargs):
        ...
    @staticmethod
    def GetInput(*args, **kwargs):
        ...
    @staticmethod
    def GetInputs(*args, **kwargs):
        ...
    @staticmethod
    def GetOutput(*args, **kwargs):
        ...
    @staticmethod
    def GetOutputs(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetShaderId(*args, **kwargs):
        ...
    @staticmethod
    def GetShaderIdAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetShaderIdAttrForRenderContext(*args, **kwargs):
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
class LightListAPI(pxr.Usd.APISchemaBase):
    class ComputeMode(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: typing.ClassVar[str] = 'LightListAPI'
        allValues: typing.ClassVar[tuple]  # value = (UsdLux.LightListAPI.ComputeModeConsultModelHierarchyCache, UsdLux.LightListAPI.ComputeModeIgnoreCache)
        @staticmethod
        def GetValueFromName(*args, **kwargs):
            ...
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    ComputeModeConsultModelHierarchyCache: typing.ClassVar[ComputeMode]  # value = UsdLux.LightListAPI.ComputeModeConsultModelHierarchyCache
    ComputeModeIgnoreCache: typing.ClassVar[ComputeMode]  # value = UsdLux.LightListAPI.ComputeModeIgnoreCache
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def ComputeLightList(*args, **kwargs):
        ...
    @staticmethod
    def CreateLightListCacheBehaviorAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLightListRel(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetLightListCacheBehaviorAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetLightListRel(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def InvalidateLightList(*args, **kwargs):
        ...
    @staticmethod
    def StoreLightList(*args, **kwargs):
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
class ListAPI(pxr.Usd.APISchemaBase):
    class ComputeMode(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: typing.ClassVar[str] = 'ListAPI'
        allValues: typing.ClassVar[tuple]  # value = (UsdLux.ListAPI.ComputeModeConsultModelHierarchyCache, UsdLux.ListAPI.ComputeModeIgnoreCache)
        @staticmethod
        def GetValueFromName(*args, **kwargs):
            ...
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    ComputeModeConsultModelHierarchyCache: typing.ClassVar[ComputeMode]  # value = UsdLux.ListAPI.ComputeModeConsultModelHierarchyCache
    ComputeModeIgnoreCache: typing.ClassVar[ComputeMode]  # value = UsdLux.ListAPI.ComputeModeIgnoreCache
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def ComputeLightList(*args, **kwargs):
        ...
    @staticmethod
    def CreateLightListCacheBehaviorAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLightListRel(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetLightListCacheBehaviorAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetLightListRel(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def InvalidateLightList(*args, **kwargs):
        ...
    @staticmethod
    def StoreLightList(*args, **kwargs):
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
class MeshLightAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 56
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
class NonboundableLightBase(pxr.UsdGeom.Xformable):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateColorAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateColorTemperatureAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateDiffuseAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateEnableColorTemperatureAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateExposureAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateFiltersRel(*args, **kwargs):
        ...
    @staticmethod
    def CreateIntensityAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateNormalizeAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSpecularAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetColorAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetColorTemperatureAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetDiffuseAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetEnableColorTemperatureAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetExposureAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetFiltersRel(*args, **kwargs):
        ...
    @staticmethod
    def GetIntensityAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetNormalizeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetSpecularAttr(*args, **kwargs):
        ...
    @staticmethod
    def LightAPI(*args, **kwargs):
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
class PluginLight(pxr.UsdGeom.Xformable):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetNodeDefAPI(*args, **kwargs):
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
class PluginLightFilter(LightFilter):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetNodeDefAPI(*args, **kwargs):
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
class PortalLight(BoundableLightBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateHeightAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateWidthAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetHeightAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetWidthAttr(*args, **kwargs):
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
class RectLight(BoundableLightBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateHeightAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateTextureFileAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateWidthAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetHeightAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetTextureFileAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetWidthAttr(*args, **kwargs):
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
class ShadowAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def ConnectableAPI(*args, **kwargs):
        ...
    @staticmethod
    def CreateInput(*args, **kwargs):
        ...
    @staticmethod
    def CreateOutput(*args, **kwargs):
        ...
    @staticmethod
    def CreateShadowColorAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateShadowDistanceAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateShadowEnableAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateShadowFalloffAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateShadowFalloffGammaAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetInput(*args, **kwargs):
        ...
    @staticmethod
    def GetInputs(*args, **kwargs):
        ...
    @staticmethod
    def GetOutput(*args, **kwargs):
        ...
    @staticmethod
    def GetOutputs(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetShadowColorAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetShadowDistanceAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetShadowEnableAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetShadowFalloffAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetShadowFalloffGammaAttr(*args, **kwargs):
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
class ShapingAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def ConnectableAPI(*args, **kwargs):
        ...
    @staticmethod
    def CreateInput(*args, **kwargs):
        ...
    @staticmethod
    def CreateOutput(*args, **kwargs):
        ...
    @staticmethod
    def CreateShapingConeAngleAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateShapingConeSoftnessAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateShapingFocusAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateShapingFocusTintAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateShapingIesAngleScaleAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateShapingIesFileAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateShapingIesNormalizeAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetInput(*args, **kwargs):
        ...
    @staticmethod
    def GetInputs(*args, **kwargs):
        ...
    @staticmethod
    def GetOutput(*args, **kwargs):
        ...
    @staticmethod
    def GetOutputs(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetShapingConeAngleAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetShapingConeSoftnessAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetShapingFocusAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetShapingFocusTintAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetShapingIesAngleScaleAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetShapingIesFileAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetShapingIesNormalizeAttr(*args, **kwargs):
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
class SphereLight(BoundableLightBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateRadiusAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateTreatAsPointAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetRadiusAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetTreatAsPointAttr(*args, **kwargs):
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
    BoundableLightBase: typing.ClassVar[str] = 'BoundableLightBase'
    CylinderLight: typing.ClassVar[str] = 'CylinderLight'
    DiskLight: typing.ClassVar[str] = 'DiskLight'
    DistantLight: typing.ClassVar[str] = 'DistantLight'
    DomeLight: typing.ClassVar[str] = 'DomeLight'
    DomeLight_1: typing.ClassVar[str] = 'DomeLight_1'
    GeometryLight: typing.ClassVar[str] = 'GeometryLight'
    LightAPI: typing.ClassVar[str] = 'LightAPI'
    LightFilter: typing.ClassVar[str] = 'LightFilter'
    LightListAPI: typing.ClassVar[str] = 'LightListAPI'
    ListAPI: typing.ClassVar[str] = 'ListAPI'
    MeshLight: typing.ClassVar[str] = 'MeshLight'
    MeshLightAPI: typing.ClassVar[str] = 'MeshLightAPI'
    NonboundableLightBase: typing.ClassVar[str] = 'NonboundableLightBase'
    PluginLight: typing.ClassVar[str] = 'PluginLight'
    PluginLightFilter: typing.ClassVar[str] = 'PluginLightFilter'
    PortalLight: typing.ClassVar[str] = 'PortalLight'
    RectLight: typing.ClassVar[str] = 'RectLight'
    ShadowAPI: typing.ClassVar[str] = 'ShadowAPI'
    ShapingAPI: typing.ClassVar[str] = 'ShapingAPI'
    SphereLight: typing.ClassVar[str] = 'SphereLight'
    VolumeLight: typing.ClassVar[str] = 'VolumeLight'
    VolumeLightAPI: typing.ClassVar[str] = 'VolumeLightAPI'
    Y: typing.ClassVar[str] = 'Y'
    Z: typing.ClassVar[str] = 'Z'
    angular: typing.ClassVar[str] = 'angular'
    automatic: typing.ClassVar[str] = 'automatic'
    collectionFilterLinkIncludeRoot: typing.ClassVar[str] = 'collection:filterLink:includeRoot'
    collectionLightLinkIncludeRoot: typing.ClassVar[str] = 'collection:lightLink:includeRoot'
    collectionShadowLinkIncludeRoot: typing.ClassVar[str] = 'collection:shadowLink:includeRoot'
    consumeAndContinue: typing.ClassVar[str] = 'consumeAndContinue'
    consumeAndHalt: typing.ClassVar[str] = 'consumeAndHalt'
    cubeMapVerticalCross: typing.ClassVar[str] = 'cubeMapVerticalCross'
    filterLink: typing.ClassVar[str] = 'filterLink'
    geometry: typing.ClassVar[str] = 'geometry'
    guideRadius: typing.ClassVar[str] = 'guideRadius'
    ignore: typing.ClassVar[str] = 'ignore'
    independent: typing.ClassVar[str] = 'independent'
    inputsAngle: typing.ClassVar[str] = 'inputs:angle'
    inputsColor: typing.ClassVar[str] = 'inputs:color'
    inputsColorTemperature: typing.ClassVar[str] = 'inputs:colorTemperature'
    inputsDiffuse: typing.ClassVar[str] = 'inputs:diffuse'
    inputsEnableColorTemperature: typing.ClassVar[str] = 'inputs:enableColorTemperature'
    inputsExposure: typing.ClassVar[str] = 'inputs:exposure'
    inputsHeight: typing.ClassVar[str] = 'inputs:height'
    inputsIntensity: typing.ClassVar[str] = 'inputs:intensity'
    inputsLength: typing.ClassVar[str] = 'inputs:length'
    inputsNormalize: typing.ClassVar[str] = 'inputs:normalize'
    inputsRadius: typing.ClassVar[str] = 'inputs:radius'
    inputsShadowColor: typing.ClassVar[str] = 'inputs:shadow:color'
    inputsShadowDistance: typing.ClassVar[str] = 'inputs:shadow:distance'
    inputsShadowEnable: typing.ClassVar[str] = 'inputs:shadow:enable'
    inputsShadowFalloff: typing.ClassVar[str] = 'inputs:shadow:falloff'
    inputsShadowFalloffGamma: typing.ClassVar[str] = 'inputs:shadow:falloffGamma'
    inputsShapingConeAngle: typing.ClassVar[str] = 'inputs:shaping:cone:angle'
    inputsShapingConeSoftness: typing.ClassVar[str] = 'inputs:shaping:cone:softness'
    inputsShapingFocus: typing.ClassVar[str] = 'inputs:shaping:focus'
    inputsShapingFocusTint: typing.ClassVar[str] = 'inputs:shaping:focusTint'
    inputsShapingIesAngleScale: typing.ClassVar[str] = 'inputs:shaping:ies:angleScale'
    inputsShapingIesFile: typing.ClassVar[str] = 'inputs:shaping:ies:file'
    inputsShapingIesNormalize: typing.ClassVar[str] = 'inputs:shaping:ies:normalize'
    inputsSpecular: typing.ClassVar[str] = 'inputs:specular'
    inputsTextureFile: typing.ClassVar[str] = 'inputs:texture:file'
    inputsTextureFormat: typing.ClassVar[str] = 'inputs:texture:format'
    inputsWidth: typing.ClassVar[str] = 'inputs:width'
    latlong: typing.ClassVar[str] = 'latlong'
    lightFilterShaderId: typing.ClassVar[str] = 'lightFilter:shaderId'
    lightFilters: typing.ClassVar[str] = 'light:filters'
    lightLink: typing.ClassVar[str] = 'lightLink'
    lightList: typing.ClassVar[str] = 'lightList'
    lightListCacheBehavior: typing.ClassVar[str] = 'lightList:cacheBehavior'
    lightMaterialSyncMode: typing.ClassVar[str] = 'light:materialSyncMode'
    lightShaderId: typing.ClassVar[str] = 'light:shaderId'
    materialGlowTintsLight: typing.ClassVar[str] = 'materialGlowTintsLight'
    mirroredBall: typing.ClassVar[str] = 'mirroredBall'
    noMaterialResponse: typing.ClassVar[str] = 'noMaterialResponse'
    orientToStageUpAxis: typing.ClassVar[str] = 'orientToStageUpAxis'
    poleAxis: typing.ClassVar[str] = 'poleAxis'
    portals: typing.ClassVar[str] = 'portals'
    scene: typing.ClassVar[str] = 'scene'
    shadowLink: typing.ClassVar[str] = 'shadowLink'
    treatAsLine: typing.ClassVar[str] = 'treatAsLine'
    treatAsPoint: typing.ClassVar[str] = 'treatAsPoint'
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class VolumeLightAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 56
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
class _CanApplyResult(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 64
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
__MFB_FULL_PACKAGE_NAME: str = 'usdLux'
