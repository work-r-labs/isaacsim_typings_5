from __future__ import annotations
from pxr.UsdUtils.complianceChecker import ComplianceChecker
from pxr.UsdUtils.fixBrokenPixarSchemas import FixBrokenPixarSchemas
from pxr.UsdUtils.updateSchemaWithSdrNode import PropertyDefiningKeys
from pxr.UsdUtils.updateSchemaWithSdrNode import SchemaDefiningKeys
from pxr.UsdUtils.updateSchemaWithSdrNode import SchemaDefiningMiscConstants
from pxr.UsdUtils.updateSchemaWithSdrNode import UpdateSchemaWithSdrNode
from pxr.UsdUtils.usdzUtils import CheckUsdzCompliance
from pxr.UsdUtils.usdzUtils import CreateUsdzPackage
from pxr.UsdUtils.usdzUtils import ExtractUsdzPackage
from pxr.UsdUtils.usdzUtils import UsdzAssetIterator
import typing
from . import complianceChecker
from . import constantsGroup
from . import fixBrokenPixarSchemas
from . import updateSchemaWithSdrNode
from . import usdzUtils
__all__ = ['CheckUsdzCompliance', 'CoalescingDiagnosticDelegate', 'CoalescingDiagnosticDelegateItem', 'CoalescingDiagnosticDelegateSharedItem', 'CoalescingDiagnosticDelegateUnsharedItem', 'ComplianceChecker', 'ConditionalAbortDiagnosticDelegate', 'ConditionalAbortDiagnosticDelegateErrorFilters', 'CreateUsdzPackage', 'ExtractUsdzPackage', 'FixBrokenPixarSchemas', 'PropertyDefiningKeys', 'RegisteredVariantSet', 'SchemaDefiningKeys', 'SchemaDefiningMiscConstants', 'SparseAttrValueWriter', 'SparseValueWriter', 'StageCache', 'TimeCodeRange', 'UpdateSchemaWithSdrNode', 'UsdStageStatsKeys', 'UsdzAssetIterator', 'complianceChecker', 'constantsGroup', 'fixBrokenPixarSchemas', 'updateSchemaWithSdrNode', 'usdzUtils']
class CoalescingDiagnosticDelegate(Boost.Python.instance):
    """
    
    A class which collects warnings and statuses from the Tf diagnostic
    manager system in a thread safe manner.
    
    
    This class allows clients to get both the unfiltered results, as well
    as a compressed view which deduplicates diagnostic events by their
    source line number, function and file from which they occurred.
    
    """
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def DumpCoalescedDiagnosticsToStderr(*args, **kwargs):
        ...
    @staticmethod
    def DumpCoalescedDiagnosticsToStdout(*args, **kwargs):
        ...
    @staticmethod
    def DumpUncoalescedDiagnostics(*args, **kwargs):
        """
        
        DumpUncoalescedDiagnostics(ostr) -> None
        
        
        Print all pending diagnostics without any coalescing to ``ostr`` .
        
        
        
        This method clears the pending diagnostics.
        
        
        Parameters
        ----------
        ostr : ostream
        
        
        """
    @staticmethod
    def TakeCoalescedDiagnostics(*args, **kwargs):
        """
        
        TakeCoalescedDiagnostics() -> list[CoalescingDiagnosticDelegate]
        
        
        Get all pending diagnostics in a coalesced form.
        
        
        
        This method clears the pending diagnostics.
        
        
        
        """
    @staticmethod
    def TakeUncoalescedDiagnostics(*args, **kwargs):
        """
        
        TakeUncoalescedDiagnostics() -> list[TfDiagnosticBase]
        
        
        Get all pending diagnostics without any coalescing.
        
        
        
        This method clears the pending diagnostics.
        
        
        
        """
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class CoalescingDiagnosticDelegateItem(Boost.Python.instance):
    """
    
    An item used in coalesced results, containing a shared component: the
    file/function/line number, and a set of unshared components: the call
    context and commentary.
    
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
    def sharedItem(*args, **kwargs):
        ...
    @property
    def unsharedItems(*args, **kwargs):
        ...
class CoalescingDiagnosticDelegateSharedItem(Boost.Python.instance):
    """
    
    The shared component in a coalesced result This type can be thought of
    as the key by which we coalesce our diagnostics.
    
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
    def sourceFileName(*args, **kwargs):
        ...
    @property
    def sourceFunction(*args, **kwargs):
        ...
    @property
    def sourceLineNumber(*args, **kwargs):
        ...
