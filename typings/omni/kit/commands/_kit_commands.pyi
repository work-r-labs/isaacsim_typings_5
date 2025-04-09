"""
pybind11 omni.kit.commands bindings
"""
from __future__ import annotations
import typing
__all__ = ['ICommand', 'ICommandBridge', 'acquire_command_bridge', 'release_command_bridge']
class ICommand:
    def do(self) -> None:
        """
                     Called when this command object is being executed,
                     either originally or in response to a redo request.
        """
    def undo(self) -> None:
        """
                     Called when this command object is being undone.
        """
class ICommandBridge:
    def create_cpp_command_object(self, extension_id: str, command_name: str, **kwargs) -> ...:
        """
                     Bridge function to call from Python to create a new instance of a C++ command.
        
                     Args:
                         extension_id: The id of the source extension that registered the command.
                         command_name: The command name, unique to the extension that registered it.
                         **kwargs: Arbitrary keyword arguments that the command will be executed with.
        
                     Return:
                         The command object if it was created, an empty object otherwise.
        """
    def disable(self) -> None:
        """
                     Disable the command bridge so that new command types can no longer be registered and deregistered from C++,
                     and so that existing command types can no longer be executed in Python (where commands are held) from C++.
                     Calling this will also cause any remaining command types previously registered in C++ to be deregistered.
        """
    def enable(self, register_function: typing.Callable, deregister_function: typing.Callable, execute_function: typing.Callable, undo_function: typing.Callable, redo_function: typing.Callable, repeat_function: typing.Callable, begin_undo_group_function: typing.Callable, end_undo_group_function: typing.Callable, begin_undo_disabled_function: typing.Callable, end_undo_disabled_function: typing.Callable) -> None:
        """
                     Enable the command bridge so that new command types can be registered and deregistered from C++,
                     and so that existing command types can be executed in Python (where commands are held) from C++.
        
                     Args:
                         register_function: Function responsible for registering new C++ command types with Python.
                         deregister_function: Function responsible for deregistering C++ command types from Python.
                         execute_function: Function responsible for executing existing commands in Python from C++.
        """
def acquire_command_bridge(plugin_name: str = None, library_path: str = None) -> ICommandBridge:
    ...
def release_command_bridge(arg0: ICommandBridge) -> None:
    ...
