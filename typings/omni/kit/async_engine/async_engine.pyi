"""
Asynchronous tasks engine for Omniverse Kit.

It runs :mod:`asyncio` ``EventLoop`` every update for one iteration (all scheduled tasks).
"""
from __future__ import annotations
import asyncio as asyncio
from asyncio import events
import carb as carb
import collections.abc
from collections.abc import Coroutine
from contextlib import suppress
import logging as logging
import omni as omni
from omni.kit.main_event_loop_wrapper.main_event_loop_wrapper import MainEventLoopWrapper
import platform as platform
import sys as sys
import threading as threading
__all__ = ['Coroutine', 'MainEventLoopWrapper', 'asyncio', 'carb', 'events', 'logger', 'logging', 'omni', 'platform', 'run_coroutine', 'suppress', 'sys', 'threading']
class _AsyncEngineDriver(omni.ext._extensions.IExt):
    """
    
        Singleton class to connect python asyncio with app update pump. EventLoop runs iteration every IApp update.
        
    """
    def _patch_event_loop(self, loop_until_done):
        """
        Monkey-patch the event loop either to keep it always running or just to add a simple run_once function
        """
    def on_shutdown(self):
        """
        Clean event loop and all running async task on extension shutdown
        """
    def on_startup(self):
        """
         Init settings and path event loop on extension startup
        """
def run_coroutine(coroutine: collections.abc.Coroutine):
    """
    Submit a coroutine object to the main event loop; return either a Task object
        if the function was called from the main thread, or a concurrent.futures.Future to access
        the result if the function was called from any other non-main thread.
    
        Args:
            coroutine (:obj:`coroutine`): The coroutine to schedule for execution.
    
        Returns:
            Union[:obj:`asyncio.Task`, :obj:`concurrent.futures.Future`]: An asyncio.Task if called from the main thread, otherwise a concurrent.futures.Future.
    
        Raises:
            TypeError: If the provided coroutine is not an actual coroutine object.
    """
logger: logging.Logger  # value = <Logger omni.kit.async_engine.async_engine (DEBUG)>
