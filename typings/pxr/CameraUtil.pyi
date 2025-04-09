"""

Camera utilities.

"""
from __future__ import annotations
import pxr.Tf
import typing
__all__ = ['ConformWindowPolicy', 'Crop', 'DontConform', 'Fit', 'Framing', 'MatchHorizontally', 'MatchVertically', 'ScreenWindowParameters']
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
    """
    
    Framing information. That is information determining how the filmback
    plane of a camera maps to the pixels of the rendered image
    (displayWindow together with pixelAspectRatio and window policy) and
    what pixels of the image will be filled by the renderer (dataWindow).
    
    The concepts of displayWindow and dataWindow are similar to the ones
    in OpenEXR, including that the x- and y-axis of the coordinate system
    point left and down, respectively.
    
    In fact, these windows mean the same here and in OpenEXR if the
    displayWindow has the same aspect ratio (when accounting for the
    pixelAspectRatio) as the filmback plane of the camera has (that is the
    ratio of the horizontalAperture to verticalAperture of, e.g., Usd's
    Camera or GfCamera).
    
    In particular, overscan can be achieved by making the dataWindow
    larger than the displayWindow.
    
    If the aspect ratios differ, a window policy is applied to the
    displayWindow to determine how the pixels correspond to the filmback
    plane. One such window policy is to take the largest rect that fits
    (centered) into the displayWindow and has the camera's aspect ratio.
    For example, if the displayWindow and dataWindow are the same and both
    have an aspect ratio smaller than the camera, the image is created by
    enlarging the camera frustum slightly in the bottom and top direction.
    
    When using the AOVs, the render buffer size is determined
    independently from the framing info. However, the dataWindow is
    supposed to be contained in the render buffer rect (in particular, the
    dataWindow cannot contain pixels withs negative coordinates - this
    restriction does not apply if, e.g., hdPrman circumvents AOVs and
    writes directly to EXR). In other words, unlike in OpenEXR, the rect
    of pixels for which we allocate storage can differ from the rect the
    renderer fills with data (dataWindow).
    
    For example, an application can set the render buffer size to match
    the widget size but use a dataWindow and displayWindow that only fills
    the render buffer horizontally to have slates at the top and bottom.
    
    """
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def ApplyToProjectionMatrix(*args, **kwargs):
        """
        
        ApplyToProjectionMatrix(projectionMatrix, windowPolicy) -> Matrix4d
        
        
        Given the projectionMatrix computed from a camera, applies the
        framing.
        
        
        To obtain a correct result, a rasterizer needs to use the resulting
        projection matrix and set the viewport to the data window.
        
        
        Parameters
        ----------
        projectionMatrix : Matrix4d
        
        windowPolicy : ConformWindowPolicy
        
        
        """
    @staticmethod
    def IsValid(*args, **kwargs):
        """
        
        IsValid() -> bool
        
        
        Is display and data window non-empty.
        
        
        
        """
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        Creates an invalid framing, i.e., with empty display and data window.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(displayWindow, dataWindow, pixelAspectRatio)
        
        
        Creates a framing with given display and data window and pixel aspect
        ratio.
        
        
        Parameters
        ----------
        displayWindow : Range2f
        
        dataWindow : Rect2i
        
        pixelAspectRatio : float
        
        
        
        ----------------------------------------------------------------------
        
        __init__(dataWindow)
        
        
        Creates a framing with equal display and data window (and assuming
        square pixels).
        
        
        Parameters
        ----------
        dataWindow : Rect2i
        
        
        """
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
    """
    
    Given a camera object, compute parameters suitable for setting up
    RenderMan.
    
    """
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(camera, fitDirection)
        
        
        Constructs screenwindow parameter.
        
        
        The optional ``fitDirection`` indicates in which direction the
        screenwindow will have length 2.
        
        
        Parameters
        ----------
        camera : Camera
        
        fitDirection : Camera.FOVDirection
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @property
    def fieldOfView(*args, **kwargs):
        """
        type : float
        
        
        The field of view.
        
        
        More precisely, the full angle perspective field of view (in degrees)
        between screen space coordinates (-1,0) and (1,0). Give these
        parameters to RiProjection as parameter after"perspective".
        """
    @property
    def screenWindow(*args, **kwargs):
        """
        type : Vec4d
        
        
        The vector (left, right, bottom, top) defining the rectangle in the
        image plane.
        
        
        Give these parameters to RiScreenWindow.
        """
    @property
    def zFacingViewMatrix(*args, **kwargs):
        """
        type : Matrix4d
        
        
        Returns the inverse of the transform for a camera that is y-Up and
        z-facing (vs the OpenGL camera that is (-z)-facing).
        
        
        Write this transform with RiConcatTransform before RiWorldBegin.
        """
Crop: ConformWindowPolicy  # value = CameraUtil.Crop
DontConform: ConformWindowPolicy  # value = CameraUtil.DontConform
Fit: ConformWindowPolicy  # value = CameraUtil.Fit
MatchHorizontally: ConformWindowPolicy  # value = CameraUtil.MatchHorizontally
MatchVertically: ConformWindowPolicy  # value = CameraUtil.MatchVertically
__MFB_FULL_PACKAGE_NAME: str = 'cameraUtil'
