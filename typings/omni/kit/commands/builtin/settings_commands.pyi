from __future__ import annotations
import carb as carb
import omni as omni
import typing
__all__ = ['ChangeDraggableSettingCommand', 'ChangeSettingCommand', 'carb', 'omni']
class ChangeDraggableSettingCommand(omni.kit.commands.command.Command):
    """
    
        Change draggable setting **Command**.
    
        Args:
            path: Path to the setting to change.
            value: New value to change to.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, path, value):
        ...
    def do(self):
        ...
class ChangeSettingCommand(omni.kit.commands.command.Command):
    """
    
        Change setting **Command**.
    
        Args:
            path: Path to the setting to change.
            value: New value to change to.
            prev: Previous value to for undo operation. If `None` current value would be saved as previous.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, path, value, prev = None):
        ...
    def do(self):
        ...
    def undo(self):
        ...
