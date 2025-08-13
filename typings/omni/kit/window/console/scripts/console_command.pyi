from __future__ import annotations
import carb as carb
import omni as omni
__all__: list[str] = ['AUTOEXEC_LIST_FILE', 'CloseCommand', 'CommandManager', 'ConsoleCommand', 'EXPECTED_SCRIPT_EXTENSIONS', 'OpenCommand', 'QuitCommand', 'SCIPRT_FOLDER_SETTING', 'SETTING_LOG_LEVEL', 'carb', 'console_log', 'console_log_error', 'console_log_info', 'console_log_warn', 'omni']
class CloseCommand(ConsoleCommand):
    def _CloseCommand__close(self, *args):
        ...
    def __init__(self):
        ...
class CommandManager:
    def _CommandManager__on_clear(self, *args) -> bool:
        ...
    def _CommandManager__on_help(self, *args) -> bool:
        ...
    def _CommandManager__on_history(self, *args) -> bool:
        ...
    def __init__(self, clear_fn: typing.Callable):
        ...
    def _get_scripts(self) -> typing.List[typing.Tuple[str, str]]:
        ...
    def execute_command(self, command: str) -> bool:
        """
        
                Execute command.
        
                Args:
                    command (str): Command string to execute.
                
        """
    def execute_file(self, script_file: str, *args) -> bool:
        """
        
                Execute command.
        
                Args:
                    script_file (str): Script file to execute.
                    args (list): Arguments to pass to the script.
        
                Returns:
                    True if command is executed successfully, False otherwise.
                
        """
    def list_commands(self, prefix: str) -> typing.List[str]:
        """
        
                List commands with prefix.
        
                Args:
                    prefix (str): Command prefix.
        
                Returns:
                    Commands list with required prefix.
                
        """
class ConsoleCommand:
    def __init__(self, name: str, description: str, function: typing.Callable):
        ...
class OpenCommand(ConsoleCommand):
    def _OpenCommand__open(self, *args):
        ...
    def __init__(self):
        ...
class QuitCommand(ConsoleCommand):
    def _QuitCommand__quit(self, *args):
        ...
    def __init__(self):
        ...
def console_log(level: int, message: str):
    ...
def console_log_error(message: str):
    ...
def console_log_info(message: str):
    ...
def console_log_warn(message: str):
    ...
AUTOEXEC_LIST_FILE: str = 'autoexec.lst'
EXPECTED_SCRIPT_EXTENSIONS: list = ['py', 'lst']
SCIPRT_FOLDER_SETTING: str = '/app/python/scriptFolders'
SETTING_LOG_LEVEL: str = '/persistent/app/extensions/console/filterLevel'
