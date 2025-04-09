from __future__ import annotations
from lula import LogLevel
from lula import set_default_logger_prefix
from lula import set_log_level
import omni as omni
import os as os
import pathlib as pathlib
__all__ = ['Extension', 'LogLevel', 'omni', 'os', 'pathlib', 'set_default_logger_prefix', 'set_log_level']
class Extension(omni.ext._extensions.IExt):
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id):
        ...
