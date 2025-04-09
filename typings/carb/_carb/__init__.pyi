from __future__ import annotations
import typing
from . import filesystem
from . import logging
__all__ = ['ColorRgb', 'ColorRgbDouble', 'ColorRgba', 'ColorRgbaDouble', 'Double2', 'Double3', 'Double4', 'Float2', 'Float3', 'Float4', 'Framework', 'Int2', 'Int3', 'Int4', 'InterfaceDesc', 'PluginDesc', 'PluginHotReload', 'PluginImplDesc', 'Subscription', 'Uint2', 'Uint3', 'Uint4', 'Version', 'answer_question', 'breakpoint', 'filesystem', 'get_framework', 'log', 'logging', 'wait_for_native_debugger']
class ColorRgb:
    """
    """
    __hash__: typing.ClassVar[None] = None
    b: float
    g: float
    r: float
    def __eq__(self, arg0: ColorRgb) -> bool:
        ...
    @typing.overload
    def __getitem__(self, arg0: int) -> float:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> list:
        ...
    def __getstate__(self) -> tuple:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: float, arg1: float, arg2: float) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: typing.Sequence) -> None:
        ...
    def __len__(self) -> int:
        ...
    def __ne__(self, arg0: ColorRgb) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    @typing.overload
    def __setitem__(self, arg0: int, arg1: float) -> None:
        ...
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: typing.Sequence) -> None:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
class ColorRgbDouble:
    """
    """
    __hash__: typing.ClassVar[None] = None
    b: float
    g: float
    r: float
    def __eq__(self, arg0: ColorRgbDouble) -> bool:
        ...
    @typing.overload
    def __getitem__(self, arg0: int) -> float:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> list:
        ...
    def __getstate__(self) -> tuple:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: float, arg1: float, arg2: float) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: typing.Sequence) -> None:
        ...
    def __len__(self) -> int:
        ...
    def __ne__(self, arg0: ColorRgbDouble) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    @typing.overload
    def __setitem__(self, arg0: int, arg1: float) -> None:
        ...
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: typing.Sequence) -> None:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
class ColorRgba:
    """
    """
    __hash__: typing.ClassVar[None] = None
    a: float
    b: float
    g: float
    r: float
    def __eq__(self, arg0: ColorRgba) -> bool:
        ...
    @typing.overload
    def __getitem__(self, arg0: int) -> float:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> list:
        ...
    def __getstate__(self) -> tuple:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: typing.Sequence) -> None:
        ...
    def __len__(self) -> int:
        ...
    def __ne__(self, arg0: ColorRgba) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    @typing.overload
    def __setitem__(self, arg0: int, arg1: float) -> None:
        ...
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: typing.Sequence) -> None:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
class ColorRgbaDouble:
    """
    """
    __hash__: typing.ClassVar[None] = None
    a: float
    b: float
    g: float
    r: float
    def __eq__(self, arg0: ColorRgbaDouble) -> bool:
        ...
    @typing.overload
    def __getitem__(self, arg0: int) -> float:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> list:
        ...
    def __getstate__(self) -> tuple:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: typing.Sequence) -> None:
        ...
    def __len__(self) -> int:
        ...
    def __ne__(self, arg0: ColorRgbaDouble) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    @typing.overload
    def __setitem__(self, arg0: int, arg1: float) -> None:
        ...
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: typing.Sequence) -> None:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
class Double2:
    """
    """
    __hash__: typing.ClassVar[None] = None
    x: float
    y: float
    def __eq__(self, arg0: Double2) -> bool:
        ...
    @typing.overload
    def __getitem__(self, arg0: int) -> float:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> list:
        ...
    def __getstate__(self) -> tuple:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: float, arg1: float) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: typing.Sequence) -> None:
        ...
    def __len__(self) -> int:
        ...
    def __ne__(self, arg0: Double2) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    @typing.overload
    def __setitem__(self, arg0: int, arg1: float) -> None:
        ...
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: typing.Sequence) -> None:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
class Double3:
    """
    """
    __hash__: typing.ClassVar[None] = None
    x: float
    y: float
    z: float
    def __eq__(self, arg0: Double3) -> bool:
        ...
    @typing.overload
    def __getitem__(self, arg0: int) -> float:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> list:
        ...
    def __getstate__(self) -> tuple:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: float, arg1: float, arg2: float) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: typing.Sequence) -> None:
        ...
    def __len__(self) -> int:
        ...
    def __ne__(self, arg0: Double3) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    @typing.overload
    def __setitem__(self, arg0: int, arg1: float) -> None:
        ...
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: typing.Sequence) -> None:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
class Double4:
    """
    """
    __hash__: typing.ClassVar[None] = None
    w: float
    x: float
    y: float
    z: float
    def __eq__(self, arg0: Double4) -> bool:
        ...
    @typing.overload
    def __getitem__(self, arg0: int) -> float:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> list:
        ...
    def __getstate__(self) -> tuple:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: typing.Sequence) -> None:
        ...
    def __len__(self) -> int:
        ...
    def __ne__(self, arg0: Double4) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    @typing.overload
    def __setitem__(self, arg0: int, arg1: float) -> None:
        ...
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: typing.Sequence) -> None:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
class Float2:
    """
    
            Pair of floating point values. These can be accessed via the named attributes, `x` & `y`, but
            also support sequence access, making them work where a list or tuple is expected.
    
            >>> f = carb.Float2(1.0, 2.0)
            >>> f[0]
            1.0
            >>> f.y
            2.0
            
    """
    __hash__: typing.ClassVar[None] = None
    x: float
    y: float
    def __eq__(self, arg0: Float2) -> bool:
        ...
    @typing.overload
    def __getitem__(self, arg0: int) -> float:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> list:
        ...
    def __getstate__(self) -> tuple:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: float, arg1: float) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: typing.Sequence) -> None:
        ...
    def __len__(self) -> int:
        ...
    def __ne__(self, arg0: Float2) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    @typing.overload
    def __setitem__(self, arg0: int, arg1: float) -> None:
        ...
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: typing.Sequence) -> None:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
class Float3:
    """
    A triplet of floating point values. These can be accessed via the named attributes, `x`, `y` & `z`, but
            also support sequence access, making them work where a list or tuple is expected.
    
            >>> v = [1, 2, 3]
            f = carb.Float3(v)
            >>> f[0]
            1.0
            >>> f.y
            2.0
            >>> f[2]
            3.0
            
    """
    __hash__: typing.ClassVar[None] = None
    x: float
    y: float
    z: float
    def __eq__(self, arg0: Float3) -> bool:
        ...
    @typing.overload
    def __getitem__(self, arg0: int) -> float:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> list:
        ...
    def __getstate__(self) -> tuple:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: float, arg1: float, arg2: float) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: typing.Sequence) -> None:
        ...
    def __len__(self) -> int:
        ...
    def __ne__(self, arg0: Float3) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    @typing.overload
    def __setitem__(self, arg0: int, arg1: float) -> None:
        ...
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: typing.Sequence) -> None:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
class Float4:
    """
    A quadruplet of floating point values. These can be accessed via the named attributes, `x`, `y`, `z` & `w`,
            but also support sequence access, making them work where a list or tuple is expected.
    
            >>> v = [1, 2, 3, 4]
            f = carb.Float4(v)
            >>> f[0]
            1.0
            >>> f.y
            2.0
            >>> f[2]
            3.0
            >>> f.w
            4.0
            
    """
    __hash__: typing.ClassVar[None] = None
    w: float
    x: float
    y: float
    z: float
    def __eq__(self, arg0: Float4) -> bool:
        ...
    @typing.overload
    def __getitem__(self, arg0: int) -> float:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> list:
        ...
    def __getstate__(self) -> tuple:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: typing.Sequence) -> None:
        ...
    def __len__(self) -> int:
        ...
    def __ne__(self, arg0: Float4) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    @typing.overload
    def __setitem__(self, arg0: int, arg1: float) -> None:
        ...
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: typing.Sequence) -> None:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
class Framework:
    def breakpoint(self):
        ...
    def get_plugins(self) -> list[PluginDesc]:
        ...
    def load_plugins(self, loaded_file_wildcards: list[str] = [], search_paths: list[str] = []) -> None:
        ...
    def start_plugin(self, plugin: str) -> None:
        ...
    def startup(self, argv: list[str] = [], config: str = None, initial_plugins_search_paths: list[str] = [], config_format: str = 'toml') -> None:
        ...
    def try_reload_plugins(self) -> None:
        ...
    def unload_all_plugins(self) -> None:
        ...
    def wait_for_native_debugger(self, timeout, stop, quiet):
        ...
