"""
pybind11 carb.profiler bindings
"""
from __future__ import annotations
import typing
__all__ = ['FlowType', 'IProfileMonitor', 'IProfiler', 'InstantType', 'ProfileEvents', 'acquire_profile_monitor_interface', 'acquire_profiler_interface', 'begin_with_location', 'end', 'is_profiler_active', 'supports_dynamic_source_locations']
class FlowType:
    """
    Members:
    
      BEGIN
    
      END
    """
    BEGIN: typing.ClassVar[FlowType]  # value = <FlowType.BEGIN: 0>
    END: typing.ClassVar[FlowType]  # value = <FlowType.END: 1>
    __members__: typing.ClassVar[dict[str, FlowType]]  # value = {'BEGIN': <FlowType.BEGIN: 0>, 'END': <FlowType.END: 1>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class IProfileMonitor:
    def get_last_profile_events(self) -> ProfileEvents:
        ...
    def mark_frame_end(self) -> None:
        ...
class IProfiler:
    def begin(self, mask: int, name: str) -> None:
        ...
    def end(self, mask: int) -> None:
        ...
    def ensure_thread(self) -> None:
        """
        Ensures that the profiler is aware of a Python thread.
        
        If the profiler is already aware of the Python thread, there is no effect.
        
        Args:
            None
        
        Returns:
            None
        """
    def flow(self, arg0: int, arg1: FlowType, arg2: int, arg3: str) -> None:
        ...
    def frame(self, arg0: int, arg1: str) -> None:
        ...
    def get_capture_mask(self) -> int:
        ...
    def instant(self, arg0: int, arg1: InstantType, arg2: str) -> None:
        ...
    def is_python_profiling_enabled(self) -> bool:
        """
        Returns whether Python cProfile-level profiling is enabled.
        
        Returns:
            True if Python function profiling is enabled, False otherwise.
        """
    def set_capture_mask(self, mask: int) -> int:
        ...
    def set_python_profiling_enabled(self, enable: bool) -> None:
        """
        Enables or disables cProfile-level Python profiling.
        
        Enabling this value causes every Python function call to be recorded through
        carb.profiler. As such, it can negatively affect performance and can lead to
        very large profiler files.
        
        Only Python threads that carb.profiler is aware of will report to the profiler.
        Calling ensure_thread() will ensure that carb.profiler is aware of a Python
        thread.
        
        Use is_python_profiling_enabled() to determine the current state of this value.
        
        Args:
            enable: True to enable the profiler or False to disable.
        
        Returns:
            None
        """
    def shutdown(self) -> None:
        ...
    def startup(self) -> None:
        ...
    def value_float(self, mask: int, value: float, name: str) -> None:
        ...
    def value_int(self, mask: int, value: int, name: str) -> None:
        ...
    def value_uint(self, mask: int, value: int, name: str) -> None:
        ...
class InstantType:
    """
    Members:
    
      THREAD
    
      PROCESS
    """
    PROCESS: typing.ClassVar[InstantType]  # value = <InstantType.PROCESS: 1>
    THREAD: typing.ClassVar[InstantType]  # value = <InstantType.THREAD: 0>
    __members__: typing.ClassVar[dict[str, InstantType]]  # value = {'THREAD': <InstantType.THREAD: 0>, 'PROCESS': <InstantType.PROCESS: 1>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ProfileEvents:
    """
    Profile Events holder
    """
    def get_main_thread_id(self) -> int:
        ...
    def get_profile_events(self, thread_id: int = 0) -> tuple:
        ...
    def get_profile_thread_ids(self) -> tuple:
        ...
def acquire_profile_monitor_interface(plugin_name: str = None, library_path: str = None) -> IProfileMonitor:
    ...
def acquire_profiler_interface(plugin_name: str = None, library_path: str = None) -> IProfiler:
    ...
def begin_with_location(mask: int, name: str, function: str = '', filepath: str = '', lineno: int = 0) -> None:
    ...
def end(mask: int) -> None:
    ...
def is_profiler_active() -> bool:
    ...
def supports_dynamic_source_locations() -> bool:
    ...
