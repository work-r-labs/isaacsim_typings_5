from __future__ import annotations
import carb as carb
import omni.kit.widget.options_button.options_button
from omni.kit.widget.options_button.options_button import OptionsButton
from omni.kit.widget.options_menu.option_custom import OptionCustom
from omni.kit.widget.options_menu.option_delegate import OptionLabelMenuItemDelegate
import omni.kit.widget.options_menu.option_item
from omni.kit.widget.options_menu.option_item import OptionItem
from omni.kit.widget.options_menu.option_separator import OptionSeparator
from omni import ui
__all__ = ['LayerOptionItem', 'LayerOptionsButton', 'OptionCustom', 'OptionItem', 'OptionLabelMenuItemDelegate', 'OptionSeparator', 'OptionsButton', 'carb', 'ui']
class LayerOptionItem(omni.kit.widget.options_menu.option_item.OptionItem):
    def _LayerOptionItem__on_value_changed(self, value: bool) -> None:
        ...
    def __init__(self, name: str, property_name: str):
        ...
    def update_value(self):
        ...
class LayerOptionsButton(omni.kit.widget.options_button.options_button.OptionsButton):
    def __init__(self, on_reload_layers_fn: callable):
        ...
    def set_item_value(self, name: str, value: bool) -> None:
        ...
