from __future__ import annotations
import asyncio.unix_events
import typing
__all__ = ['MainEventLoopWrapper']
class MainEventLoopWrapper:
    """
    Wrapper class to store a global, inter-module accessible, persistent copy of the main event loop.
    """
    g_main_event_loop: typing.ClassVar[asyncio.unix_events._UnixSelectorEventLoop]  # value = <_UnixSelectorEventLoop running=True closed=False debug=False>
