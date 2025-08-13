from __future__ import annotations
import typing
__all__: list[str] = ['ALL_INSTANCES', 'CullStyle', 'DrawMode', 'Engine', 'RenderParams', 'RendererCommandArgDescriptor', 'RendererCommandDescriptor', 'RendererSetting', 'RendererSettingType']
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
    class Parameters(Boost.Python.instance):
        """
        Parameters to construct renderer engine
        """
        __instance_size__: typing.ClassVar[int] = 128
        @staticmethod
        def __init__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
        @property
        def allowAsynchronousSceneProcessing(*args, **kwargs):
            ...
        @allowAsynchronousSceneProcessing.setter
        def allowAsynchronousSceneProcessing(*args, **kwargs):
            ...
        @property
        def driver(*args, **kwargs):
            ...
        @driver.setter
        def driver(*args, **kwargs):
            ...
        @property
        def excludedPaths(*args, **kwargs):
            ...
        @excludedPaths.setter
        def excludedPaths(*args, **kwargs):
            ...
        @property
        def gpuEnabled(*args, **kwargs):
            ...
        @gpuEnabled.setter
        def gpuEnabled(*args, **kwargs):
            ...
        @property
        def invisedPaths(*args, **kwargs):
            ...
        @invisedPaths.setter
        def invisedPaths(*args, **kwargs):
            ...
        @property
        def rendererPluginId(*args, **kwargs):
            ...
        @rendererPluginId.setter
        def rendererPluginId(*args, **kwargs):
            ...
        @property
        def rootPath(*args, **kwargs):
            ...
        @rootPath.setter
        def rootPath(*args, **kwargs):
            ...
        @property
        def sceneDelegateID(*args, **kwargs):
            ...
        @sceneDelegateID.setter
        def sceneDelegateID(*args, **kwargs):
            ...
    __instance_size__: typing.ClassVar[int] = 536
    @staticmethod
    def AddSelected(*args, **kwargs):
        ...
    @staticmethod
    def ClearSelected(*args, **kwargs):
        ...
    @staticmethod
    def GetAvailableRenderSettingsPrimPaths(*args, **kwargs):
        ...
    @staticmethod
    def GetCurrentRendererId(*args, **kwargs):
        ...
    @staticmethod
    def GetRenderStats(*args, **kwargs):
        ...
    @staticmethod
    def GetRendererAovs(*args, **kwargs):
        ...
    @staticmethod
    def GetRendererCommandDescriptors(*args, **kwargs):
        ...
    @staticmethod
    def GetRendererDisplayName(*args, **kwargs):
        ...
    @staticmethod
    def GetRendererPlugins(*args, **kwargs):
        ...
    @staticmethod
    def GetRendererSetting(*args, **kwargs):
        ...
    @staticmethod
    def GetRendererSettingsList(*args, **kwargs):
        ...
    @staticmethod
    def InvokeRendererCommand(*args, **kwargs):
        ...
    @staticmethod
    def IsColorCorrectionCapable(*args, **kwargs):
        ...
    @staticmethod
    def IsConverged(*args, **kwargs):
        ...
    @staticmethod
    def IsPauseRendererSupported(*args, **kwargs):
        ...
    @staticmethod
    def IsStopRendererSupported(*args, **kwargs):
        ...
    @staticmethod
    def PauseRenderer(*args, **kwargs):
        ...
    @staticmethod
    def PollForAsynchronousUpdates(*args, **kwargs):
        ...
    @staticmethod
    def Render(*args, **kwargs):
        ...
    @staticmethod
    def RestartRenderer(*args, **kwargs):
        ...
    @staticmethod
    def ResumeRenderer(*args, **kwargs):
        ...
    @staticmethod
    def SetActiveRenderSettingsPrimPath(*args, **kwargs):
        ...
    @staticmethod
    def SetCameraPath(*args, **kwargs):
        ...
    @staticmethod
    def SetCameraState(*args, **kwargs):
        ...
    @staticmethod
    def SetColorCorrectionSettings(*args, **kwargs):
        ...
    @staticmethod
    def SetFraming(*args, **kwargs):
        ...
    @staticmethod
    def SetLightingState(*args, **kwargs):
        ...
    @staticmethod
    def SetOverrideWindowPolicy(*args, **kwargs):
        ...
    @staticmethod
    def SetRenderBufferSize(*args, **kwargs):
        ...
    @staticmethod
    def SetRenderViewport(*args, **kwargs):
        ...
    @staticmethod
    def SetRendererAov(*args, **kwargs):
        ...
    @staticmethod
    def SetRendererPlugin(*args, **kwargs):
        ...
    @staticmethod
    def SetRendererSetting(*args, **kwargs):
        ...
    @staticmethod
    def SetSelected(*args, **kwargs):
        ...
    @staticmethod
    def SetSelectionColor(*args, **kwargs):
        ...
    @staticmethod
    def SetWindowPolicy(*args, **kwargs):
        ...
    @staticmethod
    def StopRenderer(*args, **kwargs):
        ...
    @staticmethod
    def TestIntersection(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class RenderParams(Boost.Python.instance):
    """
    Render parameters
    """
    __instance_size__: typing.ClassVar[int] = 240
    @staticmethod
    def __init__(*args, **kwargs):
        ...
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
    __instance_size__: typing.ClassVar[int] = 88
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
