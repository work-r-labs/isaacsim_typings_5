from __future__ import annotations
import typing
__all__ = ['ALL_INSTANCES', 'CullStyle', 'DrawMode', 'Engine', 'RenderParams', 'RendererCommandArgDescriptor', 'RendererCommandDescriptor', 'RendererSetting', 'RendererSettingType']
class CullStyle(Boost.Python.enum):
    CULL_STYLE_BACK: typing.ClassVar[CullStyle]  # value = pxr.UsdImagingGL.CullStyle.CULL_STYLE_BACK
    CULL_STYLE_BACK_UNLESS_DOUBLE_SIDED: typing.ClassVar[CullStyle]  # value = pxr.UsdImagingGL.CullStyle.CULL_STYLE_BACK_UNLESS_DOUBLE_SIDED
    CULL_STYLE_FRONT: typing.ClassVar[CullStyle]  # value = pxr.UsdImagingGL.CullStyle.CULL_STYLE_FRONT
    CULL_STYLE_NOTHING: typing.ClassVar[CullStyle]  # value = pxr.UsdImagingGL.CullStyle.CULL_STYLE_NOTHING
    __slots__: typing.ClassVar[tuple] = tuple()
    names: typing.ClassVar[dict]  # value = {'CULL_STYLE_NOTHING': pxr.UsdImagingGL.CullStyle.CULL_STYLE_NOTHING, 'CULL_STYLE_BACK': pxr.UsdImagingGL.CullStyle.CULL_STYLE_BACK, 'CULL_STYLE_FRONT': pxr.UsdImagingGL.CullStyle.CULL_STYLE_FRONT, 'CULL_STYLE_BACK_UNLESS_DOUBLE_SIDED': pxr.UsdImagingGL.CullStyle.CULL_STYLE_BACK_UNLESS_DOUBLE_SIDED}
    values: typing.ClassVar[dict]  # value = {1: pxr.UsdImagingGL.CullStyle.CULL_STYLE_NOTHING, 2: pxr.UsdImagingGL.CullStyle.CULL_STYLE_BACK, 3: pxr.UsdImagingGL.CullStyle.CULL_STYLE_FRONT, 4: pxr.UsdImagingGL.CullStyle.CULL_STYLE_BACK_UNLESS_DOUBLE_SIDED}
class DrawMode(Boost.Python.enum):
    DRAW_GEOM_FLAT: typing.ClassVar[DrawMode]  # value = pxr.UsdImagingGL.DrawMode.DRAW_GEOM_FLAT
    DRAW_GEOM_ONLY: typing.ClassVar[DrawMode]  # value = pxr.UsdImagingGL.DrawMode.DRAW_GEOM_ONLY
    DRAW_GEOM_SMOOTH: typing.ClassVar[DrawMode]  # value = pxr.UsdImagingGL.DrawMode.DRAW_GEOM_SMOOTH
    DRAW_POINTS: typing.ClassVar[DrawMode]  # value = pxr.UsdImagingGL.DrawMode.DRAW_POINTS
    DRAW_SHADED_FLAT: typing.ClassVar[DrawMode]  # value = pxr.UsdImagingGL.DrawMode.DRAW_SHADED_FLAT
    DRAW_SHADED_SMOOTH: typing.ClassVar[DrawMode]  # value = pxr.UsdImagingGL.DrawMode.DRAW_SHADED_SMOOTH
    DRAW_WIREFRAME: typing.ClassVar[DrawMode]  # value = pxr.UsdImagingGL.DrawMode.DRAW_WIREFRAME
    DRAW_WIREFRAME_ON_SURFACE: typing.ClassVar[DrawMode]  # value = pxr.UsdImagingGL.DrawMode.DRAW_WIREFRAME_ON_SURFACE
    __slots__: typing.ClassVar[tuple] = tuple()
    names: typing.ClassVar[dict]  # value = {'DRAW_POINTS': pxr.UsdImagingGL.DrawMode.DRAW_POINTS, 'DRAW_WIREFRAME': pxr.UsdImagingGL.DrawMode.DRAW_WIREFRAME, 'DRAW_WIREFRAME_ON_SURFACE': pxr.UsdImagingGL.DrawMode.DRAW_WIREFRAME_ON_SURFACE, 'DRAW_SHADED_FLAT': pxr.UsdImagingGL.DrawMode.DRAW_SHADED_FLAT, 'DRAW_SHADED_SMOOTH': pxr.UsdImagingGL.DrawMode.DRAW_SHADED_SMOOTH, 'DRAW_GEOM_ONLY': pxr.UsdImagingGL.DrawMode.DRAW_GEOM_ONLY, 'DRAW_GEOM_FLAT': pxr.UsdImagingGL.DrawMode.DRAW_GEOM_FLAT, 'DRAW_GEOM_SMOOTH': pxr.UsdImagingGL.DrawMode.DRAW_GEOM_SMOOTH}
    values: typing.ClassVar[dict]  # value = {0: pxr.UsdImagingGL.DrawMode.DRAW_POINTS, 1: pxr.UsdImagingGL.DrawMode.DRAW_WIREFRAME, 2: pxr.UsdImagingGL.DrawMode.DRAW_WIREFRAME_ON_SURFACE, 3: pxr.UsdImagingGL.DrawMode.DRAW_SHADED_FLAT, 4: pxr.UsdImagingGL.DrawMode.DRAW_SHADED_SMOOTH, 5: pxr.UsdImagingGL.DrawMode.DRAW_GEOM_ONLY, 6: pxr.UsdImagingGL.DrawMode.DRAW_GEOM_FLAT, 7: pxr.UsdImagingGL.DrawMode.DRAW_GEOM_SMOOTH}
