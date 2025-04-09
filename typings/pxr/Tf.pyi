"""

Tf -- Tools Foundation
"""
from __future__ import annotations
import typing
__all__ = ['CallContext', 'CppException', 'Debug', 'DiagnosticType', 'Enum', 'Error', 'ErrorException', 'Fatal', 'GetCodeLocation', 'MallocTag', 'NamedTemporaryFile', 'Notice', 'PrepareModule', 'PreparePythonModule', 'PyModuleWasLoaded', 'RaiseCodingError', 'RaiseRuntimeError', 'RefPtrTracker', 'ScopeDescription', 'ScriptModuleLoader', 'Singleton', 'Status', 'StatusObject', 'Stopwatch', 'TF_APPLICATION_EXIT_TYPE', 'TF_DIAGNOSTIC_CODING_ERROR_TYPE', 'TF_DIAGNOSTIC_FATAL_CODING_ERROR_TYPE', 'TF_DIAGNOSTIC_FATAL_ERROR_TYPE', 'TF_DIAGNOSTIC_NONFATAL_ERROR_TYPE', 'TF_DIAGNOSTIC_RUNTIME_ERROR_TYPE', 'TF_DIAGNOSTIC_STATUS_TYPE', 'TF_DIAGNOSTIC_WARNING_TYPE', 'TemplateString', 'Tf_PyEnumWrapper', 'Tf_TestAnnotatedBoolResult', 'Tf_TestPyContainerConversions', 'Tf_TestPyOptional', 'Type', 'Warn', 'Warning', 'WindowsImportWrapper']
class CallContext(Boost.Python.instance):
    """
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
    def file(*args, **kwargs):
        """
        type : char
        """
    @property
    def function(*args, **kwargs):
        """
        type : char
        """
    @property
    def line(*args, **kwargs):
        """
        type : int
        """
    @property
    def prettyFunction(*args, **kwargs):
        """
        type : char
        """
class CppException(Exception):
    pass
class Debug(Boost.Python.instance):
    """
    """
    @staticmethod
    def GetDebugSymbolDescription(*args, **kwargs):
        """
        
        **classmethod** GetDebugSymbolDescription(name) -> str
        
        
        Get a description for the specified debug symbol.
        
        
        A short description of the debug symbol is returned. This is the same
        description string that is embedded in the return value of
        GetDebugSymbolDescriptions.
        
        
        Parameters
        ----------
        name : str
        
        
        """
    @staticmethod
    def GetDebugSymbolDescriptions(*args, **kwargs):
        """
        
        **classmethod** GetDebugSymbolDescriptions() -> str
        
        
        Get a description of all debug symbols and their purpose.
        
        
        A single string describing all registered debug symbols along with
        short descriptions is returned.
        
        
        
        """
    @staticmethod
    def GetDebugSymbolNames(*args, **kwargs):
        """
        
        **classmethod** GetDebugSymbolNames() -> list[str]
        
        
        Get a listing of all debug symbols.
        
        
        
        """
    @staticmethod
    def IsDebugSymbolNameEnabled(*args, **kwargs):
        """
        
        **classmethod** IsDebugSymbolNameEnabled(name) -> bool
        
        
        True if the specified debug symbol is set.
        
        
        Parameters
        ----------
        name : str
        
        
        """
    @staticmethod
    def SetDebugSymbolsByName(*args, **kwargs):
        """
        
        **classmethod** SetDebugSymbolsByName(pattern, value) -> list[str]
        
        
        Set registered debug symbols matching ``pattern`` to ``value`` .
        
        
        All registered debug symbols matching ``pattern`` are set to ``value``
        . The only matching is an exact match with ``pattern`` , or if
        ``pattern`` ends with an'\\*'as is otherwise a prefix of a debug
        symbols. The names of all debug symbols set by this call are returned
        as a vector.
        
        
        Parameters
        ----------
        pattern : str
        
        value : bool
        
        
        """
    @staticmethod
    def SetOutputFile(*args, **kwargs):
        """
        
        **classmethod** SetOutputFile(file) -> None
        
        
        Direct debug output to *either* stdout or stderr.
        
        
        Note that *file* MUST be either stdout or stderr. If not, issue an
        error and do nothing. Debug output is issued to stdout by default. If
        the environment variable TF_DEBUG_OUTPUT_FILE is set to'stderr', then
        output is issued to stderr by default.
        
        
        Parameters
        ----------
        file : FILE
        
        
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
    """
    """
    @staticmethod
    def GetValueFromFullName(*args, **kwargs):
        """
        
        **classmethod** GetValueFromFullName(fullname, foundIt) -> Enum
        
        
        Returns the enumerated value for a fully-qualified name.
        
        
        This takes a fully-qualified enumerated value name (e.g.,
        ``"Season::WINTER"`` ) and returns the associated value. If there is
        no such name, this returns -1. Since -1 can sometimes be a valid
        value, the ``foundIt`` flag pointer, if not ``None`` , is set to
        ``true`` if the name was found and ``false`` otherwise. Also, since
        this is not a templated function, it has to return a generic value
        type, so we use ``TfEnum`` .
        
        
        Parameters
        ----------
        fullname : str
        
        foundIt : bool
        
        
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
class Error(_DiagnosticBase):
    """
    """
    class Mark(Boost.Python.instance):
        __instance_size__: typing.ClassVar[int] = 24
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
    """
    """
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
        """
        
        **classmethod** GetCallTree(tree, skipRepeated) -> bool
        
        
        Return a snapshot of memory usage.
        
        
        Returns a snapshot by writing into ``\\*tree`` . See the ``C`` \\*tree
        structure for documentation. If ``Initialize()`` has not been called,
        \\ \\*tree is set to a rather blank structure (empty vectors, empty
        strings, zero in all integral fields) and ``false`` is returned;
        otherwise, ``\\*tree`` is set with the contents of the current memory
        snapshot and ``true`` is returned. It is fine to call this function on
        the same ``\\*tree`` instance; each call simply overwrites the data
        from the last call. If /p skipRepeated is ``true`` , then any repeated
        callsite is skipped. See the ``CallTree`` documentation for more
        details.
        
        
        Parameters
        ----------
        tree : CallTree
        
        skipRepeated : bool
        
        
        """
    @staticmethod
    def GetMaxTotalBytes(*args, **kwargs):
        """
        
        **classmethod** GetMaxTotalBytes() -> int
        
        
        Return the maximum total number of bytes that have ever been allocated
        at one time.
        
        
        This is simply the maximum value of GetTotalBytes() since Initialize()
        was called.
        
        
        
        """
    @staticmethod
    def GetTotalBytes(*args, **kwargs):
        """
        
        **classmethod** GetTotalBytes() -> int
        
        
        Return total number of allocated bytes.
        
        
        The current total memory that has been allocated and not freed is
        returned. Memory allocated before calling ``Initialize()`` is not
        accounted for.
        
        
        
        """
    @staticmethod
    def Initialize(*args, **kwargs):
        """
        
        **classmethod** Initialize(errMsg) -> bool
        
        
        Initialize the memory tagging system.
        
        
        This function returns ``true`` if the memory tagging system can be
        successfully initialized or it has already been initialized.
        Otherwise, ``\\*errMsg`` is set with an explanation for the failure.
        
        Until the system is initialized, the various memory reporting calls
        will indicate that no memory has been allocated. Note also that memory
        allocated prior to calling ``Initialize()`` is not tracked i.e. all
        data refers to allocations that happen subsequent to calling
        ``Initialize()`` .
        
        
        Parameters
        ----------
        errMsg : str
        
        
        """
    @staticmethod
    def IsInitialized(*args, **kwargs):
        """
        
        **classmethod** IsInitialized() -> bool
        
        
        Return true if the tagging system is active.
        
        
        If ``Initialize()`` has been successfully called, this function
        returns ``true`` .
        
        
        
        """
    @staticmethod
    def SetCapturedMallocStacksMatchList(*args, **kwargs):
        """
        
        **classmethod** SetCapturedMallocStacksMatchList(matchList) -> None
        
        
        Sets the tags to trace.
        
        
        When memory is allocated for any tag that matches ``matchList`` a
        stack trace is recorded. When that memory is released the stack trace
        is discarded. Clients can call ``GetCapturedMallocStacks()`` to get a
        list of all recorded stack traces. This is useful for finding leaks.
        
        Traces recorded for any tag that will no longer be matched are
        discarded by this call. Traces recorded for tags that continue to be
        matched are retained.
        
        ``matchList`` is a comma, tab or newline separated list of malloc tag
        names. The names can have internal spaces but leading and trailing
        spaces are stripped. If a name ends in'\\*'then the suffix is
        wildcarded. A name can have a leading'-'or'+'to prevent or allow a
        match. Each name is considered in order and later matches override
        earlier matches. For example,'Csd\\*, -CsdScene::_Populate\\*,
        +CsdScene::_PopulatePrimCacheLocal'matches any malloc tag starting
        with'Csd'but nothing starting
        with'CsdScene::_Populate'except'CsdScene::_PopulatePrimCacheLocal'.
        Use the empty string to disable stack capturing.
        
        
        Parameters
        ----------
        matchList : str
        
        
        """
    @staticmethod
    def SetDebugMatchList(*args, **kwargs):
        """
        
        **classmethod** SetDebugMatchList(matchList) -> None
        
        
        Sets the tags to trap in the debugger.
        
        
        When memory is allocated or freed for any tag that matches
        ``matchList`` the debugger trap is invoked. If a debugger is attached
        the program will stop in the debugger, otherwise the program will
        continue to run. See ``ArchDebuggerTrap()`` and ``ArchDebuggerWait()``
        .
        
        ``matchList`` is a comma, tab or newline separated list of malloc tag
        names. The names can have internal spaces but leading and trailing
        spaces are stripped. If a name ends in'\\*'then the suffix is
        wildcarded. A name can have a leading'-'or'+'to prevent or allow a
        match. Each name is considered in order and later matches override
        earlier matches. For example,'Csd\\*, -CsdScene::_Populate\\*,
        +CsdScene::_PopulatePrimCacheLocal'matches any malloc tag starting
        with'Csd'but nothing starting
        with'CsdScene::_Populate'except'CsdScene::_PopulatePrimCacheLocal'.
        Use the empty string to disable debugging traps.
        
        
        Parameters
        ----------
        matchList : str
        
        
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
    """
    """
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
    """
    
    A *TfNotice* that is sent when a script module is loaded. Since many
    modules may be loaded at once, listeners are encouraged to defer work
    triggered by this notice to the end of an application iteration. This,
    of course, is good practice in general.
    
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
    def name(*args, **kwargs):
        """
        
        name() -> str
        
        
        Return the name of the module that was loaded.
        
        
        
        """
class RefPtrTracker(Boost.Python.instance):
    """
    
    Provides tracking of ``TfRefPtr`` objects to particular objects.
    
    Clients can enable, at compile time, tracking of ``TfRefPtr`` objects
    that point to particular instances of classes derived from
    ``TfRefBase`` . This is useful if you have a ref counted object with a
    ref count that should've gone to zero but didn't. This tracker can
    tell you every ``TfRefPtr`` that's holding the ``TfRefBase`` and a
    stack trace where it was created or last assigned to.
    
    Clients can get a report of all watched instances and how many
    ``TfRefPtr`` objects are holding them using
    ``ReportAllWatchedCounts()`` (in python use ``Tf.RefPtrTracker()``
    .GetAllWatchedCountsReport()). You can see all of the stack traces
    using ``ReportAllTraces()`` (in python use ``Tf.RefPtrTracker()``
    .GetAllTracesReport()).
    
    Clients will typically enable tracking using code like this:
    
    .. code-block:: text
    
      #include "pxr/base/tf/refPtrTracker.h"
      
      class MyRefBaseType;
      typedef TfRefPtr<MyRefBaseType> MyRefBaseTypeRefPtr;
      
      TF_DECLARE_REFPTR_TRACK(MyRefBaseType);
      
      class MyRefBaseType {
      \\.\\.\\.
      public:
          static bool _ShouldWatch(const MyRefBaseType\\*);
      \\.\\.\\.
      };
      
      TF_DEFINE_REFPTR_TRACK(MyRefBaseType, MyRefBaseType::_ShouldWatch);
    
    Note that the ``TF_DECLARE_REFPTR_TRACK()`` macro must be invoked
    before any use of the ``MyRefBaseTypeRefPtr`` type.
    
    The ``MyRefBaseType::_ShouldWatch()`` function returns ``true`` if the
    given instance of ``MyRefBaseType`` should be tracked. You can also
    use ``TfRefPtrTracker::WatchAll()`` to watch every instance (but that
    might use a lot of memory and time).
    
    If you have a base type, ``B`` , and a derived type, ``D`` , and you
    hold instances of ``D`` in a ``TfRefPtr < ``B>```` (i.e. a pointer to
    the base) then you must track both type ``B`` and type ``D`` . But you
    can use ``TfRefPtrTracker::WatchNone()`` when tracking ``B`` if you're
    not interested in instances of ``B`` .
    
    """
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
        """
        
        __init__()
        
        
        
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
    """
    
    This class is used to provide high-level descriptions about scopes of
    execution that could possibly block, or to provide relevant
    information about high-level action that would be useful in a crash
    report.
    
    This class is reasonably fast to use, especially if the message
    strings are not dynamically created, however it should not be used in
    very highly performance sensitive contexts. The cost to push & pop is
    essentially a TLS lookup plus a couple of atomic operations.
    
    """
    __instance_size__: typing.ClassVar[int] = 32
    @staticmethod
    def SetDescription(*args, **kwargs):
        """
        
        SetDescription(description) -> None
        
        
        Replace the description stack entry for this scope description.
        
        
        Caller guarantees that the string ``description`` lives at least as
        long as this TfScopeDescription object.
        
        
        Parameters
        ----------
        description : str
        
        
        
        ----------------------------------------------------------------------
        
        SetDescription(description) -> None
        
        
        Replace the description stack entry for this scope description.
        
        
        This object adopts ownership of the rvalue ``description`` .
        
        
        Parameters
        ----------
        description : str
        
        
        
        ----------------------------------------------------------------------
        
        SetDescription(description) -> None
        
        
        Replace the description stack entry for this scope description.
        
        
        Caller guarantees that the string ``description`` lives at least as
        long as this TfScopeDescription object.
        
        
        Parameters
        ----------
        description : char
        
        
        """
    @staticmethod
    def __enter__(*args, **kwargs):
        ...
    @staticmethod
    def __exit__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(arg1)
        
        
        Parameters
        ----------
        arg1 : ScopeDescription
        
        
        
        ----------------------------------------------------------------------
        
        __init__(description, context)
        
        
        Construct with a description.
        
        
        Push *description* on the stack of descriptions for this thread.
        Caller guarantees that the string ``description`` lives at least as
        long as this TfScopeDescription object.
        
        
        Parameters
        ----------
        description : str
        
        context : CallContext
        
        
        
        ----------------------------------------------------------------------
        
        __init__(description, context)
        
        
        Construct with a description.
        
        
        Push *description* on the stack of descriptions for this thread. This
        object adopts ownership of the rvalue ``description`` .
        
        
        Parameters
        ----------
        description : str
        
        context : CallContext
        
        
        
        ----------------------------------------------------------------------
        
        __init__(description, context)
        
        
        Construct with a description.
        
        
        Push *description* on the stack of descriptions for this thread.
        Caller guarantees that the string ``description`` lives at least as
        long as this TfScopeDescription object.
        
        
        Parameters
        ----------
        description : char
        
        context : CallContext
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class ScriptModuleLoader(Boost.Python.instance):
    """
    
    Provides low-level facilities for shared modules with script
    bindings to register themselves with their dependences, and provides a
    mechanism whereby those script modules will be loaded when necessary.
    Currently, this is when one of our script modules is loaded, when
    TfPyInitialize is called, and when Plug opens shared modules.
    
    Generally, user code will not make use of this.
    
    """
    @staticmethod
    def GetModuleNames(*args, **kwargs):
        """
        
        GetModuleNames() -> list[str]
        
        
        Return a list of all currently known modules in a valid dependency
        order.
        
        
        
        """
    @staticmethod
    def GetModulesDict(*args, **kwargs):
        """
        
        GetModulesDict() -> python.dict
        
        
        Return a python dict containing all currently known modules under
        their canonical names.
        
        
        
        """
    @staticmethod
    def WriteDotFile(*args, **kwargs):
        """
        
        WriteDotFile(file) -> None
        
        
        Write a graphviz dot-file for the dependency graph of all.
        
        
        currently known modules/modules to *file*.
        
        
        Parameters
        ----------
        file : str
        
        
        """
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
        """
        
        __init__()
        
        
        
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
    """
    """
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
    """
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def AddFrom(*args, **kwargs):
        """
        
        AddFrom(t) -> None
        
        
        Adds the accumulated time and sample count from ``t`` into the
        ``TfStopwatch`` .
        
        
        If you have several timers taking measurements, and you wish to
        combine them together, you can add one timer's results into another;
        for example, ``t2.AddFrom(t1)`` will add ``t1`` 's time and sample
        count into ``t2`` .
        
        
        Parameters
        ----------
        t : Stopwatch
        
        
        """
    @staticmethod
    def Reset(*args, **kwargs):
        """
        
        Reset() -> None
        
        
        Resets the accumulated time and the sample count to zero.
        
        
        
        """
    @staticmethod
    def Start(*args, **kwargs):
        """
        
        Start() -> None
        
        
        Record the current time for use by the next ``Stop()`` call.
        
        
        The ``Start()`` function records the current time. A subsequent call
        to ``Start()`` before a call to ``Stop()`` simply records a later
        current time, but does not change the accumulated time of the
        ``TfStopwatch`` .
        
        
        
        """
    @staticmethod
    def Stop(*args, **kwargs):
        """
        
        Stop() -> None
        
        
        Increases the accumulated time stored in the ``TfStopwatch`` .
        
        
        The ``Stop()`` function increases the accumulated time by the duration
        between the current time and the last time recorded by a ``Start()``
        call. A subsequent call to ``Stop()`` before another call to
        ``Start()`` will therefore double-count time and throw off the
        results.
        
        A ``TfStopwatch`` also counts the number of samples it has taken.
        The"sample count"is simply the number of times that ``Stop()`` has
        been called.
        
        
        
        """
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @property
    def microseconds(*args, **kwargs):
        """
        type : int
        
        
        Return the accumulated time in microseconds.
        
        
        Note that 45 minutes will overflow a 32-bit counter, so take care to
        save the result in an ``int64_t`` , and not a regular ``int`` or
        ``long`` .
        """
    @property
    def milliseconds(*args, **kwargs):
        """
        type : int
        
        
        Return the accumulated time in milliseconds.
        """
    @property
    def nanoseconds(*args, **kwargs):
        """
        type : int
        
        
        Return the accumulated time in nanoseconds.
        
        
        Note that this number can easily overflow a 32-bit counter, so take
        care to save the result in an ``int64_t`` , and not a regular ``int``
        or ``long`` .
        """
    @property
    def sampleCount(*args, **kwargs):
        """
        type : int
        
        
        Return the current sample count.
        
        
        The sample count, which is simply the number of calls to ``Stop()``
        since creation or a call to ``Reset()`` , is useful for computing
        average running times of a repeated task.
        """
    @property
    def seconds(*args, **kwargs):
        """
        type : float
        
        
        Return the accumulated time in seconds as a ``double`` .
        """
