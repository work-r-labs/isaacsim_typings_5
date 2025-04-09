from __future__ import annotations
import asyncio as asyncio
import dataclasses
from dataclasses import dataclass
from dataclasses import field
from dataclasses import fields
from functools import partial
import omni as omni
from omni.kit.viewport.menubar.core.menu_item.viewport_menu_spacer import ViewportMenuSpacer
from omni.kit.viewport.menubar.core.viewport_menu_model import AbstractViewportMenuItem
from omni.kit.viewport.menubar.core.viewport_menu_model import AbstractViewportMenubarItem
from omni.kit.viewport.menubar.core.viewport_menu_model import MenuDisplayStatus
from omni.kit.viewport.menubar.core.viewport_menu_model import pop_from_scope
from omni.kit.viewport.menubar.core.viewport_menu_model import push_to_scope
from omni import ui
import typing
__all__: list = ['ViewportMenubar']
class MenubarContext:
    """
    MenubarContext(**kwargs)
    """
    __dataclass_fields__: typing.ClassVar[dict]  # value = {'frame': Field(name='frame',type=<class 'omni.ui._ui.Frame'>,default=None,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'background_rectangle': Field(name='background_rectangle',type=<class 'omni.ui._ui.Rectangle'>,default=None,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'resize_future': Field(name='resize_future',type=<class '_asyncio.Future'>,default=None,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'spacer_width': Field(name='spacer_width',type=<class 'float'>,default=-1,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'sub_menu_expand': Field(name='sub_menu_expand',type=typing.Dict,default=<dataclasses._MISSING_TYPE object>,default_factory=<class 'dict'>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD)}
    __dataclass_params__: typing.ClassVar[dataclasses._DataclassParams]  # value = _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False)
    __hash__: typing.ClassVar[None] = None
    __match_args__: typing.ClassVar[tuple] = ('frame', 'background_rectangle', 'resize_future', 'spacer_width', 'sub_menu_expand')
    background_rectangle = None
    frame = None
    resize_future = None
    spacer_width: typing.ClassVar[int] = -1
    def __eq__(self, other):
        ...
    def __init__(self, **kwargs):
        ...
    def __repr__(self):
        ...
class ViewportMenubar(omni.kit.viewport.menubar.core.viewport_menu_model.AbstractViewportMenubarItem):
    """
    Default viewport menubar, at the top of viewport.
    """
    def _ViewportMenubar__check_contract(self, menu_items: typing.List[omni.kit.viewport.menubar.core.viewport_menu_model.AbstractViewportMenuItem], factory_args: dict) -> bool:
        ...
    def _ViewportMenubar__on_menu_expand_changed(self, factory_args: typing.Dict):
        ...
    def _ViewportMenubar__resize_menubar(self, factory_args: dict) -> None:
        ...
    def _ViewportMenubar__resize_menubar_async(self, factory_args: dict) -> None:
        ...
    def __enter__(self):
        ...
    def __exit__(self, exc_type, exc_value, traceback):
        ...
    def __init__(self, name: str = '', direction: omni.ui._ui.Direction = ..., spacing: omni.ui._ui.Length = 10, style: typing.Optional[typing.Dict] = None, background_visible: bool = False, visible_setting_path: typing.Optional[str] = None):
        """
        
                Constructor.
        
                Args:
                    name (str): Viewport menubar name.
                    direction (ui.Direction): Layout direction of menu items in this menubar, defaults to ui.Direction.LEFT_TO_RIGHT.
                    spacing (ui.Length): Spacing between items, defaults to 10 pixels.
                    style (Optional[Dict]): Additional UI style, defaults to None.
                    background_visible (bool): Show background for menu bar, defaults to False.
                    visible_setting_path (Optional[str]): Setting path for menu bar visibility, defaults to None.
                
        """
    def _build_menubar(self, menu_items: typing.List[omni.kit.viewport.menubar.core.viewport_menu_model.AbstractViewportMenuItem], factory_args: typing.Dict, content_clipping = True):
        ...
    def build_fn(self, menu_items: typing.List[omni.kit.viewport.menubar.core.viewport_menu_model.AbstractViewportMenuItem], factory_args: typing.Dict, content_clipping: bool = True):
        """
        
                Callback to build menu bar.
        
                Args:
                    menu_items (List[AbstractViewportMenuItem]): Menu items.
                    factory_args (dict): Argument related to viewport for this menu bar.
        
                Keyword Args:
                    content_clipping (bool): Menubar content clipping, defaults to True.
                
        """
    def destroy(self) -> None:
        """
        Release resources
        """
    def invalidate(self) -> None:
        """
        Callback to refresh menu bar
        """
    @property
    def background_visible(self) -> bool:
        """
        Menu bar background visibility
        """
    @background_visible.setter
    def background_visible(self, visible: bool) -> None:
        ...
    @property
    def show_separator(self) -> bool:
        """
        If show separator in viewport menu bar
        """
    @show_separator.setter
    def show_separator(self, visible: bool) -> None:
        ...
    @property
    def spacing(self) -> omni.ui._ui.Length:
        """
        Spacing for menu item in this viewport menu bar
        """
    @spacing.setter
    def spacing(self, value: omni.ui._ui.Length) -> None:
        ...
    @property
    def style(self) -> typing.Dict:
        """
        Menu bar UI style
        """
    @property
    def visible(self) -> bool:
        """
        Menu bar visibility
        """
    @visible.setter
    def visible(self, value: bool) -> None:
        ...