class Engine(Boost.Python.instance):
    """
    UsdImaging Renderer class
    """
    __instance_size__: typing.ClassVar[int] = 448
    @staticmethod
    def AddSelected(*args, **kwargs):
        """
        
        AddSelected(path, instanceIndex) -> None
        
        
        Add a path with instanceIndex to the list of prim paths that should be
        included in selection highlighting.
        
        
        UsdImagingDelegate::ALL_INSTANCES can be used for highlighting all
        instances if path is an instancer.
        
        
        Parameters
        ----------
        path : Path
        
        instanceIndex : int
        
        
        """
    @staticmethod
    def ClearSelected(*args, **kwargs):
        """
        
        ClearSelected() -> None
        
        
        Clear the list of prim paths that should be included in selection
        highlighting.
        
        
        
        """
    @staticmethod
    def GetCurrentRendererId(*args, **kwargs):
        """
        
        GetCurrentRendererId() -> str
        
        
        Return the id of the currently used renderer plugin.
        
        
        
        """
    @staticmethod
    def GetRenderStats(*args, **kwargs):
        """
        
        GetRenderStats() -> VtDictionary
        
        
        Returns render statistics.
        
        
        The contents of the dictionary will depend on the current render
        delegate.
        
        
        
        """
    @staticmethod
    def GetRendererAovs(*args, **kwargs):
        """
        
        GetRendererAovs() -> list[str]
        
        
        Return the vector of available renderer AOV settings.
        
        
        
        """
    @staticmethod
    def GetRendererCommandDescriptors(*args, **kwargs):
        """
        
        GetRendererCommandDescriptors() -> HdCommandDescriptors
        
        
        Return command deescriptors for commands supported by the active
        render delegate.
        
        
        
        """
    @staticmethod
    def GetRendererDisplayName(*args, **kwargs):
        """
        
        **classmethod** GetRendererDisplayName(id) -> str
        
        
        Return the user-friendly description of a renderer plugin.
        
        
        Parameters
        ----------
        id : str
        
        
        """
    @staticmethod
    def GetRendererPlugins(*args, **kwargs):
        """
        
        **classmethod** GetRendererPlugins() -> list[str]
        
        
        Return the vector of available render-graph delegate plugins.
        
        
        
        """
    @staticmethod
    def GetRendererSetting(*args, **kwargs):
        """
        
        GetRendererSetting(id) -> VtValue
        
        
        Gets a renderer setting's current value.
        
        
        Parameters
        ----------
        id : str
        
        
        """
    @staticmethod
    def GetRendererSettingsList(*args, **kwargs):
        """
        
        GetRendererSettingsList() -> UsdImagingGLRendererSettingsList
        
        
        Returns the list of renderer settings.
        
        
        
        """
    @staticmethod
    def InvokeRendererCommand(*args, **kwargs):
        """
        
        InvokeRendererCommand(command, args) -> bool
        
        
        Invokes command on the active render delegate.
        
        
        If successful, returns ``true`` , returns ``false`` otherwise. Note
        that the command will not succeeed if it is not among those returned
        by GetRendererCommandDescriptors() for the same active render
        delegate.
        
        
        Parameters
        ----------
        command : str
        
        args : HdCommandArgs
        
        
        """
    @staticmethod
    def IsColorCorrectionCapable(*args, **kwargs):
        """
        
        **classmethod** IsColorCorrectionCapable() -> bool
        
        
        Returns true if the platform is color correction capable.
        
        
        
        """
    @staticmethod
    def IsConverged(*args, **kwargs):
        """
        
        IsConverged() -> bool
        
        
        Returns true if the resulting image is fully converged.
        
        
        (otherwise, caller may need to call Render() again to refine the
        result)
        
        
        
        """
    @staticmethod
    def IsHydraEnabled(*args, **kwargs):
        """
        
        **classmethod** IsHydraEnabled() -> bool
        
        
        Returns true if Hydra is enabled for GL drawing.
        
        
        
        """
    @staticmethod
    def IsPauseRendererSupported(*args, **kwargs):
        """
        
        IsPauseRendererSupported() -> bool
        
        
        Query the renderer as to whether it supports pausing and resuming.
        
        
        
        """
    @staticmethod
    def IsStopRendererSupported(*args, **kwargs):
        """
        
        IsStopRendererSupported() -> bool
        
        
        Query the renderer as to whether it supports stopping and restarting.
        
        
        
        """
    @staticmethod
    def PauseRenderer(*args, **kwargs):
        """
        
        PauseRenderer() -> bool
        
        
        Pause the renderer.
        
        
        Returns ``true`` if successful.
        
        
        
        """
    @staticmethod
    def Render(*args, **kwargs):
        """
        
        Render(root, params) -> None
        
        
        Entry point for kicking off a render.
        
        
        Parameters
        ----------
        root : Prim
        
        params : RenderParams
        
        
        """
    @staticmethod
    def RestartRenderer(*args, **kwargs):
        """
        
        RestartRenderer() -> bool
        
        
        Restart the renderer.
        
        
        Returns ``true`` if successful.
        
        
        
        """
    @staticmethod
    def ResumeRenderer(*args, **kwargs):
        """
        
        ResumeRenderer() -> bool
        
        
        Resume the renderer.
        
        
        Returns ``true`` if successful.
        
        
        
        """
    @staticmethod
    def SetCameraPath(*args, **kwargs):
        """
        
        SetCameraPath(id) -> None
        
        
        Scene camera API Set the scene camera path to use for rendering.
        
        
        Parameters
        ----------
        id : Path
        
        
        """
    @staticmethod
    def SetCameraState(*args, **kwargs):
        """
        
        SetCameraState(viewMatrix, projectionMatrix) -> None
        
        
        Free camera API Set camera framing state directly (without pointing to
        a camera on the USD stage).
        
        
        The projection matrix is expected to be pre-adjusted for the window
        policy.
        
        
        Parameters
        ----------
        viewMatrix : Matrix4d
        
        projectionMatrix : Matrix4d
        
        
        """
    @staticmethod
    def SetColorCorrectionSettings(*args, **kwargs):
        """
        
        SetColorCorrectionSettings(ccType, ocioDisplay, ocioView, ocioColorSpace, ocioLook) -> None
        
        
        Set ``ccType`` to one of the HdxColorCorrectionTokens: {disabled,
        sRGB, openColorIO}.
        
        
        If'openColorIO'is used, ``ocioDisplay`` , ``ocioView`` ,
        ``ocioColorSpace`` and ``ocioLook`` are options the client may supply
        to configure OCIO. ``ocioColorSpace`` refers to the input (source)
        color space. The default value is substituted if an option isn't
        specified. You can find the values for these strings inside the
        profile/config .ocio file. For example:
        
        displays: rec709g22: !<View>{name: studio, colorspace: linear, looks:
        studio_65_lg2}
        
        
        Parameters
        ----------
        ccType : str
        
        ocioDisplay : str
        
        ocioView : str
        
        ocioColorSpace : str
        
        ocioLook : str
        
        
        """
    @staticmethod
    def SetFraming(*args, **kwargs):
        """
        
        SetFraming(framing) -> None
        
        
        Determines how the filmback of the camera is mapped into the pixels of
        the render buffer and what pixels of the render buffer will be
        rendered into.
        
        
        Parameters
        ----------
        framing : Framing
        
        
        """
    @staticmethod
    def SetLightingState(*args, **kwargs):
        """
        
        SetLightingState(src) -> None
        
        
        Copy lighting state from another lighting context.
        
        
        Parameters
        ----------
        src : GlfSimpleLightingContext
        
        
        
        ----------------------------------------------------------------------
        
        SetLightingState(lights, material, sceneAmbient) -> None
        
        
        Set lighting state Derived classes should ensure that passing an empty
        lights vector disables lighting.
        
        
        lights
        
        is the set of lights to use, or empty to disable lighting.
        
        
        Parameters
        ----------
        lights : list[SimpleLight]
        
        material : SimpleMaterial
        
        sceneAmbient : Vec4f
        
        
        """
    @staticmethod
    def SetOverrideWindowPolicy(*args, **kwargs):
        """
        
        SetOverrideWindowPolicy(policy) -> None
        
        
        Specifies whether to force a window policy when conforming the frustum
        of the camera to match the display window of the camera framing.
        
        
        If set to {false, \\.\\.\\.}, the window policy of the specified
        camera will be used.
        
        Note: std::pair<bool, \\.\\.\\.>is used instead of
        std::optional<\\.\\.\\.>because the latter is only available in C++17
        or later.
        
        
        Parameters
        ----------
        policy : tuple[bool, ConformWindowPolicy]
        
        
        """
    @staticmethod
    def SetRenderBufferSize(*args, **kwargs):
        """
        
        SetRenderBufferSize(size) -> None
        
        
        Set the size of the render buffers baking the AOVs.
        
        
        GUI applications should set this to the size of the window.
        
        
        Parameters
        ----------
        size : Vec2i
        
        
        """
    @staticmethod
    def SetRenderViewport(*args, **kwargs):
        """
        
        SetRenderViewport(viewport) -> None
        
        
        Set the viewport to use for rendering as (x,y,w,h), where (x,y)
        represents the lower left corner of the viewport rectangle, and (w,h)
        is the width and height of the viewport in pixels.
        
        
        Deprecated
        
        Use SetFraming and SetRenderBufferSize instead.
        
        
        Parameters
        ----------
        viewport : Vec4d
        
        
        """
    @staticmethod
    def SetRendererAov(*args, **kwargs):
        """
        
        SetRendererAov(id) -> bool
        
        
        Set the current renderer AOV to ``id`` .
        
        
        Parameters
        ----------
        id : str
        
        
        """
    @staticmethod
    def SetRendererPlugin(*args, **kwargs):
        """
        
        SetRendererPlugin(id) -> bool
        
        
        Set the current render-graph delegate to ``id`` .
        
        
        the plugin will be loaded if it's not yet.
        
        
        Parameters
        ----------
        id : str
        
        
        """
    @staticmethod
    def SetRendererSetting(*args, **kwargs):
        """
        
        SetRendererSetting(id, value) -> None
        
        
        Sets a renderer setting's value.
        
        
        Parameters
        ----------
        id : str
        
        value : VtValue
        
        
        """
    @staticmethod
    def SetSelected(*args, **kwargs):
        """
        
        SetSelected(paths) -> None
        
        
        Sets (replaces) the list of prim paths that should be included in
        selection highlighting.
        
        
        These paths may include root paths which will be expanded internally.
        
        
        Parameters
        ----------
        paths : list[Path]
        
        
        """
    @staticmethod
    def SetSelectionColor(*args, **kwargs):
        """
        
        SetSelectionColor(color) -> None
        
        
        Sets the selection highlighting color.
        
        
        Parameters
        ----------
        color : Vec4f
        
        
        """
    @staticmethod
    def SetWindowPolicy(*args, **kwargs):
        """
        
        SetWindowPolicy(policy) -> None
        
        
        Set the window policy to use.
        
        
        XXX: This is currently used for scene cameras set via SetCameraPath.
        See comment in SetCameraState for the free cam.
        
        
        Parameters
        ----------
        policy : ConformWindowPolicy
        
        
        """
    @staticmethod
    def StopRenderer(*args, **kwargs):
        """
        
        StopRenderer() -> bool
        
        
        Stop the renderer.
        
        
        Returns ``true`` if successful.
        
        
        
        """
    @staticmethod
    def TestIntersection(*args, **kwargs):
        """
        
        TestIntersection(viewMatrix, projectionMatrix, root, params, outHitPoint, outHitNormal, outHitPrimPath, outHitInstancerPath, outHitInstanceIndex, outInstancerContext) -> bool
        
        
        Finds closest point of intersection with a frustum by rendering.
        
        
        This method uses a PickRender and a customized depth buffer to find an
        approximate point of intersection by rendering. This is less accurate
        than implicit methods or rendering with GL_SELECT, but leverages any
        data already cached in the renderer.
        
        Returns whether a hit occurred and if so, ``outHitPoint`` will contain
        the intersection point in world space (i.e. ``projectionMatrix`` and
        ``viewMatrix`` factored back out of the result), and ``outHitNormal``
        will contain the world space normal at that point.
        
        ``outHitPrimPath`` will point to the gprim selected by the pick.
        ``outHitInstancerPath`` will point to the point instancer (if
        applicable) of that gprim. For nested instancing, outHitInstancerPath
        points to the closest instancer.
        
        
        Parameters
        ----------
        viewMatrix : Matrix4d
        
        projectionMatrix : Matrix4d
        
        root : Prim
        
        params : RenderParams
        
        outHitPoint : Vec3d
        
        outHitNormal : Vec3d
        
        outHitPrimPath : Path
        
        outHitInstancerPath : Path
        
        outHitInstanceIndex : int
        
        outInstancerContext : HdInstancerContext
        
        
        """
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(driver)
        
        
        A HdDriver, containing the Hgi of your choice, can be optionally
        passed in during construction.
        
        
        This can be helpful if you application creates multiple
        UsdImagingGLEngine that wish to use the same HdDriver / Hgi.
        
        
        Parameters
        ----------
        driver : HdDriver
        
        
        
        ----------------------------------------------------------------------
        
        __init__(rootPath, excludedPaths, invisedPaths, sceneDelegateID, driver)
        
        
        Parameters
        ----------
        rootPath : Path
        
        excludedPaths : list[Path]
        
        invisedPaths : list[Path]
        
        sceneDelegateID : Path
        
        driver : HdDriver
        
        
        
        ----------------------------------------------------------------------
        
        __init__(arg1)
        
        
        Parameters
        ----------
        arg1 : Engine
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class RenderParams(Boost.Python.instance):
    """
    Render parameters
    """
    __instance_size__: typing.ClassVar[int] = 232
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @property
    def applyRenderState(*args, **kwargs):
        ...
    @applyRenderState.setter
    def applyRenderState(*args, **kwargs):
        ...
    @property
    def bboxLineColor(*args, **kwargs):
        ...
    @bboxLineColor.setter
    def bboxLineColor(*args, **kwargs):
        ...
    @property
    def bboxLineDashSize(*args, **kwargs):
        ...
    @bboxLineDashSize.setter
    def bboxLineDashSize(*args, **kwargs):
        ...
    @property
    def bboxes(*args, **kwargs):
        ...
    @bboxes.setter
    def bboxes(*args, **kwargs):
        ...
    @property
    def clearColor(*args, **kwargs):
        ...
    @clearColor.setter
    def clearColor(*args, **kwargs):
        ...
    @property
    def clipPlanes(*args, **kwargs):
        ...
    @clipPlanes.setter
    def clipPlanes(*args, **kwargs):
        ...
    @property
    def colorCorrectionMode(*args, **kwargs):
        ...
    @colorCorrectionMode.setter
    def colorCorrectionMode(*args, **kwargs):
        ...
    @property
    def complexity(*args, **kwargs):
        ...
    @complexity.setter
    def complexity(*args, **kwargs):
        ...
    @property
    def cullStyle(*args, **kwargs):
        ...
    @cullStyle.setter
    def cullStyle(*args, **kwargs):
        ...
    @property
    def drawMode(*args, **kwargs):
        ...
    @drawMode.setter
    def drawMode(*args, **kwargs):
        ...
    @property
    def enableIdRender(*args, **kwargs):
        ...
    @enableIdRender.setter
    def enableIdRender(*args, **kwargs):
        ...
    @property
    def enableLighting(*args, **kwargs):
        ...
    @enableLighting.setter
    def enableLighting(*args, **kwargs):
        ...
    @property
    def enableSampleAlphaToCoverage(*args, **kwargs):
        ...
    @enableSampleAlphaToCoverage.setter
    def enableSampleAlphaToCoverage(*args, **kwargs):
        ...
    @property
    def enableSceneLights(*args, **kwargs):
        ...
    @enableSceneLights.setter
    def enableSceneLights(*args, **kwargs):
        ...
    @property
    def enableSceneMaterials(*args, **kwargs):
        ...
    @enableSceneMaterials.setter
    def enableSceneMaterials(*args, **kwargs):
        ...
    @property
    def enableUsdDrawModes(*args, **kwargs):
        ...
    @enableUsdDrawModes.setter
    def enableUsdDrawModes(*args, **kwargs):
        ...
    @property
    def forceRefresh(*args, **kwargs):
        ...
    @forceRefresh.setter
    def forceRefresh(*args, **kwargs):
        ...
    @property
    def frame(*args, **kwargs):
        ...
    @frame.setter
    def frame(*args, **kwargs):
        ...
    @property
    def gammaCorrectColors(*args, **kwargs):
        ...
    @gammaCorrectColors.setter
    def gammaCorrectColors(*args, **kwargs):
        ...
    @property
    def highlight(*args, **kwargs):
        ...
    @highlight.setter
    def highlight(*args, **kwargs):
        ...
    @property
    def ocioColorSpace(*args, **kwargs):
        ...
    @ocioColorSpace.setter
    def ocioColorSpace(*args, **kwargs):
        ...
    @property
    def ocioDisplay(*args, **kwargs):
        ...
    @ocioDisplay.setter
    def ocioDisplay(*args, **kwargs):
        ...
    @property
    def ocioLook(*args, **kwargs):
        ...
    @ocioLook.setter
    def ocioLook(*args, **kwargs):
        ...
    @property
    def ocioView(*args, **kwargs):
        ...
    @ocioView.setter
    def ocioView(*args, **kwargs):
        ...
    @property
    def overrideColor(*args, **kwargs):
        ...
    @overrideColor.setter
    def overrideColor(*args, **kwargs):
        ...
    @property
    def showGuides(*args, **kwargs):
        ...
    @showGuides.setter
    def showGuides(*args, **kwargs):
        ...
    @property
    def showProxy(*args, **kwargs):
        ...
    @showProxy.setter
    def showProxy(*args, **kwargs):
        ...
    @property
    def showRender(*args, **kwargs):
        ...
    @showRender.setter
    def showRender(*args, **kwargs):
        ...
    @property
    def wireframeColor(*args, **kwargs):
        ...
    @wireframeColor.setter
    def wireframeColor(*args, **kwargs):
        ...
