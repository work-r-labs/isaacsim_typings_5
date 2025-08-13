"""

Camera utilities.

"""
from __future__ import annotations
import pxr.Tf
import typing
__all__: list[str] = ['ConformWindowPolicy', 'Crop', 'DontConform', 'Fit', 'Framing', 'MatchHorizontally', 'MatchVertically', 'ScreenWindowParameters']
class ConformWindowPolicy(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: typing.ClassVar[str] = ''
    allValues: typing.ClassVar[tuple]  # value = (CameraUtil.MatchVertically, CameraUtil.MatchHorizontally, CameraUtil.Fit, CameraUtil.Crop, CameraUtil.DontConform)
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
class Framing(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 64
    @staticmethod
    def ApplyToProjectionMatrix(*args, **kwargs):
        ...
    @staticmethod
    def ComputeFilmbackWindow(*args, **kwargs):
        ...
    @staticmethod
    def IsValid(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
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
    def dataWindow(*args, **kwargs):
        ...
    @dataWindow.setter
    def dataWindow(*args, **kwargs):
        ...
    @property
    def displayWindow(*args, **kwargs):
        ...
    @displayWindow.setter
    def displayWindow(*args, **kwargs):
        ...
    @property
    def pixelAspectRatio(*args, **kwargs):
        ...
    @pixelAspectRatio.setter
    def pixelAspectRatio(*args, **kwargs):
        ...
class ScreenWindowParameters(Boost.Python.instance):
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @property
    def fieldOfView(*args, **kwargs):
        ...
    @property
    def screenWindow(*args, **kwargs):
        ...
    @property
    def zFacingViewMatrix(*args, **kwargs):
        ...
Crop: ConformWindowPolicy  # value = CameraUtil.Crop
DontConform: ConformWindowPolicy  # value = CameraUtil.DontConform
Fit: ConformWindowPolicy  # value = CameraUtil.Fit
MatchHorizontally: ConformWindowPolicy  # value = CameraUtil.MatchHorizontally
MatchVertically: ConformWindowPolicy  # value = CameraUtil.MatchVertically
__MFB_FULL_PACKAGE_NAME: str = 'cameraUtil'
