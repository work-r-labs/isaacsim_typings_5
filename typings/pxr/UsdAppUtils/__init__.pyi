from __future__ import annotations
import typing
from . import cameraArgs
from . import colorArgs
from . import complexityArgs
from . import framesArgs
from . import rendererArgs
__all__: list[str] = ['FrameRecorder', 'cameraArgs', 'colorArgs', 'complexityArgs', 'framesArgs', 'rendererArgs']
class FrameRecorder(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 600
    @staticmethod
    def GetCurrentRendererId(*args, **kwargs):
        ...
    @staticmethod
    def Record(*args, **kwargs):
        ...
    @staticmethod
    def SetCameraLightEnabled(*args, **kwargs):
        ...
    @staticmethod
    def SetColorCorrectionMode(*args, **kwargs):
        ...
    @staticmethod
    def SetComplexity(*args, **kwargs):
        ...
    @staticmethod
    def SetImageWidth(*args, **kwargs):
        ...
    @staticmethod
    def SetIncludedPurposes(*args, **kwargs):
        ...
    @staticmethod
    def SetRendererPlugin(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
__MFB_FULL_PACKAGE_NAME: str = 'usdAppUtils'
