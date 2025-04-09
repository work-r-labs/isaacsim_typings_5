"""

Trace -- Utilities for counting and recording events.
"""
from __future__ import annotations
import typing
__all__ = ['AggregateNode', 'Collector', 'Reporter', 'TraceFunction', 'TraceMethod', 'TraceScope']
class AggregateNode(Boost.Python.instance):
    """
    
    A representation of a call tree. Each node represents one or more
    calls that occurred in the trace. Multiple calls to a child node are
    aggregated into one node.
    
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
        Raises an exception
        This class cannot be instantiated from Python
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
    def children(*args, **kwargs):
        """
        type : list[AggregateNode]
        """
    @property
    def count(*args, **kwargs):
        """
        type : int
        
        
        Returns the call count of this node.
        
        
        ``recursive`` determines if recursive calls are counted.
        """
    @property
    def exclusiveCount(*args, **kwargs):
        """
        type : int
        
        
        Returns the exclusive count.
        """
    @property
    def exclusiveTime(*args, **kwargs):
        """
        type : TimeStamp
        
        
        Returns the time spent in this node but not its children.
        """
    @property
    def expanded(*args, **kwargs):
        """
        type : bool
        
        
        Returns whether this node is expanded in a gui.
        
        ----------------------------------------------------------------------
        
        type : None
        
        
        Sets whether or not this node is expanded in a gui.
        """
    @expanded.setter
    def expanded(*args, **kwargs):
        ...
    @property
    def expired(*args, **kwargs):
        """
        True if this object has expired, False otherwise.
        """
    @property
    def id(*args, **kwargs):
        """
        type : Id
        
        
        Returns the node's id.
        """
    @property
    def inclusiveTime(*args, **kwargs):
        """
        type : TimeStamp
        
        
        Returns the total time of this node ands its children.
        """
    @property
    def key(*args, **kwargs):
        """
        type : str
        
        
        Returns the node's key.
        """
class Collector(Boost.Python.instance):
    """
    
    This is a singleton class that records TraceEvent instances and
    populates TraceCollection instances.
    
    All public methods of TraceCollector are safe to call from any thread.
    
    """
    @staticmethod
    def BeginEvent(*args, **kwargs):
        """
        
        BeginEvent(key) -> TimeStamp
        
        
        Record a begin event with *key* if ``Category`` is enabled.
        
        
        A matching end event is expected some time in the future.
        
        If the key is known at compile time ``BeginScope`` and ``Scope``
        methods are preferred because they have lower overhead.
        
        The TimeStamp of the TraceEvent or 0 if the collector is disabled.
        
        BeginScope
        
        Scope
        
        
        Parameters
        ----------
        key : Key
        
        
        """
    @staticmethod
    def BeginEventAtTime(*args, **kwargs):
        """
        
        BeginEventAtTime(key, ms) -> None
        
        
        Record a begin event with *key* at a specified time if ``Category`` is
        enabled.
        
        
        This version of the method allows the passing of a specific number of
        elapsed milliseconds, *ms*, to use for this event. This method is used
        for testing and debugging code.
        
        
        Parameters
        ----------
        key : Key
        
        ms : float
        
        
        """
    @staticmethod
    def Clear(*args, **kwargs):
        """
        
        Clear() -> None
        
        
        Clear all pending events from the collector.
        
        
        No TraceCollection will be made for these events.
        
        
        
        """
    @staticmethod
    def EndEvent(*args, **kwargs):
        """
        
        EndEvent(key) -> TimeStamp
        
        
        Record an end event with *key* if ``Category`` is enabled.
        
        
        A matching begin event must have preceded this end event.
        
        If the key is known at compile time EndScope and Scope methods are
        preferred because they have lower overhead.
        
        The TimeStamp of the TraceEvent or 0 if the collector is disabled.
        
        EndScope
        
        Scope
        
        
        Parameters
        ----------
        key : Key
        
        
        """
    @staticmethod
    def EndEventAtTime(*args, **kwargs):
        """
        
        EndEventAtTime(key, ms) -> None
        
        
        Record an end event with *key* at a specified time if ``Category`` is
        enabled.
        
        
        This version of the method allows the passing of a specific number of
        elapsed milliseconds, *ms*, to use for this event. This method is used
        for testing and debugging code.
        
        
        Parameters
        ----------
        key : Key
        
        ms : float
        
        
        """
    @staticmethod
    def GetLabel(*args, **kwargs):
        """
        
        GetLabel() -> str
        
        
        Return the label associated with this collector.
        
        
        
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
    def enabled(*args, **kwargs):
        """
        **classmethod** type : bool
        
        
        Returns whether collection of events is enabled for DefaultCategory.
        
        ----------------------------------------------------------------------
        
        type : None
        
        
        Enables or disables collection of events for DefaultCategory.
        """
    @enabled.setter
    def enabled(*args, **kwargs):
        ...
    @property
    def expired(*args, **kwargs):
        """
        True if this object has expired, False otherwise.
        """
    @property
    def pythonTracingEnabled(*args, **kwargs):
        """
        type : None
        
        
        Set whether automatic tracing of all python scopes is enabled.
        
        ----------------------------------------------------------------------
        
        type : bool
        
        
        Returns whether automatic tracing of all python scopes is enabled.
        """
    @pythonTracingEnabled.setter
    def pythonTracingEnabled(*args, **kwargs):
        ...