class CoalescingDiagnosticDelegateUnsharedItem(Boost.Python.instance):
    """
    
    The unshared component in a coalesced result.
    
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
    def commentary(*args, **kwargs):
        ...
    @property
    def context(*args, **kwargs):
        ...
class ConditionalAbortDiagnosticDelegate(Boost.Python.instance):
    """
    
    A class that allows client application to instantiate a diagnostic
    delegate that can be used to abort operations for a non fatal USD
    error or warning based on immutable include exclude rules defined for
    this instance.
    
    
    These rules are regex strings where case sensitive matching is done on
    error/warning text or the location of the code path where the
    error/warning occured. Note that these rules will be respected only
    during the lifetime of the delegate. Include Rules determine what
    errors or warnings will cause a fatal abort. Exclude Rules determine
    what errors or warnings matched from the Include Rules should not
    cause the fatal abort. Example: to abort on all errors and warnings
    coming from"\\*pxr\\*"codepath but not
    from"\\*ConditionalAbortDiagnosticDelegate\\*", a client can create
    the following delegate:
    
    .. code-block:: text
    
      UsdUtilsConditionalAbortDiagnosticDelegateErrorFilters includeFilters;
      UsdUtilsConditionalAbortDiagnosticDelegateErrorFilters excludeFilters;
      includeFilters.SetCodePathFilters({"\\*pxr\\*"});
      excludeFilters.SetCodePathFilters({"\\*ConditionalAbortDiagnosticDelegate\\*"});
      UsdUtilsConditionalAbortDiagnosticDelegate delegate = 
          UsdUtilsConditionalAbortDiagnosticDelegate(includeFilters,
              excludeFilters);
    
    
    """
    __instance_size__: typing.ClassVar[int] = 120
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(includeFilters, excludeFilters)
        
        
        Constructor to initialize conditionalAbortDiagnosticDelegate.
        
        
        Responsible for adding this delegate instance to TfDiagnosticMgr and
        also sets the ``includeFilters`` and ``excludeFilters``
        
        The _includeFilters and _excludeFilters are immutable
        
        
        Parameters
        ----------
        includeFilters : ConditionalAbortDiagnosticDelegateErrorFilters
        
        excludeFilters : ConditionalAbortDiagnosticDelegateErrorFilters
        
        
        
        ----------------------------------------------------------------------
        
        __init__()
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(delegate)
        
        
        Parameters
        ----------
        delegate : ConditionalAbortDiagnosticDelegate
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class ConditionalAbortDiagnosticDelegateErrorFilters(Boost.Python.instance):
    """
    
    A class which represents the inclusion exclusion filters on which
    errors will be matched stringFilters: matching and filtering will be
    done on explicit string of the error/warning codePathFilters: matching
    and filtering will be done on errors/warnings coming from a specific
    usd code path.
    
    """
    __instance_size__: typing.ClassVar[int] = 64
    @staticmethod
    def GetCodePathFilters(*args, **kwargs):
        """
        
        GetCodePathFilters() -> list[str]
        
        
        
        """
    @staticmethod
    def GetStringFilters(*args, **kwargs):
        """
        
        GetStringFilters() -> list[str]
        
        
        
        """
    @staticmethod
    def SetCodePathFilters(*args, **kwargs):
        """
        
        SetCodePathFilters(codePathFilters) -> None
        
        
        Parameters
        ----------
        codePathFilters : list[str]
        
        
        """
    @staticmethod
    def SetStringFilters(*args, **kwargs):
        """
        
        SetStringFilters(stringFilters) -> None
        
        
        Parameters
        ----------
        stringFilters : list[str]
        
        
        """
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(stringFilters, codePathFilters)
        
        
        Parameters
        ----------
        stringFilters : list[str]
        
        codePathFilters : list[str]
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class RegisteredVariantSet(Boost.Python.instance):
    """
    Info for registered variant set
    """
    class SelectionExportPolicy(Boost.Python.enum):
        """
        
        This specifies how the variantSet should be treated during export.
        
        
        Note, in the plugInfo.json, the values for these enum's are
        lowerCamelCase.
        
        """
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
    """
    
    A utility class for authoring time-varying attribute values with
    simple run-length encoding, by skipping any redundant time-samples.
    Time-samples that are close enough to each other, with relative
    difference smaller than a fixed epsilon value are considered to be
    equivalent. This is to avoid unnecessary authoring of time-samples
    caused by numerical fuzz in certain computations.
    
    For vectors, matrices, and other composite types (like quaternions and
    arrays), each component is compared with the corresponding component
    for closeness. The chosen epsilon value for double precision floating
    point numbers is 1e-12. For single-precision, it is 1e-6 and for half-
    precision, it is 1e-2.
    
    Example c++ usage:
    
    .. code-block:: text
    
      UsdGeomSphere sphere = UsdGeomSphere::Define(stage, SdfPath("/Sphere"));
      UsdAttribute radius = sphere.CreateRadiusAttr();
      UsdUtilsSparseAttrValueWriter attrValueWriter(radius, 
              /\\*defaultValue\\*/ VtValue(1.0));
      attrValueWriter.SetTimeSample(VtValue(10.0), UsdTimeCode(1.0));
      attrValueWriter.SetTimeSample(VtValue(10.0), UsdTimeCode(2.0));
      attrValueWriter.SetTimeSample(VtValue(10.0), UsdTimeCode(3.0));
      attrValueWriter.SetTimeSample(VtValue(20.0), UsdTimeCode(4.0));
    
    Equivalent python example:
    
    .. code-block:: text
    
      sphere = UsdGeom.Sphere.Define(stage, Sdf.Path("/Sphere"))
      radius = sphere.CreateRadiusAttr()
      attrValueWriter = UsdUtils.SparseAttrValueWriter(radius, defaultValue=1.0)
      attrValueWriter.SetTimeSample(10.0, 1.0)
      attrValueWriter.SetTimeSample(10.0, 2.0)
      attrValueWriter.SetTimeSample(10.0, 3.0)
      attrValueWriter.SetTimeSample(20.0, 4.0)
    
    In the above examples, the specified default value of radius (1.0)
    will not be authored into scene description since it matches the
    fallback value. Additionally, the time-sample authored at time=2.0
    will be skipped since it is redundant. Also note that for correct
    behavior, the calls to SetTimeSample() must be made with sequentially
    increasing time values. If not, a coding error is issued and the
    authored animation may be incorrect.
    
    """
    @staticmethod
    def SetTimeSample(*args, **kwargs):
        """
        
        SetTimeSample(value, time) -> bool
        
        
        Sets a new time-sample on the attribute with given ``value`` at the
        given ``time`` .
        
        
        The time-sample is only authored if it's different from the previously
        set time-sample, in which case the previous time-sample is also
        authored, in order to to end the previous run of contiguous identical
        values and start a new run.
        
        This incurs a copy of ``value`` . Also, the value will be held in
        memory at least until the next time-sample is written or until the
        SparseAttrValueWriter instance is destroyed.
        
        
        Parameters
        ----------
        value : VtValue
        
        time : TimeCode
        
        
        
        ----------------------------------------------------------------------
        
        SetTimeSample(value, time) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        For efficiency, this function swaps out the given ``value`` , leaving
        it empty.
        
        
        The value will be held in memory at least until the next time-sample
        is written or until the SparseAttrValueWriter instance is destroyed.
        
        
        Parameters
        ----------
        value : VtValue
        
        time : TimeCode
        
        
        """
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(attr, defaultValue)
        
        
        The constructor initializes the data required for run-length encoding
        of time-samples.
        
        
        It also sets the default value of ``attr`` to ``defaultValue`` , if
        ``defaultValue`` is non-empty and different from the existing default
        value of ``attr`` .
        
        ``defaultValue`` can be unspecified (or left empty) if you don't care
        about authoring a default value. In this case, the sparse authoring
        logic is initialized with the existing authored default value or the
        fallback value, if ``attr`` has one.
        
        
        Parameters
        ----------
        attr : Attribute
        
        defaultValue : VtValue
        
        
        
        ----------------------------------------------------------------------
        
        __init__(attr, defaultValue)
        
        
        The constructor initializes the data required for run-length encoding
        of time-samples.
        
        
        It also sets the default value of ``attr`` to ``defaultValue`` , if
        ``defaultValue`` is non-empty and different from the existing default
        value of ``attr`` .
        
        It ``defaultValue`` is null or points to an empty VtValue, the sparse
        authoring logic is initialized with the existing authored default
        value or the fallback value, if ``attr`` has one.
        
        For efficiency, this function swaps out the given ``defaultValue`` ,
        leaving it empty.
        
        
        Parameters
        ----------
        attr : Attribute
        
        defaultValue : VtValue
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class SparseValueWriter(Boost.Python.instance):
    """
    
    Utility class that manages sparse authoring of a set of UsdAttributes.
    It does this by maintaining a map of UsdAttributes to their
    corresponding UsdUtilsSparseAttrValueWriter objects.
    
    To use this class, simply instantiate an instance of it and invoke the
    SetAttribute() method with various attributes and their associated
    time-samples.
    
    If the attribute has a default value, SetAttribute() must be called
    with time=Default first (multiple times, if necessary), followed by
    calls to author time-samples in sequentially increasing time order.
    
    This class is not threadsafe. In general, authoring to a single USD
    layer from multiple threads isn't threadsafe. Hence, there is little
    value in making this class threadsafe. Example c++ usage:
    
    .. code-block:: text
    
      UsdGeomCylinder cylinder = UsdGeomCylinder::Define(stage, SdfPath("/Cylinder"));
      UsdAttribute radius = cylinder.CreateRadiusAttr();
      UsdAttribute height = cylinder.CreateHeightAttr();
      UsdUtilsSparseValueWriter valueWriter;
      valueWriter.SetAttribute(radius, 2.0, UsdTimeCode::Default());
      valueWriter.SetAttribute(height, 2.0, UsdTimeCode::Default());
      
      valueWriter.SetAttribute(radius, 10.0, UsdTimeCode(1.0));
      valueWriter.SetAttribute(radius, 20.0, UsdTimeCode(2.0));
      valueWriter.SetAttribute(radius, 20.0, UsdTimeCode(3.0));
      valueWriter.SetAttribute(radius, 20.0, UsdTimeCode(4.0));
      
      valueWriter.SetAttribute(height, 2.0, UsdTimeCode(1.0));
      valueWriter.SetAttribute(height, 2.0, UsdTimeCode(2.0));
      valueWriter.SetAttribute(height, 3.0, UsdTimeCode(3.0));
      valueWriter.SetAttribute(height, 3.0, UsdTimeCode(4.0));
    
    Equivalent python code:
    
    .. code-block:: text
    
      cylinder = UsdGeom.Cylinder.Define(stage, Sdf.Path("/Cylinder"))
      radius = cylinder.CreateRadiusAttr()
      height = cylinder.CreateHeightAttr()
      valueWriter = UsdUtils.SparseValueWriter()
      valueWriter.SetAttribute(radius, 2.0, Usd.TimeCode.Default())
      valueWriter.SetAttribute(height, 2.0, Usd.TimeCode.Default())
      
      valueWriter.SetAttribute(radius, 10.0, 1.0)
      valueWriter.SetAttribute(radius, 20.0, 2.0)
      valueWriter.SetAttribute(radius, 20.0, 3.0)
      valueWriter.SetAttribute(radius, 20.0, 4.0)
      
      valueWriter.SetAttribute(height, 2.0, 1.0)
      valueWriter.SetAttribute(height, 2.0, 2.0)
      valueWriter.SetAttribute(height, 3.0, 3.0)
      valueWriter.SetAttribute(height, 3.0, 4.0)
    
    In the above example,
    
       - The default value of the"height"attribute is not authored into
         scene description since it matches the fallback value.
    
       - Time-samples at time=3.0 and time=4.0 will be skipped for the
         radius attribute.
    
       - For the"height"attribute, the first timesample at time=1.0 will
         be skipped since it matches the default value.
    
       - The last time-sample at time=4.0 will also be skipped
         for"height"since it matches the previously written value at time=3.0.
    
    
    """
    __instance_size__: typing.ClassVar[int] = 72
    @staticmethod
    def GetSparseAttrValueWriters(*args, **kwargs):
        """
        
        GetSparseAttrValueWriters() -> list[SparseAttrValueWriter]
        
        
        Returns a new vector of UsdUtilsSparseAttrValueWriter populated from
        the attrValueWriter map.
        
        
        
        """
    @staticmethod
    def SetAttribute(*args, **kwargs):
        """
        
        SetAttribute(attr, value, time) -> bool
        
        
        Sets the value of ``attr`` to ``value`` at time ``time`` .
        
        
        The value is written sparsely, i.e., the default value is authored
        only if it is different from the fallback value or the existing
        default value, and any redundant time-samples are skipped when the
        attribute value does not change significantly between consecutive
        time-samples.
        
        
        Parameters
        ----------
        attr : Attribute
        
        value : VtValue
        
        time : TimeCode
        
        
        
        ----------------------------------------------------------------------
        
        SetAttribute(attr, value, time) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        For efficiency, this function swaps out the given ``value`` , leaving
        it empty.
        
        
        The value will be held in memory at least until the next time-sample
        is written or until the SparseAttrValueWriter instance is destroyed.
        
        
        Parameters
        ----------
        attr : Attribute
        
        value : VtValue
        
        time : TimeCode
        
        
        
        ----------------------------------------------------------------------
        
        SetAttribute(attr, value, time) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        attr : Attribute
        
        value : T
        
        time : TimeCode
        
        
        """
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class StageCache(Boost.Python.instance):
    """
    
    The UsdUtilsStageCache class provides a simple interface for handling
    a singleton usd stage cache for use by all USD clients. This way code
    from any location can make use of the same cache to maximize stage
    reuse.
    
    """
    __instance_size__: typing.ClassVar[int] = 24
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get() -> StageCache
        
        
        Returns the singleton stage cache.
        
        
        
        """
    @staticmethod
    def GetSessionLayerForVariantSelections(*args, **kwargs):
        """
        
        **classmethod** GetSessionLayerForVariantSelections(modelName, variantSelections) -> Layer
        
        
        Given variant selections as a vector of pairs (vector in case order
        matters to the client), constructs a session layer with overs on the
        given root modelName with the variant selections, or returns a cached
        session layer with those opinions.
        
        
        Parameters
        ----------
        modelName : str
        
        variantSelections : list[tuple[str, str]]
        
        
        """
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class TimeCodeRange(Boost.Python.instance):
    """
    
    Represents a range of UsdTimeCode values as start and end time codes
    and a stride value.
    
    A UsdUtilsTimeCodeRange can be iterated to retrieve all time code
    values in the range. The range may be empty, it may contain a single
    time code, or it may represent multiple time codes from start to end.
    The interval defined by the start and end time codes is closed on both
    ends.
    
    Note that when constructing a UsdUtilsTimeCodeRange,
    UsdTimeCode::EarliestTime() and UsdTimeCode::Default() cannot be used
    as the start or end time codes. Also, the end time code cannot be less
    than the start time code for positive stride values, and the end time
    code cannot be greater than the start time code for negative stride
    values. Finally, the stride value cannot be zero. If any of these
    conditions are not satisfied, then an invalid empty range will be
    returned.
    
    """
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
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateFromFrameSpec(*args, **kwargs):
        """
        
        **classmethod** CreateFromFrameSpec(frameSpec) -> TimeCodeRange
        
        
        Create a time code range from ``frameSpec`` .
        
        
        A FrameSpec is a compact string representation of a time code range. A
        FrameSpec may contain up to three floating point values for the start
        time code, end time code, and stride values of a time code range.
        
        A FrameSpec containing just a single floating point value represents a
        time code range containing only that time code.
        
        A FrameSpec containing two floating point values separated by the
        range separator (':') represents a time code range from the first
        value as the start time code to the second values as the end time
        code.
        
        A FrameSpec that specifies both a start and end time code value may
        also optionally specify a third floating point value as the stride,
        separating it from the first two values using the stride separator
        ('x').
        
        The following are examples of valid FrameSpecs: 123 101:105 105:101
        101:109x2 101:110x2 101:104x0.5
        
        An empty string corresponds to an invalid empty time code range.
        
        A coding error will be issued if the given string is malformed.
        
        
        Parameters
        ----------
        frameSpec : str
        
        
        """
    @staticmethod
    def IsValid(*args, **kwargs):
        """
        
        IsValid() -> bool
        
        
        Return true if this range contains one or more time codes, or false
        otherwise.
        
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        Construct an invalid empty range.
        
        
        The start time code will be initialized to zero, and any iteration of
        the range will yield no time codes.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(timeCode)
        
        
        Construct a range containing only the given ``timeCode`` .
        
        
        An iteration of the range will yield only that time code.
        
        
        Parameters
        ----------
        timeCode : TimeCode
        
        
        
        ----------------------------------------------------------------------
        
        __init__(startTimeCode, endTimeCode)
        
        
        Construct a range containing the time codes from ``startTimeCode`` to
        ``endTimeCode`` .
        
        
        If ``endTimeCode`` is greater than or equal to ``startTimeCode`` ,
        then the stride will be 1.0. Otherwise, the stride will be -1.0.
        
        
        Parameters
        ----------
        startTimeCode : TimeCode
        
        endTimeCode : TimeCode
        
        
        
        ----------------------------------------------------------------------
        
        __init__(startTimeCode, endTimeCode, stride)
        
        
        Construct a range containing the time codes from ``startTimeCode`` to
        ``endTimeCode`` using the stride value ``stride`` .
        
        
        UsdTimeCode::EarliestTime() and UsdTimeCode::Default() cannot be used
        as ``startTimeCode`` or ``endTimeCode`` . If ``stride`` is a positive
        value, then ``endTimeCode`` cannot be less than ``startTimeCode`` . If
        ``stride`` is a negative value, then ``endTimeCode`` cannot be greater
        than ``startTimeCode`` . Finally, the stride value cannot be zero. If
        any of these conditions are not satisfied, then a coding error will be
        issued and an invalid empty range will be returned.
        
        
        Parameters
        ----------
        startTimeCode : TimeCode
        
        endTimeCode : TimeCode
        
        stride : float
        
        
        """
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
        """
        
        empty() -> bool
        
        
        Return true if this range contains no time codes, or false otherwise.
        
        
        
        """
    @property
    def endTimeCode(*args, **kwargs):
        """
        type : TimeCode
        
        
        Return the end time code of this range.
        """
    @property
    def frameSpec(*args, **kwargs):
        ...
    @property
    def startTimeCode(*args, **kwargs):
        """
        type : TimeCode
        
        
        Return the start time code of this range.
        """
    @property
    def stride(*args, **kwargs):
        """
        type : float
        
        
        Return the stride value of this range.
        """
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
