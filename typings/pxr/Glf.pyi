"""

glf

"""
from __future__ import annotations
import typing
__all__ = ['DrawTarget', 'GLQueryObject', 'SimpleLight', 'SimpleMaterial', 'Texture']
class DrawTarget(Boost.Python.instance):
    """
    
    A class representing a GL render target with mutliple image
    attachments.
    
    A DrawTarget is essentially a custom render pass into which several
    arbitrary variables can be output into. These can later be used as
    texture samplers by GLSL shaders.
    
    The DrawTarget maintains a map of named attachments that correspond to
    GL_TEXTURE_2D mages. By default, DrawTargets also create a depth
    component that is used both as a depth buffer during the draw pass,
    and can later be accessed as a regular GL_TEXTURE_2D data. Stencils
    are also available (by setting the format to GL_DEPTH_STENCIL and the
    internalFormat to GL_DEPTH24_STENCIL8)
    
    """
    @staticmethod
    def AddAttachment(*args, **kwargs):
        """
        
        AddAttachment(name, format, type, internalFormat) -> None
        
        
        Add an attachment to the DrawTarget.
        
        
        Parameters
        ----------
        name : str
        
        format : GLenum
        
        type : GLenum
        
        internalFormat : GLenum
        
        
        """
    @staticmethod
    def Bind(*args, **kwargs):
        """
        
        Bind() -> None
        
        
        Binds the framebuffer.
        
        
        
        """
    @staticmethod
    def Unbind(*args, **kwargs):
        """
        
        Unbind() -> None
        
        
        Unbinds the framebuffer.
        
        
        
        """
    @staticmethod
    def WriteToFile(*args, **kwargs):
        """
        
        WriteToFile(name, filename, viewMatrix, projectionMatrix) -> bool
        
        
        Write the Attachment buffer to an image file (debugging).
        
        
        Parameters
        ----------
        name : str
        
        filename : str
        
        viewMatrix : Matrix4d
        
        projectionMatrix : Matrix4d
        
        
        """
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
        """
        
        __init__(size, requestMSAA)
        
        
        Parameters
        ----------
        size : Vec2i
        
        requestMSAA : bool
        
        
        
        ----------------------------------------------------------------------
        
        __init__(drawtarget)
        
        
        Parameters
        ----------
        drawtarget : DrawTarget
        
        
        """
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
    """
    
    Represents a GL query object in Glf
    
    """
    __instance_size__: typing.ClassVar[int] = 24
    @staticmethod
    def Begin(*args, **kwargs):
        """
        
        Begin(target) -> None
        
        
        Begin query for the given ``target`` target has to be one of
        GL_SAMPLES_PASSED, GL_ANY_SAMPLES_PASSED,
        GL_ANY_SAMPLES_PASSED_CONSERVATIVE, GL_PRIMITIVES_GENERATED
        GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN GL_TIME_ELAPSED,
        GL_TIMESTAMP.
        
        
        Parameters
        ----------
        target : GLenum
        
        
        """
    @staticmethod
    def BeginPrimitivesGenerated(*args, **kwargs):
        """
        
        BeginPrimitivesGenerated() -> None
        
        
        equivalent to Begin(GL_PRIMITIVES_GENERATED).
        
        
        The number of primitives sent to the rasterizer by the scoped drawing
        command will be returned.
        
        
        
        """
    @staticmethod
    def BeginSamplesPassed(*args, **kwargs):
        """
        
        BeginSamplesPassed() -> None
        
        
        equivalent to Begin(GL_SAMPLES_PASSED).
        
        
        The number of samples that pass the depth test for all drawing
        commands within the scope of the query will be returned.
        
        
        
        """
    @staticmethod
    def BeginTimeElapsed(*args, **kwargs):
        """
        
        BeginTimeElapsed() -> None
        
        
        equivalent to Begin(GL_TIME_ELAPSED).
        
        
        The time that it takes for the GPU to execute all of the scoped
        commands will be returned in nanoseconds.
        
        
        
        """
    @staticmethod
    def End(*args, **kwargs):
        """
        
        End() -> None
        
        
        End query.
        
        
        
        """
    @staticmethod
    def GetResult(*args, **kwargs):
        """
        
        GetResult() -> int
        
        
        Return the query result (synchronous) stalls CPU until the result
        becomes available.
        
        
        
        """
    @staticmethod
    def GetResultNoWait(*args, **kwargs):
        """
        
        GetResultNoWait() -> int
        
        
        Return the query result (asynchronous) returns 0 if the result hasn't
        been available.
        
        
        
        """
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(arg1)
        
        
        Parameters
        ----------
        arg1 : GLQueryObject
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class SimpleLight(Boost.Python.instance):
    """
    """
    __instance_size__: typing.ClassVar[int] = 376
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(position)
        
        
        Parameters
        ----------
        position : Vec4f
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @property
    def ambient(*args, **kwargs):
        """
        type : None
        
        ----------------------------------------------------------------------
        
        type : Vec4f
        """
    @ambient.setter
    def ambient(*args, **kwargs):
        ...
    @property
    def attenuation(*args, **kwargs):
        """
        type : None
        
        ----------------------------------------------------------------------
        
        type : Vec3f
        """
    @attenuation.setter
    def attenuation(*args, **kwargs):
        ...
    @property
    def diffuse(*args, **kwargs):
        """
        type : None
        
        ----------------------------------------------------------------------
        
        type : Vec4f
        """
    @diffuse.setter
    def diffuse(*args, **kwargs):
        ...
    @property
    def hasShadow(*args, **kwargs):
        """
        type : None
        """
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
        """
        type : None
        
        ----------------------------------------------------------------------
        
        type : bool
        """
    @isCameraSpaceLight.setter
    def isCameraSpaceLight(*args, **kwargs):
        ...
    @property
    def isDomeLight(*args, **kwargs):
        """
        type : None
        
        ----------------------------------------------------------------------
        
        type : bool
        """
    @isDomeLight.setter
    def isDomeLight(*args, **kwargs):
        ...
    @property
    def position(*args, **kwargs):
        """
        type : None
        
        ----------------------------------------------------------------------
        
        type : Vec4f
        """
    @position.setter
    def position(*args, **kwargs):
        ...
    @property
    def shadowBias(*args, **kwargs):
        """
        type : None
        
        ----------------------------------------------------------------------
        
        type : float
        """
    @shadowBias.setter
    def shadowBias(*args, **kwargs):
        ...
    @property
    def shadowBlur(*args, **kwargs):
        """
        type : None
        
        ----------------------------------------------------------------------
        
        type : float
        """
    @shadowBlur.setter
    def shadowBlur(*args, **kwargs):
        ...
    @property
    def shadowIndexEnd(*args, **kwargs):
        """
        type : None
        
        ----------------------------------------------------------------------
        
        type : int
        """
    @shadowIndexEnd.setter
    def shadowIndexEnd(*args, **kwargs):
        ...
    @property
    def shadowIndexStart(*args, **kwargs):
        """
        type : None
        
        ----------------------------------------------------------------------
        
        type : int
        """
    @shadowIndexStart.setter
    def shadowIndexStart(*args, **kwargs):
        ...
    @property
    def shadowMatrices(*args, **kwargs):
        """
        type : None
        
        ----------------------------------------------------------------------
        
        type : list[Matrix4d]
        """
    @shadowMatrices.setter
    def shadowMatrices(*args, **kwargs):
        ...
    @property
    def shadowResolution(*args, **kwargs):
        """
        type : None
        
        ----------------------------------------------------------------------
        
        type : int
        """
    @shadowResolution.setter
    def shadowResolution(*args, **kwargs):
        ...
    @property
    def specular(*args, **kwargs):
        """
        type : None
        
        ----------------------------------------------------------------------
        
        type : Vec4f
        """
    @specular.setter
    def specular(*args, **kwargs):
        ...
    @property
    def spotCutoff(*args, **kwargs):
        """
        type : None
        
        ----------------------------------------------------------------------
        
        type : float
        """
    @spotCutoff.setter
    def spotCutoff(*args, **kwargs):
        ...
    @property
    def spotDirection(*args, **kwargs):
        """
        type : None
        
        ----------------------------------------------------------------------
        
        type : Vec3f
        """
    @spotDirection.setter
    def spotDirection(*args, **kwargs):
        ...
    @property
    def spotFalloff(*args, **kwargs):
        """
        type : None
        
        ----------------------------------------------------------------------
        
        type : float
        """
    @spotFalloff.setter
    def spotFalloff(*args, **kwargs):
        ...
    @property
    def transform(*args, **kwargs):
        """
        type : None
        
        ----------------------------------------------------------------------
        
        type : Matrix4d
        """
    @transform.setter
    def transform(*args, **kwargs):
        ...
