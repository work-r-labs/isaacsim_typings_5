"""
This module extends several metadata for instructing UX implementation, and it provides APIs for accessing those metadata.
"""
from __future__ import annotations
from omni.usd.editor.editor import get_display_name
from omni.usd.editor.editor import is_always_pick_model
from omni.usd.editor.editor import is_hide_in_stage_window
from omni.usd.editor.editor import is_hide_in_ui
from omni.usd.editor.editor import is_no_delete
from omni.usd.editor.editor import set_always_pick_model
from omni.usd.editor.editor import set_display_name
from omni.usd.editor.editor import set_hide_in_stage_window
from omni.usd.editor.editor import set_hide_in_ui
from omni.usd.editor.editor import set_no_delete
from pxr import Usd
from . import editor
__all__: list = ['HIDE_IN_STAGE_WINDOW', 'NO_DELETE', 'ALWAYS_PICK_MODEL', 'DISPLAY_NAME', 'set_hide_in_stage_window', 'is_hide_in_stage_window', 'set_no_delete', 'is_no_delete', 'set_always_pick_model', 'is_always_pick_model', 'set_hide_in_ui', 'is_hide_in_ui', 'set_display_name', 'get_display_name']
ALWAYS_PICK_MODEL: str = 'always_pick_model'
DISPLAY_NAME: str = 'displayName'
HIDE_IN_STAGE_WINDOW: str = 'hide_in_stage_window'
HIDE_IN_UI: str = 'omni:kit:hideInUI'
NO_DELETE: str = 'no_delete'
