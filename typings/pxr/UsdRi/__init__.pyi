from __future__ import annotations
import pxr.Usd
import typing
__all__: list[str] = ['MaterialAPI', 'RenderPassAPI', 'SplineAPI', 'StatementsAPI', 'Tokens']
class MaterialAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def ComputeInterfaceInputConsumersMap(*args, **kwargs):
        ...
    @staticmethod
    def CreateDisplacementAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSurfaceAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateVolumeAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetDisplacement(*args, **kwargs):
        ...
    @staticmethod
    def GetDisplacementAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetDisplacementOutput(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetSurface(*args, **kwargs):
        ...
    @staticmethod
    def GetSurfaceAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSurfaceOutput(*args, **kwargs):
        ...
    @staticmethod
    def GetVolume(*args, **kwargs):
        ...
    @staticmethod
    def GetVolumeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetVolumeOutput(*args, **kwargs):
        ...
    @staticmethod
    def SetDisplacementSource(*args, **kwargs):
        ...
    @staticmethod
    def SetSurfaceSource(*args, **kwargs):
        ...
    @staticmethod
    def SetVolumeSource(*args, **kwargs):
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
class RenderPassAPI(pxr.Usd.APISchemaBase):
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
    def GetCameraVisibilityCollectionAPI(*args, **kwargs):
        ...
    @staticmethod
    def GetMatteCollectionAPI(*args, **kwargs):
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
class SplineAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 80
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateInterpolationAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreatePositionsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateValuesAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetInterpolationAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetPositionsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetValuesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetValuesTypeName(*args, **kwargs):
        ...
    @staticmethod
    def Validate(*args, **kwargs):
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
class StatementsAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateRiAttribute(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetCoordinateSystem(*args, **kwargs):
        ...
    @staticmethod
    def GetModelCoordinateSystems(*args, **kwargs):
        ...
    @staticmethod
    def GetModelScopedCoordinateSystems(*args, **kwargs):
        ...
    @staticmethod
    def GetRiAttribute(*args, **kwargs):
        ...
    @staticmethod
    def GetRiAttributeName(*args, **kwargs):
        ...
    @staticmethod
    def GetRiAttributeNameSpace(*args, **kwargs):
        ...
    @staticmethod
    def GetRiAttributes(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetScopedCoordinateSystem(*args, **kwargs):
        ...
    @staticmethod
    def HasCoordinateSystem(*args, **kwargs):
        ...
    @staticmethod
    def HasScopedCoordinateSystem(*args, **kwargs):
        ...
    @staticmethod
    def IsRiAttribute(*args, **kwargs):
        ...
    @staticmethod
    def MakeRiAttributePropertyName(*args, **kwargs):
        ...
    @staticmethod
    def SetCoordinateSystem(*args, **kwargs):
        ...
    @staticmethod
    def SetScopedCoordinateSystem(*args, **kwargs):
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
    RiMaterialAPI: typing.ClassVar[str] = 'RiMaterialAPI'
    RiRenderPassAPI: typing.ClassVar[str] = 'RiRenderPassAPI'
    RiSplineAPI: typing.ClassVar[str] = 'RiSplineAPI'
    StatementsAPI: typing.ClassVar[str] = 'StatementsAPI'
    bspline: typing.ClassVar[str] = 'bspline'
    cameraVisibility: typing.ClassVar[str] = 'cameraVisibility'
    catmullRom: typing.ClassVar[str] = 'catmull-rom'
    collectionCameraVisibilityIncludeRoot: typing.ClassVar[str] = 'collection:cameraVisibility:includeRoot'
    constant: typing.ClassVar[str] = 'constant'
    interpolation: typing.ClassVar[str] = 'interpolation'
    linear: typing.ClassVar[str] = 'linear'
    matte: typing.ClassVar[str] = 'matte'
    outputsRiDisplacement: typing.ClassVar[str] = 'outputs:ri:displacement'
    outputsRiSurface: typing.ClassVar[str] = 'outputs:ri:surface'
    outputsRiVolume: typing.ClassVar[str] = 'outputs:ri:volume'
    positions: typing.ClassVar[str] = 'positions'
    renderContext: typing.ClassVar[str] = 'ri'
    spline: typing.ClassVar[str] = 'spline'
    values: typing.ClassVar[str] = 'values'
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
__MFB_FULL_PACKAGE_NAME: str = 'usdRi'
