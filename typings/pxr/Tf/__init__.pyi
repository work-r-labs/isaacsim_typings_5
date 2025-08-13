"""

Tf -- Tools Foundation
"""
from __future__ import annotations
import typing
__all__: list[str] = ['CallContext', 'CppException', 'Debug', 'DiagnosticType', 'Enum', 'Error', 'ErrorException', 'Fatal', 'GetCodeLocation', 'MallocTag', 'NamedTemporaryFile', 'Notice', 'PrepareModule', 'PreparePythonModule', 'PyModuleWasLoaded', 'RaiseCodingError', 'RaiseRuntimeError', 'RefPtrTracker', 'ScopeDescription', 'ScriptModuleLoader', 'Singleton', 'Status', 'StatusObject', 'Stopwatch', 'TF_APPLICATION_EXIT_TYPE', 'TF_DIAGNOSTIC_CODING_ERROR_TYPE', 'TF_DIAGNOSTIC_FATAL_CODING_ERROR_TYPE', 'TF_DIAGNOSTIC_FATAL_ERROR_TYPE', 'TF_DIAGNOSTIC_NONFATAL_ERROR_TYPE', 'TF_DIAGNOSTIC_RUNTIME_ERROR_TYPE', 'TF_DIAGNOSTIC_STATUS_TYPE', 'TF_DIAGNOSTIC_WARNING_TYPE', 'TemplateString', 'Tf_PyEnumWrapper', 'Tf_TestAnnotatedBoolResult', 'Tf_TestPyContainerConversions', 'Tf_TestPyOptionalBoost', 'Tf_TestPyOptionalStd', 'Type', 'Warn', 'Warning', 'WindowsImportWrapper']
class CallContext(Boost.Python.instance):
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
    def file(*args, **kwargs):
        ...
    @property
    def function(*args, **kwargs):
        ...
    @property
    def line(*args, **kwargs):
        ...
    @property
    def prettyFunction(*args, **kwargs):
        ...
class CppException(Exception):
    pass
class Debug(Boost.Python.instance):
    @staticmethod
    def GetDebugSymbolDescription(*args, **kwargs):
        ...
    @staticmethod
    def GetDebugSymbolDescriptions(*args, **kwargs):
        ...
    @staticmethod
    def GetDebugSymbolNames(*args, **kwargs):
        ...
    @staticmethod
    def IsDebugSymbolNameEnabled(*args, **kwargs):
        ...
    @staticmethod
    def SetDebugSymbolsByName(*args, **kwargs):
        ...
    @staticmethod
    def SetOutputFile(*args, **kwargs):
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
class DiagnosticType(Tf_PyEnumWrapper):
    _baseName: typing.ClassVar[str] = ''
    allValues: typing.ClassVar[tuple]  # value = (Tf.TF_DIAGNOSTIC_CODING_ERROR_TYPE, Tf.TF_DIAGNOSTIC_FATAL_CODING_ERROR_TYPE, Tf.TF_DIAGNOSTIC_RUNTIME_ERROR_TYPE, Tf.TF_DIAGNOSTIC_FATAL_ERROR_TYPE, Tf.TF_DIAGNOSTIC_NONFATAL_ERROR_TYPE, Tf.TF_DIAGNOSTIC_WARNING_TYPE, Tf.TF_DIAGNOSTIC_STATUS_TYPE, Tf.TF_APPLICATION_EXIT_TYPE)
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
class Enum(Boost.Python.instance):
    @staticmethod
    def GetValueFromFullName(*args, **kwargs):
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
class Error(_DiagnosticBase):
    class Mark(Boost.Python.instance):
        __instance_size__: typing.ClassVar[int] = 32
        @staticmethod
        def Clear(*args, **kwargs):
            ...
        @staticmethod
        def GetErrors(*args, **kwargs):
            """
            
            
            A list of the errors held by this mark.
            """
        @staticmethod
        def IsClean(*args, **kwargs):
            ...
        @staticmethod
        def SetMark(*args, **kwargs):
            ...
        @staticmethod
        def __init__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
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
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def errorCode(*args, **kwargs):
        """
        The error code posted for this error.
        """
    @property
    def errorCodeString(*args, **kwargs):
        """
        The error code posted for this error, as a string.
        """
class ErrorException(RuntimeError):
    def __init__(self, *args):
        ...
    def __str__(self):
        ...
