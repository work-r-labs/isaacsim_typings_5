from __future__ import annotations
import asyncio as asyncio
import carb as carb
from functools import partial
import omni as omni
from omni.kit.app._impl import SettingChangeSubscription
from omni.kit.viewport.menubar.core.delegate.icon_menu_delegate import IconMenuDelegate
from omni.kit.viewport.menubar.core.delegate.viewport_menu_delegate import ViewportMenuDelegate
from omni.kit.viewport.menubar.core.menu_item.radio_menu_collection import RadioMenuCollection
from omni.kit.viewport.menubar.core.menu_item.selectable_menu_item import SelectableMenuItem
from omni.kit.viewport.menubar.core.menu_item.viewport_menu_container import ViewportMenuContainer
from omni.kit.viewport.menubar.core.model.combobox_model import SettingComboBoxModel
from omni.kit.viewport.menubar.core.viewport_menu_model import MenuDisplayStatus
from omni.kit.viewport.menubar.render.hd_renderer_list import HdRendererList
from omni.kit.viewport.menubar.render.menu_item.single_render_menu_item import SingleRenderMenuItem
from omni import ui
import os as os
import typing
__all__: list = ['RendererMenuContainer']
class BoolStringModel(omni.ui._ui.SimpleBoolModel):
    def _BoolStringModel__setting_changed(self, item: carb.dictionary._dictionary.Item, event_type: carb.settings._settings.ChangeEventType):
        ...
    def __del__(self):
        ...
    def __init__(self, setting_path: str, *args, value_map: typing.Sequence[str] = ('default', 'disabled'), **kwargs):
        ...
    def destroy(self):
        ...
    def get_value(self) -> bool:
        ...
    def get_value_as_bool(self) -> bool:
        ...
    def get_value_as_string(self) -> bool:
        ...
    def set_value(self, value: bool) -> bool:
        ...
class DebugShadingModel(omni.kit.viewport.menubar.core.model.combobox_model.SettingComboBoxModel):
    def __del__(self):
        ...
    def __init__(self, viewport_api):
        ...
    def _get_current_index_by_value(self, value: typing.Any, default: int = 0) -> int:
        ...
    def _on_change(self, *args, **kwargs) -> None:
        ...
    def empty(self):
        ...
    def on_current_changed(self):
        ...
class DisableMaterialModel(BoolStringModel):
    def set_value(self, value: bool) -> bool:
        ...
class FlashLightModel(BoolStringModel):
    def __init__(self, setting_path: str, *args, **kwargs):
        ...
class MenuContext:
    def _MenuContext__on_usd_context_event(self, event: omni.usd._usd.StageEventType):
        ...
    def _MenuContext__render_settings_changed(self, *args, **kwargs):
        ...
    def __init__(self, root_menu: omni.ui._ui.Menu, viewport_api, renderer_changed_fn: typing.Callable):
        ...
    def add_destroyables(self, key: str, destroyables: typing.Sequence):
        ...
    def destroy(self, key: str = None):
        ...
    def set_default_state(self):
        ...
    @property
    def delegate(self) -> omni.ui._ui.MenuDelegate:
        ...
    @property
    def root_menu(self) -> omni.ui._ui.Menu:
        ...
    @property
    def viewport_api(self):
        ...
