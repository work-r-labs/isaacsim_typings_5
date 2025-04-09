from __future__ import annotations
import asyncio as asyncio
import carb as carb
from carb.profiler._profiler import FlowType
from carb.profiler._profiler import IProfileMonitor
from carb.profiler._profiler import IProfiler
from carb.profiler._profiler import InstantType
from carb.profiler._profiler import ProfileEvents
from carb.profiler._profiler import acquire_profile_monitor_interface
from carb.profiler._profiler import acquire_profiler_interface
from carb.profiler._profiler import begin_with_location
from carb.profiler._profiler import end
from carb.profiler._profiler import is_profiler_active
from carb.profiler._profiler import supports_dynamic_source_locations
import functools as functools
from . import _profiler
__all__ = ['FlowType', 'IProfileMonitor', 'IProfiler', 'InstantType', 'ProfileEvents', 'acquire_profile_monitor_interface', 'acquire_profiler_interface', 'asyncio', 'begin', 'begin_with_location', 'carb', 'end', 'functools', 'is_profiler_active', 'profile', 'supports_dynamic_source_locations']
def begin(mask, name, stack_offset = 0):
    ...
def profile(func = None, mask = 1, zone_name = None, add_args = False):
    """
    Decorator to profile function call
    
        Example:
    
        .. code-block:: python
    
            import carb.profiler
    
            @carb.profiler.profile
            def foo():
                pass
    
            # Or:
            @carb.profiler.profile(mask=10, zone_name="Foonction", add_args=True)
            def foo():
                pass
        
    """
__copyright__: str = 'Copyright (c) 2020-2021, NVIDIA CORPORATION. All rights reserved.'
__license__: str = '\nNVIDIA CORPORATION and its licensors retain all intellectual property\nand proprietary rights in and to this software, related documentation\nand any modifications thereto. Any use, reproduction, disclosure or\ndistribution of this software and related documentation without an express\nlicense agreement from NVIDIA CORPORATION is strictly prohibited.\n'