class RendererCommandArgDescriptor(Boost.Python.instance):
    """
    Renderer Command Argument Metadata
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
    def argName(*args, **kwargs):
        ...
    @property
    def defaultValue(*args, **kwargs):
        ...
class RendererCommandDescriptor(Boost.Python.instance):
    """
    Renderer Command Metadata
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
    def commandArgs(*args, **kwargs):
        ...
    @property
    def commandDescription(*args, **kwargs):
        ...
    @property
    def commandName(*args, **kwargs):
        ...
class RendererSetting(Boost.Python.instance):
    """
    Renderer Setting Metadata
    """
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @property
    def defValue(*args, **kwargs):
        ...
    @property
    def key(*args, **kwargs):
        ...
    @property
    def name(*args, **kwargs):
        ...
    @property
    def type(*args, **kwargs):
        ...
class RendererSettingType(Boost.Python.enum):
    FLAG: typing.ClassVar[RendererSettingType]  # value = pxr.UsdImagingGL.RendererSettingType.FLAG
    FLOAT: typing.ClassVar[RendererSettingType]  # value = pxr.UsdImagingGL.RendererSettingType.FLOAT
    INT: typing.ClassVar[RendererSettingType]  # value = pxr.UsdImagingGL.RendererSettingType.INT
    STRING: typing.ClassVar[RendererSettingType]  # value = pxr.UsdImagingGL.RendererSettingType.STRING
    __slots__: typing.ClassVar[tuple] = tuple()
    names: typing.ClassVar[dict]  # value = {'FLAG': pxr.UsdImagingGL.RendererSettingType.FLAG, 'INT': pxr.UsdImagingGL.RendererSettingType.INT, 'FLOAT': pxr.UsdImagingGL.RendererSettingType.FLOAT, 'STRING': pxr.UsdImagingGL.RendererSettingType.STRING}
    values: typing.ClassVar[dict]  # value = {0: pxr.UsdImagingGL.RendererSettingType.FLAG, 1: pxr.UsdImagingGL.RendererSettingType.INT, 2: pxr.UsdImagingGL.RendererSettingType.FLOAT, 3: pxr.UsdImagingGL.RendererSettingType.STRING}
ALL_INSTANCES: int = -1
__MFB_FULL_PACKAGE_NAME: str = 'usdImagingGL'
