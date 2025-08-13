"""

glf

"""
from __future__ import annotations
import typing
__all__: list[str] = ['DrawTarget', 'GLQueryObject', 'SimpleLight', 'SimpleMaterial', 'Texture']
class DrawTarget(Boost.Python.instance):
    @staticmethod
    def AddAttachment(*args, **kwargs):
        ...
    @staticmethod
    def Bind(*args, **kwargs):
        ...
    @staticmethod
    def Unbind(*args, **kwargs):
        ...
    @staticmethod
    def WriteToFile(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        """
        
        
        True if this object has not expired.  False otherwise.
        """
    @staticmethod
    def __eq__(*args, **kwargs):
        """
        
        
        Equality operator:  x == y
        """
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __lt__(*args, **kwargs):
        """
        
        
        Less than operator: x < y
        """
    @staticmethod
    def __ne__(*args, **kwargs):
        """
        
        
        Non-equality operator: x != y
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @property
    def expired(*args, **kwargs):
        """
        True if this object has expired, False otherwise.
        """
class GLQueryObject(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 32
    @staticmethod
    def Begin(*args, **kwargs):
        ...
    @staticmethod
    def BeginPrimitivesGenerated(*args, **kwargs):
        ...
    @staticmethod
    def BeginSamplesPassed(*args, **kwargs):
        ...
    @staticmethod
    def BeginTimeElapsed(*args, **kwargs):
        ...
    @staticmethod
    def End(*args, **kwargs):
        ...
    @staticmethod
    def GetResult(*args, **kwargs):
        ...
    @staticmethod
    def GetResultNoWait(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class SimpleLight(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 456
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @property
    def ambient(*args, **kwargs):
        ...
    @ambient.setter
    def ambient(*args, **kwargs):
        ...
    @property
    def attenuation(*args, **kwargs):
        ...
    @attenuation.setter
    def attenuation(*args, **kwargs):
        ...
    @property
    def diffuse(*args, **kwargs):
        ...
    @diffuse.setter
    def diffuse(*args, **kwargs):
        ...
    @property
    def hasShadow(*args, **kwargs):
        ...
    @hasShadow.setter
    def hasShadow(*args, **kwargs):
        ...
    @property
    def id(*args, **kwargs):
        ...
    @id.setter
    def id(*args, **kwargs):
        ...
    @property
    def isCameraSpaceLight(*args, **kwargs):
        ...
    @isCameraSpaceLight.setter
    def isCameraSpaceLight(*args, **kwargs):
        ...
    @property
    def isDomeLight(*args, **kwargs):
        ...
    @isDomeLight.setter
    def isDomeLight(*args, **kwargs):
        ...
    @property
    def position(*args, **kwargs):
        ...
    @position.setter
    def position(*args, **kwargs):
        ...
    @property
    def shadowBias(*args, **kwargs):
        ...
    @shadowBias.setter
    def shadowBias(*args, **kwargs):
        ...
    @property
    def shadowBlur(*args, **kwargs):
        ...
    @shadowBlur.setter
    def shadowBlur(*args, **kwargs):
        ...
    @property
    def shadowIndexEnd(*args, **kwargs):
        ...
    @shadowIndexEnd.setter
    def shadowIndexEnd(*args, **kwargs):
        ...
    @property
    def shadowIndexStart(*args, **kwargs):
        ...
    @shadowIndexStart.setter
    def shadowIndexStart(*args, **kwargs):
        ...
    @property
    def shadowMatrices(*args, **kwargs):
        ...
    @shadowMatrices.setter
    def shadowMatrices(*args, **kwargs):
        ...
    @property
    def shadowResolution(*args, **kwargs):
        ...
    @shadowResolution.setter
    def shadowResolution(*args, **kwargs):
        ...
    @property
    def specular(*args, **kwargs):
        ...
    @specular.setter
    def specular(*args, **kwargs):
        ...
    @property
    def spotCutoff(*args, **kwargs):
        ...
    @spotCutoff.setter
    def spotCutoff(*args, **kwargs):
        ...
    @property
    def spotDirection(*args, **kwargs):
        ...
    @spotDirection.setter
    def spotDirection(*args, **kwargs):
        ...
    @property
    def spotFalloff(*args, **kwargs):
        ...
    @spotFalloff.setter
    def spotFalloff(*args, **kwargs):
        ...
    @property
    def transform(*args, **kwargs):
        ...
    @transform.setter
    def transform(*args, **kwargs):
        ...
class SimpleMaterial(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 96
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @property
    def ambient(*args, **kwargs):
        ...
    @ambient.setter
    def ambient(*args, **kwargs):
        ...
    @property
    def diffuse(*args, **kwargs):
        ...
    @diffuse.setter
    def diffuse(*args, **kwargs):
        ...
    @property
    def emission(*args, **kwargs):
        ...
    @emission.setter
    def emission(*args, **kwargs):
        ...
    @property
    def shininess(*args, **kwargs):
        ...
    @shininess.setter
    def shininess(*args, **kwargs):
        ...
    @property
    def specular(*args, **kwargs):
        ...
    @specular.setter
    def specular(*args, **kwargs):
        ...
class Texture(Boost.Python.instance):
    @staticmethod
    def GetTextureMemoryAllocated(*args, **kwargs):
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
    @property
    def magFilterSupported(*args, **kwargs):
        ...
    @property
    def memoryRequested(*args, **kwargs):
        ...
    @memoryRequested.setter
    def memoryRequested(*args, **kwargs):
        ...
    @property
    def memoryUsed(*args, **kwargs):
        ...
    @property
    def minFilterSupported(*args, **kwargs):
        ...
__MFB_FULL_PACKAGE_NAME: str = 'glf'
