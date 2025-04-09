from __future__ import annotations
import asyncio as asyncio
import omni as omni
from omni.kit.viewport.menubar.core.viewport_menu_model import AbstractViewportMenuItem
from omni import ui
__all__: list = ['ViewportButtonItem']
class ViewportButtonItem(omni.kit.viewport.menubar.core.viewport_menu_model.AbstractViewportMenuItem):
    """
    
        A menu item has a button with flyout window or drop-down menu:
            Left click: toggle
    
            Right click: show flyout window or menu options
        
    """
    def __init__(self, text: str = '', name: str = '', onclick_fn: typing.Callable = None, build_menu_fn: typing.Callable[[NoneType], typing.List[omni.ui._ui.MenuItem]] = None, build_window_fn: typing.Callable[[NoneType], omni.ui._ui.Window] = None, visible_setting_path: typing.Optional[str] = None, order_setting_path: typing.Optional[str] = None, expand_setting_path: typing.Optional[str] = None, alignment: omni.ui._ui.Alignment = ..., enabled: bool = True, has_triangle: bool = False, triangle_size: float = 6, style: typing.Optional[typing.Dict] = None):
        """
        
                Constructor.
        
                Keyword args:
                    text (str): Button text, defaults to "".
                    name (str): Button name, defaults to "".
                    onclick_fn (Callable): Callback when button clicked, defaults to None
                    build_menu_fn (Callable[[None], List[ui.MenuItem]]): Callback to create flyout menu when right click, defaults to None.
                    build_window_fn (Callable[[None], ui.Window]): Callback to create flyout window when right click, defaults to None.
                    visible_setting_path (Optional[str]): Setting path for button visibility, defaults to None.
                    order_setting_path (Optional[str]): Setting path for button order in menu bar, defaults to None.
                    expand_setting_path (Optional[str]): Setting path for button expand state in menu bar, defaults to None.
                    alignment (ui.Alignment): Flyout window/menu alignment with button, defaults to ui.Alignment.RIGHT_BOTTOM.
                    enabled (bool): Button enabled state, defaults to True.
                    has_triangle (bool): Show drop-down carrot, defaults to False.
                    triangle_size (float): Size of drop-down carrot, defaults to 6 pixels.
                    style (Optional[Dict]): Button additional UI style, defaults to None.
                
        """
    def _build_menu(self) -> None:
        ...
    def _invalidate(self) -> None:
        ...
    def _on_mouse_clicked_fn(self, button):
        ...
    def _show_menu(self):
        ...
    def _show_window(self):
        ...
    def build_fn(self, factory: typing.Dict) -> None:
        """
        
                Callback when build this button menu item. Reimplement it to have own customized item.
        
                Args:
                    factory (dict): Argument related to viewport.
                
        """
    def destroy(self) -> None:
        """
        Release resources
        """
    def invalidate(self) -> None:
        """
        Refresh menu
        """
    def on_right_clicked_fn(self):
        """
        Show flyout window/menu when right click on button
        """
    @property
    def button(self) -> typing.Optional[omni.ui._ui.Button]:
        """
        Button widget
        """
    @property
    def checked(self) -> bool:
        """
        Button checked state
        """
    @checked.setter
    def checked(self, value: bool) -> None:
        ...
    @property
    def enabled(self) -> bool:
        """
        Button enable state
        """
    @enabled.setter
    def enabled(self, value: bool) -> None:
        ...
    @property
    def menu_item(self) -> omni.ui._ui.Menu:
        """
        Menu item widget
        """
    @property
    def name(self) -> str:
        ...
    @name.setter
    def name(self, value: str) -> None:
        """
        Button name
        """
    @property
    def selected(self) -> bool:
        """
        Button selected state
        """
    @selected.setter
    def selected(self, value: bool) -> None:
        ...
    @property
    def visible(self) -> bool:
        """
        Button visibility
        """
    @visible.setter
    def visible(self, value: bool) -> None:
        ...
    @property
    def window(self) -> omni.ui._ui.Window:
        """
        Flyout window
        """
