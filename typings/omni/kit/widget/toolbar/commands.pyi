from __future__ import annotations
import omni as omni
import typing
__all__: list = ['ToolbarPlayButtonClickedCommand', 'ToolbarPauseButtonClickedCommand', 'ToolbarStopButtonClickedCommand', 'ToolbarPlayFilterCheckedCommand', 'ToolbarPlayFilterSelectAllCommand']
class ToolbarPauseButtonClickedCommand(omni.kit.commands.command.Command):
    """
    
        On clicked toolbar pause button **Command**.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def do(self):
        ...
class ToolbarPlayButtonClickedCommand(omni.kit.commands.command.Command):
    """
    
        On clicked toolbar play button **Command**.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def do(self):
        ...
class ToolbarPlayFilterCheckedCommand(omni.kit.commands.command.Command):
    """
    
        Change settings depending on the status of play filter checkboxes **Command**.
    
        Args:
            path: Path to the setting to change.
            enabled: New value to change to.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, setting_path, enabled):
        ...
    def do(self):
        ...
    def undo(self):
        ...
class ToolbarPlayFilterSelectAllCommand(omni.kit.commands.command.Command):
    """
    
        Sets all play filter settings to True **Command**.
    
        Args:
            settings: Paths to the settings.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, settings):
        ...
    def do(self):
        ...
    def undo(self):
        ...
class ToolbarStopButtonClickedCommand(omni.kit.commands.command.Command):
    """
    
        On clicked toolbar stop button **Command**.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def do(self):
        ...