class TemplateString(Boost.Python.instance):
    """
    """
    __instance_size__: typing.ClassVar[int] = 32
    @staticmethod
    def GetEmptyMapping(*args, **kwargs):
        """
        
        GetEmptyMapping() -> Mapping
        
        
        Returns an empty mapping for the current template.
        
        
        This method first calls IsValid to ensure that the template is valid.
        
        
        
        """
    @staticmethod
    def GetParseErrors(*args, **kwargs):
        """
        
        GetParseErrors() -> list[str]
        
        
        Returns any error messages generated during template parsing.
        
        
        
        """
    @staticmethod
    def SafeSubstitute(*args, **kwargs):
        """
        
        SafeSubstitute(arg1) -> str
        
        
        Like Substitute() , except that if placeholders are missing from the
        mapping, instead of raising a coding error, the original placeholder
        will appear in the resulting string intact.
        
        
        Parameters
        ----------
        arg1 : Mapping
        
        
        """
    @staticmethod
    def Substitute(*args, **kwargs):
        """
        
        Substitute(arg1) -> str
        
        
        Performs the template substitution, returning a new string.
        
        
        The mapping contains keys which match the placeholders in the
        template. If a placeholder is found for which no mapping is present, a
        coding error is raised.
        
        
        Parameters
        ----------
        arg1 : Mapping
        
        
        """
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        Constructs a new template string.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(template_)
        
        
        Constructs a new template string.
        
        
        Parameters
        ----------
        template_ : str
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def template(*args, **kwargs):
        """
        type : str
        
        
        Returns the template source string supplied to the constructor.
        """
    @property
    def valid(*args, **kwargs):
        """
        type : bool
        
        
        Returns true if the current template is well formed.
        
        
        Empty templates are valid.
        """
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
    __instance_size__: typing.ClassVar[int] = 32
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
    __instance_size__: typing.ClassVar[int] = 24
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
class Tf_TestPyOptional(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 24
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
    """
    
    TfType represents a dynamic runtime type.
    
    TfTypes are created and discovered at runtime, rather than compile
    time.
    
    Features:
    
       - unique typename
    
       - safe across DSO boundaries
    
       - can represent C++ types, pure Python types, or Python subclasses
         of wrapped C++ types
    
       - lightweight value semantics  you can copy and default construct
         TfType, unlike ``std::type_info`` .
    
       - totally ordered  can use as a ``std::map`` key
    
    
    """
    Unknown: typing.ClassVar[Type]  # value = Tf.Type.Unknown
    __instance_size__: typing.ClassVar[int] = 24
    @staticmethod
    def AddAlias(*args, **kwargs):
        """
        
        **classmethod** AddAlias(base, name) -> None
        
        
        Add an alias name for this type under the given base type.
        
        
        Aliases are similar to typedefs in C++: they provide an alternate name
        for a type. The alias is defined with respect to the given ``base``
        type. Aliases must be unique with respect to both other aliases
        beneath that base type and names of derived types of that base.
        
        
        Parameters
        ----------
        base : Type
        
        name : str
        
        
        
        ----------------------------------------------------------------------
        
        AddAlias(name) -> None
        
        
        Add an alias for DERIVED beneath BASE.
        
        
        This is a convenience method, that declares both DERIVED and BASE as
        TfTypes before adding the alias.
        
        
        Parameters
        ----------
        name : str
        
        
        """
    @staticmethod
    def Define(*args, **kwargs):
        """
        
        **classmethod** Define() -> Type
        
        
        Define a TfType with the given C++ type T and C++ base types B.
        
        
        Each of the base types will be declared (but not defined) as TfTypes
        if they have not already been.
        
        The typeName of the created TfType will be the canonical demangled
        RTTI type name, as defined by GetCanonicalTypeName() .
        
        It is an error to attempt to define a type that has already been
        defined.
        
        
        
        
        ----------------------------------------------------------------------
        
        Define() -> Type
        
        
        Define a TfType with the given C++ type T and no bases.
        
        
        See the other Define() template for more details.
        
        C++ does not allow default template arguments for function templates,
        so we provide this separate definition for the case of no bases.
        
        
        
        """
    @staticmethod
    def Find(*args, **kwargs):
        """
        
        **classmethod** Find() -> Type
        
        
        Retrieve the ``TfType`` corresponding to type ``T`` .
        
        
        The type ``T`` must have been declared or defined in the type system
        or the ``TfType`` corresponding to an unknown type is returned.
        
        IsUnknown()
        
        
        
        
        ----------------------------------------------------------------------
        
        Find(obj) -> Type
        
        
        Retrieve the ``TfType`` corresponding to ``obj`` .
        
        
        The ``TfType`` corresponding to the actual object represented by
        ``obj`` is returned; this may not be the object returned by
        ``TfType::Find<T>()`` if ``T`` is a polymorphic type.
        
        This works for Python subclasses of the C++ type ``T`` as well, as
        long as ``T`` has been wrapped using TfPyPolymorphic.
        
        Of course, the object's type must have been declared or defined in the
        type system or the ``TfType`` corresponding to an unknown type is
        returned.
        
        IsUnknown()
        
        
        Parameters
        ----------
        obj : T
        
        
        
        ----------------------------------------------------------------------
        
        Find(t) -> Type
        
        
        Retrieve the ``TfType`` corresponding to an obj with the given
        ``type_info`` .
        
        
        Parameters
        ----------
        t : type_info
        
        
        """
    @staticmethod
    def FindByName(*args, **kwargs):
        """
        
        **classmethod** FindByName(name) -> Type
        
        
        Retrieve the ``TfType`` corresponding to the given ``name`` .
        
        
        Every type defined in the TfType system has a unique, implementation
        independent name. In addition, aliases can be added to identify a type
        underneath a specific base type; see TfType::AddAlias() . The given
        name will first be tried as an alias under the root type, and
        subsequently as a typename.
        
        This method is equivalent to:
        
        .. code-block:: text
        
          TfType::GetRoot().FindDerivedByName(name)
        
        For any object ``obj`` ,
        
        .. code-block:: text
        
          Find(obj) == FindByName( Find(obj).GetTypeName() )
        
        
        
        Parameters
        ----------
        name : str
        
        
        """
    @staticmethod
    def FindDerivedByName(*args, **kwargs):
        """
        
        **classmethod** FindDerivedByName(name) -> Type
        
        
        Retrieve the ``TfType`` that derives from this type and has the given
        alias or typename.
        
        
        
        AddAlias
        
        
        Parameters
        ----------
        name : str
        
        
        
        ----------------------------------------------------------------------
        
        FindDerivedByName(name) -> Type
        
        
        Retrieve the ``TfType`` that derives from BASE and has the given alias
        or typename.
        
        
        This is a convenience method, and is equivalent to:
        
        .. code-block:: text
        
          TfType::Find<BASE>().FindDerivedByName(name)
        
        
        
        Parameters
        ----------
        name : str
        
        
        """
    @staticmethod
    def GetAliases(*args, **kwargs):
        """
        
        GetAliases(derivedType) -> list[str]
        
        
        Returns a vector of the aliases registered for the derivedType under
        this, the base type.
        
        
        
        AddAlias()
        
        
        Parameters
        ----------
        derivedType : Type
        
        
        """
    @staticmethod
    def GetAllAncestorTypes(*args, **kwargs):
        """
        
        GetAllAncestorTypes(result) -> None
        
        
        Build a vector of all ancestor types inherited by this type.
        
        
        The starting type is itself included, as the first element of the
        results vector.
        
        Types are given in"C3"resolution order, as used for new-style classes
        starting in Python 2.3. This algorithm is more complicated than a
        simple depth-first traversal of base classes, in order to prevent some
        subtle errors with multiple-inheritance. See the references below for
        more background.
        
        This can be expensive; consider caching the results. TfType does not
        cache this itself since it is not needed internally.
        
        Guido van Rossum."Unifying types and classes in Python 2.2: Method
        resolution order."
        http://www.python.org/download/releases/2.2.2/descrintro/#mro
        
        Barrett, Cassels, Haahr, Moon, Playford, Withington."A Monotonic
        Superclass Linearization for Dylan."OOPSLA 96.
        http://www.webcom.com/haahr/dylan/linearization-oopsla96.html
        
        
        Parameters
        ----------
        result : list[Type]
        
        
        """
    @staticmethod
    def GetAllDerivedTypes(*args, **kwargs):
        """
        
        GetAllDerivedTypes(result) -> None
        
        
        Return the set of all types derived (directly or indirectly) from this
        type.
        
        
        Parameters
        ----------
        result : set[Type]
        
        
        """
    @staticmethod
    def GetRoot(*args, **kwargs):
        """
        
        **classmethod** GetRoot() -> Type
        
        
        Return the root type of the type hierarchy.
        
        
        All known types derive (directly or indirectly) from the root. If a
        type is specified with no bases, it is implicitly considered to derive
        from the root type.
        
        
        
        """
    @staticmethod
    def IsA(*args, **kwargs):
        """
        
        IsA(queryType) -> bool
        
        
        Return true if this type is the same as or derived from ``queryType``
        .
        
        
        If ``queryType`` is unknown, this always returns ``false`` .
        
        
        Parameters
        ----------
        queryType : Type
        
        
        
        ----------------------------------------------------------------------
        
        IsA() -> bool
        
        
        Return true if this type is the same as or derived from T.
        
        
        This is equivalent to:
        
        .. code-block:: text
        
          IsA(Find<T>())
        
        
        
        
        """
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
        """
        
        __init__()
        
        
        Construct an TfType representing an unknown type.
        
        
        To actually register a new type with the TfType system, see
        TfType::Declare() .
        
        Note that this always holds true:
        
        .. code-block:: text
        
          TfType().IsUnknown() == true
        
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(info)
        
        
        Parameters
        ----------
        info : _TypeInfo
        
        
        """
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
        """
        type : list[Type]
        
        
        Return a vector of types from which this type was derived.
        """
    @property
    def derivedTypes(*args, **kwargs):
        ...
    @property
    def isEnumType(*args, **kwargs):
        """
        type : bool
        
        
        Return true if this is an enum type.
        """
    @property
    def isPlainOldDataType(*args, **kwargs):
        """
        type : bool
        
        
        Return true if this is a plain old data type, as defined by C++.
        """
    @property
    def isUnknown(*args, **kwargs):
        """
        type : bool
        
        
        Return true if this is the unknown type, representing a type unknown
        to the TfType system.
        
        
        The unknown type does not derive from the root type, or any other
        type.
        """
    @property
    def pythonClass(*args, **kwargs):
        """
        type : TfPyObjWrapper
        
        
        Return the Python class object for this type.
        
        
        If this type is unknown or has not yet had a Python class defined,
        this will return ``None`` , as an empty ``TfPyObjWrapper``
        
        DefinePythonClass()
        """
    @property
    def sizeof(*args, **kwargs):
        """
        type : int
        
        
        Return the size required to hold an instance of this type on the stack
        (does not include any heap allocated memory the instance uses).
        
        
        This is what the C++ sizeof operator returns for the type, so this
        value is not very useful for Python types (it will always be
        sizeof(boost::python::object)).
        """
    @property
    def typeName(*args, **kwargs):
        """
        type : str
        
        
        Return the machine-independent name for this type.
        
        
        This name is specified when the TfType is declared.
        
        Declare()
        """
class Warning(_DiagnosticBase):
    """
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
    def __repr__(*args, **kwargs):
        ...
class WindowsImportWrapper:
    def __enter__(self):
        ...
    def __exit__(self, exc_type, ex_val, exc_tb):
        ...
class _ClassWithClassMethod(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 24
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
    Fuji: typing.ClassVar[str] = 'Fuji'
    McIntosh: typing.ClassVar[str] = 'McIntosh'
    Pippin: typing.ClassVar[str] = 'Pippin'
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
    Fuji: typing.ClassVar[str] = 'Fuji'
    McIntosh: typing.ClassVar[str] = 'McIntosh'
    Pippin: typing.ClassVar[str] = 'Pippin'
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
        By default, the information is returned at the current stack-frame; thus::
    
            info = GetCodeLocation()
    
        will return information about the line that GetCodeLocation() was called 
        from. One can write: ::
    
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
