from __future__ import annotations
import asyncio as asyncio
import carb as carb
import omni as omni
from omni.kit.window.console.scripts.console_command import CommandManager
from omni.kit.window.console.scripts.console_command import console_log_info
from omni import ui
__all__: list[str] = ['CommandInput', 'CommandManager', 'asyncio', 'carb', 'console_log_info', 'omni', 'ui']
class CommandInput:
    def _CommandInput__on_command_input_changed(self, model) -> None:
        ...
    def _CommandInput__on_command_input_end(self, model) -> None:
        ...
    def _CommandInput__on_mouse_released(self, btn: int) -> None:
        ...
    def __init__(self, command_manager: omni.kit.window.console.scripts.console_command.CommandManager, cmd_input_visible_model: omni.ui._ui.SimpleBoolModel) -> None:
        """
        
                Input field for command.
        
                Args:
                    command_manager (CommandManager): Manager to execute commands.
                    cmd_input_visible_model (ui.SimpleBoolModel): Model to show/hide command input.
                
        """
    def _build_ui(self) -> None:
        ...
    def _focus(self):
        ...
    def destroy(self):
        ...