VIEWPORT_MENUBAR_STYLE: dict  # value = {'Menu.Title': {'color': 'viewport_menubar_title', 'background_color': 'viewport_menubar_title_background'}, 'Menu.Title:hovered': {'background_color': 'viewport_menubar_selection', 'border_width': 1, 'border_color': 'viewport_menubar_selection_border'}, 'Menu.Title:pressed': {'background_color': 'viewport_menubar_selection'}, 'Menu.Item': {'color': 'viewport_menubar_light', 'margin_width': 'viewport_menubar_item_margin', 'margin_height': 'viewport_menubar_item_margin_height'}, 'MenuBar.Window': {'background_color': 'viewport_menubar_background', 'border_width': 0, 'border_radius': 0}, 'MenuBar.Item': {'color': 'viewport_menubar_light', 'padding': 0, 'margin_width': 'viewport_menubar_item_margin', 'margin_height': 'viewport_menubar_item_margin'}, 'MenuBar.Item::menubar': {'color': 'viewport_menubar_light', 'padding': 0, 'margin_width': 0, 'margin_height': 0}, 'MenuBar.Item.Background': {'background_color': 'viewport_menubar_background', 'border_radius': 'viewport_menubar_border_radius', 'padding': 1, 'margin': 2}, 'Menu.Item.Background': {'background_color': 'viewport_menubar_background', 'border_radius': 'viewport_menubar_border_radius', 'padding': 0, 'margin_width': 0, 'margin_height': 2}, 'Menu.Item.CloseMark': {'color': 0}, 'Menu.Item.CloseMark:checked': {'color': 'viewport_menubar_light'}, 'MenuBar.Item.Triangle': {'background_color': 'viewport_menubar_light'}, 'Menu.Separator': {'color': 'viewport_menubar_medium', 'margin_height': 'viewport_menubar_item_margin_height', 'border_width': 1.5}, 'Menu.Item.Separator': {'color': 'viewport_menubar_medium', 'margin_height': 'viewport_menubar_item_margin_height', 'border_width': 20}, 'Menu.Window': {'background_color': 'viewport_menubar_background', 'border_width': 0, 'border_radius': 0, 'background_selected_color': 'viewport_menubar_selection', 'secondary_padding': 1, 'secondary_selected_color': 'viewport_menubar_selection_border', 'margin': 2}, 'MenuItem': {'background_selected_color': 'viewport_menubar_selection', 'secondary_padding': 1, 'secondary_selected_color': 'viewport_menubar_selection_border'}, 'Slider': {'border_radius': 100, 'border_width': 1, 'border_color': 'viewport_menubar_medium', 'background_color': 65793, 'color': 'viewport_menubar_light', 'secondary_color': 'viewport_menubar_medium', 'draw_mode': <SliderDrawMode.FILLED: 0>, 'padding': 0}, 'Slider:disabled': {'color': 'viewport_menubar_medium'}, 'Menu.Item.Label': {'color': 'viewport_menubar_light', 'margin_width': 'viewport_menubar_item_margin'}, 'Menu.Item.Label:disabled': {'color': 'viewport_menubar_medium'}, 'Menu.Item.Text': {'color': 'viewport_menubar_light'}, 'Menu.Item.Text:disabled': {'color': 'viewport_menubar_medium'}, 'Menu.Item.Icon': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.core-107.1.2+d02c707b/data/icons/none.svg', 'color': 4292269782, 'padding': 0, 'margin_width': 2, 'margin_height': 2}, 'Menu.Item.Icon:selected': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.core-107.1.2+d02c707b/data/icons/check_solid.svg'}, 'Menu.Item.RadioMark': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.core-107.1.2+d02c707b/data/icons/radiomark.svg', 'color': 'viewport_menubar_selection_border', 'margin_width': 'viewport_menubar_item_margin'}, 'Menu.Item.Status': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.core-107.1.2+d02c707b/data/icons/none.svg', 'color': 'viewport_menubar_selection_border', 'margin_width': 'viewport_menubar_item_margin'}, 'Menu.Item.Status:checked': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.core-107.1.2+d02c707b/data/icons/radiomark.svg'}, 'Menu.Item.Status:selected': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.core-107.1.2+d02c707b/data/icons/check_solid.svg'}, 'Menu.Item.Status::Category.None': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.core-107.1.2+d02c707b/data/icons/none.svg'}, 'Menu.Item.Status::Category.All': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.core-107.1.2+d02c707b/data/icons/check_solid.svg'}, 'Menu.Item.Status::Category.Mixed': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.core-107.1.2+d02c707b/data/icons/mixed_checkbox.svg', 'margin_width': 2}, 'ComboBox': {'background_color': 0, 'secondary_color': 0, 'color': 'viewport_menubar_light', 'secondary_selected_color': 'viewport_menubar_light', 'secondary_background_color': 'viewport_menubar_background', 'selected_color': 'viewport_menubar_selection', 'padding': 4, 'font_size': 14}, 'ComboBox:disabled': {'color': 'viewport_menubar_medium'}, 'CheckBox': {'border_radius': 1}, 'CheckBox:disabled': {'background_color': 'viewport_menubar_medium'}, 'Label': {'color': 'viewport_menubar_light'}, 'Menu.Button': {'color': 'viewport_menubar_selection_border', 'background_color': 0, 'padding': 0, 'margin_width': 'viewport_menubar_item_margin', 'margin_height': 'viewport_menubar_item_margin_height', 'stack_direction': <Direction.LEFT_TO_RIGHT: 0>}, 'Menubar.Hover': {'background_color': 0, 'padding': 1, 'margin': 1}, 'Menubar.Hover:hovered': {'background_color': 'viewport_menubar_selection', 'border_color': 'viewport_menubar_selection_border_button', 'border_width': 1.5}, 'Menubar.Hover:pressed': {'background_color': 'viewport_menubar_selection', 'border_color': 'viewport_menubar_selection_border_button', 'border_width': 1.5}, 'Rectangle::reset_invalid': {'background_color': 4283453520, 'border_radius': 2}, 'Rectangle::reset': {'background_color': 4288707919, 'border_radius': 2}}
