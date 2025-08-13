from __future__ import annotations
from pxr.UsdUtils.complianceChecker import ComplianceChecker
from pxr.UsdUtils.fixBrokenPixarSchemas import FixBrokenPixarSchemas
from pxr.UsdUtils.updateSchemaWithSdrNode import PropertyDefiningKeys
from pxr.UsdUtils.updateSchemaWithSdrNode import SchemaDefiningKeys
from pxr.UsdUtils.updateSchemaWithSdrNode import SchemaDefiningMiscConstants
from pxr.UsdUtils.updateSchemaWithSdrNode import UpdateSchemaWithSdrNode
from pxr.UsdUtils.usdzUtils import ExtractUsdzPackage
from pxr.UsdUtils.usdzUtils import UsdzAssetIterator
import typing
from . import complianceChecker
from . import constantsGroup
from . import fixBrokenPixarSchemas
from . import updateSchemaWithSdrNode
from . import usdzUtils
__all__: list[str] = ['CoalescingDiagnosticDelegate', 'CoalescingDiagnosticDelegateItem', 'CoalescingDiagnosticDelegateSharedItem', 'CoalescingDiagnosticDelegateUnsharedItem', 'ComplianceChecker', 'ConditionalAbortDiagnosticDelegate', 'ConditionalAbortDiagnosticDelegateErrorFilters', 'DependencyInfo', 'ExtractUsdzPackage', 'FixBrokenPixarSchemas', 'PropertyDefiningKeys', 'RegisteredVariantSet', 'SchemaDefiningKeys', 'SchemaDefiningMiscConstants', 'SparseAttrValueWriter', 'SparseValueWriter', 'StageCache', 'TimeCodeRange', 'UpdateSchemaWithSdrNode', 'UsdStageStatsKeys', 'UsdzAssetIterator', 'complianceChecker', 'constantsGroup', 'fixBrokenPixarSchemas', 'updateSchemaWithSdrNode', 'usdzUtils']
class CoalescingDiagnosticDelegate(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def DumpCoalescedDiagnosticsToStderr(*args, **kwargs):
        ...
    @staticmethod
    def DumpCoalescedDiagnosticsToStdout(*args, **kwargs):
        ...
    @staticmethod
    def DumpUncoalescedDiagnostics(*args, **kwargs):
        ...
    @staticmethod
    def TakeCoalescedDiagnostics(*args, **kwargs):
        ...
    @staticmethod
    def TakeUncoalescedDiagnostics(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class CoalescingDiagnosticDelegateItem(Boost.Python.instance):
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
    def sharedItem(*args, **kwargs):
        ...
    @property
    def unsharedItems(*args, **kwargs):
        ...
class CoalescingDiagnosticDelegateSharedItem(Boost.Python.instance):
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
    def sourceFileName(*args, **kwargs):
        ...
    @property
    def sourceFunction(*args, **kwargs):
        ...
    @property
    def sourceLineNumber(*args, **kwargs):
        ...
class CoalescingDiagnosticDelegateUnsharedItem(Boost.Python.instance):
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
    def commentary(*args, **kwargs):
        ...
    @property
    def context(*args, **kwargs):
        ...
class ConditionalAbortDiagnosticDelegate(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 128
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class ConditionalAbortDiagnosticDelegateErrorFilters(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 72
    @staticmethod
    def GetCodePathFilters(*args, **kwargs):
        ...
    @staticmethod
    def GetStringFilters(*args, **kwargs):
        ...
    @staticmethod
    def SetCodePathFilters(*args, **kwargs):
        ...
    @staticmethod
    def SetStringFilters(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class DependencyInfo(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 80
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @property
    def assetPath(*args, **kwargs):
        ...
    @property
    def dependencies(*args, **kwargs):
        ...
class RegisteredVariantSet(Boost.Python.instance):
    """
    Info for registered variant set
    """
    class SelectionExportPolicy(Boost.Python.enum):
        Always: typing.ClassVar[SelectionExportPolicy]  # value = pxr.UsdUtils.SelectionExportPolicy.Always
        IfAuthored: typing.ClassVar[SelectionExportPolicy]  # value = pxr.UsdUtils.SelectionExportPolicy.IfAuthored
        Never: typing.ClassVar[SelectionExportPolicy]  # value = pxr.UsdUtils.SelectionExportPolicy.Never
        __slots__: typing.ClassVar[tuple] = tuple()
        names: typing.ClassVar[dict]  # value = {'IfAuthored': pxr.UsdUtils.SelectionExportPolicy.IfAuthored, 'Always': pxr.UsdUtils.SelectionExportPolicy.Always, 'Never': pxr.UsdUtils.SelectionExportPolicy.Never}
        values: typing.ClassVar[dict]  # value = {1: pxr.UsdUtils.SelectionExportPolicy.IfAuthored, 2: pxr.UsdUtils.SelectionExportPolicy.Always, 0: pxr.UsdUtils.SelectionExportPolicy.Never}
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
    def name(*args, **kwargs):
        ...
    @property
    def selectionExportPolicy(*args, **kwargs):
        ...
class SparseAttrValueWriter(Boost.Python.instance):
    @staticmethod
    def SetTimeSample(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class SparseValueWriter(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 80
    @staticmethod
    def GetSparseAttrValueWriters(*args, **kwargs):
        ...
    @staticmethod
    def SetAttribute(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class StageCache(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 32
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetSessionLayerForVariantSelections(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class TimeCodeRange(Boost.Python.instance):
    class Tokens(Boost.Python.instance):
        EmptyTimeCodeRange: typing.ClassVar[str] = 'NONE'
        RangeSeparator: typing.ClassVar[str] = ':'
        StrideSeparator: typing.ClassVar[str] = 'x'
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    class _Iterator(Boost.Python.instance):
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __iter__(*args, **kwargs):
            ...
        @staticmethod
        def __next__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateFromFrameSpec(*args, **kwargs):
        ...
    @staticmethod
    def IsValid(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __iter__(*args, **kwargs):
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
    @staticmethod
    def empty(*args, **kwargs):
        ...
    @property
    def endTimeCode(*args, **kwargs):
        ...
    @property
    def frameSpec(*args, **kwargs):
        ...
    @property
    def startTimeCode(*args, **kwargs):
        ...
    @property
    def stride(*args, **kwargs):
        ...
class UsdStageStatsKeys(Boost.Python.instance):
    activePrimCount: typing.ClassVar[str] = 'activePrimCount'
    approxMemoryInMb: typing.ClassVar[str] = 'approxMemoryInMb'
    assetCount: typing.ClassVar[str] = 'assetCount'
    inactivePrimCount: typing.ClassVar[str] = 'inactivePrimCount'
    instanceCount: typing.ClassVar[str] = 'instanceCount'
    instancedModelCount: typing.ClassVar[str] = 'instancedModelCount'
    modelCount: typing.ClassVar[str] = 'modelCount'
    primCounts: typing.ClassVar[str] = 'primCounts'
    primCountsByType: typing.ClassVar[str] = 'primCountsByType'
    primary: typing.ClassVar[str] = 'primary'
    prototypeCount: typing.ClassVar[str] = 'prototypeCount'
    prototypes: typing.ClassVar[str] = 'prototypes'
    pureOverCount: typing.ClassVar[str] = 'pureOverCount'
    totalInstanceCount: typing.ClassVar[str] = 'totalInstanceCount'
    totalPrimCount: typing.ClassVar[str] = 'totalPrimCount'
    untyped: typing.ClassVar[str] = 'untyped'
    usedLayerCount: typing.ClassVar[str] = 'usedLayerCount'
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
__MFB_FULL_PACKAGE_NAME: str = 'usdUtils'
