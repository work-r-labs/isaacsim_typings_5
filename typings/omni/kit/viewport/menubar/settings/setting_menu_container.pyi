from __future__ import annotations
import carb as carb
from functools import partial
from omni.kit.viewport.menubar.core.delegate.checkbox_menu_delegate import CheckboxMenuDelegate
from omni.kit.viewport.menubar.core.delegate.icon_menu_delegate import IconMenuDelegate
from omni.kit.viewport.menubar.core.delegate.slider_menu_delegate import SliderMenuDelegate
import omni.kit.viewport.menubar.core.menu_item.color_menu_item
from omni.kit.viewport.menubar.core.menu_item.color_menu_item import FloatArraySettingColorMenuItem
import omni.kit.viewport.menubar.core.menu_item.viewport_menu_container
from omni.kit.viewport.menubar.core.menu_item.viewport_menu_container import ViewportMenuContainer
import omni.kit.viewport.menubar.core.model.setting_model
from omni.kit.viewport.menubar.core.model.setting_model import SettingModel
from omni.kit.viewport.menubar.core.model.setting_model import SettingModelWithDefaultValue
from omni.kit.viewport.menubar.core.utils import menu_is_tearable
from omni.kit.viewport.menubar.settings.menu_item.settings_renderer_menu_item import SettingsRendererMenuItem
from omni.kit.viewport.menubar.settings.menu_item.settings_transform_manipulator import SettingsTransformManipulator
from omni import ui
import omni.ui.color_utils
import typing
__all__: list = ['SettingMenuContainer']
class BoundingColorMenuItem(omni.kit.viewport.menubar.core.menu_item.color_menu_item.FloatArraySettingColorMenuItem):
    def __init__(self):
        ...
class GridColorMenuItem(omni.kit.viewport.menubar.core.menu_item.color_menu_item.FloatArraySettingColorMenuItem):
    def __init__(self):
        ...
class MenuContext:
    renderer_menu_item: typing.Optional[omni.kit.viewport.menubar.settings.menu_item.settings_renderer_menu_item.SettingsRendererMenuItem]
    def __init__(self):
        ...
    def add_carb_subscription(self, carb_sub: carb.settings._settings.SubscriptionId):
        ...
    def destroy(self):
        ...
    @property
    def settings(self):
        ...
class SelectionColorMenuItem(omni.kit.viewport.menubar.core.menu_item.color_menu_item.FloatArraySettingColorMenuItem):
    def __init__(self):
        ...
    def on_color_changed(self, colors: typing.List[float]) -> None:
        ...
class SelectionColorSetting(ViewportSetting):
    INTERSECTION: typing.ClassVar[str] = '/persistent/app/viewport/outline/intersection/color'
    OUTLINE: typing.ClassVar[str] = '/persistent/app/viewport/outline/color'
    def __init__(self, default: typing.Any):
        ...
    def reset(self, settings):
        ...
class SettingMenuContainer(omni.kit.viewport.menubar.core.menu_item.viewport_menu_container.ViewportMenuContainer):
    """
    The menu with the viewport settings
    """
    def _SettingMenuContainer__build_advanced_navigation_items(self, menu_ctx: MenuContext):
        ...
    def _SettingMenuContainer__build_debug_settings(self, menu_ctx: MenuContext):
        ...
    def _SettingMenuContainer__build_gizmo_menu_items(self, menu_ctx: MenuContext):
        ...
    def _SettingMenuContainer__build_grid_menu_items(self, menu_ctx: MenuContext):
        ...
    def _SettingMenuContainer__build_navigation_menu_items(self, menu_ctx: MenuContext) -> None:
        ...
    def _SettingMenuContainer__build_navigation_speed_items(self, menu_ctx: MenuContext):
        ...
    def _SettingMenuContainer__build_selection_menu_items(self, menu_ctx: MenuContext):
        ...
    def _SettingMenuContainer__build_ui_menu_items(self, menu_ctx: MenuContext):
        ...
    def _SettingMenuContainer__reset_settings(self, viewport_api_id: str):
        ...
    def __init__(self):
        ...
    def _build_menu(self, factory: typing.Dict) -> None:
        ...
    def _show_viewport_preference(self) -> None:
        ...
    def build_fn(self, factory: typing.Dict):
        ...
    def destroy(self):
        ...