class MallocTag(Boost.Python.instance):
    class CallTree(Boost.Python.instance):
        class CallSite(Boost.Python.instance):
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
            def nBytes(*args, **kwargs):
                ...
            @property
            def name(*args, **kwargs):
                ...
        class PathNode(Boost.Python.instance):
            @staticmethod
            def GetChildren(*args, **kwargs):
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
            @property
            def nAllocations(*args, **kwargs):
                ...
            @property
            def nBytes(*args, **kwargs):
                ...
            @property
            def nBytesDirect(*args, **kwargs):
                ...
            @property
            def siteName(*args, **kwargs):
                ...
        @staticmethod
        def GetCallSites(*args, **kwargs):
            ...
        @staticmethod
        def GetPrettyPrintString(*args, **kwargs):
            ...
        @staticmethod
        def GetRoot(*args, **kwargs):
            ...
        @staticmethod
        def LogReport(*args, **kwargs):
            ...
        @staticmethod
        def Report(*args, **kwargs):
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
    @staticmethod
    def GetCallStacks(*args, **kwargs):
        ...
    @staticmethod
    def GetCallTree(*args, **kwargs):
        ...
    @staticmethod
    def GetMaxTotalBytes(*args, **kwargs):
        ...
    @staticmethod
    def GetTotalBytes(*args, **kwargs):
        ...
    @staticmethod
    def Initialize(*args, **kwargs):
        ...
    @staticmethod
    def IsInitialized(*args, **kwargs):
        ...
    @staticmethod
    def SetCapturedMallocStacksMatchList(*args, **kwargs):
        ...
    @staticmethod
    def SetDebugMatchList(*args, **kwargs):
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
class NamedTemporaryFile:
    """
    A named temporary file which keeps the internal file handle closed. 
           A class which constructs a temporary file(that isn't open) on __enter__,
           provides its name as an attribute, and deletes it on __exit__. 
           
           Note: The constructor args for this object match those of 
           python's tempfile.mkstemp() function, and will have the same effect on
           the underlying file created.
    """
    def __enter__(self):
        ...
    def __exit__(self, *args):
        ...
    def __init__(self, suffix = '', prefix = '', dir = None, text = False):
        ...
    @property
    def name(self):
        """
        The path for the temporary file created.
        """