class Int2:
    """
    """
    __hash__: typing.ClassVar[None] = None
    x: int
    y: int
    def __eq__(self, arg0: Int2) -> bool:
        ...
    @typing.overload
    def __getitem__(self, arg0: int) -> int:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> list:
        ...
    def __getstate__(self) -> tuple:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: typing.Sequence) -> None:
        ...
    def __len__(self) -> int:
        ...
    def __ne__(self, arg0: Int2) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    @typing.overload
    def __setitem__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: typing.Sequence) -> None:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
class Int3:
    """
    """
    __hash__: typing.ClassVar[None] = None
    x: int
    y: int
    z: int
    def __eq__(self, arg0: Int3) -> bool:
        ...
    @typing.overload
    def __getitem__(self, arg0: int) -> int:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> list:
        ...
    def __getstate__(self) -> tuple:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int, arg2: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: typing.Sequence) -> None:
        ...
    def __len__(self) -> int:
        ...
    def __ne__(self, arg0: Int3) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    @typing.overload
    def __setitem__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: typing.Sequence) -> None:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
class Int4:
    """
    """
    __hash__: typing.ClassVar[None] = None
    w: int
    x: int
    y: int
    z: int
    def __eq__(self, arg0: Int4) -> bool:
        ...
    @typing.overload
    def __getitem__(self, arg0: int) -> int:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> list:
        ...
    def __getstate__(self) -> tuple:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: typing.Sequence) -> None:
        ...
    def __len__(self) -> int:
        ...
    def __ne__(self, arg0: Int4) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    @typing.overload
    def __setitem__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: typing.Sequence) -> None:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
