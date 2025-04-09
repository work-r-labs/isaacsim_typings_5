from __future__ import annotations
from carb._carb import ColorRgb
from carb._carb import ColorRgbDouble
from carb._carb import ColorRgba
from carb._carb import ColorRgbaDouble
from carb._carb import Double2
from carb._carb import Double3
from carb._carb import Double4
from carb._carb import Float2
from carb._carb import Float3
from carb._carb import Float4
from carb._carb import Framework
from carb._carb import Int2
from carb._carb import Int3
from carb._carb import Int4
from carb._carb import InterfaceDesc
from carb._carb import PluginDesc
from carb._carb import PluginHotReload
from carb._carb import PluginImplDesc
from carb._carb import Subscription
from carb._carb import Uint2
from carb._carb import Uint3
from carb._carb import Uint4
from carb._carb import Version
from carb._carb import answer_question
from carb._carb import breakpoint
from carb._carb import filesystem
from carb._carb import get_framework
from carb._carb import log
from carb._carb import logging
from carb._carb import wait_for_native_debugger
import sys as sys
from . import _carb
from . import audio
from . import dictionary
from . import eventdispatcher
from . import events
from . import input
from . import profiler
from . import settings
from . import tokens
from . import variant
from . import windowing
__all__ = ['ColorRgb', 'ColorRgbDouble', 'ColorRgba', 'ColorRgbaDouble', 'Double2', 'Double3', 'Double4', 'Float2', 'Float3', 'Float4', 'Framework', 'Int2', 'Int3', 'Int4', 'InterfaceDesc', 'PluginDesc', 'PluginHotReload', 'PluginImplDesc', 'Subscription', 'Uint2', 'Uint3', 'Uint4', 'Version', 'answer_question', 'audio', 'breakpoint', 'dictionary', 'eventdispatcher', 'events', 'filesystem', 'get_framework', 'input', 'log', 'log_error', 'log_info', 'log_verbose', 'log_warn', 'logging', 'profiler', 'settings', 'sys', 'tokens', 'variant', 'wait_for_native_debugger', 'windowing']
def _get_caller_info():
    ...
def log_error(msg):
    ...
def log_info(msg):
    ...
def log_verbose(msg):
    ...
def log_warn(msg):
    ...
__copyright__: str = 'Copyright (c) 2018-2021, NVIDIA CORPORATION. All rights reserved.'
__license__: str = '\nNVIDIA CORPORATION and its licensors retain all intellectual property\nand proprietary rights in and to this software, related documentation\nand any modifications thereto. Any use, reproduction, disclosure or\ndistribution of this software and related documentation without an express\nlicense agreement from NVIDIA CORPORATION is strictly prohibited.\n'
