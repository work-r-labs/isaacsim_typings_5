from __future__ import annotations
import os as os
import sys as sys
from . import _physicsSchemaTools
from . import units
from . import units_db
__all__: list[str] = ['current_version', 'os', 'py38', 'sys', 'units', 'units_db']
__MFB_FULL_PACKAGE_NAME: str = 'physicsSchemaTools'
current_version: sys.version_info  # value = sys.version_info(major=3, minor=11, micro=13, releaselevel='final', serial=0)
py38: tuple = (3, 8)
