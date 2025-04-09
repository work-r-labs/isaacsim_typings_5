from __future__ import annotations
from omni.kit.viewport.window.events.delegate import ViewportEventDelegate
from omni.kit.viewport.window.events.delegate import ViewportEventDelegate as _ui_delegate_setup
from . import delegate
__all__: list = ['ViewportEventDelegate', 'add_event_delegation', 'remove_event_delegation', 'set_ui_delegate']
def add_event_delegation(scene_view, viewport_api):
    ...
def remove_event_delegation(in_scene_view):
    ...
def set_ui_delegate(ui_delegate_setup):
    ...
_ui_delegate_list: list  # value = [<omni.kit.viewport.window.events.delegate.ViewportEventDelegate object>]