class Reporter(Boost.Python.instance):
    """
    
    This class converts streams of TraceEvent objects into call trees
    which can then be used as a data source to a GUI or written out to a
    file.
    
    """
    globalReporter: typing.ClassVar[Reporter]  # value = <pxr.Trace.Reporter object>
    @staticmethod
    def ClearTree(*args, **kwargs):
        """
        
        ClearTree() -> None
        
        
        Clears event tree and counters.
        
        
        
        """
    @staticmethod
    def GetLabel(*args, **kwargs):
        """
        
        GetLabel() -> str
        
        
        Return the label associated with this reporter.
        
        
        
        """
    @staticmethod
    def Report(*args, **kwargs):
        """
        
        Report(s, iterationCount) -> None
        
        
        Generates a report to the ostream *s*, dividing all times by
        *iterationCount*.
        
        
        Parameters
        ----------
        s : ostream
        
        iterationCount : int
        
        
        """
    @staticmethod
    def ReportChromeTracing(*args, **kwargs):
        """
        
        ReportChromeTracing(s) -> None
        
        
        Generates a timeline trace report suitable for viewing in Chrome's
        trace viewer.
        
        
        Parameters
        ----------
        s : ostream
        
        
        """
    @staticmethod
    def ReportChromeTracingToFile(*args, **kwargs):
        ...
    @staticmethod
    def ReportTimes(*args, **kwargs):
        """
        
        ReportTimes(s) -> None
        
        
        Generates a report of the times to the ostream *s*.
        
        
        Parameters
        ----------
        s : ostream
        
        
        """
    @staticmethod
    def UpdateTraceTrees(*args, **kwargs):
        """
        
        UpdateTraceTrees() -> None
        
        
        This fully re-builds the event and aggregate trees from whatever the
        current collection holds.
        
        
        It is ok to call this multiple times in case the collection gets
        appended on inbetween.
        
        If we want to have multiple reporters per collector, this will need to
        be changed so that all reporters reporting on a collector update their
        respective trees.
        
        
        
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
        
        __init__(label, dataSource)
        
        
        Parameters
        ----------
        label : str
        
        dataSource : DataSource
        
        
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
    def aggregateTreeRoot(*args, **kwargs):
        """
        type : AggregateNode
        
        
        Returns the root node of the aggregated call tree.
        """
    @property
    def expired(*args, **kwargs):
        """
        True if this object has expired, False otherwise.
        """
    @property
    def foldRecursiveCalls(*args, **kwargs):
        """
        type : bool
        
        
        Returns the current setting for recursion folding for stack trace
        event reporting.
        
        ----------------------------------------------------------------------
        
        type : None
        
        
        When stack trace event reporting, this sets whether or not recursive
        calls are folded in the output.
        
        
        Recursion folding is useful when the stacks contain deep recursive
        structures.
        """
    @foldRecursiveCalls.setter
    def foldRecursiveCalls(*args, **kwargs):
        ...
    @property
    def groupByFunction(*args, **kwargs):
        """
        type : bool
        
        
        Returns the current group-by-function state.
        
        ----------------------------------------------------------------------
        
        type : None
        
        
        This affects only stack trace event reporting.
        
        
        If ``true`` then all events in a function are grouped together
        otherwise events are split out by address.
        """
    @groupByFunction.setter
    def groupByFunction(*args, **kwargs):
        ...
    @property
    def shouldAdjustForOverheadAndNoise(*args, **kwargs):
        """
        type : None
        
        
        Set whether or not the reporter should adjust scope times for overhead
        and noise.
        """
    @shouldAdjustForOverheadAndNoise.setter
    def shouldAdjustForOverheadAndNoise(*args, **kwargs):
        ...
def TraceFunction(obj):
    """
    A decorator that enables tracing the function that it decorates.
        If you decorate with 'TraceFunction' the function will be traced in the
        global collector.
    """
def TraceMethod(obj):
    """
    A convenience.  Same as TraceFunction but changes the recorded
        label to use the term 'method' rather than 'function'.
    """
def TraceScope(*args, **kwds):
    """
    A context manager that calls BeginEvent on the global collector on enter 
        and EndEvent on exit.
    """
__MFB_FULL_PACKAGE_NAME: str = 'trace'
