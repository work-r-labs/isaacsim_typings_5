from __future__ import annotations
import carb as carb
import concurrent as concurrent
import dataclasses
from dataclasses import dataclass
from dataclasses import field
from dataclasses import fields
import functools as functools
from functools import partial
import omni as omni
from omni.kit.async_engine.async_engine import run_coroutine
from omni.kit.viewport.menubar.camera.camera_list_delegate import CameraListDelegate
from omni.kit.viewport.menubar.camera.camera_widget_delegate_manager import CameraWidgetDelegateManager
from omni.kit.viewport.menubar.camera.commands import SetViewportCameraCommand
from omni.kit.viewport.menubar.camera.menu_item.auto_exposure import CameraAutoExposure
from omni.kit.viewport.menubar.camera.menu_item.expand_menu_item import ExpandMenuItem
from omni.kit.viewport.menubar.camera.menu_item.focal_distance import CameraFocalDistance
from omni.kit.viewport.menubar.camera.menu_item.fstop import CameraFStop
from omni.kit.viewport.menubar.camera.menu_item.lens import CameraLens
from omni.kit.viewport.menubar.camera.menu_item.single_camera_menu_item import NoCameraMenuItem
from omni.kit.viewport.menubar.camera.menu_item.single_camera_menu_item import SingleCameraMenuItem
from omni.kit.viewport.menubar.camera.utils import get_camera_display
from omni.kit.viewport.menubar.core.delegate.separator_menu_delegate import SeparatorDelegate
from omni.kit.viewport.menubar.core.delegate.viewport_menu_delegate import ViewportMenuDelegate
from omni.kit.viewport.menubar.core.menu_item.viewport_menu_container import ViewportMenuContainer
from omni.kit.viewport.menubar.core.model.usd_attribute_model import USDAttributeModel
from omni.kit.viewport.menubar.core.model.usd_attribute_model import USDFloatAttributeModel
from omni.kit.viewport.menubar.core.utils import menu_is_tearable
from omni.kit.viewport.menubar.core.viewport_menu_model import MenuDisplayStatus
from omni import ui
import pxr.Sdf
from pxr import Sdf
from pxr import Tf
from pxr import Trace
from pxr import Usd
import pxr.Usd
from pxr import UsdGeom
import traceback as traceback
import typing
import weakref as weakref
__all__: list = ['CameraMenuContainer']
class CameraMenuContainer(omni.kit.viewport.menubar.core.menu_item.viewport_menu_container.ViewportMenuContainer):
    """
    The menu with the list of cameras
    """
    def _CameraMenuContainer__build_lock_item(self, viewport_api, camera_path: pxr.Sdf.Path):
        ...
    def _CameraMenuContainer__camera_changed(self, camera_path: pxr.Sdf.Path, viewport_api):
        ...
    def _CameraMenuContainer__camera_clicked(self, camera_path: pxr.Sdf.Path, viewport_api):
        ...
    def _CameraMenuContainer__ensure_valid_camera(self, viewport_api, camera_path: pxr.Sdf.Path):
        ...
    def _CameraMenuContainer__full_invalidate(self):
        ...
    def _CameraMenuContainer__get_lock_model(self, stage: pxr.Usd.Stage, camera_path: pxr.Sdf.Path):
        ...
    def _CameraMenuContainer__get_session_camera_paths(self, stage: pxr.Usd.Stage):
        ...
    def _CameraMenuContainer__rebuild_cameras(self, viewport_api, check_validity: bool = False, removed_camera: pxr.Sdf.Path = None, added_camera: pxr.Sdf.Path = None):
        ...
    def _CameraMenuContainer__render_settings_changed(self, camera_path: pxr.Sdf.Path, resolution: typing.Tuple[int, int], viewport_api):
        ...
    def _CameraMenuContainer__sub_global_expand(self):
        ...
    def _CameraMenuContainer__unsub_global_expand(self):
        ...
    def __del__(self):
        ...
    def __init__(self):
        ...
    def _build_camera_collections(self, viewport_context, root: omni.ui._ui.Menu):
        ...
    def _build_cameras(self, viewport_api, session_cameras: bool, ui_shown: bool = False, force_build: bool = False):
        """
        Build the menu with the list of the cameras
        """
    def _build_create_camera(self, viewport_context, root: omni.ui._ui.Menu):
        ...
    def _build_expand(self, viewport_context) -> None:
        ...
    def _build_menu(self, viewport_context):
        """
        Build the first level menu
        """
    def _create_from_view(self, viewport_api):
        ...
    def _on_lock_changed(self, model: omni.ui._ui.AbstractValueModel, viewport_api) -> None:
        ...
    def _on_menu_collection_triggered(self, menu: omni.ui._ui.MenuItemCollection, checked: bool):
        ...
    def build_fn(self, viewport_context: typing.Dict):
        """
        Entry point for the menu bar
        """
    def can_contract(self, factory_args: typing.Dict) -> bool:
        ...
    def contract(self, factory_args: typing.Dict) -> bool:
        ...
    def deregister_menu_item(self, create_menu_item_fn: typing.Callable[[ForwardRef('viewport_context'), omni.ui._ui.Menu], NoneType]):
        ...
    def destroy(self):
        ...
    def expand(self, factory_args: typing.Dict) -> None:
        ...
    def get_display_status(self, factory_args: typing.Dict) -> omni.kit.viewport.menubar.core.viewport_menu_model.MenuDisplayStatus:
        ...
    def get_require_size(self, factory_args: typing.Dict, expand: bool = False) -> float:
        ...
    def register_menu_item(self, create_menu_item_fn: typing.Callable[[ForwardRef('viewport_context'), omni.ui._ui.Menu], NoneType], order: int = 0):
        ...
    def set_menu_item_type(self, menu_item_type: typing.Callable[..., ForwardRef('SingleCameraMenuItemBase')]):
        """
        
                Set the menu type for the default created camera
        
                Args:
                    menu_item_type: callable that will create the menu item
                
        """
