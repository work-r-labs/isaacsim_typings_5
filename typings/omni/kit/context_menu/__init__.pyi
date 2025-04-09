"""

Context menu implementation classes. This is the full context menu seen in viewport and stage windows.
"""
from __future__ import annotations
from omni.kit.context_menu.scripts import context_menu
from omni.kit.context_menu.scripts.context_menu import ContextMenuExtension
from omni.kit.context_menu.scripts.context_menu import close_menu
from omni.kit.context_menu.scripts.context_menu import get_hovered_prim
from omni.kit.context_menu.scripts.context_menu import get_instance
from omni.kit.context_menu.scripts.context_menu import post_notification
from omni.kit.context_menu.scripts import singleton
from omni.kit.context_menu.scripts import style
from omni.kit.context_menu.scripts import viewport_menu
from omni.kit.context_menu.scripts.viewport_menu import ViewportMenu
from omni.kit.widget.context_menu.context_menu import get_instance as get_widget_instance
from omni.kit.widget.context_menu.context_menu import reorder_menu_dict
from omni.kit.widget.context_menu.custom_menu_dict import add_menu
from omni.kit.widget.context_menu.custom_menu_dict import get_menu_dict
from omni.kit.widget.context_menu.custom_menu_dict import get_menu_event_stream
from . import scripts
__all__ = ['ContextMenuExtension', 'SETTING_HIDE_CREATE_MENU', 'ViewportMenu', 'add_menu', 'close_menu', 'context_menu', 'get_hovered_prim', 'get_instance', 'get_menu_dict', 'get_menu_event_stream', 'get_widget_instance', 'post_notification', 'reorder_menu_dict', 'scripts', 'singleton', 'style', 'viewport_menu']
SETTING_HIDE_CREATE_MENU: str = '/exts/omni.kit.context_menu/hideCreateMenu'
