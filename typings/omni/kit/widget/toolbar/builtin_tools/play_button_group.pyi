from __future__ import annotations
import carb as carb
from carb.input import KeyboardInput as Key
import omni as omni
from omni.kit.commands.command import execute
from omni.kit.widget.options_menu.option_custom import OptionCustom
from omni.kit.widget.options_menu.option_item import OptionItem
from omni.kit.widget.options_menu.option_separator import OptionSeparator
from omni.kit.widget.options_menu.options_menu import OptionsMenu
from omni.kit.widget.options_menu.options_model import OptionsModel
from omni.kit.widget.toolbar.builtin_tools.models.setting_model import BoolSettingModel
from omni.kit.widget.toolbar.builtin_tools.models.timeline_model import TimelinePlayPauseModel
from omni.kit.widget.toolbar.hotkey import Hotkey
from omni.kit.widget.toolbar.widget_group import WidgetGroup
from omni import ui
import typing
__all__: list = ['PlayButtonGroup']
class PlayButtonGroup(omni.kit.widget.toolbar.widget_group.WidgetGroup):
    PLAY_ANIMATIONS_SETTING: typing.ClassVar[str] = '/app/player/playAnimations'
    PLAY_AUDIO_SETTING: typing.ClassVar[str] = '/app/player/audio/enabled'
    PLAY_COMPUTEGRAPH_SETTING: typing.ClassVar[str] = '/app/player/playComputegraph'
    PLAY_SIMULATIONS_SETTING: typing.ClassVar[str] = '/app/player/playSimulations'
    all_settings_paths: typing.ClassVar[list] = ['/app/player/playAnimations', '/app/player/audio/enabled', '/app/player/playSimulations', '/app/player/playComputegraph']
    def __init__(self):
        ...
    def _build_options_menu(self):
        ...
    def _invoke_context_menu(self, button_id: str, min_menu_entries: int = 1):
        """
        
                Function to invoke context menu.
        
                Args:
                    button_id: button_id of the context menu to be invoked.
                    min_menu_entries: minimal number of menu entries required for menu to be visible (default 1).
                
        """
    def _on_setting_changed(self, item, event_type, menu_item):
        ...
    def _on_timeline_event(self, e):
        ...
    def _select_all(self):
        ...
    def clean(self):
        ...
    def create(self, default_size):
        ...
    def get_style(self):
        ...
PAUSE_TOOL_NAME: str = 'Pause'
PLAY_TOOL_NAME: str = 'Play'