class MenuContext:
    """
    MenuContext(**kwargs)
    """
    __dataclass_fields__: typing.ClassVar[dict]  # value = {'root_menu': Field(name='root_menu',type=<class 'omni.ui._ui.Menu'>,default=None,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'delegate': Field(name='delegate',type=<class 'omni.ui._ui.MenuDelegate'>,default=None,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'settings_menu': Field(name='settings_menu',type=<class 'omni.ui._ui.Menu'>,default=None,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'settings_container': Field(name='settings_container',type=<class 'omni.ui._ui.ZStack'>,default=None,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'settings_width': Field(name='settings_width',type=<class 'int'>,default=0,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'expand_container': Field(name='expand_container',type=<class 'omni.ui._ui.ZStack'>,default=None,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'expand_item': Field(name='expand_item',type=<class 'omni.kit.viewport.menubar.camera.menu_item.expand_menu_item.ExpandMenuItem'>,default=None,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'expand_width': Field(name='expand_width',type=<class 'int'>,default=0,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'expand_model': Field(name='expand_model',type=<class 'omni.ui._ui.SimpleBoolModel'>,default=None,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'camera_collection': Field(name='camera_collection',type=<class 'omni.ui._ui.MenuItemCollection'>,default=None,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'camera_path': Field(name='camera_path',type=<class 'str'>,default=None,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'selected_camera_item': Field(name='selected_camera_item',type=<class 'omni.ui._ui.MenuItem'>,default=None,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'camera_list': Field(name='camera_list',type=typing.Optional[omni.kit.viewport.menubar.camera.camera_menu_container._CameraList],default=None,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'stage_sub': Field(name='stage_sub',type=<class 'carb._carb.Subscription'>,default=None,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'expanded_sub': Field(name='expanded_sub',type=<class 'carb._carb.Subscription'>,default=None,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'render_settings_changed_sub': Field(name='render_settings_changed_sub',type=<class 'carb._carb.Subscription'>,default=None,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'lock_menu_sub': Field(name='lock_menu_sub',type=<class 'carb._carb.Subscription'>,default=None,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'settings_items': Field(name='settings_items',type=typing.List[omni.ui._ui.MenuItem],default=<dataclasses._MISSING_TYPE object>,default_factory=<class 'list'>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'camera_to_menu': Field(name='camera_to_menu',type=typing.Dict[pxr.Sdf.Path, typing.Tuple[omni.kit.viewport.menubar.camera.menu_item.single_camera_menu_item.SingleCameraMenuItem, bool]],default=<dataclasses._MISSING_TYPE object>,default_factory=<class 'dict'>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD)}
    __dataclass_params__: typing.ClassVar[dataclasses._DataclassParams]  # value = _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False)
    __hash__: typing.ClassVar[None] = None
    __match_args__: typing.ClassVar[tuple] = ('root_menu', 'delegate', 'settings_menu', 'settings_container', 'settings_width', 'expand_container', 'expand_item', 'expand_width', 'expand_model', 'camera_collection', 'camera_path', 'selected_camera_item', 'camera_list', 'stage_sub', 'expanded_sub', 'render_settings_changed_sub', 'lock_menu_sub', 'settings_items', 'camera_to_menu')
    camera_collection = None
    camera_list = None
    camera_path = None
    delegate = None
    expand_container = None
    expand_item = None
    expand_model = None
    expand_width: typing.ClassVar[int] = 0
    expanded_sub = None
    lock_menu_sub = None
    render_settings_changed_sub = None
    root_menu = None
    saved_expand: typing.ClassVar[bool] = False
    selected_camera_item = None
    settings_container = None
    settings_menu = None
    settings_width: typing.ClassVar[int] = 0
    stage_sub = None
    def __eq__(self, other):
        ...
    def __init__(self, **kwargs):
        ...
    def __repr__(self):
        ...
