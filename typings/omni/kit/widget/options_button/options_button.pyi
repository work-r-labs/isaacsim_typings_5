from __future__ import annotations
from omni.kit.widget.options_menu.option_item import OptionItem
from omni.kit.widget.options_menu.options_menu import OptionsMenu
import omni.kit.widget.options_menu.options_model
from omni.kit.widget.options_menu.options_model import OptionsModel
from omni import ui
import omni.ui._ui
__all__ = ['OptionItem', 'OptionsButton', 'OptionsMenu', 'OptionsModel', 'UI_STYLE', 'ui']
class OptionsButton:
    """
    A button that includes a popup menu for options.
    
        Args:
            option_items (List[OptionItem]): Option items.
            width (ui.Length): Button width. Default ui.Pixel(24).
            height (ui.Length): Button height. Default ui.Pixel(24).
            hide_on_click (bool): Hide popup menu if menu item clicked. Default False.
            menu_width (ui.Length): Width of popup menu item. Default ui.Fraction(1).
            style (dict): External widget style. Default empty.
    """
    def __init__(self, option_items: typing.List[omni.kit.widget.options_menu.option_item.OptionItem], width: omni.ui._ui.Length = ..., height: omni.ui._ui.Length = ..., hide_on_click: bool = False, menu_width: omni.ui._ui.Length = ..., style: typing.Dict = {}):
        """
        Constructor for OptionsButton.
        """
    def _build_ui(self) -> None:
        ...
    def _on_mouse_pressed(self, btn) -> None:
        ...
    def _on_mouse_released(self, btn) -> None:
        ...
    def _show_options_menu(self):
        ...
    def destroy(self) -> None:
        """
        Clears models and destroys the options menu.
        """
    @property
    def button(self) -> omni.ui._ui.Button:
        """
        Gets the ui.Button used as the options button.
        
                Returns:
                    ui.Button: The button widget.
        """
    @property
    def model(self) -> omni.kit.widget.options_menu.options_model.OptionsModel:
        """
        Gets the OptionsModel associated with the button.
        
                Returns:
                    OptionsModel: The model used for options.
        """
UI_STYLE: dict  # value = {'OptionsButton': {'background_color': 0, 'margin_width': 0, 'padding': 4, 'border_radius': 2}, 'OptionsButton:selected': {'background_color': 'shade:4280230179'}, 'OptionsButton.Image': {'background_color': 0, 'color': 'shade:4289243304', 'image_url': '/home/chris/isaacsim/extscache/omni.kit.widget.options_button-1.0.3+d02c707b/data/icons/settings.svg', 'alignment': <Alignment.CENTER: 72>}, 'OptionsButton.Image:selected': {'color': 'shade:4294952756'}, 'OptionsButton:hovered': {'background_color': 4285427310}}