class InterfaceDesc:
    def __repr__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def version(self) -> Version:
        ...
class PluginDesc:
    @property
    def dependencies(self) -> list[InterfaceDesc]:
        ...
    @property
    def impl(self) -> PluginImplDesc:
        ...
    @property
    def interfaces(self) -> list[InterfaceDesc]:
        ...
    @property
    def libPath(self) -> str:
        ...
class PluginHotReload:
    """
    Members:
    
      DISABLED
    
      ENABLED
    """
    DISABLED: typing.ClassVar[PluginHotReload]  # value = <PluginHotReload.DISABLED: 0>
    ENABLED: typing.ClassVar[PluginHotReload]  # value = <PluginHotReload.ENABLED: 1>
    __members__: typing.ClassVar[dict[str, PluginHotReload]]  # value = {'DISABLED': <PluginHotReload.DISABLED: 0>, 'ENABLED': <PluginHotReload.ENABLED: 1>}
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
class PluginImplDesc:
    @property
    def author(self) -> str:
        ...
    @property
    def build(self) -> str:
        ...
    @property
    def description(self) -> str:
        ...
    @property
    def hotReload(self) -> PluginHotReload:
        ...
    @property
    def name(self) -> str:
        ...
class Subscription:
    """
    
            Subscription holder.
    
            This object is returned by different subscription functions. Subscription lifetime is associated with this object. You can
            it while you need subscribed callback to be called. Then you can explicitly make it equal to `None` or call `unsubscribe` method or `del` it to unsubscribe.
    
            Quite common patter of usage is when you have a class which subscribes to various callbacks and you want to subscription to stay valid while class instance is alive.
    
            .. code-block:: python
    
                class Foo:
                    def __init__(self):
                        events = carb.events.get_events_interface()
                        stream = events.create_event_stream()
                        self._event_sub = stream.subscribe_to_pop(0, self._on_event)
    
                    def _on_event(self, e):
                        print(f'event {e}')
    
            >>> f = Foo()
            >>> # f receives some events
            >>> f._event_sub = None
            >>> f = None
            
    """
    def __init__(self, arg0: typing.Callable[[], None]) -> None:
        ...
    def unsubscribe(self) -> None:
        ...