class SimpleMaterial(Boost.Python.instance):
    """
    """
    __instance_size__: typing.ClassVar[int] = 88
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @property
    def ambient(*args, **kwargs):
        """
        type : None
        
        ----------------------------------------------------------------------
        
        type : Vec4f
        """
    @ambient.setter
    def ambient(*args, **kwargs):
        ...
    @property
    def diffuse(*args, **kwargs):
        """
        type : None
        
        ----------------------------------------------------------------------
        
        type : Vec4f
        """
    @diffuse.setter
    def diffuse(*args, **kwargs):
        ...
    @property
    def emission(*args, **kwargs):
        """
        type : None
        
        ----------------------------------------------------------------------
        
        type : Vec4f
        """
    @emission.setter
    def emission(*args, **kwargs):
        ...
    @property
    def shininess(*args, **kwargs):
        """
        type : None
        
        ----------------------------------------------------------------------
        
        type : float
        """
    @shininess.setter
    def shininess(*args, **kwargs):
        ...
    @property
    def specular(*args, **kwargs):
        """
        type : None
        
        ----------------------------------------------------------------------
        
        type : Vec4f
        """
    @specular.setter
    def specular(*args, **kwargs):
        ...
class Texture(Boost.Python.instance):
    """
    
    Represents a texture object in Glf.
    
    A texture is typically defined by reading texture image data from an
    image file but a texture might also represent an attachment of a draw
    target.
    
    """
    @staticmethod
    def GetTextureMemoryAllocated(*args, **kwargs):
        """
        
        **classmethod** GetTextureMemoryAllocated() -> int
        
        
        static reporting function
        
        
        
        """
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
        """
        type : bool
        """
    @property
    def memoryRequested(*args, **kwargs):
        """
        type : None
        
        
        Specify the amount of memory the user wishes to allocate to the
        texture.
        
        ----------------------------------------------------------------------
        
        type : int
        
        
        Amount of memory the user wishes to allocate to the texture.
        """
    @memoryRequested.setter
    def memoryRequested(*args, **kwargs):
        ...
    @property
    def memoryUsed(*args, **kwargs):
        """
        type : int
        
        
        Amount of memory used to store the texture.
        """
    @property
    def minFilterSupported(*args, **kwargs):
        """
        type : bool
        """
__MFB_FULL_PACKAGE_NAME: str = 'glf'
