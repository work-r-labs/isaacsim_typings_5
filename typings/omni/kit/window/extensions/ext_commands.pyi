"""
This module defines a command for enabling or disabling extensions in the omni.kit application.
"""
from __future__ import annotations
import omni as omni
import typing
__all__: list = ['ToggleExtension']
class ToggleExtension(omni.kit.commands.command.Command):
    """
    Toggle extension **Command**.  Enables/disables an extension.
    
        Args:
            ext_id (str): Extension id.
            enable (bool): Enable or disable.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, ext_id: str, enable: bool):
        """
        Initializes the command to toggle an extension's enabled state.
        """
    def do(self):
        """
        Executes the command to enable or disable the specified extension.
        """