class Uint2:
    """
    """
    __hash__: typing.ClassVar[None] = None
    x: int
    y: int
    def __eq__(self, arg0: Uint2) -> bool:
        ...
    @typing.overload
    def __getitem__(self, arg0: int) -> int:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> list:
        ...
    def __getstate__(self) -> tuple:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: typing.Sequence) -> None:
        ...
    def __len__(self) -> int:
        ...
    def __ne__(self, arg0: Uint2) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    @typing.overload
    def __setitem__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: typing.Sequence) -> None:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
class Uint3:
    """
    """
    __hash__: typing.ClassVar[None] = None
    x: int
    y: int
    z: int
    def __eq__(self, arg0: Uint3) -> bool:
        ...
    @typing.overload
    def __getitem__(self, arg0: int) -> int:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> list:
        ...
    def __getstate__(self) -> tuple:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int, arg2: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: typing.Sequence) -> None:
        ...
    def __len__(self) -> int:
        ...
    def __ne__(self, arg0: Uint3) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    @typing.overload
    def __setitem__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: typing.Sequence) -> None:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
class Uint4:
    """
    """
    __hash__: typing.ClassVar[None] = None
    w: int
    x: int
    y: int
    z: int
    def __eq__(self, arg0: Uint4) -> bool:
        ...
    @typing.overload
    def __getitem__(self, arg0: int) -> int:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> list:
        ...
    def __getstate__(self) -> tuple:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: typing.Sequence) -> None:
        ...
    def __len__(self) -> int:
        ...
    def __ne__(self, arg0: Uint4) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    @typing.overload
    def __setitem__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: typing.Sequence) -> None:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
class Version:
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    def __repr__(self) -> str:
        ...
    @property
    def major(self) -> int:
        ...
    @property
    def minor(self) -> int:
        ...
def answer_question(question: str) -> str:
    """
            This function can answer some questions.
    
            It currently only answers a limited set of questions so don't expect it to know everything.
    
            Args:
                question: The question passed to the function, trailing question mark is not necessary and
                    casing is not important.
    
            Returns:
                The answer to the question or empty string if it doesn't know the answer.
    """
def breakpoint() -> None:
    """
    Issues a hardware breakpoint.
    
    Warning: If a native debugger is not attached, this can cause an application
    error resulting in a crash.
    
    Args:
        None
    
    Returns:
        None
    """
def get_framework() -> ...:
    ...
def log(source: str, level: int, fileName: str, functionName: str, lineNumber: int, message: str) -> None:
    ...
def wait_for_native_debugger(timeout: float = -1.0, stop: bool = False, quiet: bool = False) -> bool:
    """
    Waits for a debugger to attach.
    
    Blocks (with GIL released) until a native debugger attaches to the process or a
    timeout occurs.
    
    Args:
        timeout: The time in seconds to wait. Negative values mean to wait forever.
                 A value of 0 will check if a native debugger is attached without
                 waiting. Optional, default value is -1.
        stop:    If True, a breakpoint is triggered immediately after a debugger
                 attaches. If a timeout is reached instead, no breakpoint is
                 triggered. Optional, default value is False.
        quiet:   When called if a debugger is not already attached a message is
                 printed to stdout unless this is True. Optional, default value is
                 False.
    
    Returns:
        True if a native debugger attached, False if a timeout is reached.
    """
