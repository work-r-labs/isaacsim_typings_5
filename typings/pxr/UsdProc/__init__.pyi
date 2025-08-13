from __future__ import annotations
import pxr.UsdGeom
import typing
__all__: list[str] = ['GenerativeProcedural', 'Tokens']
class GenerativeProcedural(pxr.UsdGeom.Boundable):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateProceduralSystemAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetProceduralSystemAttr(*args, **kwargs):
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
    GenerativeProcedural: typing.ClassVar[str] = 'GenerativeProcedural'
    proceduralSystem: typing.ClassVar[str] = 'proceduralSystem'
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
__MFB_FULL_PACKAGE_NAME: str = 'usdProc'