class VIEWPORT_SETTINGS:
    ADAPTIVE_SPEED: typing.ClassVar[ViewportSetting]  # value = <omni.kit.viewport.menubar.settings.setting_menu_container.ViewportSetting object>
    BBOX_LINE_COLOR: typing.ClassVar[ViewportSetting]  # value = <omni.kit.viewport.menubar.settings.setting_menu_container.ViewportSetting object>
    CAMERA_STOP_ON_UP: typing.ClassVar[ViewportSetting]  # value = <omni.kit.viewport.menubar.settings.setting_menu_container.ViewportSetting object>
    CAM_UPDATE_CLAMPING: typing.ClassVar[ViewportSetting]  # value = <omni.kit.viewport.menubar.settings.setting_menu_container.ViewportSetting object>
    DOUBLE_CLICK_COI: typing.ClassVar[ViewportSetting]  # value = <omni.kit.viewport.menubar.settings.setting_menu_container.ViewportSetting object>
    FLY_IGNORE_VIEW_DIRECTION: typing.ClassVar[ViewportSetting]  # value = <omni.kit.viewport.menubar.settings.setting_menu_container.ViewportSetting object>
    GAMEPAD_CONTROL: typing.ClassVar[ViewportSetting]  # value = <omni.kit.viewport.menubar.settings.setting_menu_container.ViewportSetting object>
    GESTURE_ENABLED: typing.ClassVar[ViewportSetting]  # value = <omni.kit.viewport.menubar.settings.setting_menu_container.ViewportSetting object>
    GESTURE_RADIUS: typing.ClassVar[ViewportSetting]  # value = <omni.kit.viewport.menubar.settings.setting_menu_container.ViewportSetting object>
    GESTURE_TIME: typing.ClassVar[ViewportSetting]  # value = <omni.kit.viewport.menubar.settings.setting_menu_container.ViewportSetting object>
    GIZMO_GLOBAL_SCALE: typing.ClassVar[ViewportSetting]  # value = <omni.kit.viewport.menubar.settings.setting_menu_container.ViewportSetting object>
    GIZMO_LINE_WIDTH: typing.ClassVar[ViewportSetting]  # value = <omni.kit.viewport.menubar.settings.setting_menu_container.ViewportSetting object>
    GIZMO_MAX_FADEOUT: typing.ClassVar[ViewportSetting]  # value = <omni.kit.viewport.menubar.settings.setting_menu_container.ViewportSetting object>
    GIZMO_MIN_FADEOUT: typing.ClassVar[ViewportSetting]  # value = <omni.kit.viewport.menubar.settings.setting_menu_container.ViewportSetting object>
    GIZMO_SCALE: typing.ClassVar[ViewportSetting]  # value = <omni.kit.viewport.menubar.settings.setting_menu_container.ViewportSetting object>
    GIZMO_SCALE_ENABLED: typing.ClassVar[ViewportSetting]  # value = <omni.kit.viewport.menubar.settings.setting_menu_container.ViewportSetting object>
    GRID_FADE: typing.ClassVar[ViewportSetting]  # value = <omni.kit.viewport.menubar.settings.setting_menu_container.ViewportSetting object>
    GRID_LINE_COLOR: typing.ClassVar[ViewportSetting]  # value = <omni.kit.viewport.menubar.settings.setting_menu_container.ViewportSetting object>
    GRID_LINE_WIDTH: typing.ClassVar[ViewportSetting]  # value = <omni.kit.viewport.menubar.settings.setting_menu_container.ViewportSetting object>
    GRID_SCALE: typing.ClassVar[ViewportSetting]  # value = <omni.kit.viewport.menubar.settings.setting_menu_container.ViewportSetting object>
    INERTIA_ANOUNT: typing.ClassVar[ViewportSetting]  # value = <omni.kit.viewport.menubar.settings.setting_menu_container.ViewportSetting object>
    INERTIA_ENABLED: typing.ClassVar[ViewportSetting]  # value = <omni.kit.viewport.menubar.settings.setting_menu_container.ViewportSetting object>
    LOOK_SPEED_HORIZ: typing.ClassVar[ViewportSetting]  # value = <omni.kit.viewport.menubar.settings.setting_menu_container.ViewportSetting object>
    LOOK_SPEED_VERT: typing.ClassVar[ViewportSetting]  # value = <omni.kit.viewport.menubar.settings.setting_menu_container.ViewportSetting object>
    NAVIGATION_SPEED: typing.ClassVar[ViewportSetting]  # value = <omni.kit.viewport.menubar.settings.setting_menu_container.ViewportSetting object>
    NAVIGATION_SPEED_MULTAMOUNT: typing.ClassVar[ViewportSetting]  # value = <omni.kit.viewport.menubar.settings.setting_menu_container.ViewportSetting object>
    OBJECT_CENTRIC: typing.ClassVar[ViewportSetting]  # value = <omni.kit.viewport.menubar.settings.setting_menu_container.ViewportSetting object>
    OUTLINE_COLOR: typing.ClassVar[SelectionColorSetting]  # value = <omni.kit.viewport.menubar.settings.setting_menu_container.SelectionColorSetting object>
    ROTATION_SMOOTH_ALWAYS: typing.ClassVar[ViewportSetting]  # value = <omni.kit.viewport.menubar.settings.setting_menu_container.ViewportSetting object>
    ROTATION_SMOOTH_ENABLED: typing.ClassVar[ViewportSetting]  # value = <omni.kit.viewport.menubar.settings.setting_menu_container.ViewportSetting object>
    ROTATION_SMOOTH_SCALE: typing.ClassVar[ViewportSetting]  # value = <omni.kit.viewport.menubar.settings.setting_menu_container.ViewportSetting object>
    SELECTION_LINE_WIDTH: typing.ClassVar[ViewportSetting]  # value = <omni.kit.viewport.menubar.settings.setting_menu_container.ViewportSetting object>
    SHOW_SPEED_ON_START: typing.ClassVar[ViewportSetting]  # value = <omni.kit.viewport.menubar.settings.setting_menu_container.ViewportSetting object>
    TUMBLE_SPEED: typing.ClassVar[ViewportSetting]  # value = <omni.kit.viewport.menubar.settings.setting_menu_container.ViewportSetting object>
    UI_BACKGROUND_OPACITY: typing.ClassVar[ViewportSetting]  # value = <omni.kit.viewport.menubar.settings.setting_menu_container.ViewportSetting object>
    UI_BRIGHTNESS: typing.ClassVar[ViewportSetting]  # value = <omni.kit.viewport.menubar.settings.setting_menu_container.ViewportSetting object>
    ZOOM_SPEED: typing.ClassVar[ViewportSetting]  # value = <omni.kit.viewport.menubar.settings.setting_menu_container.ViewportSetting object>
