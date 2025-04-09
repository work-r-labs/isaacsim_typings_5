from __future__ import annotations
import asyncio as asyncio
import carb as carb
import collections as collections
from functools import lru_cache
import logging as logging
import omni as omni
from omni.kit.app._app import IApp
from omni.kit.app._app import IAppScripting
from omni.kit.app._app import acquire_app_interface
from omni.kit.app._app import crash
from omni.kit.app._impl.app_iface import get_app
from omni.kit.app._impl.app_iface import get_app_interface
from omni.kit.app._impl.telemetry_helpers import send_telemetry_event
import os as os
import sys as sys
import traceback as traceback
from . import app_iface
from . import telemetry_helpers
__all__: list = ['APP_SCRIPTING_EVENT_COMMAND', 'APP_SCRIPTING_EVENT_STDOUT', 'APP_SCRIPTING_EVENT_STDERR', 'RUN_LOOP_DEFAULT', 'RUN_LOOP_SIMULATION', 'RUN_LOOP_RENDERING', 'RUN_LOOP_UI', 'POST_QUIT_EVENT_TYPE', 'PRE_SHUTDOWN_EVENT_TYPE', 'EVENT_APP_STARTED', 'EVENT_APP_READY', 'EVENT_ORDER_DEFAULT', 'UPDATE_ORDER_PYTHON_ASYNC_FUTURE_BEGIN_UPDATE', 'UPDATE_ORDER_PYTHON_ASYNC_FUTURE_END_UPDATE', 'UPDATE_ORDER_PYTHON_EXEC_BEGIN_UPDATE', 'UPDATE_ORDER_PYTHON_EXEC_END_UPDATE', 'UPDATE_ORDER_USD', 'UPDATE_ORDER_UNSPECIFIED', 'UPDATE_ORDER_FABRIC_FLUSH', 'UPDATE_ORDER_HYDRA_RENDER', 'UPDATE_ORDER_UI_RENDER', 'POST_UPDATE_ORDER_PYTHON_ASYNC_FUTURE', 'POST_UPDATE_ORDER_PYTHON_EXEC', 'IApp', 'acquire_app_interface', 'IAppScripting', 'crash', 'get_app_interface', 'get_app', 'telemetry_helpers', 'send_telemetry_event', 'log_deprecation', 'deprecated', 'SettingChangeSubscription']
class SettingChangeSubscription:
    """
    
        Setting change subscription wrapper to make it scoped (auto unsubscribe on del)
        
    """
    def __del__(self):
        ...
    def __init__(self, path: str, on_change: typing.Callable):
        ...
class StreamInterceptor:
    def __getattr__(self, attr):
        ...
    def __init__(self, mq, is_stdout, log_std):
        ...
    def flush(self):
        ...
    def isatty(self):
        ...
    def write(self, msg):
        ...
class _CarbLogHandler(logging.StreamHandler):
    """
    
        A handler class to redirect all python logs into carb logger.
        
    """
    def emit(self, record):
        ...
def _gc_profile_callback(phase, info):
    ...
def _is_developer_warnings_enabled(*args, **kwargs):
    ...
def _set_default_and_get_setting(path, default = None):
    ...
def _setup_gc():
    ...
def _shutdown_kit_scripting():
    ...
def _startup_kit_scripting():
    """
    Internal method to be called by IApp.
    
        Setups stdout and stderr interceptors to push them into IApp's scripting event stream.
        
    """
def _toggle_gc_profiling(enable: bool):
    ...
def deprecated(message = ''):
    """
    Decorator which can be used to mark functions or classes as deprecated. It will result in warn log when the function is used or a class is instantiated.
    """
def log_deprecation(message: str):
    """
    Log deprecation message.
    """
APP_SCRIPTING_EVENT_COMMAND: int = 0
APP_SCRIPTING_EVENT_STDERR: int = 2
APP_SCRIPTING_EVENT_STDOUT: int = 1
EVENT_APP_READY: int = 6559629015549994352
EVENT_APP_STARTED: int = 4314192531916293802
EVENT_ORDER_DEFAULT: int = 0
GLOBAL_EVENT_APP_READY: str = 'omni.kit.app:ready'
GLOBAL_EVENT_APP_STARTED: str = 'omni.kit.app:started'
GLOBAL_EVENT_POST_QUIT: str = 'omni.kit.app:post_quit'
GLOBAL_EVENT_PRE_SHUTDOWN: str = 'omni.kit.app:pre_shutdown'
GLOBAL_EVENT_SCRIPT_COMMAND: str = 'omni.kit.app:script_command'
GLOBAL_EVENT_SCRIPT_COMMAND_IMMEDIATE: str = 'omni.kit.app:script_command:immediate'
GLOBAL_EVENT_SCRIPT_STDERR: str = 'omni.kit.app:script_stderr'
GLOBAL_EVENT_SCRIPT_STDERR_IMMEDIATE: str = 'omni.kit.app:script_stderr:immediate'
GLOBAL_EVENT_SCRIPT_STDOUT: str = 'omni.kit.app:script_stdout'
GLOBAL_EVENT_SCRIPT_STDOUT_IMMEDIATE: str = 'omni.kit.app:script_stdout:immediate'
POST_QUIT_EVENT_TYPE: int = 0
POST_UPDATE_ORDER_PYTHON_ASYNC_FUTURE: int = -25
POST_UPDATE_ORDER_PYTHON_EXEC: int = -10
PRE_SHUTDOWN_EVENT_TYPE: int = 1
RUN_LOOP_DEFAULT: str = 'main'
RUN_LOOP_RENDERING: str = 'rendering'
RUN_LOOP_SIMULATION: str = 'simulation'
RUN_LOOP_UI: str = 'ui'
UPDATE_ORDER_FABRIC_FLUSH: int = 20
UPDATE_ORDER_HYDRA_RENDER: int = 30
UPDATE_ORDER_PYTHON_ASYNC_FUTURE_BEGIN_UPDATE: int = -50
UPDATE_ORDER_PYTHON_ASYNC_FUTURE_END_UPDATE: int = 50
UPDATE_ORDER_PYTHON_EXEC_BEGIN_UPDATE: int = -45
UPDATE_ORDER_PYTHON_EXEC_END_UPDATE: int = 100
UPDATE_ORDER_UI_RENDER: int = 15
UPDATE_ORDER_UNSPECIFIED: int = 0
UPDATE_ORDER_USD: int = -10
_app_ready_sub: carb.eventdispatcher._eventdispatcher.ObserverGuard  # value = <carb.eventdispatcher._eventdispatcher.ObserverGuard object>
_logLevelToCarbLogLevel: dict = {50: 2, 40: 1, 30: 0, 20: -1, 10: -2, 0: -2}
