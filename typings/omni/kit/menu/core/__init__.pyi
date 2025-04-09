"""

Core menu class. Used by omni.kit.menu.utils and omni.kit.context_menu to build menus.
"""
from __future__ import annotations
from omni.kit.menu.core.core import DictReadOnly
from omni.kit.menu.core.core import IconMenuBaseDelegate
from omni.kit.menu.core.core import MenuEventType
from omni.kit.menu.core.core import has_delegate_func
from omni.kit.menu.core.core import uiMenu
from omni.kit.menu.core.core import uiMenuItem
from . import core
__all__ = ['DictReadOnly', 'IconMenuBaseDelegate', 'MenuEventType', 'core', 'has_delegate_func', 'uiMenu', 'uiMenuItem']