VIEWPORT_MENUBAR_STYLE: dict  # value = {'Menu.Title': {'color': 'viewport_menubar_title', 'background_color': 'viewport_menubar_title_background'}, 'Menu.Title:hovered': {'background_color': 'viewport_menubar_selection', 'border_width': 1, 'border_color': 'viewport_menubar_selection_border'}, 'Menu.Title:pressed': {'background_color': 'viewport_menubar_selection'}, 'Menu.Item': {'color': 'viewport_menubar_light', 'margin_width': 'viewport_menubar_item_margin', 'margin_height': 'viewport_menubar_item_margin_height'}, 'MenuBar.Window': {'background_color': 'viewport_menubar_background', 'border_width': 0, 'border_radius': 0}, 'MenuBar.Item': {'color': 'viewport_menubar_light', 'padding': 0, 'margin_width': 'viewport_menubar_item_margin', 'margin_height': 'viewport_menubar_item_margin'}, 'MenuBar.Item::menubar': {'color': 'viewport_menubar_light', 'padding': 0, 'margin_width': 0, 'margin_height': 0}, 'MenuBar.Item.Background': {'background_color': 'viewport_menubar_background', 'border_radius': 'viewport_menubar_border_radius', 'padding': 1, 'margin': 2}, 'Menu.Item.Background': {'background_color': 'viewport_menubar_background', 'border_radius': 'viewport_menubar_border_radius', 'padding': 0, 'margin_width': 0, 'margin_height': 2}, 'Menu.Item.CloseMark': {'color': 0}, 'Menu.Item.CloseMark:checked': {'color': 'viewport_menubar_light'}, 'MenuBar.Item.Triangle': {'background_color': 'viewport_menubar_light'}, 'Menu.Separator': {'color': 'viewport_menubar_medium', 'margin_height': 'viewport_menubar_item_margin_height', 'border_width': 1.5}, 'Menu.Item.Separator': {'color': 'viewport_menubar_medium', 'margin_height': 'viewport_menubar_item_margin_height', 'border_width': 20}, 'Menu.Window': {'background_color': 'viewport_menubar_background', 'border_width': 0, 'border_radius': 0, 'background_selected_color': 'viewport_menubar_selection', 'secondary_padding': 1, 'secondary_selected_color': 'viewport_menubar_selection_border', 'margin': 2}, 'MenuItem': {'background_selected_color': 'viewport_menubar_selection', 'secondary_padding': 1, 'secondary_selected_color': 'viewport_menubar_selection_border'}, 'Slider': {'border_radius': 100, 'border_width': 1, 'border_color': 'viewport_menubar_medium', 'background_color': 65793, 'color': 'viewport_menubar_light', 'secondary_color': 'viewport_menubar_medium', 'draw_mode': <SliderDrawMode.FILLED: 0>, 'padding': 0}, 'Slider:disabled': {'color': 'viewport_menubar_medium'}, 'Menu.Item.Label': {'color': 'viewport_menubar_light', 'margin_width': 'viewport_menubar_item_margin'}, 'Menu.Item.Label:disabled': {'color': 'viewport_menubar_medium'}, 'Menu.Item.Text': {'color': 'viewport_menubar_light'}, 'Menu.Item.Text:disabled': {'color': 'viewport_menubar_medium'}, 'Menu.Item.Icon': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.core-107.1.2+d02c707b/data/icons/none.svg', 'color': 4292269782, 'padding': 0, 'margin_width': 2, 'margin_height': 2}, 'Menu.Item.Icon:selected': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.core-107.1.2+d02c707b/data/icons/check_solid.svg'}, 'Menu.Item.RadioMark': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.core-107.1.2+d02c707b/data/icons/radiomark.svg', 'color': 'viewport_menubar_selection_border', 'margin_width': 'viewport_menubar_item_margin'}, 'Menu.Item.Status': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.core-107.1.2+d02c707b/data/icons/none.svg', 'color': 'viewport_menubar_selection_border', 'margin_width': 'viewport_menubar_item_margin'}, 'Menu.Item.Status:checked': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.core-107.1.2+d02c707b/data/icons/radiomark.svg'}, 'Menu.Item.Status:selected': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.core-107.1.2+d02c707b/data/icons/check_solid.svg'}, 'Menu.Item.Status::Category.None': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.core-107.1.2+d02c707b/data/icons/none.svg'}, 'Menu.Item.Status::Category.All': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.core-107.1.2+d02c707b/data/icons/check_solid.svg'}, 'Menu.Item.Status::Category.Mixed': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.core-107.1.2+d02c707b/data/icons/mixed_checkbox.svg', 'margin_width': 2}, 'ComboBox': {'background_color': 0, 'secondary_color': 0, 'color': 'viewport_menubar_light', 'secondary_selected_color': 'viewport_menubar_light', 'secondary_background_color': 'viewport_menubar_background', 'selected_color': 'viewport_menubar_selection', 'padding': 4, 'font_size': 14}, 'ComboBox:disabled': {'color': 'viewport_menubar_medium'}, 'CheckBox': {'border_radius': 1}, 'CheckBox:disabled': {'background_color': 'viewport_menubar_medium'}, 'Label': {'color': 'viewport_menubar_light'}, 'Menu.Button': {'color': 'viewport_menubar_selection_border', 'background_color': 0, 'padding': 0, 'margin_width': 'viewport_menubar_item_margin', 'margin_height': 'viewport_menubar_item_margin_height', 'stack_direction': <Direction.LEFT_TO_RIGHT: 0>}, 'Menubar.Hover': {'background_color': 0, 'padding': 1, 'margin': 1}, 'Menubar.Hover:hovered': {'background_color': 'viewport_menubar_selection', 'border_color': 'viewport_menubar_selection_border_button', 'border_width': 1.5}, 'Menubar.Hover:pressed': {'background_color': 'viewport_menubar_selection', 'border_color': 'viewport_menubar_selection_border_button', 'border_width': 1.5}, 'Rectangle::reset_invalid': {'background_color': 4283453520, 'border_radius': 2}, 'Rectangle::reset': {'background_color': 4288707919, 'border_radius': 2}}