class _CameraList:
    """
    The object that watches USD for the list of cameras
    """
    @staticmethod
    def _CameraList__delayed_prim_changed(*args, **kwargs):
        """
        
                Create/remove dirty items that was collected from TfNotice. Can be
                called any time to pump changes.
                
        """
    @staticmethod
    def _CameraList__get_usd_rt_stage(stage: pxr.Usd.Stage):
        ...
    @staticmethod
    def _CameraList__on_usd_changed(*args, **kwargs):
        """
        Called by Usd.Notice.ObjectsChanged
        """
    def _CameraList__filter(self, camera_prim: pxr.Usd.Prim) -> bool:
        ...
    def __del__(self):
        ...
    def __init__(self, stage, callback):
        ...
    def destroy(self):
        ...
    @property
    def camera_list(self) -> typing.List[pxr.Sdf.Path]:
        ...
    @property
    def is_dirty(self):
        ...
def _show_camera_in_menu(prim: pxr.Usd.Prim):
    ...
def handle_exception(func):
    """
    
        Decorator to print exception in async functions
        
    """
CAMERA_ACTIONS_MAP: dict = {'omni.kit.viewport.actions::perspective_camera': '/OmniverseKit_Persp', 'omni.kit.viewport.actions::top_camera': '/OmniverseKit_Top', 'omni.kit.viewport.actions::front_camera': '/OmniverseKit_Front', 'omni.kit.viewport.actions::right_camera': '/OmniverseKit_Right'}
CAMERA_LOCK_NAME: str = 'omni:kit:cameraLock'
SESSION_CAMERAS: dict = {'/OmniverseKit_Persp': 'Perspective', '/OmniverseKit_Top': 'Top', '/OmniverseKit_Front': 'Front', '/OmniverseKit_Right': 'Right'}
UI_STYLE: dict  # value = {'Menu.Item.Icon::UnlockedCamera': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.camera-107.0.2+d02c707b/data/icons/camera_viewport.svg'}, 'Menu.Item.Icon::UnlockedCameraWithoutHovered': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.camera-107.0.2+d02c707b/data/icons/camera_viewport.svg'}, 'Menu.Item.Icon::UnlockedCamera:hovered': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.camera-107.0.2+d02c707b/data/icons/lock_dark.svg'}, 'Menu.Item.Icon::LockedCamera': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.camera-107.0.2+d02c707b/data/icons/viewport_cameras_locked.svg'}, 'Menu.Item.Icon::LockedCameraWithoutHovered': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.camera-107.0.2+d02c707b/data/icons/viewport_cameras_locked.svg'}, 'Menu.Item.Icon::LockedCamera:hovered': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.camera-107.0.2+d02c707b/data/icons/unlock_dark.svg'}, 'Menu.Item.Icon::Expand': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.camera-107.0.2+d02c707b/data/icons/expand.svg', 'color': 'viewport_menubar_background'}, 'Menu.Item.Icon::Expand:checked': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.camera-107.0.2+d02c707b/data/icons/contract.svg'}, 'Menu.Item.Icon::Lock': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.camera-107.0.2+d02c707b/data/icons/unlock_dark.svg', 'color': 'viewport_menubar_background'}, 'Menu.Item.Icon::Lock:checked': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.camera-107.0.2+d02c707b/data/icons/lock_dark.svg'}, 'Menu.Item.Icon::Sample': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.camera-107.0.2+d02c707b/data/icons/focalSample_viewport.svg'}, 'Menu.Item.Icon::Sample:disabled': {'color': 'viewport_menubar_medium'}, 'Menu.Item.Icon::Add': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.camera-107.0.2+d02c707b/data/icons/add.svg', 'color': 'viewport_menubar_selection_border'}, 'Menu.Item.Icon::Lens': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.camera-107.0.2+d02c707b/data/icons/lens.svg'}, 'Menu.Item.Icon::FocalDistance': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.camera-107.0.2+d02c707b/data/icons/focal_distance.svg'}, 'Menu.Item.Icon::FStop': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.camera-107.0.2+d02c707b/data/icons/Fstop.svg'}, 'Menu.Item.Button': {'background_color': 0, 'margin': 0, 'padding': 0}, 'Menu.Item.Button.Image::OptionBox': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.camera-107.0.2+d02c707b/data/icons/settings_submenu.svg'}, 'Menu.Item.Button.Image::CameraLocked': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.camera-107.0.2+d02c707b/data/icons/lock_dark.svg'}, 'Menu.Item.Button.Image::CameraUnlocked': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.camera-107.0.2+d02c707b/data/icons/unlock_dark.svg'}, 'MenuBar.Item::transparent': {}}