class RendererMenuContainer(omni.kit.viewport.menubar.core.menu_item.viewport_menu_container.ViewportMenuContainer):
    """
    The menu with the list of renderers
    """
    PXR_IN_USE: typing.ClassVar[str] = '/app/viewport/omni_hydra_pxr_in_use'
    _RendererMenuContainer__enabled_engines: typing.ClassVar[generator]  # value = <generator object HdRendererList.enabled_engines at 0x709f44093ca0>
    def _RendererMenuContainer__add_destroyables(self, viewport_api, key: str, destroyables: typing.Sequence):
        ...
    def _RendererMenuContainer__build_render_options(self, viewport_context):
        ...
    def _RendererMenuContainer__build_renderers(self, viewport_context):
        """
        Build the menu with the list of the renderers
        """
    def _RendererMenuContainer__build_rendering_settings(self, viewport_context):
        """
        Build the rendering settings presets
        """
    def _RendererMenuContainer__build_shading_modes(self, viewport_context):
        """
        Build the shading modes
        """
    def _RendererMenuContainer__dirty_menu(self, *args, **kwargs):
        """
        Rebuild everything
        """
    def _RendererMenuContainer__dirty_renderers(self, *args, **kwargs):
        ...
    def _RendererMenuContainer__ext_changed(self, ext_name: str, enabled: bool):
        ...
    def _RendererMenuContainer__ext_disabled(self, ext_name: str, *args, **kwargs):
        ...
    def _RendererMenuContainer__ext_enabled(self, ext_name: str, *args, **kwargs):
        ...
    def _RendererMenuContainer__get_current_name(self, viewport_api):
        """
        Returns display name of the current renderer
        """
    def _RendererMenuContainer__hide_on_click(self, viewport_context: typing.Dict = None):
        ...
    def _RendererMenuContainer__load_setting_file(self, preset_name):
        ...
    def _RendererMenuContainer__load_settings(self, viewport_context):
        ...
    def _RendererMenuContainer__pxr_available(self, settings, viewport_api):
        ...
    def _RendererMenuContainer__reset_settings(self):
        ...
    def _RendererMenuContainer__save_settings(self, viewport_context):
        ...
    def _RendererMenuContainer__set_menu_label(self, menu_context: MenuContext, viewport_api):
        ...
    def _RendererMenuContainer__setup_extenion_watching(self):
        ...
    def _RendererMenuContainer__show_render_preferences(self, *args, **kwargs) -> None:
        ...
    def __init__(self):
        ...
    def _build_menu(self, viewport_context):
        """
        Build the first level menu
        """
    def build_fn(self, viewport_context: typing.Dict):
        """
        Entry point for the menu bar
        """
    def can_contract(self, factory_args: dict) -> bool:
        ...
    def contract(self, factory_args: dict) -> bool:
        ...
    def destroy(self):
        ...
    def expand(self, factory_args: dict) -> None:
        ...
    def get_display_status(self, factory_args: dict) -> omni.kit.viewport.menubar.core.viewport_menu_model.MenuDisplayStatus:
        ...
    def get_require_size(self, factory_args: dict, expand: bool = False) -> float:
        ...
    def set_menu_item_type(self, menu_item_type: typing.Callable[..., ForwardRef('SingleRenderMenuItemBase')]):
        """
        
                Set the menu type for the default created renderer
        
                Args:
                    menu_item_type: callable that will create the menu item
                
        """
    @property
    def render_list(self):
        """
        Returns the list of available renderers
        """
class ShadingModeModel(BoolStringModel):
    def set_value(self, value: bool) -> bool:
        ...
LIGHTING_MODE: str = '/rtx/useViewLightingMode'
MATERIAL_MODE: str = '/exts/omni.kit.viewport.menubar.render/materialMode'
RENDER_ACTIONS_MAP: dict = {'omni.kit.viewport.actions::set_renderer_rtx_realtime': 'RTX - Real-Time', 'omni.kit.viewport.actions::set_renderer_rtx_pathtracing': 'RTX - Interactive (Path Tracing)', 'omni.kit.viewport.actions::set_renderer_iray': 'RTX - Accurate (Iray)', 'omni.kit.viewport.actions::set_renderer_pxr_storm': 'Pixar Storm', 'omni.kit.viewport.actions::toggle_wireframe': 'Wireframe'}
SHADING_MODE: str = '/exts/omni.kit.viewport.menubar.render/shadingMode'
UI_STYLE: dict = {'Menu.Item.Icon::Renderer': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.render-107.0.8+d02c707b/data/icons/viewport_renderer.svg'}, 'Menu.Item.Button': {'background_color': 0, 'margin': 0, 'padding': 0}, 'Menu.Item.Button.Image::OptionBox': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.render-107.0.8+d02c707b/data/icons/settings_submenu.svg'}}
