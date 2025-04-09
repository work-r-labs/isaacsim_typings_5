"""
This module contains bindings to C++ omni::kit::IApp interface, core C++ part of Omniverse Kit.

All the function are in omni.kit.IApp class, to get it use get_app_interface method, which caches
acquire interface call:

    >>> import omni.kit.app
    >>> a = omni.kit.app.get_app()
"""
from __future__ import annotations
from omni.kit.app._app import IApp
from omni.kit.app._app import IAppScripting
from omni.kit.app._app import acquire_app_interface
from omni.kit.app._app import crash
from omni.kit.app._impl import SettingChangeSubscription
from omni.kit.app._impl import _shutdown_kit_scripting
from omni.kit.app._impl import _startup_kit_scripting
from omni.kit.app._impl.app_iface import get_app
from omni.kit.app._impl.app_iface import get_app_interface
from omni.kit.app._impl import deprecated
from omni.kit.app._impl import log_deprecation
from omni.kit.app._impl import telemetry_helpers
from omni.kit.app._impl.telemetry_helpers import send_telemetry_event
from . import _app
from . import _impl
__all__ = ['APP_SCRIPTING_EVENT_COMMAND', 'APP_SCRIPTING_EVENT_STDERR', 'APP_SCRIPTING_EVENT_STDOUT', 'EVENT_APP_READY', 'EVENT_APP_STARTED', 'EVENT_ORDER_DEFAULT', 'IApp', 'IAppScripting', 'POST_QUIT_EVENT_TYPE', 'POST_UPDATE_ORDER_PYTHON_ASYNC_FUTURE', 'POST_UPDATE_ORDER_PYTHON_EXEC', 'PRE_SHUTDOWN_EVENT_TYPE', 'RUN_LOOP_DEFAULT', 'RUN_LOOP_RENDERING', 'RUN_LOOP_SIMULATION', 'RUN_LOOP_UI', 'SettingChangeSubscription', 'UPDATE_ORDER_FABRIC_FLUSH', 'UPDATE_ORDER_HYDRA_RENDER', 'UPDATE_ORDER_PYTHON_ASYNC_FUTURE_BEGIN_UPDATE', 'UPDATE_ORDER_PYTHON_ASYNC_FUTURE_END_UPDATE', 'UPDATE_ORDER_PYTHON_EXEC_BEGIN_UPDATE', 'UPDATE_ORDER_PYTHON_EXEC_END_UPDATE', 'UPDATE_ORDER_UI_RENDER', 'UPDATE_ORDER_UNSPECIFIED', 'UPDATE_ORDER_USD', 'acquire_app_interface', 'crash', 'deprecated', 'get_app', 'get_app_interface', 'log_deprecation', 'send_telemetry_event', 'telemetry_helpers']
APP_SCRIPTING_EVENT_COMMAND: int = 0
APP_SCRIPTING_EVENT_STDERR: int = 2
APP_SCRIPTING_EVENT_STDOUT: int = 1
EVENT_APP_READY: int = 6559629015549994352
EVENT_APP_STARTED: int = 4314192531916293802
EVENT_ORDER_DEFAULT: int = 0
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
