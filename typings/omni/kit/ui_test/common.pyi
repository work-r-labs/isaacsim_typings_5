from __future__ import annotations
import asyncio as asyncio
import carb as carb
import logging as logging
import omni as omni
import sys as sys
__all__ = ['InitExt', 'asyncio', 'carb', 'human_delay', 'logger', 'logging', 'omni', 'setup_logging', 'sys', 'wait_n_updates', 'wait_n_updates_internal']
class InitExt(omni.ext._extensions.IExt):
    def on_startup(self):
        ...
def human_delay(human_delay_speed: int = 2):
    """
    Imitate human delay/slowness.
    
        In practice that function just waits couple of frames, but semantically it is different from other wait function.
        It is used when we want to wait because it would look like normal person interaction. E.g. instead of moving mouse
        and clicking with speed of light wait a bit.
    
        This is also a place where delay can be increased with a setting to debug UI tests.
        
    """
def setup_logging():
    ...
def wait_n_updates(update_count = 2):
    """
    Wait N updates (frames).
    """
def wait_n_updates_internal(update_count = 2):
    ...
logger: logging.Logger  # value = <Logger omni.kit.ui_test.common (DEBUG)>
