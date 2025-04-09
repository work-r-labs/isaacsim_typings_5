"""
Commands for Omniverse Kit.

:mod:`omni.kit.commands` module is used to register and execute **Commands**. It is built on top of :mod:`omni.kit.undo` module to enable undo/redo operations with **Commands**.

**Command** is any class with ``do()`` method and optionally ``undo()`` method. If **Command** has ``undo()`` method it is put on the undo stack when executed.
It must be inherited from :class:`Command` class for type checking.

Example of creating your command, registering it, passing arguments and undoing.

.. code-block:: python

    class MyOrange(omni.kit.commands.Command):
        def __init__(self, bar: list):
            self._bar = bar

        def do(self):
            self._bar.append('orange')

        def undo(self):
            del self._bar[-1]

>>> import omni.kit.commands
>>> omni.kit.commands.register(MyOrangeCommand)
>>> my_list = []
>>> omni.kit.commands.execute("MyOrange", bar=my_list)
>>> my_list
['orange']
>>> import omni.kit.undo
>>> omni.kit.undo.undo()
>>> my_list
[]
>>> omni.kit.undo.redo()
>>> my_list
['orange']

"""
from __future__ import annotations
import omni as omni
from omni.kit.commands.command import Command
from omni.kit.commands.command import _log_error
from omni.kit.commands.command import create
from omni.kit.commands.command import execute
from omni.kit.commands.command import execute_argv
from omni.kit.commands.command import get_argument_parser_from_function
from omni.kit.commands.command import get_command_class
from omni.kit.commands.command import get_command_class_signature
from omni.kit.commands.command import get_command_doc
from omni.kit.commands.command import get_command_parameters
from omni.kit.commands.command import get_commands
from omni.kit.commands.command import get_commands_list
from omni.kit.commands.command import register
from omni.kit.commands.command import register_all_commands_in_module
from omni.kit.commands.command import register_callback
from omni.kit.commands.command import set_logging_enabled
from omni.kit.commands.command import unregister
from omni.kit.commands.command import unregister_callback
from omni.kit.commands.command import unregister_module_commands
from omni.kit.commands.command_actions import deregister_actions
from omni.kit.commands.command_actions import register_actions
from omni.kit.commands.command_bridge import CommandBridge
from omni.kit.commands.on_change import _dispatch_changed
from omni.kit.commands.on_change import subscribe_on_change
from omni.kit.commands.on_change import unsubscribe_on_change
from . import _kit_commands
from . import builtin
from . import command
from . import command_actions
from . import command_bridge
from . import on_change
__all__: list = ['Command', 'create', 'register', 'register_all_commands_in_module', 'unregister_module_commands', 'unregister', 'PRE_DO_CALLBACK', 'POST_DO_CALLBACK', 'PRE_UNDO_CALLBACK', 'POST_UNDO_CALLBACK', 'register_callback', 'unregister_callback', 'get_command_class', 'get_command_class_signature', 'get_command_doc', 'get_command_parameters', 'get_commands', 'get_commands_list', 'execute', 'execute_argv', 'get_argument_parser_from_function', 'set_logging_enabled', 'subscribe_on_change', 'unsubscribe_on_change']
class CommandExt(omni.ext._extensions.IExt):
    """
    Monitor for new extensions and register all commands in python modules of those extensions,
           along with setting up a bridge that allows commands to be registered and executed from C++,
           and registration of actions that wrap some basic command functionality like undo and redo.
        
    """
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id):
        ...
POST_DO_CALLBACK: str = 'post_do'
POST_UNDO_CALLBACK: str = 'post_undo'
PRE_DO_CALLBACK: str = 'pre_do'
PRE_UNDO_CALLBACK: str = 'pre_undo'
