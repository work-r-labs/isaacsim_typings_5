from __future__ import annotations
import carb as carb
from functools import partial
from omni.kit.viewport.menubar.core.delegate.icon_menu_delegate import IconMenuDelegate
from omni.kit.viewport.menubar.core.delegate.viewport_menu_delegate import ViewportMenuDelegate
from omni.kit.viewport.menubar.core.menu_item.category_menu_container import CategoryMenuContainer
from omni.kit.viewport.menubar.core.menu_item.selectable_menu_item import SelectableMenuItem
import omni.kit.viewport.menubar.core.menu_item.viewport_menu_container
from omni.kit.viewport.menubar.core.menu_item.viewport_menu_container import ViewportMenuContainer
import omni.kit.viewport.menubar.core.model.category_model
from omni.kit.viewport.menubar.core.model.category_model import BaseCategoryItem
from omni.kit.viewport.menubar.core.model.category_model import CategoryCollectionItem
from omni.kit.viewport.menubar.core.model.category_model import CategoryCustomItem
from omni.kit.viewport.menubar.core.model.category_model import CategoryStateItem
from omni.kit.viewport.menubar.core.model.category_model import SimpleCategoryModel
from omni.kit.viewport.menubar.core.model.setting_model import SettingModel
from omni import ui
__all__: list = ['DisplayMenuContainer']
class DisplayMenuContainer(omni.kit.viewport.menubar.core.menu_item.viewport_menu_container.ViewportMenuContainer):
    """
    The menu with the visibility settings
    """
    def _DisplayMenuContainer__excludes_changed(self, *args, **kwargs) -> None:
        ...
    def _DisplayMenuContainer__mem_type_changed(self, *args, **kwargs):
        ...
    def _DisplayMenuContainer__trigger_action(self, action: str, *args, **kwargs):
        ...
    def __init__(self):
        ...
    def _build_menu_items(self, viewport_context: dict, *args, **kwargs):
        ...
    def build_fn(self, viewport_context: dict):
        ...
    def deregister_custom_category_item(self, category: str, item: omni.kit.viewport.menubar.core.model.category_model.BaseCategoryItem):
        ...
    def deregister_custom_setting(self, text: str):
        ...
    def destroy(self):
        ...
    def register_custom_category_item(self, category: str, item: omni.kit.viewport.menubar.core.model.category_model.BaseCategoryItem, section: str):
        ...
    def register_custom_setting(self, text: str, setting_path: str):
        ...
def _make_viewport_setting(viewport_api_id: str, setting: str):
    ...
DEFAULT_CATEGORIES: list = ['Heads Up Display', 'Show By Type', 'Show By Purpose']
DEFAULT_SECTION: str = 'default'
DISPLAY_ACTIONS_MAP: dict = {'omni.kit.viewport.actions::toggle_bounding_box_visibility': 'Bounding Box', 'omni.kit.viewport.actions::toggle_grid_visibility': 'Grid', 'omni.kit.viewport.actions::toggle_camera_visibility': 'Cameras', 'omni.kit.viewport.actions::toggle_light_visibility': 'Lights', 'omni.kit.viewport.actions::toggle_skeleton_visibility': 'Skeletons', 'omni.kit.viewport.actions::toggle_audio_visibility': 'Audio', 'omni.kit.viewport.actions::toggle_mesh_visibility': 'Meshes', 'omni.kit.viewport.actions::toggle_selection_hilight_visibility': 'Selection Outline', 'omni.kit.viewport.actions::toggle_axis_visibility': 'Axis', 'omni.kit.viewport.actions::toggle_show_by_purpose_render': 'Render', 'omni.kit.viewport.actions::toggle_show_by_purpose_proxy': 'Proxy', 'omni.kit.viewport.actions::toggle_show_by_purpose_guide': 'Guide'}
HEADS_UP_CATEGORY_NAME: str = 'Heads Up Display'
SHOW_BY_PURPOSE_CATEGORY_NAME: str = 'Show By Purpose'
SHOW_BY_TYPE_CATEGORY_NAME: str = 'Show By Type'
SHOW_BY_TYPE_EXCLUDE_LIST: str = '/exts/omni.kit.viewport.menubar.display/showByType/exclude_list'
UI_STYLE: dict = {'Menu.Item.Icon::Display': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.display-107.0.3+d02c707b/data/icons/viewport_visibility.svg'}}
