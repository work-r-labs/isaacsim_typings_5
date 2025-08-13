from __future__ import annotations
import pxr.Usd
import pxr.UsdGeom
import typing
__all__: list[str] = ['AssetPreviewsAPI', 'SpatialAudio', 'Tokens']
class AssetPreviewsAPI(pxr.Usd.APISchemaBase):
    class Thumbnails(Boost.Python.instance):
        __instance_size__: typing.ClassVar[int] = 88
        @staticmethod
        def __init__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
        @staticmethod
        def __repr__(*args, **kwargs):
            ...
        @property
        def defaultImage(*args, **kwargs):
            ...
        @defaultImage.setter
        def defaultImage(*args, **kwargs):
            ...
    __instance_size__: typing.ClassVar[int] = 64
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def ClearDefaultThumbnails(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAssetDefaultPreviews(*args, **kwargs):
        ...
    @staticmethod
    def GetDefaultThumbnails(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def SetDefaultThumbnails(*args, **kwargs):
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
class SpatialAudio(pxr.UsdGeom.Xformable):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateAuralModeAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateEndTimeAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateFilePathAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateGainAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMediaOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreatePlaybackModeAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateStartTimeAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAuralModeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetEndTimeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetFilePathAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetGainAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMediaOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetPlaybackModeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetStartTimeAttr(*args, **kwargs):
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
    AssetPreviewsAPI: typing.ClassVar[str] = 'AssetPreviewsAPI'
    SpatialAudio: typing.ClassVar[str] = 'SpatialAudio'
    auralMode: typing.ClassVar[str] = 'auralMode'
    defaultImage: typing.ClassVar[str] = 'defaultImage'
    endTime: typing.ClassVar[str] = 'endTime'
    filePath: typing.ClassVar[str] = 'filePath'
    gain: typing.ClassVar[str] = 'gain'
    loopFromStage: typing.ClassVar[str] = 'loopFromStage'
    loopFromStart: typing.ClassVar[str] = 'loopFromStart'
    loopFromStartToEnd: typing.ClassVar[str] = 'loopFromStartToEnd'
    mediaOffset: typing.ClassVar[str] = 'mediaOffset'
    nonSpatial: typing.ClassVar[str] = 'nonSpatial'
    onceFromStart: typing.ClassVar[str] = 'onceFromStart'
    onceFromStartToEnd: typing.ClassVar[str] = 'onceFromStartToEnd'
    playbackMode: typing.ClassVar[str] = 'playbackMode'
    previewThumbnails: typing.ClassVar[str] = 'previews:thumbnails'
    previewThumbnailsDefault: typing.ClassVar[str] = 'previews:thumbnails:default'
    previews: typing.ClassVar[str] = 'previews'
    spatial: typing.ClassVar[str] = 'spatial'
    startTime: typing.ClassVar[str] = 'startTime'
    thumbnails: typing.ClassVar[str] = 'thumbnails'
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
__MFB_FULL_PACKAGE_NAME: str = 'usdMedia'
