from __future__ import annotations
import asyncio as asyncio
import carb as carb
from functools import lru_cache
import omni.kit.app._app
from omni.kit.app._app import IApp
from omni.kit.app._app import IAppScripting
from omni.kit.app._app import acquire_app_interface
from omni.kit.app._app import crash
__all__ = ['APP_SCRIPTING_EVENT_COMMAND', 'APP_SCRIPTING_EVENT_STDERR', 'APP_SCRIPTING_EVENT_STDOUT', 'EVENT_APP_READY', 'EVENT_APP_STARTED', 'EVENT_ORDER_DEFAULT', 'GLOBAL_EVENT_APP_READY', 'GLOBAL_EVENT_APP_STARTED', 'GLOBAL_EVENT_POST_QUIT', 'GLOBAL_EVENT_PRE_SHUTDOWN', 'GLOBAL_EVENT_SCRIPT_COMMAND', 'GLOBAL_EVENT_SCRIPT_COMMAND_IMMEDIATE', 'GLOBAL_EVENT_SCRIPT_STDERR', 'GLOBAL_EVENT_SCRIPT_STDERR_IMMEDIATE', 'GLOBAL_EVENT_SCRIPT_STDOUT', 'GLOBAL_EVENT_SCRIPT_STDOUT_IMMEDIATE', 'IApp', 'IAppScripting', 'POST_QUIT_EVENT_TYPE', 'POST_UPDATE_ORDER_PYTHON_ASYNC_FUTURE', 'POST_UPDATE_ORDER_PYTHON_EXEC', 'PRE_SHUTDOWN_EVENT_TYPE', 'RUN_LOOP_DEFAULT', 'RUN_LOOP_RENDERING', 'RUN_LOOP_SIMULATION', 'RUN_LOOP_UI', 'UPDATE_ORDER_FABRIC_FLUSH', 'UPDATE_ORDER_HYDRA_RENDER', 'UPDATE_ORDER_PYTHON_ASYNC_FUTURE_BEGIN_UPDATE', 'UPDATE_ORDER_PYTHON_ASYNC_FUTURE_END_UPDATE', 'UPDATE_ORDER_PYTHON_EXEC_BEGIN_UPDATE', 'UPDATE_ORDER_PYTHON_EXEC_END_UPDATE', 'UPDATE_ORDER_UI_RENDER', 'UPDATE_ORDER_UNSPECIFIED', 'UPDATE_ORDER_USD', 'acquire_app_interface', 'asyncio', 'carb', 'crash', 'get_app', 'get_app_interface', 'lru_cache']
def _next_update_async(self) -> float:
    """
    Wait for next update of Omniverse Kit. Return delta time in seconds
    """
def _post_update_async(self) -> float:
    ...
def _pre_update_async(self) -> float:
    """
    Wait for next update of Omniverse Kit. Return delta time in seconds
    """
def get_app() -> omni.kit.app._app.IApp:
    """
    Returns cached :class:`omni.kit.app.IApp` interface. (shorthand)
    """
def get_app_interface(*args, **kwargs):
    """
    Returns cached :class:`omni.kit.app.IApp` interface
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
