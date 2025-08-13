from __future__ import annotations
import carb as carb
from functools import partial
import omni as omni
from omni.kit.widget.filter.filter import FilterButton
from omni.kit.widget.options_menu.option_custom import OptionCustom
from omni.kit.widget.options_menu.option_delegate import OptionLabelMenuItemDelegate
from omni.kit.widget.options_menu.option_item import OptionItem
from omni.kit.widget.options_menu.option_separator import OptionSeparator
from omni.kit.window.console.scripts.log_view import LogView
from omni import ui
__all__: list[str] = ['ConsoleToolbar', 'FilterButton', 'LogView', 'OptionCustom', 'OptionItem', 'OptionLabelMenuItemDelegate', 'OptionSeparator', 'SETTING_LOG_SOURCES', 'SearchField', 'ToolbarButton', 'carb', 'omni', 'partial', 'ui']
class ConsoleToolbar:
    def _ConsoleToolbar__get_errors_button_text(self) -> str:
        ...
    def _ConsoleToolbar__get_log_file(self) -> str:
        ...
    def _ConsoleToolbar__get_warnings_button_text(self) -> str:
        ...
    def _ConsoleToolbar__on_clear_all_sources(self):
        ...
    def _ConsoleToolbar__on_error_changed(self, _) -> None:
        ...
    def _ConsoleToolbar__on_select_all_sources(self):
        ...
    def _ConsoleToolbar__on_source_changed(self, tree_item, changed_item, event_type):
        ...
    def _ConsoleToolbar__on_warning_changed(self, _) -> None:
        ...
    def __init__(self, log_view: omni.kit.window.console.scripts.log_view.LogView, cmd_input_visible_model: omni.ui._ui.SimpleBoolModel):
        """
        
                Toolbar in console window.
        
                Args:
                    log_view (LogView): Log view.
                    cmd_input_visible_model (ui.SimpleBoolModel): Model for visibility of command input field.
                
        """
    def _build_filter_button(self):
        ...
    def _build_filter_items(self) -> typing.List[omni.kit.widget.options_menu.option_item.OptionItem]:
        ...
    def _build_ui(self):
        ...
    def _open_log_file(self):
        ...
    def _open_log_folder(self):
        ...
    def _set_log_level(self, level: int) -> None:
        ...
    def _show_command_input(self):
        ...
    def destroy(self):
        """
        Destroy toolbar
        """
class SearchField:
    def _SearchField__on_input_changed(self, model: omni.ui._ui.SimpleStringModel):
        ...
    def __init__(self, on_input_changed_fn: typing.Callable[[str], NoneType]):
        """
        
                Search field in toolbar.
        
                Args:
                    on_input_changed_fn (Callable[[str], None]): Callabck when input value changed.
                
        """
    def destroy(self):
        ...
class ToolbarButton(omni.ui._ui.Button):
    def __init__(self, name: str, tooltip: str, clicked_fn: callable, text: str = '', visible: bool = True):
        """
        
                Button in toolbar.
        
                Args:
                    name (str): Button name. Used for style.
                    tooltip (str): Button tooltip.
                    clicked_fn (callable): Callback when button clicked.
                    text (str): Button text. Default "" means no text displayed.
                
        """
SETTING_LOG_SOURCES: str = '/persistent/app/extensions/console/sources'