class ViewportSetting:
    def __init__(self, key: str, default: typing.Any, set_default: bool = True, read_incoming: bool = False):
        ...
    def reset(self, settings):
        ...
    def set_default(self, settings):
        ...
    @property
    def default(self) -> typing.Any:
        ...
class ViewportSettingModel(omni.kit.viewport.menubar.core.model.setting_model.SettingModelWithDefaultValue):
    def __init__(self, viewport_setting: ViewportSetting, draggable: bool = False):
        ...
BRIGHTNESS_VALUE_RANGE_MAX: float = 1.0
BRIGHTNESS_VALUE_RANGE_MIN: float = 0.25
CAM_VELOCITY_MAX: str = '/persistent/app/viewport/camVelocityMax'
CAM_VELOCITY_MIN: str = '/persistent/app/viewport/camVelocityMin'
CAM_VELOCITY_SCALER_MAX: str = '/persistent/app/viewport/camVelocityScalerMax'
CAM_VELOCITY_SCALER_MIN: str = '/persistent/app/viewport/camVelocityScalerMin'
OUTLINE_COLOR_INDEX: int = 1020
SETTING_UI_BRIGHTNESS_MAX: str = '/app/viewport/ui/maxBrightness'
SETTING_UI_BRIGHTNESS_MIN: str = '/app/viewport/ui/minBrightness'
UI_STYLE: dict  # value = {'Menu.Item.Icon::Settings': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.settings-107.0.3+d02c707b/data/icons/viewport_settings.svg'}, 'ResolutionLink': {'background_color': 0, 'margin': 0, 'padding': 2}, 'ResolutionLink.Image': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.settings-107.0.3+d02c707b/data/icons/link_dark.svg', 'margin': 0}, 'ResolutionLink.Image:checked': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.settings-107.0.3+d02c707b/data/icons/link.svg'}, 'ComboBox::ratio': {'background_color': 0, 'padding': 4, 'margin': 0}, 'Menu.Item.Button::save': {'padding': 0, 'margin': 0, 'background_color': 0}, 'Menu.Item.Button.Image::save': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.settings-107.0.3+d02c707b/data/icons/save.svg', 'color': 'viewport_menubar_light'}, 'Menu.Item.Button.Image::save:checked': {'color': 'shade:4291663622'}, 'Ratio.Background': {'background_color': 4282664004, 'border_color': 4288770075, 'border_width': 1}, 'Resolution.Text': {'color': 'input_hint'}, 'Resolution.Name': {'color': 'viewport_menubar_light'}, 'Resolution.Del': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.settings-107.0.3+d02c707b/data/icons/delete.svg'}}
cl: omni.ui.color_utils.ColorShade  # value = <omni.ui.color_utils.ColorShade object>
