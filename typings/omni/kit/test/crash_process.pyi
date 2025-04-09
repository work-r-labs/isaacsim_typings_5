from __future__ import annotations
import asyncio as asyncio
__all__ = ['asyncio', 'crash_process']
def _crash_process_win(pid, timeout = 30):
    ...
def _warning(stream, msg):
    ...
def crash_process(process, stream, timeout = 60):
    """
    
        Triggers a crash dump in the test process, terminating the process.
    
        Returns True if the test process was terminated, False if the process is still running.
        
    """
