from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.window.console._console import ConsoleLogView
from omni import ui
__all__: list[str] = ['ConsoleLogView', 'LogView', 'SETTING_LOG_LEVEL', 'carb', 'omni', 'ui']
class LogView:
    def _LogView__copy_message(self):
        ...
    def _LogView__on_log_changed(self, verbose: int, info: int, warn: int, error: int):
        ...
    def _LogView__on_mouse_pressed(self, button: int):
        ...
    def _LogView__select_all_logs(self):
        ...
    def __init__(self):
        """
        
                Wrapper of ConsoleLogView to show/manager log view.
                
        """
    def build_widget(self):
        ...
    def clear(self) -> None:
        """
        
                Clear log items, filters and counters.
        
                args requied for comm
                
        """
    def destroy(self):
        """
        Destroy log view
        """
    def search(self, text: str) -> None:
        """
        
                Search logs by message text.
        
                Args:
                    text (str): Message text to search logs.
                
        """
    def set_log_level(self, level: int) -> None:
        """
        
                Set log level.
        
                Args:
                    level (int): Log level. Could be carb.logging.LEVEL_XXX.
                
        """
SETTING_LOG_LEVEL: str = '/persistent/app/extensions/console/filterLevel'
