from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.actions.core.actions import get_action_registry
__all__ = ['carb', 'deregister_hotkeys', 'get_action_registry', 'omni', 'register_hotkeys']
def deregister_hotkeys(extension_id: str):
    ...
def register_hotkeys(extension_id: str, window_name: typing.Optional[str] = None):
    ...
_HOTKEYS_EXT: str = 'omni.kit.hotkeys.core'
