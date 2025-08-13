from __future__ import annotations
import pxr.Usd
import typing
__all__: list[str] = ['GenerativeProceduralAPI', 'Tokens']
class GenerativeProceduralAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateProceduralSystemAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateProceduralTypeAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetProceduralSystemAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetProceduralTypeAttr(*args, **kwargs):
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
    HwPrimvar_1: typing.ClassVar[str] = 'HwPrimvar_1'
    HwPtexTexture_1: typing.ClassVar[str] = 'HwPtexTexture_1'
    HwUvTexture_1: typing.ClassVar[str] = 'HwUvTexture_1'
    HydraGenerativeProceduralAPI: typing.ClassVar[str] = 'HydraGenerativeProceduralAPI'
    black: typing.ClassVar[str] = 'black'
    clamp: typing.ClassVar[str] = 'clamp'
    displayLookBxdf: typing.ClassVar[str] = 'displayLook:bxdf'
    faceIndex: typing.ClassVar[str] = 'faceIndex'
    faceOffset: typing.ClassVar[str] = 'faceOffset'
    frame: typing.ClassVar[str] = 'frame'
    hydraGenerativeProcedural: typing.ClassVar[str] = 'hydraGenerativeProcedural'
    infoFilename: typing.ClassVar[str] = 'inputs:file'
    infoVarname: typing.ClassVar[str] = 'inputs:varname'
    linear: typing.ClassVar[str] = 'linear'
    linearMipmapLinear: typing.ClassVar[str] = 'linearMipmapLinear'
    linearMipmapNearest: typing.ClassVar[str] = 'linearMipmapNearest'
    magFilter: typing.ClassVar[str] = 'magFilter'
    minFilter: typing.ClassVar[str] = 'minFilter'
    mirror: typing.ClassVar[str] = 'mirror'
    nearest: typing.ClassVar[str] = 'nearest'
    nearestMipmapLinear: typing.ClassVar[str] = 'nearestMipmapLinear'
    nearestMipmapNearest: typing.ClassVar[str] = 'nearestMipmapNearest'
    primvarsHdGpProceduralType: typing.ClassVar[str] = 'primvars:hdGp:proceduralType'
    proceduralSystem: typing.ClassVar[str] = 'proceduralSystem'
    repeat: typing.ClassVar[str] = 'repeat'
    textureMemory: typing.ClassVar[str] = 'textureMemory'
    useMetadata: typing.ClassVar[str] = 'useMetadata'
    uv: typing.ClassVar[str] = 'uv'
    wrapS: typing.ClassVar[str] = 'wrapS'
    wrapT: typing.ClassVar[str] = 'wrapT'
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
__MFB_FULL_PACKAGE_NAME: str = 'usdHydra'
