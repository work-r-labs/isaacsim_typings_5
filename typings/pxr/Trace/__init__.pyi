"""

Trace -- Utilities for counting and recording events.
"""
from __future__ import annotations
import typing
__all__: list[str] = ['AggregateNode', 'Collector', 'Reporter', 'TraceFunction', 'TraceMethod', 'TraceScope']
class AggregateNode(Boost.Python.instance):
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
        ...
    @property
    def count(*args, **kwargs):
        ...
    @property
    def exclusiveCount(*args, **kwargs):
        ...
    @property
    def exclusiveTime(*args, **kwargs):
        ...
    @property
    def expanded(*args, **kwargs):
        ...
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
        ...
    @property
    def inclusiveTime(*args, **kwargs):
        ...
    @property
    def key(*args, **kwargs):
        ...
class Collector(Boost.Python.instance):
    @staticmethod
    def BeginEvent(*args, **kwargs):
        ...
    @staticmethod
    def BeginEventAtTime(*args, **kwargs):
        ...
    @staticmethod
    def Clear(*args, **kwargs):
        ...
    @staticmethod
    def EndEvent(*args, **kwargs):
        ...
    @staticmethod
    def EndEventAtTime(*args, **kwargs):
        ...
    @staticmethod
    def GetLabel(*args, **kwargs):
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
    def enabled(*args, **kwargs):
        ...
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
        ...
    @pythonTracingEnabled.setter
    def pythonTracingEnabled(*args, **kwargs):
        ...
class Reporter(Boost.Python.instance):
    globalReporter: typing.ClassVar[Reporter]  # value = <pxr.Trace.Reporter object>
    @staticmethod
    def ClearTree(*args, **kwargs):
        ...
    @staticmethod
    def GetLabel(*args, **kwargs):
        ...
    @staticmethod
    def Report(*args, **kwargs):
        ...
    @staticmethod
    def ReportChromeTracing(*args, **kwargs):
        ...
    @staticmethod
    def ReportChromeTracingToFile(*args, **kwargs):
        ...
    @staticmethod
    def ReportTimes(*args, **kwargs):
        ...
    @staticmethod
    def UpdateTraceTrees(*args, **kwargs):
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
    def aggregateTreeRoot(*args, **kwargs):
        ...
    @property
    def expired(*args, **kwargs):
        """
        True if this object has expired, False otherwise.
        """
    @property
    def foldRecursiveCalls(*args, **kwargs):
        ...
    @foldRecursiveCalls.setter
    def foldRecursiveCalls(*args, **kwargs):
        ...
    @property
    def groupByFunction(*args, **kwargs):
        ...
    @groupByFunction.setter
    def groupByFunction(*args, **kwargs):
        ...
    @property
    def shouldAdjustForOverheadAndNoise(*args, **kwargs):
        ...
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