class Notice(Boost.Python.instance):
    class Listener(Boost.Python.instance):
        """
        Represents the Notice connection between senders and receivers of notices.  When a Listener object expires the connection is broken. You can also use the Revoke() function to break the connection. A Listener object is returned from the Register() and  RegisterGlobally() functions. 
        """
        @staticmethod
        def Revoke(*args, **kwargs):
            """
            
            
            Revoke() 
            
            Revoke interest by a notice listener.  This function revokes interest in the particular notice type and call-back method that its Listener object was registered for. 
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
    @staticmethod
    def Register(*args, **kwargs):
        """
        
        
        Register( noticeType, callback, sender ) -> Listener 
        
        noticeType : Tf.Notice
        callback : function
        sender : object
        
        Register a listener as being interested in a TfNotice  type from a specific sender.  Notice listener will get sender  as an argument.     Registration of interest in a notice class N automatically  registers interest in all classes derived from N.  When a  notice of appropriate type is received, the listening object's  member-function method is called with the notice.     To reverse the registration, call Revoke() on the Listener object returned by this call. 
        
        Register( noticeType, callback, sender ) -> Listener 
        
        noticeType : Tf.Notice
        callback : function
        sender : object
        
        Register a listener as being interested in a TfNotice  type from a specific sender.  Notice listener will get sender  as an argument.     Registration of interest in a notice class N automatically  registers interest in all classes derived from N.  When a  notice of appropriate type is received, the listening object's  member-function method is called with the notice.     To reverse the registration, call Revoke() on the Listener object returned by this call. 
        """
    @staticmethod
    def RegisterGlobally(*args, **kwargs):
        """
        
        
        RegisterGlobally( noticeType, callback ) -> Listener 
        
        noticeType : Tf.Notice
        callback : function
        
        Register a listener as being interested in a TfNotice type from any sender.  The notice listener does not get sender as an argument. 
        """
    @staticmethod
    def Send(*args, **kwargs):
        """
        
        
        Send(sender) 
        
        sender : object 
        
        Deliver the notice to interested listeners, returning the number of interested listeners. This is the recommended form of Send.  It takes the sender as an argument. Listeners that registered for the given sender AND listeners that registered globally will get the notice. 
        
        Send(sender) 
        
        sender : object 
        
        Deliver the notice to interested listeners, returning the number of interested listeners. This is the recommended form of Send.  It takes the sender as an argument. Listeners that registered for the given sender AND listeners that registered globally will get the notice. 
        """
    @staticmethod
    def SendGlobally(*args, **kwargs):
        """
        
        
        SendGlobally() 
        
        Deliver the notice to interested listeners.   For most clients it is recommended to use the Send(sender) version of Send() rather than this one.  Clients that use this form of Send will prevent listeners from being able to register to receive notices based on the sender of the notice. ONLY listeners that registered globally will get the notice. 
        """
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class PyModuleWasLoaded(Notice):
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def name(*args, **kwargs):
        ...
class RefPtrTracker(Boost.Python.instance):
    @staticmethod
    def GetAllTracesReport(*args, **kwargs):
        ...
    @staticmethod
    def GetAllWatchedCountsReport(*args, **kwargs):
        ...
    @staticmethod
    def GetTracesReportForWatched(*args, **kwargs):
        ...
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
        ...
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
    def __new__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @property
    def expired(*args, **kwargs):
        """
        True if this object has expired, False otherwise.
        """
class ScopeDescription(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 64
    @staticmethod
    def SetDescription(*args, **kwargs):
        ...
    @staticmethod
    def __enter__(*args, **kwargs):
        ...
    @staticmethod
    def __exit__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class ScriptModuleLoader(Boost.Python.instance):
    @staticmethod
    def GetModuleNames(*args, **kwargs):
        ...
    @staticmethod
    def GetModulesDict(*args, **kwargs):
        ...
    @staticmethod
    def WriteDotFile(*args, **kwargs):
        ...
    @staticmethod
    def _LoadModulesForLibrary(*args, **kwargs):
        ...
    @staticmethod
    def _RegisterLibrary(*args, **kwargs):
        ...
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
        ...
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
    def __new__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @property
    def expired(*args, **kwargs):
        """
        True if this object has expired, False otherwise.
        """
class Singleton(Boost.Python.instance):
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __new__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class StatusObject(_DiagnosticBase):
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class Stopwatch(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def AddFrom(*args, **kwargs):
        ...
    @staticmethod
    def Reset(*args, **kwargs):
        ...
    @staticmethod
    def Start(*args, **kwargs):
        ...
    @staticmethod
    def Stop(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @property
    def microseconds(*args, **kwargs):
        ...
    @property
    def milliseconds(*args, **kwargs):
        ...
    @property
    def nanoseconds(*args, **kwargs):
        ...
    @property
    def sampleCount(*args, **kwargs):
        ...
    @property
    def seconds(*args, **kwargs):
        ...
class TemplateString(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def GetEmptyMapping(*args, **kwargs):
        ...
    @staticmethod
    def GetParseErrors(*args, **kwargs):
        ...
    @staticmethod
    def SafeSubstitute(*args, **kwargs):
        ...
    @staticmethod
    def Substitute(*args, **kwargs):
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
    @property
    def template(*args, **kwargs):
        ...
    @property
    def valid(*args, **kwargs):
        ...
class Tf_PyEnumWrapper(Enum):
    @staticmethod
    def __and__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __ge__(*args, **kwargs):
        ...
    @staticmethod
    def __gt__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __invert__(*args, **kwargs):
        ...
    @staticmethod
    def __le__(*args, **kwargs):
        ...
    @staticmethod
    def __lt__(*args, **kwargs):
        ...
    @staticmethod
    def __or__(*args, **kwargs):
        ...
    @staticmethod
    def __rand__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __ror__(*args, **kwargs):
        ...
    @staticmethod
    def __rxor__(*args, **kwargs):
        ...
    @staticmethod
    def __xor__(*args, **kwargs):
        ...
    @property
    def displayName(*args, **kwargs):
        ...
    @property
    def fullName(*args, **kwargs):
        ...
    @property
    def name(*args, **kwargs):
        ...
    @property
    def value(*args, **kwargs):
        ...
class Tf_TestAnnotatedBoolResult(Boost.Python.instance):
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
    def annotation(*args, **kwargs):
        ...
class Tf_TestPyContainerConversions(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 32
    @staticmethod
    def GetPairTimesTwo(*args, **kwargs):
        ...
    @staticmethod
    def GetTokens(*args, **kwargs):
        ...
    @staticmethod
    def GetVectorTimesTwo(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class Tf_TestPyOptionalBoost(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 32
    @staticmethod
    def TakesOptional(*args, **kwargs):
        ...
    @staticmethod
    def TestOptionalChar(*args, **kwargs):
        ...
    @staticmethod
    def TestOptionalDouble(*args, **kwargs):
        ...
    @staticmethod
    def TestOptionalFloat(*args, **kwargs):
        ...
    @staticmethod
    def TestOptionalInt(*args, **kwargs):
        ...
    @staticmethod
    def TestOptionalLong(*args, **kwargs):
        ...
    @staticmethod
    def TestOptionalShort(*args, **kwargs):
        ...
    @staticmethod
    def TestOptionalString(*args, **kwargs):
        ...
    @staticmethod
    def TestOptionalStringVector(*args, **kwargs):
        ...
    @staticmethod
    def TestOptionalUChar(*args, **kwargs):
        ...
    @staticmethod
    def TestOptionalUInt(*args, **kwargs):
        ...
    @staticmethod
    def TestOptionalULong(*args, **kwargs):
        ...
    @staticmethod
    def TestOptionalUShort(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class Tf_TestPyOptionalStd(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 32
    @staticmethod
    def TakesOptional(*args, **kwargs):
        ...
    @staticmethod
    def TestOptionalChar(*args, **kwargs):
        ...
    @staticmethod
    def TestOptionalDouble(*args, **kwargs):
        ...
    @staticmethod
    def TestOptionalFloat(*args, **kwargs):
        ...
    @staticmethod
    def TestOptionalInt(*args, **kwargs):
        ...
    @staticmethod
    def TestOptionalLong(*args, **kwargs):
        ...
    @staticmethod
    def TestOptionalShort(*args, **kwargs):
        ...
    @staticmethod
    def TestOptionalString(*args, **kwargs):
        ...
    @staticmethod
    def TestOptionalStringVector(*args, **kwargs):
        ...
    @staticmethod
    def TestOptionalUChar(*args, **kwargs):
        ...
    @staticmethod
    def TestOptionalUInt(*args, **kwargs):
        ...
    @staticmethod
    def TestOptionalULong(*args, **kwargs):
        ...
    @staticmethod
    def TestOptionalUShort(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class Type(Boost.Python.instance):
    Unknown: typing.ClassVar[Type]  # value = Tf.Type.Unknown
    __instance_size__: typing.ClassVar[int] = 32
    @staticmethod
    def AddAlias(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Find(*args, **kwargs):
        ...
    @staticmethod
    def FindByName(*args, **kwargs):
        ...
    @staticmethod
    def FindDerivedByName(*args, **kwargs):
        ...
    @staticmethod
    def GetAliases(*args, **kwargs):
        ...
    @staticmethod
    def GetAllAncestorTypes(*args, **kwargs):
        ...
    @staticmethod
    def GetAllDerivedTypes(*args, **kwargs):
        ...
    @staticmethod
    def GetRoot(*args, **kwargs):
        ...
    @staticmethod
    def IsA(*args, **kwargs):
        ...
    @staticmethod
    def _DumpTypeHierarchy(*args, **kwargs):
        """
        
        
        _DumpTypeHierarchy(TfType): Diagnostic method to print the type hierarchy beneath a given TfType.
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __ge__(*args, **kwargs):
        ...
    @staticmethod
    def __gt__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __le__(*args, **kwargs):
        ...
    @staticmethod
    def __lt__(*args, **kwargs):
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
    def baseTypes(*args, **kwargs):
        ...
    @property
    def derivedTypes(*args, **kwargs):
        ...
    @property
    def isEnumType(*args, **kwargs):
        ...
    @property
    def isPlainOldDataType(*args, **kwargs):
        ...
    @property
    def isUnknown(*args, **kwargs):
        ...
    @property
    def pythonClass(*args, **kwargs):
        ...
    @property
    def sizeof(*args, **kwargs):
        ...
    @property
    def typeName(*args, **kwargs):
        ...
