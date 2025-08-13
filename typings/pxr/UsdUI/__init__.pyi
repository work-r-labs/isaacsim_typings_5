from __future__ import annotations
import pxr.Usd
import typing
__all__: list[str] = ['Backdrop', 'NodeGraphNodeAPI', 'SceneGraphPrimAPI', 'Tokens']
class Backdrop(pxr.Usd.Typed):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateDescriptionAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetDescriptionAttr(*args, **kwargs):
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
class NodeGraphNodeAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateDisplayColorAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateExpansionStateAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateIconAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreatePosAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSizeAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateStackingOrderAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetDisplayColorAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetExpansionStateAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetIconAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetPosAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetSizeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetStackingOrderAttr(*args, **kwargs):
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
class SceneGraphPrimAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateDisplayGroupAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateDisplayNameAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetDisplayGroupAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetDisplayNameAttr(*args, **kwargs):
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
    Backdrop: typing.ClassVar[str] = 'Backdrop'
    NodeGraphNodeAPI: typing.ClassVar[str] = 'NodeGraphNodeAPI'
    SceneGraphPrimAPI: typing.ClassVar[str] = 'SceneGraphPrimAPI'
    closed: typing.ClassVar[str] = 'closed'
    minimized: typing.ClassVar[str] = 'minimized'
    open: typing.ClassVar[str] = 'open'
    uiDescription: typing.ClassVar[str] = 'ui:description'
    uiDisplayGroup: typing.ClassVar[str] = 'ui:displayGroup'
    uiDisplayName: typing.ClassVar[str] = 'ui:displayName'
    uiNodegraphNodeDisplayColor: typing.ClassVar[str] = 'ui:nodegraph:node:displayColor'
    uiNodegraphNodeExpansionState: typing.ClassVar[str] = 'ui:nodegraph:node:expansionState'
    uiNodegraphNodeIcon: typing.ClassVar[str] = 'ui:nodegraph:node:icon'
    uiNodegraphNodePos: typing.ClassVar[str] = 'ui:nodegraph:node:pos'
    uiNodegraphNodeSize: typing.ClassVar[str] = 'ui:nodegraph:node:size'
    uiNodegraphNodeStackingOrder: typing.ClassVar[str] = 'ui:nodegraph:node:stackingOrder'
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
__MFB_FULL_PACKAGE_NAME: str = 'usdUI'
