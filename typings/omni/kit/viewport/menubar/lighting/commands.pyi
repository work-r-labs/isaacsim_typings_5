from __future__ import annotations
import omni as omni
from omni.kit.viewport.menubar.lighting.actions import _set_lighting_mode
import typing
__all__ = ['SetLightingMenuModeCommand', 'omni', 'register_commands', 'unregister_commands']
class SetLightingMenuModeCommand(omni.kit.commands.command.Command):
    """
    
        Set the current lighting rig
    
        Args:
            lighting_mode: (str) The lgihting mode to set to
            usd_context_name: (str) The UsdContext to target
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, lighting_mode: str, usd_context_name: str = '', *args, **kwargs):
        ...
    def do(self):
        ...
    def undo(self):
        ...
def register_commands():
    ...
def unregister_commands(cmds):
    ...
