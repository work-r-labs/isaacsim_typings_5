from __future__ import annotations
import asyncio as asyncio
import omni.kit.widget.options_menu.option_item
from omni.kit.widget.options_menu.option_item import OptionItem
from omni.kit.widget.options_menu.options_menu import OptionsMenu
import omni.kit.widget.options_menu.options_model
from omni.kit.widget.options_menu.options_model import OptionsModel
from omni import ui
import omni.ui._ui
__all__: list[str] = ['FilterButton', 'FilterModel', 'OptionItem', 'OptionsMenu', 'OptionsModel', 'TIME_HOLD_SHOW_MENU', 'UI_STYLE', 'asyncio', 'ui']
class FilterButton:
    """
    
        A filter button with an associated popup menu.
    
        Kwargs:
            option_items (List[OptionItem]): Option items.
            width (ui.Length): Button width. Default ui.Pixel(24).
            height (ui.Length): Button height. Default ui.Pixel(24).
            hide_on_click (bool): Hide popup menu if menu item clicked. Default False.
            menu_width (ui.Length): Width of popup menu item. Default ui.Fraction(1).
            style (dict): External widget style. Default empty.
        
    """
    def __init__(self, option_items: typing.List[omni.kit.widget.options_menu.option_item.OptionItem], width: omni.ui._ui.Length = ..., height: omni.ui._ui.Length = ..., hide_on_click: bool = False, menu_width: omni.ui._ui.Length = ..., carot_size: omni.ui._ui.Length = ..., style: typing.Dict = {}):
        ...
    def _build_ui(self) -> None:
        ...
    def _on_item_changed(self, model: omni.kit.widget.options_menu.options_model.OptionsModel, item: omni.kit.widget.options_menu.option_item.OptionItem) -> None:
        ...
    def _on_mouse_double_clicked(self, btn) -> None:
        ...
    def _on_mouse_pressed(self, btn) -> None:
        ...
    def _on_mouse_released(self, btn) -> None:
        ...
    def _schedule_show_menu(self):
        ...
    def _show_options_menu(self):
        ...
    def _toggle_filter(self):
        ...
    def destroy(self) -> None:
        ...
    @property
    def button(self) -> omni.ui._ui.Button:
        """
        Filter button widget
        """
    @property
    def model(self) -> FilterModel:
        """
        Model for filter options
        """
class FilterModel(omni.kit.widget.options_menu.options_model.OptionsModel):
    """
    
        Filter model.
        
    """
    def __init__(self, option_items: typing.List[omni.kit.widget.options_menu.option_item.OptionItem]):
        ...
TIME_HOLD_SHOW_MENU: float = 0.08
UI_STYLE: dict  # value = {'FilterButton': {'background_color': 0, 'margin_width': 0, 'padding': 2, 'border_radius': 2}, 'FilterButton:selected': {'background_color': 'shade:4280230179'}, 'FilterButton.Image': {'background_color': 0, 'color': 'shade:4289243304', 'image_url': '/home/chris/videos/isaacsim/_build/linux-x86_64/release/extscache/omni.kit.widget.filter-1.1.4+8131b85d/data/icons/filter_tint.svg', 'alignment': <Alignment.CENTER: 72>}, 'FilterButton.Image:selected': {'color': 'shade:4294952756'}, 'FilterButton:hovered': {'background_color': 4285427310}, 'FilterButton.Carot': {'background_color': 'shade:4289243304'}, 'FilterButton.Carot:selected': {'background_color': 'shade:4294952756'}}
