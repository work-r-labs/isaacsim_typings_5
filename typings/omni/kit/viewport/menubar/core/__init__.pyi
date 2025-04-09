"""
This extension provides a comprehensive system for creating and managing custom menu bars and items within the viewport UI in Omniverse Kit applications.
"""
from __future__ import annotations
from omni.kit.viewport.menubar.core.delegate.abstract_widget_menu_delegate import AbstractWidgetMenuDelegate
from omni.kit.viewport.menubar.core.delegate.category_menu_delegate import CategoryMenuDelegate
from omni.kit.viewport.menubar.core.delegate.checkbox_menu_delegate import CheckboxMenuDelegate
from omni.kit.viewport.menubar.core.delegate.color_menu_delegate import ColorMenuDelegate
from omni.kit.viewport.menubar.core.delegate.combobox_menu_delegate import ComboBoxMenuDelegate
from omni.kit.viewport.menubar.core.delegate.icon_menu_delegate import IconMenuDelegate
from omni.kit.viewport.menubar.core.delegate.label_menu_delegate import LabelMenuDelegate
from omni.kit.viewport.menubar.core.delegate.separator_menu_delegate import SeparatorDelegate
from omni.kit.viewport.menubar.core.delegate.slider_menu_delegate import SliderMenuDelegate
from omni.kit.viewport.menubar.core.delegate.spinner_menu_delegate import SpinnerMenuDelegate
from omni.kit.viewport.menubar.core.delegate.viewport_menu_delegate import ViewportMenuDelegate
from omni.kit.viewport.menubar.core.extension import ViewportMenuBarExtension
from omni.kit.viewport.menubar.core.extension import get_instance
from omni.kit.viewport.menubar.core.menu_item.category_menu_collection import CategoryMenuCollection
from omni.kit.viewport.menubar.core.menu_item.category_menu_container import CategoryMenuContainer
from omni.kit.viewport.menubar.core.menu_item.color_menu_item import AbstractColorMenuItem
from omni.kit.viewport.menubar.core.menu_item.color_menu_item import FloatArraySettingColorMenuItem
from omni.kit.viewport.menubar.core.menu_item.radio_menu_collection import RadioMenuCollection
from omni.kit.viewport.menubar.core.menu_item.selectable_menu_item import SelectableMenuItem
from omni.kit.viewport.menubar.core.menu_item.viewport_button_item import ViewportButtonItem
from omni.kit.viewport.menubar.core.menu_item.viewport_menu_container import ViewportMenuContainer
from omni.kit.viewport.menubar.core.menu_item.viewport_menu_item import ViewportMenuItem
from omni.kit.viewport.menubar.core.menu_item.viewport_menu_separator import ViewportMenuSeparator
from omni.kit.viewport.menubar.core.menu_item.viewport_menu_spacer import ViewportMenuSpacer
from omni.kit.viewport.menubar.core.menu_item.viewport_menubar_item import ViewportMenubar
from omni.kit.viewport.menubar.core.model.category_model import BaseCategoryItem
from omni.kit.viewport.menubar.core.model.category_model import CategoryCollectionItem
from omni.kit.viewport.menubar.core.model.category_model import CategoryCustomItem
from omni.kit.viewport.menubar.core.model.category_model import CategoryStateItem
from omni.kit.viewport.menubar.core.model.category_model import CategoryStatus
from omni.kit.viewport.menubar.core.model.category_model import SimpleCategoryModel
from omni.kit.viewport.menubar.core.model.combobox_model import ComboBoxItem
from omni.kit.viewport.menubar.core.model.combobox_model import ComboBoxModel
from omni.kit.viewport.menubar.core.model.combobox_model import SettingComboBoxModel
from omni.kit.viewport.menubar.core.model.list_model import SimpleListItem
from omni.kit.viewport.menubar.core.model.list_model import SimpleListModel
from omni.kit.viewport.menubar.core.model.reset_button import ResetButton
from omni.kit.viewport.menubar.core.model.reset_button import ResetHelper
from omni.kit.viewport.menubar.core.model.setting_model import SettingModel
from omni.kit.viewport.menubar.core.model.setting_model import SettingModelWithDefaultValue
from omni.kit.viewport.menubar.core.model.usd_attribute_model import USDAttributeModel
from omni.kit.viewport.menubar.core.model.usd_attribute_model import USDBoolAttributeModel
from omni.kit.viewport.menubar.core.model.usd_attribute_model import USDFloatAttributeModel
from omni.kit.viewport.menubar.core.model.usd_attribute_model import USDIntAttributeModel
from omni.kit.viewport.menubar.core.model.usd_attribute_model import USDStringAttributeModel
from omni.kit.viewport.menubar.core.model.usd_metadata_model import USDMetadataModel
from omni.kit.viewport.menubar.core.utils import menu_is_tearable
from omni.kit.viewport.menubar.core.viewport_menu_model import AbstractViewportMenuItem
from omni.kit.viewport.menubar.core.viewport_menu_model import AbstractViewportMenubarItem
from omni.kit.viewport.menubar.core.viewport_menu_model import MenuDisplayStatus
from omni.kit.viewport.menubar.core.viewport_menu_model import get_item as get_menu_item
from . import delegate
from . import extension
from . import menu_item
from . import model
from . import preference
from . import style
from . import utils
from . import viewport_layer
from . import viewport_menu_model
__all__: list = ['get_instance', 'ViewportMenuBarExtension', 'AbstractViewportMenubarItem', 'AbstractViewportMenuItem', 'DEFAULT_MENUBAR_NAME', 'VIEWPORT_MENUBAR_STYLE', 'MenuDisplayStatus', 'CategoryStatus', 'AbstractWidgetMenuDelegate', 'ViewportMenuDelegate', 'CategoryMenuDelegate', 'CheckboxMenuDelegate', 'ColorMenuDelegate', 'ComboBoxMenuDelegate', 'IconMenuDelegate', 'LabelMenuDelegate', 'SeparatorDelegate', 'SliderMenuDelegate', 'SpinnerMenuDelegate', 'CategoryMenuCollection', 'CategoryMenuContainer', 'AbstractColorMenuItem', 'FloatArraySettingColorMenuItem', 'RadioMenuCollection', 'SelectableMenuItem', 'ViewportButtonItem', 'ViewportMenuContainer', 'ViewportMenuItem', 'ViewportMenuSeparator', 'ViewportMenuSpacer', 'ViewportMenubar', 'BaseCategoryItem', 'CategoryCollectionItem', 'CategoryCustomItem', 'CategoryStateItem', 'SimpleCategoryModel', 'ComboBoxItem', 'ComboBoxModel', 'SettingComboBoxModel', 'SimpleListItem', 'SimpleListModel', 'SettingModel', 'SettingModelWithDefaultValue', 'USDAttributeModel', 'USDBoolAttributeModel', 'USDFloatAttributeModel', 'USDIntAttributeModel', 'USDStringAttributeModel', 'USDMetadataModel', 'ResetButton', 'ResetHelper']
DEFAULT_MENUBAR_NAME: str = '__DEFAULT__MENUBAR__'
VIEWPORT_MENUBAR_STYLE: dict  # value = {'Menu.Title': {'color': 'viewport_menubar_title', 'background_color': 'viewport_menubar_title_background'}, 'Menu.Title:hovered': {'background_color': 'viewport_menubar_selection', 'border_width': 1, 'border_color': 'viewport_menubar_selection_border'}, 'Menu.Title:pressed': {'background_color': 'viewport_menubar_selection'}, 'Menu.Item': {'color': 'viewport_menubar_light', 'margin_width': 'viewport_menubar_item_margin', 'margin_height': 'viewport_menubar_item_margin_height'}, 'MenuBar.Window': {'background_color': 'viewport_menubar_background', 'border_width': 0, 'border_radius': 0}, 'MenuBar.Item': {'color': 'viewport_menubar_light', 'padding': 0, 'margin_width': 'viewport_menubar_item_margin', 'margin_height': 'viewport_menubar_item_margin'}, 'MenuBar.Item::menubar': {'color': 'viewport_menubar_light', 'padding': 0, 'margin_width': 0, 'margin_height': 0}, 'MenuBar.Item.Background': {'background_color': 'viewport_menubar_background', 'border_radius': 'viewport_menubar_border_radius', 'padding': 1, 'margin': 2}, 'Menu.Item.Background': {'background_color': 'viewport_menubar_background', 'border_radius': 'viewport_menubar_border_radius', 'padding': 0, 'margin_width': 0, 'margin_height': 2}, 'Menu.Item.CloseMark': {'color': 0}, 'Menu.Item.CloseMark:checked': {'color': 'viewport_menubar_light'}, 'MenuBar.Item.Triangle': {'background_color': 'viewport_menubar_light'}, 'Menu.Separator': {'color': 'viewport_menubar_medium', 'margin_height': 'viewport_menubar_item_margin_height', 'border_width': 1.5}, 'Menu.Item.Separator': {'color': 'viewport_menubar_medium', 'margin_height': 'viewport_menubar_item_margin_height', 'border_width': 20}, 'Menu.Window': {'background_color': 'viewport_menubar_background', 'border_width': 0, 'border_radius': 0, 'background_selected_color': 'viewport_menubar_selection', 'secondary_padding': 1, 'secondary_selected_color': 'viewport_menubar_selection_border', 'margin': 2}, 'MenuItem': {'background_selected_color': 'viewport_menubar_selection', 'secondary_padding': 1, 'secondary_selected_color': 'viewport_menubar_selection_border'}, 'Slider': {'border_radius': 100, 'border_width': 1, 'border_color': 'viewport_menubar_medium', 'background_color': 65793, 'color': 'viewport_menubar_light', 'secondary_color': 'viewport_menubar_medium', 'draw_mode': <SliderDrawMode.FILLED: 0>, 'padding': 0}, 'Slider:disabled': {'color': 'viewport_menubar_medium'}, 'Menu.Item.Label': {'color': 'viewport_menubar_light', 'margin_width': 'viewport_menubar_item_margin'}, 'Menu.Item.Label:disabled': {'color': 'viewport_menubar_medium'}, 'Menu.Item.Text': {'color': 'viewport_menubar_light'}, 'Menu.Item.Text:disabled': {'color': 'viewport_menubar_medium'}, 'Menu.Item.Icon': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.core-107.1.2+d02c707b/data/icons/none.svg', 'color': 4292269782, 'padding': 0, 'margin_width': 2, 'margin_height': 2}, 'Menu.Item.Icon:selected': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.core-107.1.2+d02c707b/data/icons/check_solid.svg'}, 'Menu.Item.RadioMark': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.core-107.1.2+d02c707b/data/icons/radiomark.svg', 'color': 'viewport_menubar_selection_border', 'margin_width': 'viewport_menubar_item_margin'}, 'Menu.Item.Status': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.core-107.1.2+d02c707b/data/icons/none.svg', 'color': 'viewport_menubar_selection_border', 'margin_width': 'viewport_menubar_item_margin'}, 'Menu.Item.Status:checked': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.core-107.1.2+d02c707b/data/icons/radiomark.svg'}, 'Menu.Item.Status:selected': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.core-107.1.2+d02c707b/data/icons/check_solid.svg'}, 'Menu.Item.Status::Category.None': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.core-107.1.2+d02c707b/data/icons/none.svg'}, 'Menu.Item.Status::Category.All': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.core-107.1.2+d02c707b/data/icons/check_solid.svg'}, 'Menu.Item.Status::Category.Mixed': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.core-107.1.2+d02c707b/data/icons/mixed_checkbox.svg', 'margin_width': 2}, 'ComboBox': {'background_color': 0, 'secondary_color': 0, 'color': 'viewport_menubar_light', 'secondary_selected_color': 'viewport_menubar_light', 'secondary_background_color': 'viewport_menubar_background', 'selected_color': 'viewport_menubar_selection', 'padding': 4, 'font_size': 14}, 'ComboBox:disabled': {'color': 'viewport_menubar_medium'}, 'CheckBox': {'border_radius': 1}, 'CheckBox:disabled': {'background_color': 'viewport_menubar_medium'}, 'Label': {'color': 'viewport_menubar_light'}, 'Menu.Button': {'color': 'viewport_menubar_selection_border', 'background_color': 0, 'padding': 0, 'margin_width': 'viewport_menubar_item_margin', 'margin_height': 'viewport_menubar_item_margin_height', 'stack_direction': <Direction.LEFT_TO_RIGHT: 0>}, 'Menubar.Hover': {'background_color': 0, 'padding': 1, 'margin': 1}, 'Menubar.Hover:hovered': {'background_color': 'viewport_menubar_selection', 'border_color': 'viewport_menubar_selection_border_button', 'border_width': 1.5}, 'Menubar.Hover:pressed': {'background_color': 'viewport_menubar_selection', 'border_color': 'viewport_menubar_selection_border_button', 'border_width': 1.5}, 'Rectangle::reset_invalid': {'background_color': 4283453520, 'border_radius': 2}, 'Rectangle::reset': {'background_color': 4288707919, 'border_radius': 2}}
