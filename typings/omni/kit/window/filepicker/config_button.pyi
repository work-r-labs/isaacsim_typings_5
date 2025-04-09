from __future__ import annotations
import carb as carb
import omni.kit.widget.options_button.options_button
from omni.kit.widget.options_button.options_button import OptionsButton
import omni.kit.widget.options_menu.option_item
from omni.kit.widget.options_menu.option_item import OptionItem
import omni.kit.widget.options_menu.options_model
from omni.kit.widget.options_menu.options_model import OptionsModel
__all__: list = ['SAVED_SETTINGS_OPTIONS_MENU', 'ConfigItem', 'ConfigButton']
class ConfigButton(omni.kit.widget.options_button.options_button.OptionsButton):
    def _ConfigButton__on_value_changed(self, model: omni.kit.widget.options_menu.options_model.OptionsModel, item: ConfigItem) -> None:
        ...
    def __init__(self, enable_soft_delete: bool, on_value_changed_fn: typing.Callable[[typing.Dict[str, bool]], NoneType] = None):
        ...
    def destroy(self):
        ...
    @property
    def values(self) -> typing.Dict[str, bool]:
        """
        
                Option values in dict.
                
        """
    @values.setter
    def values(self, v: typing.Dict[str, bool]) -> bool:
        ...
class ConfigItem(omni.kit.widget.options_menu.option_item.OptionItem):
    def _ConfigItem__get_default(self, default: bool) -> bool:
        ...
    def _ConfigItem__on_value_changed(self, value: bool) -> None:
        ...
    def __init__(self, name: str, text: str, default: bool):
        ...
SAVED_SETTINGS_OPTIONS_MENU: str = '/persistent/app/omniverse/filepicker/options_menu/'
