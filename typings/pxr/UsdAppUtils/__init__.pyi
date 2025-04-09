from __future__ import annotations
import typing
from . import cameraArgs
from . import colorArgs
from . import complexityArgs
from . import framesArgs
from . import rendererArgs
__all__ = ['FrameRecorder', 'cameraArgs', 'colorArgs', 'complexityArgs', 'framesArgs', 'rendererArgs']
class FrameRecorder(Boost.Python.instance):
    """
    
    A utility class for recording images of USD stages.
    
    UsdAppUtilsFrameRecorder uses Hydra to produce recorded images of a
    USD stage looking through a particular UsdGeomCamera on that stage at
    a particular UsdTimeCode. The images generated will be effectively the
    same as what you would see in the viewer in usdview.
    
    Note that it is assumed that an OpenGL context has already been setup.
    
    """
    __instance_size__: typing.ClassVar[int] = 496
    @staticmethod
    def GetCurrentRendererId(*args, **kwargs):
        """
        
        GetCurrentRendererId() -> str
        
        
        Gets the ID of the Hydra renderer plugin that will be used for
        recording.
        
        
        
        """
    @staticmethod
    def Record(*args, **kwargs):
        """
        
        Record(stage, usdCamera, timeCode, outputImagePath) -> bool
        
        
        Records an image and writes the result to ``outputImagePath`` .
        
        
        The recorded image will represent the view from ``usdCamera`` looking
        at the imageable prims on USD stage ``stage`` at time ``timeCode`` .
        
        If ``usdCamera`` is not a valid camera, a camera will be computed to
        automatically frame the stage geometry.
        
        Returns true if the image was generated and written successfully, or
        false otherwise.
        
        
        Parameters
        ----------
        stage : Stage
        
        usdCamera : Camera
        
        timeCode : TimeCode
        
        outputImagePath : str
        
        
        """
    @staticmethod
    def SetColorCorrectionMode(*args, **kwargs):
        """
        
        SetColorCorrectionMode(colorCorrectionMode) -> None
        
        
        Sets the color correction mode to be used for recording.
        
        
        By default, color correction is disabled.
        
        
        Parameters
        ----------
        colorCorrectionMode : str
        
        
        """
    @staticmethod
    def SetComplexity(*args, **kwargs):
        """
        
        SetComplexity(complexity) -> None
        
        
        Sets the level of refinement complexity.
        
        
        The default complexity is"low"(1.0).
        
        
        Parameters
        ----------
        complexity : float
        
        
        """
    @staticmethod
    def SetImageWidth(*args, **kwargs):
        """
        
        SetImageWidth(imageWidth) -> None
        
        
        Sets the width of the recorded image.
        
        
        The height of the recorded image will be computed using this value and
        the aspect ratio of the camera used for recording.
        
        The default image width is 960 pixels.
        
        
        Parameters
        ----------
        imageWidth : int
        
        
        """
    @staticmethod
    def SetIncludedPurposes(*args, **kwargs):
        """
        
        SetIncludedPurposes(purposes) -> None
        
        
        Sets the UsdGeomImageable purposes to be used for rendering.
        
        
        We will **always** include"default"purpose, and by default, we will
        also include UsdGeomTokens->proxy. Use this method to explicitly
        enumerate an alternate set of purposes to be included along
        with"default".
        
        
        Parameters
        ----------
        purposes : list[str]
        
        
        """
    @staticmethod
    def SetRendererPlugin(*args, **kwargs):
        """
        
        SetRendererPlugin(id) -> bool
        
        
        Sets the Hydra renderer plugin to be used for recording.
        
        
        Parameters
        ----------
        id : str
        
        
        """
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
__MFB_FULL_PACKAGE_NAME: str = 'usdAppUtils'