class Warning(_DiagnosticBase):
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class WindowsImportWrapper:
    def __enter__(self):
        ...
    def __exit__(self, exc_type, ex_val, exc_tb):
        ...
class _ClassWithClassMethod(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 32
    @staticmethod
    def Test(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class _ClassWithVarArgInit(Boost.Python.instance):
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
        ...
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
    def allowExtraArgs(*args, **kwargs):
        ...
    @property
    def args(*args, **kwargs):
        ...
    @property
    def expired(*args, **kwargs):
        """
        True if this object has expired, False otherwise.
        """
    @property
    def kwargs(*args, **kwargs):
        ...
class _DiagnosticBase(Boost.Python.instance):
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
        """
        The commentary string describing this error.
        """
    @property
    def diagnosticCode(*args, **kwargs):
        """
        The diagnostic code posted.
        """
    @property
    def diagnosticCodeString(*args, **kwargs):
        """
        The error code posted for this error, as a string.
        """
    @property
    def sourceFileName(*args, **kwargs):
        """
        The source file name that the error was posted from.
        """
    @property
    def sourceFunction(*args, **kwargs):
        """
        The source function that the error was posted from.
        """
    @property
    def sourceLineNumber(*args, **kwargs):
        """
        The source line number that the error was posted from.
        """
class _Enum(Boost.Python.instance):
    class TestEnum2(Tf_PyEnumWrapper):
        _baseName: typing.ClassVar[str] = '_Enum'
        allValues: typing.ClassVar[tuple]  # value = (Tf._Enum.One, Tf._Enum.Two, Tf._Enum.Three)
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
    class TestKeywords(Tf_PyEnumWrapper):
        False_: typing.ClassVar[TestKeywords]  # value = Tf._Enum.TestKeywords.False_
        None_: typing.ClassVar[TestKeywords]  # value = Tf._Enum.TestKeywords.None_
        True_: typing.ClassVar[TestKeywords]  # value = Tf._Enum.TestKeywords.True_
        _baseName: typing.ClassVar[str] = '_Enum.TestKeywords'
        allValues: typing.ClassVar[tuple]  # value = (Tf._Enum.TestKeywords.None_, Tf._Enum.TestKeywords.False_, Tf._Enum.TestKeywords.True_, Tf._Enum.TestKeywords.print_, Tf._Enum.TestKeywords.import_, Tf._Enum.TestKeywords.global_)
        global_: typing.ClassVar[TestKeywords]  # value = Tf._Enum.TestKeywords.global_
        import_: typing.ClassVar[TestKeywords]  # value = Tf._Enum.TestKeywords.import_
        print_: typing.ClassVar[TestKeywords]  # value = Tf._Enum.TestKeywords.print_
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
    class TestScopedEnum(Tf_PyEnumWrapper):
        Alef: typing.ClassVar[TestScopedEnum]  # value = Tf._Enum.TestScopedEnum.Alef
        Bet: typing.ClassVar[TestScopedEnum]  # value = Tf._Enum.TestScopedEnum.Bet
        Gimel: typing.ClassVar[TestScopedEnum]  # value = Tf._Enum.TestScopedEnum.Gimel
        _baseName: typing.ClassVar[str] = '_Enum.TestScopedEnum'
        allValues: typing.ClassVar[tuple]  # value = (Tf._Enum.TestScopedEnum.Alef, Tf._Enum.TestScopedEnum.Bet, Tf._Enum.TestScopedEnum.Gimel)
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
    One: typing.ClassVar[TestEnum2]  # value = Tf._Enum.One
    Three: typing.ClassVar[TestEnum2]  # value = Tf._Enum.Three
    Two: typing.ClassVar[TestEnum2]  # value = Tf._Enum.Two
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class _TestBase(Boost.Python.instance):
    @staticmethod
    def TestCallVirtual(*args, **kwargs):
        ...
    @staticmethod
    def Virtual(*args, **kwargs):
        ...
    @staticmethod
    def Virtual2(*args, **kwargs):
        ...
    @staticmethod
    def Virtual3(*args, **kwargs):
        ...
    @staticmethod
    def Virtual4(*args, **kwargs):
        ...
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
        ...
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
class _TestDerived(_TestBase):
    @staticmethod
    def Virtual(*args, **kwargs):
        ...
    @staticmethod
    def Virtual2(*args, **kwargs):
        ...
    @staticmethod
    def Virtual3(*args, **kwargs):
        ...
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
        ...
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
class _TestEnum(Tf_PyEnumWrapper):
    _baseName: typing.ClassVar[str] = ''
    allValues: typing.ClassVar[tuple]  # value = (Tf._Alpha, Tf._Bravo, Tf._Charlie, Tf._Delta)
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
class _TestScopedEnum(Tf_PyEnumWrapper):
    Beryllium: typing.ClassVar[_TestScopedEnum]  # value = Tf._TestScopedEnum.Beryllium
    Boron: typing.ClassVar[_TestScopedEnum]  # value = Tf._TestScopedEnum.Boron
    Hydrogen: typing.ClassVar[_TestScopedEnum]  # value = Tf._TestScopedEnum.Hydrogen
    Lithium: typing.ClassVar[_TestScopedEnum]  # value = Tf._TestScopedEnum.Lithium
    _baseName: typing.ClassVar[str] = '_TestScopedEnum'
    allValues: typing.ClassVar[tuple]  # value = (Tf._TestScopedEnum.Hydrogen, Tf._TestScopedEnum.Lithium, Tf._TestScopedEnum.Beryllium, Tf._TestScopedEnum.Boron)
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
class _TestStaticMethodError(Boost.Python.instance):
    @staticmethod
    def Error(*args, **kwargs):
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
class _TestStaticTokens(Boost.Python.instance):
    orange: typing.ClassVar[str] = 'orange'
    pear: typing.ClassVar[str] = "d'Anjou"
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class _testStaticTokens(Boost.Python.instance):
    orange: typing.ClassVar[str] = 'orange'
    pear: typing.ClassVar[str] = "d'Anjou"
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
def Fatal(msg):
    """
    Raise a fatal error to the Tf Diagnostic system.
    """
def GetCodeLocation(framesUp):
    """
    Returns a tuple (moduleName, functionName, fileName, lineNo).
    
        To trace the current location of python execution, use GetCodeLocation().
        By default, the information is returned at the current stack-frame; thus
    
            info = GetCodeLocation()
    
        will return information about the line that GetCodeLocation() was called 
        from. One can write:
    
            def genericDebugFacility():
                info = GetCodeLocation(1)
                # print out data
    
    
            def someCode():
                ...
                if bad:
                    genericDebugFacility()
    
        and genericDebugFacility() will get information associated with its caller, 
        i.e. the function someCode().
    """
def PrepareModule(module, result):
    """
    PrepareModule(module, result) -- Prepare an extension module at import
        time.  Generally, this should only be called by the __init__.py script for a
        module upon loading a boost python module (generally '_libName.so').
    """
def PreparePythonModule(moduleName = None):
    """
    Prepare an extension module at import time.  This will import the
        Python module associated with the caller's module (e.g. '_tf' for 'pxr.Tf')
        or the module with the specified moduleName and copy its contents into
        the caller's local namespace.
    
        Generally, this should only be called by the __init__.py script for a module
        upon loading a boost python module (generally '_libName.so').
    """
def RaiseCodingError(msg):
    """
    Raise a coding error to the Tf Diagnostic system.
    """
def RaiseRuntimeError(msg):
    """
    Raise a runtime error to the Tf Diagnostic system.
    """
def Status(msg, verbose = True):
    """
    Issues a status update to the Tf diagnostic system.
    
        If verbose is True (the default) then information about where in the code
        the status update was issued from is included.
        
    """
def Warn(msg, template = ''):
    """
    Issue a warning via the TfDiagnostic system.
    
        At this time, template is ignored.
        
    """
TF_APPLICATION_EXIT_TYPE: DiagnosticType  # value = Tf.TF_APPLICATION_EXIT_TYPE
TF_DIAGNOSTIC_CODING_ERROR_TYPE: DiagnosticType  # value = Tf.TF_DIAGNOSTIC_CODING_ERROR_TYPE
TF_DIAGNOSTIC_FATAL_CODING_ERROR_TYPE: DiagnosticType  # value = Tf.TF_DIAGNOSTIC_FATAL_CODING_ERROR_TYPE
TF_DIAGNOSTIC_FATAL_ERROR_TYPE: DiagnosticType  # value = Tf.TF_DIAGNOSTIC_FATAL_ERROR_TYPE
TF_DIAGNOSTIC_NONFATAL_ERROR_TYPE: DiagnosticType  # value = Tf.TF_DIAGNOSTIC_NONFATAL_ERROR_TYPE
TF_DIAGNOSTIC_RUNTIME_ERROR_TYPE: DiagnosticType  # value = Tf.TF_DIAGNOSTIC_RUNTIME_ERROR_TYPE
TF_DIAGNOSTIC_STATUS_TYPE: DiagnosticType  # value = Tf.TF_DIAGNOSTIC_STATUS_TYPE
TF_DIAGNOSTIC_WARNING_TYPE: DiagnosticType  # value = Tf.TF_DIAGNOSTIC_WARNING_TYPE
_Alpha: _TestEnum  # value = Tf._Alpha
_Bravo: _TestEnum  # value = Tf._Bravo
_Charlie: _TestEnum  # value = Tf._Charlie
_Delta: _TestEnum  # value = Tf._Delta
__MFB_FULL_PACKAGE_NAME: str = 'tf'
